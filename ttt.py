import random

class TicTacToe():

    LINE = "\n" + "-" * 30
    INVALID_INPUT = "\nInvalid Input. Please try again."
    WIN_COMBINATIONS: list[list[int]] = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows 
                                         [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
                                         [0, 4, 8], [2, 4, 6]] # Diagonals

    def __init__(self):
        self.board: list[str] =  ["-", "-", "-",
                                  "-", "-", "-",
                                  "-", "-", "-"]
        self.is_player_X: bool = True

    # =================== LOGIC ===================
    def get_computer_pos(self) -> int:
        while True:
            pos = random.randint(0, 8)
            if self.check_pos_empty(pos): return pos

    def check_pos_empty(self, pos: int) -> bool:
        if not self.board[pos] == "-": return False
        return True

    @staticmethod
    def check_win(board: list) -> str | None:
        return None

    def play(self) -> None:
        while True:
            # Checks if Player input is valid & if the position is empty
            while True:
                try:
                    print(self.print_board(self.board))
                    human_pos: int = int(self.get_human_pos())
                    if human_pos > 0 and human_pos < 9:
                        human_pos -= 1
                        if self.check_pos_empty(human_pos):
                            break
                        else:
                            print("That Position is already occupied.")

                except ValueError:
                    print(TicTacToe.INVALID_INPUT)
            
            # Get Computer board position
            computer_pos = self.get_computer_pos()

            # Update Board
            self.board[human_pos] = "X" if self.is_player_X else "O"
            self.board[computer_pos] = "O" if self.is_player_X else "X"
    
            # Check if there are any win combinations
            if self.check_win(self.board) == "X":
                print(TicTacToe.LINE)
                print("\nPlayer has won!" if self.is_player_X else "Computer has won!")
                print(TicTacToe.LINE)
                break
            elif self.check_win(self.board) == "O":
                print(TicTacToe.LINE)
                print("\nComputer has won!" if self.is_player_X else "Player has won!")
                print(TicTacToe.LINE)
                break
            elif self.check_win(self.board) == None:
                print(TicTacToe.LINE)
                print("\nPlayer and Computer tied!")
                print(TicTacToe.LINE)
                break
    
    def start(self) -> None:
        self.menu()

        while (True):
            symbol = self.input_player_symbol()
            if symbol in "XO":
                self.is_player_X = True if symbol == "X" else False
                print(TicTacToe.LINE)
                break
            else:
                print(TicTacToe.INVALID_INPUT)
    
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
            if index == 2 or index == 5 or index == 8: # Add new Line
                updated_board += f"{row}\n "
            else:
                updated_board += f'{row} | '
        return "\n " + updated_board
    
    @staticmethod 
    def get_human_pos() -> str:
        return input("Set your Symbol (1-9): ")