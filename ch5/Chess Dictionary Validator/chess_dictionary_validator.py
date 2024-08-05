def isValidChessBoard(board):
    valid_spaces = {f"{c}{r}" for c in "abcdefgh" for r in "12345678"}
    valid_pieces = {"king", "queen", "rook", "bishop", "knight", "pawn"}

    wKing = bKing = 0
    wPieces = bPieces = 0
    wPawns = bPawns = 0

    for position, piece in board.items():
        # Check if the position is valid
        if position not in valid_spaces:
            return False

        # Check if the piece name is valid
        if piece != " " and (
            len(piece) < 5 or piece[0] not in "wb" or piece[1:] not in valid_pieces
        ):
            return False

        if piece == "wking":
            wKing += 1
        elif piece == "bking":
            bKing += 1
        elif piece.startswith("w"):
            wPieces += 1
            if piece == "wpawn":
                wPawns += 1
        elif piece.startswith("b"):
            bPieces += 1
            if piece == "bpawn":
                bPawns += 1

    # Check king counts
    if wKing != 1 or bKing != 1:
        return False

    # Check piece counts
    if wPieces > 16 or bPieces > 16:
        return False

    # Check pawn counts
    if wPawns > 8 or bPawns > 8:
        return False

    return True


# Example usage:
board = {
    "a8": "bking",
    "b8": " ",
    "c8": " ",
    "d8": " ",
    "e8": " ",
    "f8": " ",
    "g8": " ",
    "h8": " ",
    "a7": " ",
    "b7": " ",
    "c7": " ",
    "d7": " ",
    "e7": " ",
    "f7": " ",
    "g7": " ",
    "h7": " ",
    "a6": " ",
    "b6": " ",
    "c6": " ",
    "d6": " ",
    "e6": " ",
    "f6": " ",
    "g6": " ",
    "h6": " ",
    "a5": " ",
    "b5": " ",
    "c5": " ",
    "d5": " ",
    "e5": " ",
    "f5": " ",
    "g5": " ",
    "h5": " ",
    "a4": " ",
    "b4": " ",
    "c4": " ",
    "d4": " ",
    "e4": " ",
    "f4": " ",
    "g4": " ",
    "h4": " ",
    "a3": " ",
    "b3": " ",
    "c3": " ",
    "d3": " ",
    "e3": " ",
    "f3": " ",
    "g3": " ",
    "h3": " ",
    "a2": " ",
    "b2": " ",
    "c2": " ",
    "d2": " ",
    "e2": " ",
    "f2": " ",
    "g2": " ",
    "h2": " ",
    "a1": "wking",
    "b1": " ",
    "c1": " ",
    "d1": " ",
    "e1": " ",
    "f1": " ",
    "g1": " ",
    "h1": " ",
}

print(isValidChessBoard(board))  # Output: True or False
