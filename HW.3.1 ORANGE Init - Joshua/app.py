# app.py
import ast
import operator as op
import math
import random
import streamlit as st

st.set_page_config(page_title="Math Check", page_icon="🧮")

st.title("🧮 Math Equation Checker (with random easy problem)")
st.write(
    "Enter a math expression (numbers, + - * / % // **, parentheses). "
    "Press **Set equation** to lock it, then enter your answer and press **Check Answer**.\n\n"
    "Use **Random easy math problem** to auto-fill a simple problem."
)

# ---------- Safe evaluator ----------
_ALLOWED_BINOPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.FloorDiv: op.floordiv,
    ast.Pow: op.pow,
}
_ALLOWED_UNARYOPS = {ast.UAdd: lambda x: +x, ast.USub: lambda x: -x}
_MAX_ABS_RESULT = 1e12
_MAX_ABS_BASE_FOR_POW = 1e6
_MAX_ABS_EXPONENT = 10

def safe_eval(expr: str):
    if not expr or not expr.strip():
        raise ValueError("Empty expression.")
    try:
        parsed = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Syntax error: {e}")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)
            raise ValueError("Only numeric constants allowed.")
        if isinstance(node, ast.Num):
            return float(node.n)
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type in _ALLOWED_UNARYOPS:
                return _ALLOWED_UNARYOPS[op_type](_eval(node.operand))
            raise ValueError("Unsupported unary operator.")
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type not in _ALLOWED_BINOPS:
                raise ValueError("Unsupported binary operator.")
            if op_type is ast.Pow:
                if abs(right) > _MAX_ABS_EXPONENT:
                    raise ValueError(f"Exponent too large (abs > {_MAX_ABS_EXPONENT}).")
                if abs(left) > _MAX_ABS_BASE_FOR_POW:
                    raise ValueError("Base too large for exponentiation.")
            try:
                result = _ALLOWED_BINOPS[op_type](left, right)
            except ZeroDivisionError:
                raise ValueError("Division by zero.")
            if math.isfinite(result) and abs(result) <= _MAX_ABS_RESULT:
                return float(result)
            raise ValueError("Result out of allowed range or not finite.")
        raise ValueError(f"Unsupported element: {type(node).__name__}")

    return _eval(parsed)

# ---------- Session-state defaults (initialize BEFORE widget creation) ----------
defaults = {
    "correct_answer": None,
    "eq_text": "",
    "feedback": "",
    "eq_input": "",           # the text_input for equation will use this key
    "user_answer_input": "",  # the answer text_input will use this key
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------- Callbacks ----------
def on_set_equation():
    expr = st.session_state.eq_input.strip()
    st.session_state.feedback = ""
    if expr == "":
        st.session_state.feedback = "Please enter an equation first."
        return
    try:
        result = safe_eval(expr)
    except ValueError as e:
        st.session_state.correct_answer = None
        st.session_state.eq_text = ""
        st.session_state.feedback = f"Invalid equation: {e}"
        return
    st.session_state.correct_answer = result
    st.session_state.eq_text = expr
    st.session_state.user_answer_input = ""
    st.session_state.feedback = "Equation accepted — now enter your answer."

def on_check_answer():
    user_ans = st.session_state.user_answer_input
    if user_ans is None or str(user_ans).strip() == "":
        st.session_state.feedback = "Please type an answer first."
        return
    # parse user's answer safely (accept numeric expressions)
    try:
        user_val = safe_eval(str(user_ans))
    except ValueError:
        try:
            user_val = float(user_ans)
        except Exception:
            st.session_state.feedback = "Could not parse your answer as a number. Try `1.5` or `3/4`."
            return

    correct = st.session_state.correct_answer
    if correct is None:
        st.session_state.feedback = "No valid equation is set."
        return

    # integer-friendly comparison
    if math.isclose(correct, round(correct), rel_tol=1e-12, abs_tol=1e-12):
        if math.isclose(user_val, round(correct), rel_tol=1e-9, abs_tol=1e-9):
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = f"❌ Incorrect. The correct answer is {round(correct)}."
    else:
        if math.isclose(user_val, correct, rel_tol=1e-9, abs_tol=1e-9):
            st.session_state.feedback = "✅ Correct (within tolerance)!"
        else:
            st.session_state.feedback = f"❌ Incorrect. The correct answer is {correct}."

def generate_easy_problem():
    """Return a simple expression string (easy): + - * or integer division result."""
    op = random.choice(["+", "-", "*", "/"])
    if op == "/":
        # create an integer division with exact result: dividend / divisor = quotient
        divisor = random.randint(1, 12)
        quotient = random.randint(1, 12)
        dividend = divisor * quotient
        expr = f"{dividend}/{divisor}"
    else:
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        expr = f"{a}{op}{b}"
    return expr

def on_random_problem():
    expr = generate_easy_problem()
    # Set the equation input widget's session state (allowed inside callback)
    st.session_state.eq_input = expr
    # Immediately evaluate & lock the equation (so it's ready to answer)
    try:
        result = safe_eval(expr)
    except ValueError as e:
        st.session_state.correct_answer = None
        st.session_state.eq_text = ""
        st.session_state.feedback = f"Generated invalid equation (unexpected): {e}"
        return
    st.session_state.correct_answer = result
    st.session_state.eq_text = expr
    st.session_state.user_answer_input = ""
    st.session_state.feedback = f"Random problem set: `{expr}` — enter your answer."

# ---------- UI ----------
col1, col2 = st.columns([3, 1])
with col1:
    # equation input widget uses key "eq_input"
    st.text_input("Enter a math equation", key="eq_input", placeholder="e.g. 3*(2+1)/4")
with col2:
    st.button("Set equation", on_click=on_set_equation)
    # new random-problem button placed in the same UI area
    st.button("Random easy math problem", on_click=on_random_problem)

if st.session_state.correct_answer is None:
    st.info("No valid equation set yet. Enter an expression and press **Set equation**.")
    st.markdown("**Examples:** `2+2`, `3*(4-1)/2`, `5**2`, `10//3`, `7 % 3`")
else:
    st.markdown(f"**Equation:** `{st.session_state.eq_text}`")

    # user answer widget uses key "user_answer_input"
    st.text_input("Your answer (type a number)", key="user_answer_input")

    st.button("Check Answer", on_click=on_check_answer)

    if st.button("Show Correct Answer"):
        correct = st.session_state.correct_answer
        if correct is None:
            st.session_state.feedback = "No correct answer to show."
        elif math.isclose(correct, round(correct), rel_tol=1e-12, abs_tol=1e-12):
            st.session_state.feedback = f"The correct answer is {round(correct)}."
        else:
            st.session_state.feedback = f"The correct answer is {correct}."

    # Removed the Clear button — instruct user how to try a new equation
    st.info("To try a new equation, replace the expression in the box at the top of the page and press **Set equation**.")

# Display feedback (map emoji prefixes to the right st.*)
fb = st.session_state.feedback
if fb:
    if fb.startswith("✅"):
        st.success(fb)
    elif fb.startswith("❌") or fb.startswith("Invalid") or fb.startswith("Could not"):
        st.error(fb)
    else:
        st.info(fb)
