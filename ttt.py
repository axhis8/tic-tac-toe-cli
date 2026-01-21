from constants import Difficulty, Ending
import random

class TicTacToe():

    PLAYER: str = "player"
    COMPUTER: str = "computer"
    LINE: str = "\n" + "-" * 30
    INVALID_INPUT: str = "\nInvalid Input. Please try again."
    WIN_COMBINATIONS: list[list[int]] = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows 
                                         [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
                                         [0, 4, 8], [2, 4, 6]] # Diagonals

    def __init__(self) -> None:
        self.board: list[str] =  ["-", "-", "-",
                                  "-", "-", "-",
                                  "-", "-", "-"]
        self.players: dict[str, str] = {TicTacToe.PLAYER: "X", TicTacToe.COMPUTER: "O"}
        self.player_turn: bool = True
        self.difficulty: Difficulty = Difficulty.EASY

    # =================== MINIMAX AI ===================    
    @staticmethod
    def get_empty_pos(board: list) -> list:
        empty_board_index: list[int] = []
        for index, pos in enumerate(board):
            if pos == "-":
                empty_board_index.append(index)
        return empty_board_index
    
    # We evaluate what is the best move for the AI, as the AI can't "see" the best move, but it can judge with numbers. So the highest points shows AI the best move, while the lowest the worst. It is, so the AI can actually see & judge.
    @staticmethod
    def evaluate(board: list, ai_symbol: str, human_symbol: str) -> int | None:
        winner: str = TicTacToe.check_win(board)

        if winner == ai_symbol:
            return 10
        elif winner == Ending.DRAW:
            return 0
        elif winner == human_symbol:
            return -10
        else:
            return None
    
    # It is a static method, so it doesn't call for every instance, which would result lag
    @staticmethod
    def minimax(board: list, ai_symbol: str, human_symbol: str, is_maximizing: bool) -> int:
        winner: str = TicTacToe.check_win(board)
        # If the game is over, return - and when this method calls itself, it shows that the best score is given through the move-simulation, and the AI can stop & continue best possible move (which would only return Ending.DRAW or it's symbol, but never one which the AI would loose with)
        if winner is not None: 
            return TicTacToe.evaluate(board, ai_symbol, human_symbol)
        
        if is_maximizing:
            best_score: float = -float('inf') # Set the score to low as possible - a boilerplate to start on for the for loop, so anything higher than this might be the better result (with max() tho, we get the best possible result, with comparing each move and the moves before)
            for move in TicTacToe.get_empty_pos(board): # Get all empty Positions in board
                board[move] = ai_symbol # Simulate Position
                score: int = TicTacToe.minimax(board, ai_symbol, human_symbol, False) # Switch turn, so the AI simulates humans, who would try to get the worst possible outcome for the AI
                board[move] = "-" # Reset Position, so it wouldn't show on the real board and to simulate for next possible moves
                best_score = max(score, best_score) # Get best Position, compared to the simulation of the last move
        
        else:
            best_score: float = float('inf')
            for move in TicTacToe.get_empty_pos(board):
                board[move] = human_symbol
                score: int = TicTacToe.minimax(board, ai_symbol, human_symbol, True) 
                board[move] = "-"
                best_score = min(score, best_score)
        
        return best_score
    # So each move simulation gets a point (-10 - which means it would make us loose, 0 - which returns a draw and 10 which would make the AI win) and the AI get's the moves with 10 or if not possible, 0. But never -10. (because it already simulated all possible moves and outcomes & TicTacToe is a simple game where even with the best moves, you may get max a draw)
    
    def get_advanced_computer_pos(self) -> int:
        best_score: float = -float('inf') # boilerplate, as explained in the minimax() method
        best_move_index: int = -1 # boilerplate: -1 as it's not a valid move/field
        for field_index in TicTacToe.get_empty_pos(self.board):

            self.board[field_index] = self.players[TicTacToe.COMPUTER] # 1. Simulate a move in the empty field
            score = TicTacToe.minimax(self.board, self.players[TicTacToe.COMPUTER], self.players[TicTacToe.PLAYER], is_maximizing=False) # 2. Call the minimax() method to get the highest score if we make this move, we give is_maximizing=False, because the next move would be the human
            self.board[field_index] = "-" # Delete last move, so it won't appear on the real one, as this is an simulation

            # Compares the score from the minimax() method, if it was better than the last move so we know the best possible move, as it also saves the index of the move
            if score > best_score: 
                best_move_index = field_index
                best_score = score

        return best_move_index
        
    # =================== LOGIC =================== 
    def get_middle_computer_pos(self) -> int:
        rand_difficulty: int = random.randint(0, 1)
        if rand_difficulty:
            return self.get_advanced_computer_pos()
        elif not rand_difficulty:
            return self.get_easy_computer_pos()

    def get_easy_computer_pos(self) -> int:
        while True:
            pos: int = random.randint(0, 8)
            if self.check_pos_empty(pos): return pos
    
    def get_difficulty_computer(self, difficulty: int) -> int:
        match difficulty:
            case Difficulty.EASY:
                return self.get_easy_computer_pos()
            case Difficulty.MIDDLE:
                return self.get_middle_computer_pos()
            case Difficulty.IMPOSSIBLE:
                return self.get_advanced_computer_pos()

    # Checks if Player input is valid & if the position is empty
    def get_valid_human_pos(self) -> int:
        while True:
            try:
                human_pos: int = int(TicTacToe.get_input_human_pos())
                if human_pos > 0 and human_pos < 10:
                    human_pos -= 1
                    if self.check_pos_empty(human_pos):
                        return human_pos
                    else:
                        print("That Position is already occupied.\n")
                else:
                    print(TicTacToe.INVALID_INPUT)
            except ValueError:
                print(TicTacToe.INVALID_INPUT)

    # Check if a Position is empty for placing validation
    def check_pos_empty(self, pos: int) -> bool:
        if not self.board[pos] == "-": return False
        return True

    @staticmethod
    def check_win(board: list) -> str | None:

        # Check if any win combinations are met
        for win_combination in TicTacToe.WIN_COMBINATIONS:
                # Check if X won
                if all(board[i] == "X" for i in win_combination):
                    return Ending.X_WON
        
                # Check if O won
                elif all(board[i] == "O" for i in win_combination):
                    return Ending.O_WON
        
        # Check Draw
        if not "-" in board:
            return Ending.DRAW

        # Continue Game
        return None

    def start(self) -> None:
        TicTacToe.print_menu()

        # Let human choose his symbol
        while True:
            symbol = TicTacToe.get_input_player_symbol()
            if symbol in self.players.values():
                if symbol == "X":
                    self.players[TicTacToe.PLAYER] = "X"
                    self.players[TicTacToe.COMPUTER] = "O"
                    self.player_turn = True
                else:
                    self.players[TicTacToe.PLAYER] = "O"
                    self.players[TicTacToe.COMPUTER] = "X"
                    self.player_turn = False
                break
            else:
                print(TicTacToe.INVALID_INPUT)

        while True:
            try:
                difficulty: int = int(TicTacToe.get_input_player_difficulty())
                if difficulty in (d.value for d in Difficulty):
                    self.difficulty = Difficulty(difficulty)
                    break
                else:
                    print(TicTacToe.INVALID_INPUT)
            except ValueError:
                print(TicTacToe.INVALID_INPUT)
    
        self.play()

    # Game Loop
    def play(self) -> None:
        while True:
            
            # Print board
            if self.player_turn: print(TicTacToe.LINE) 
            if self.player_turn: print(TicTacToe.get_board(self.board))

            # Get board position
            placed_pos: int = self.get_valid_human_pos() if self.player_turn else self.get_difficulty_computer(self.difficulty)

            # Set board position
            symbol = self.players[TicTacToe.PLAYER if self.player_turn else TicTacToe.COMPUTER]
            self.board[placed_pos] = symbol

            # Check if there is a winner
            if TicTacToe.check_win(self.board): break

            # Change turn (boolean flip)
            self.player_turn = not self.player_turn

        winner = TicTacToe.check_win(self.board)
        self.print_end_game_menu(winner)

    # =================== UI ===================
    @staticmethod
    def print_menu() -> None:
        print(TicTacToe.LINE)
        print("\nTIC TAC TOE\n")

    @staticmethod
    def get_input_player_symbol() -> str:
        human_symbol: str = input("Choose your Symbol (X/O): ").upper().strip()
        return human_symbol

    @staticmethod
    def get_input_player_difficulty() -> str:
        print("\nCHOOSE YOUR DIFFICULTY:")
        print("1. Easy")
        print("2. Middle")
        print("3. Impossible")

        difficulty: str = input("\nChoice (1 - 3): ").lower().strip()
        return difficulty
    
    @staticmethod
    def get_board(board) -> str:
        updated_board: str = ""
        for index, row in enumerate(board):
            if index == 2 or index == 5 or index == 8: # Add new Line
                updated_board += f"{row}\n "
            else:
                updated_board += f'{row} | '
        return "\n " + updated_board
    
    @staticmethod 
    def get_input_human_pos() -> str:
        return input("Place your Symbol (1-9): ")

    def print_end_game_menu(self, winner) -> None:
        print(TicTacToe.LINE)
        print("\n GAME OVER")
        print(TicTacToe.get_board(self.board))

        match winner:
            case Ending.X_WON:
                print("Player has won!" if self.players[TicTacToe.PLAYER] == "X" else "Computer has won!")
            case Ending.O_WON:
                print("Computer has won!" if self.players[TicTacToe.COMPUTER] == "O" else "Player has won!")
            case Ending.DRAW:
                print("Player and Computer tied!")

        print(TicTacToe.LINE)