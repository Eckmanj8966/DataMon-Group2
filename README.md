# DataMon-Group2
- **What worked:**
The Menu and Answer Checker give the requested results when prompted. 
(E.c. when the user enter a math problem, it asks them for the answer and gives feedback depending on if it was correct or incorrect.)
- **What Didn't:**
At the moment, if the user doesn't enter the correct type of character (e.g. enter a number between 1-4 and they enter "b"), it would crash the program.
- **What to do differently (next steps):**
The next steps would be adding memory bank as well as the number guesser, while also making improvements to menus and user experience. Change function name from "datamon_functions.py" to "answer_checker.py".


## User Stories:
1. Answer Checker:
User inputs math problems → program checks correctness.
Adaptation: program can generate random math problems instead of relying on parent input.
2. Memory Bank:
Original: parent stored problems for child to solve later.
Adaptation: program generates and stores problems for recall/redo.
3. Number Guesser:
Gamemode where user tries to guess a secret number with feedback.
user selects a random secret number so that the user can play a game with feedback
the user guesses numbers, program picks apart the question so that the user solves not just for the answer, but ensures that key also understand the question as a whole.

Summary of What the Program Does: 
In the beginning the program starts with a main menu (4 choices).

Answer Checker (choice 1) lets the user:
Pick an operation (+, -, *, /). Enter numbers.
Try to solve the problem.Get feedback if correct or not.

Memory Bank (choice 2) → Not built yet (just prints "DEBUG: 2").
Memory Bank will store problems automatically + allow playback (user can solve stored problems later).

Number Guesser (choice 3) → Not built yet (just prints "DEBUG: 3").
Number Guesser game will – random secret number, user guesses with feedback, game ends when guessed, attempts displayed.

Exit (choice 4) → Ends the program.
