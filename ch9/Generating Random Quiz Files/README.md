# Random Quiz Generator

This Python script generates multiple quiz files with questions about US state capitals, along with their corresponding answer keys. Each quiz is unique, with questions and answer choices presented in random order.

## Features

- Generates a specified number of quiz files.
- Each quiz contains questions about the capitals of all 50 US states.
- The order of the questions and answer choices are randomized.
- An answer key is provided for each quiz.

## Requirements

- Python 3.x

## Usage

1. Ensure you have Python 3 installed on your machine.
2. Save the script to a file, e.g., `randomQuizGenerator.py`.
3. Run the script:

   ```sh
   python3 randomQuizGenerator.py
   ```

4. The script will generate 35 quiz files (`capitalsquiz1.txt` to `capitalsquiz35.txt`) and their corresponding answer keys (`capitalsquiz_answers1.txt` to `capitalsquiz_answers35.txt`) in the same directory.

## Code Explanation

### Quiz Data

The `CAPITALS` dictionary contains US states as keys and their capitals as values.

### Main Logic

The script generates a specified number of quiz files (`no_of_quiz_files`). For each quiz:

1. **File Creation**: Creates a quiz file and an answer key file.
2. **Quiz Header**: Writes a header to the quiz file.
3. **Question Generation**: 
   - Shuffles the order of the states.
   - For each state, selects the correct capital and three random incorrect capitals.
   - Writes the question and answer choices to the quiz file.
   - Writes the correct answer to the answer key file.

## Areas for Improvement

1. **Customization**: Allow the user to specify the number of quiz files and questions per quiz.
2. **Difficulty Levels**: Implement different difficulty levels by varying the number of options and including hints.
3. **Question Variety**: Add different types of questions, such as multiple-choice, true/false, and fill-in-the-blank.
4. **User Interface**: Create a graphical user interface (GUI) to make the quiz generation process more interactive and user-friendly.
