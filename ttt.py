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

        # Check if any win combinations are met
        for win_combination in TicTacToe.WIN_COMBINATIONS:
                # Check if X won
                if all(board[i] == "X" for i in win_combination):
                    return "X"
        
                # Check if O won
                elif all(board[i] == "O" for i in win_combination):
                    return "O"
        
        # Check Draw
        if not "-" in board:
            return "DRAW"

        # Continue Game
        return None

    # Game Loop
    def play(self) -> None:
        while True:
            board = self.board
            # Checks if Player input is valid & if the position is empty
            while True:
                try:
                    print(self.print_board(board))
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
    
            # Check if there is a winner
            winner = self.check_win(board)
            if winner:
                print(TicTacToe.LINE)
                print("\n GAME OVER")
                print(self.print_board(board))

                match winner:
                    case "X":
                        print("Player has won!" if self.is_player_X else "Computer has won!")
                    case "O":
                        print("Computer has won!" if self.is_player_X else "Player has won!")
                    case "DRAW":
                        print("Player and Computer tied!")

                print(TicTacToe.LINE)
                break
            print(TicTacToe.LINE)
    
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