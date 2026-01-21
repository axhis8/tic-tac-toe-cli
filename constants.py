from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MIDDLE = 2
    IMPOSSIBLE = 3

class Ending(Enum):
    X_WON = "X"
    O_WON = "O"
    DRAW = "DRAW"