from enum import Enum
from typing import Final

# =========== States ==========    
class Difficulty(Enum):
    EASY = 1
    MIDDLE = 2
    IMPOSSIBLE = 3

class Ending(Enum):
    X_WON = "X"
    O_WON = "O"
    DRAW = "DRAW"

class Player(Enum):
    HUMAN = "human"
    COMPUTER = "computer"

# =========== UI Strings ==========    
LINE: Final = "\n" + "-" * 30
INVALID_INPUT: Final = "\nInvalid Input. Please try again."

# =========== Logic ==========    
WIN_COMBINATIONS: Final = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows 
                           [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
                           [0, 4, 8], [2, 4, 6]] # Diagonals
