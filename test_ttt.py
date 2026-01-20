from ttt import TicTacToe

class TestCheckWinX:

    def test_check_win_horizontal_top(self) -> None:
        board = [["X", "X", "X"],
                 ["-", "-", "O"],
                 ["-", "-", "O"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_horizontal_middle(self) -> None:
        board = [["O", "O", "X"],
                 ["X", "X", "X"],
                 ["O", "-", "O"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_horizontal_bottom(self) -> None:
        board = [["X", "O", "X"],
                 ["O", "-", "O"],
                 ["X", "X", "X"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_vertical_first(self) -> None:
        board = [["X", "O", "X"],
                 ["X", "-", "O"],
                 ["X", "O", "O"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_vertical_second(self) -> None:
        board = [["O", "X", "-"],
                 ["O", "X", "O"],
                 ["X", "X", "O"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_vertical_third(self) -> None:
        board = [["X", "O", "X"],
                 ["O", "O", "X"],
                 ["O", "X", "X"]]
        assert TicTacToe.check_win(board) == "X"
    
    def test_check_win_diagonal_first(self) -> None:
        board = [["X", "O", "X"],
                 ["O", "X", "O"],
                 ["O", "O", "X"]]
        assert TicTacToe.check_win(board) == "X"

    def test_check_win_diagonal_second(self) -> None:
        board = [["X", "O", "X"],
                 ["-", "X", "O"],
                 ["X", "O", "-"]]
        assert TicTacToe.check_win(board) == "X"


class TestCheckWinO:

    def test_check_win_horizontal_top(self) -> None:
        board = [["O", "O", "O"],
                 ["-", "-", "X"],
                 ["-", "-", "X"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_horizontal_middle(self) -> None:
        board = [["X", "X", "O"],
                 ["O", "O", "O"],
                 ["X", "-", "X"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_horizontal_bottom(self) -> None:
        board = [["O", "X", "O"],
                 ["X", "-", "X"],
                 ["O", "O", "O"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_vertical_first(self) -> None:
        board = [["O", "X", "O"],
                 ["O", "-", "X"],
                 ["O", "X", "X"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_vertical_second(self) -> None:
        board = [["X", "O", "-"],
                 ["X", "O", "X"],
                 ["O", "O", "X"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_vertical_third(self) -> None:
        board = [["O", "X", "O"],
                 ["X", "X", "O"],
                 ["X", "O", "O"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_diagonal_first(self) -> None:
        board = [["O", "X", "O"],
                 ["X", "O", "X"],
                 ["X", "X", "O"]]
        assert TicTacToe.check_win(board) == "O"

    def test_check_win_diagonal_second(self) -> None:
        board = [["O", "X", "O"],
                 ["-", "O", "X"],
                 ["O", "X", "-"]]
        assert TicTacToe.check_win(board) == "O"
    

class TestPrintBoard:
    def test_print_board_empty(self) -> None:
        board: list[str] = ["-", "-", "-",
                            "-", "-", "-",
                            "-", "-", "-"]
        
        result_board: str = f'- - -\n' * 3
        assert TicTacToe.print_board(board) == result_board
    
    def test_print_board_X_example(self) -> None:
        board: list[str] = ["X", "-", "-",
                            "-", "X", "-",
                            "O", "O", "X"]
        
        result_board: str = "X - -\n" \
                            "- X -\n" \
                            "O O X\n"
        assert TicTacToe.print_board(board) == result_board

    def test_print_board_X_full(self) -> None:
        board: list[str] = ["O", "O", "O",
                            "O", "X", "X",
                            "X", "O", "X"]
        
        result_board: str = "O O O\n" \
                            "O X X\n" \
                            "X O X\n"
        assert TicTacToe.print_board(board) == result_board