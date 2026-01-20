import random

class TicTacToe():

    LINE = "\n" + "-" * 30
    WIN_COMBINATIONS: list[list[int]] = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows 
                                         [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
                                         [0, 4, 8], [2, 4, 6]] # Diagonals

    def __init__(self):
        self.board: list[str] =  ["-", "-", "-",
                                  "-", "-", "-",
                                  "-", "-", "-"]
        
        self.is_player_X: bool = True

        self.SYMBOLS = ["X", "O"]

    # =================== LOGIC ===================
    def get_computer_pos(self) -> str:
        pass

    def get_human_pos(self) -> str:
        pass

    @staticmethod
    def check_win(board: list) -> str | None:
        return None

    def play(self) -> None:
        human_pos = self.get_human_pos()
        computer_pos = self.get_computer_pos()
        self.check_win(self.board)
        self.print_board(self.board)
    
    def start(self) -> None:
        self.menu()

        while (True):
            symbol = self.input_player_symbol()
            if symbol in self.SYMBOLS:
                self.is_player_X = True if symbol == "X" else False
                print(TicTacToe.LINE)
                break
            else:
                print("\nInvalid Input. Please try again.")
    
        self.play()

    # =================== UI ===================
    @staticmethod
    def menu():
        print(TicTacToe.LINE)
        print("\nTIC TAC TOE\n")

    @staticmethod
    def input_player_symbol() -> str:
        human_symbol: str = input("Do you want to be X or O? (X/O): ").upper().strip()
        return human_symbol
        
    @staticmethod
    def print_board(board) -> str:
        updated_board: str = ""
        for index, row in enumerate(board):
            if index == 2 or index == 5 or index == 8: # Add a new Line
                updated_board += f"{row}\n"
            else:
                updated_board += f'{row} '
        return updated_board
    
    @staticmethod 
    def input_player_pos():
        pass