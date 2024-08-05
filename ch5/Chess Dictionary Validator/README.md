# Chess Dictionary Validator
![Chess Board]('D:\Study\Python Learning\back-end\basics\ch5\Chess Dictionary Validator\board.jpeg')

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Function Details](#function-details)
- [Validation Rules](#validation-rules)
- [Error Handling](#error-handling)
- [Future Improvements](#future-improvements)

## Description

The Chess Dictionary Validator is a Python project that provides a function to validate a chess board configuration. This function, `isValidChessBoard()`, takes a dictionary representation of a chess board and checks if it adheres to specific rules of chess piece placement and counts.

## Features

- Validates chess board configurations
- Checks for correct number and placement of kings
- Ensures piece counts are within legal limits
- Verifies that all pieces are on valid board positions

## Usage

To use the Chess Dictionary Validator, import the function into your Python script and call it with a dictionary representing a chess board:

```python
from chess_validator import isValidChessBoard

board = {
    "a8": "bking",
    "a1": "wking",
    # ... other positions ...
}

is_valid = isValidChessBoard(board)
print(is_valid)  # Output: True or False
```

## Validation Rules

The function checks the following rules:
1. Exactly one black king and one white king.
2. Each player has at most 16 pieces.
3. Each player has at most 8 pawns.
4. All pieces are on valid spaces from 'a1' to 'h8'.
5. Piece names start with 'w' or 'b' (for white or black) followed by the piece name.

## Error Handling
The function returns False if any of the following conditions are met:

- Invalid position on the board
- Invalid piece name
- Incorrect number of kings
- Too many pieces for a player
- Too many pawns for a player

## Future Improvements

- Add specific error messages for different types of invalidity
- Implement a chess board visualization feature
- Extend the function to check for valid piece movements
- Add unit tests for comprehensive function testing


