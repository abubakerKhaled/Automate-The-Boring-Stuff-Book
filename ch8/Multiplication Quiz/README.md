# Multiplication Quiz

This is a simple Python program that quizzes the user on basic multiplication problems. The program presents a series of multiplication questions, and the user must answer them within a time limit. The user's score is displayed at the end.

## Features

- Randomly generated multiplication questions.
- Time limit of 8 seconds per question.
- A maximum of 3 attempts per question.
- Feedback on whether the answer is correct or incorrect.
- Final score displayed at the end.

## Requirements

- Python 3
- `pyinputplus` module

## Installation

1. Ensure you have Python 3 installed on your machine.
2. Install the `pyinputplus` module if you haven't already:

   ```sh
   pip install pyinputplus
   ```

## How to Use

1. Run the program.
2. Answer each multiplication question within the time limit.
3. After each question, the program will indicate if your answer was correct or incorrect.
4. At the end of the quiz, your final score will be displayed.

## Code Explanation

### Main Quiz Logic

The main logic for the quiz is contained in a loop that runs for a specified number of questions. It generates random multiplication questions, checks the user's answers, and keeps track of the score.

```python
import pyinputplus as pyip
import random
import time

num_of_questions = 10
correct_answers = 0

for question_number in range(num_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (question_number+1, num1, num2)

    try:
        pyip.inputStr(prompt, 
                      allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, 
                      limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_answers += 1
        time.sleep(1)

print("Score: %s / %s" % (correct_answers, num_of_questions))
```

### Explanation of Key Functions

- `random.randint(a, b)`: Generates a random integer between `a` and `b` (inclusive).
- `pyip.inputStr(prompt, allowRegexes, blockRegexes, timeout, limit)`: Prompts the user for input, with specific rules for allowed and blocked answers, a time limit, and a maximum number of attempts.
- `pyip.TimeoutException`: Raised when the user fails to answer within the time limit.
- `pyip.RetryLimitException`: Raised when the user exceeds the maximum number of attempts.

## Areas for Improvement

1. **Customization**: Allow the user to set the number of questions, time limit, and maximum number of attempts.
2. **Difficulty Levels**: Implement different difficulty levels with larger numbers and more complex problems.
3. **User Interface**: Create a graphical user interface (GUI) to make the quiz more interactive and visually appealing.
4. **Feedback Mechanism**: Provide more detailed feedback, such as the correct answer after a wrong attempt.

## Conclusion

This multiplication quiz is a fun and educational way to practice basic multiplication skills. The program can be further enhanced by adding customization options, difficulty levels, a graphical interface, and more detailed feedback.
