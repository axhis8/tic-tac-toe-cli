from src.tictactoe import TicTacToe
from src.constants import Ending
import pytest


class TestCheckWinX:

    @pytest.mark.parametrize("board", [
        (["X", "X", "X", # horizontal top
          "-", "-", "O",
          "-", "-", "O"]),

        (["O", "O", "X", # horizontal middle
          "X", "X", "X",
          "O", "-", "O"]),

        (["X", "O", "X", # horizontal bottom
          "O", "-", "O",
          "X", "X", "X"]),

        (["X", "O", "X", # vertical left
          "X", "-", "O",
          "X", "O", "O"]),

        (["O", "X", "-", # vertical middle
          "O", "X", "O",
          "X", "X", "O"]),

        (["X", "O", "X", # vertical right
          "O", "O", "X",
          "O", "X", "X"]),

        (["X", "O", "X", # diagonal right
          "O", "X", "O",
          "O", "O", "X"]),

        (["X", "O", "X", # diagonal left
          "-", "X", "O",
          "X", "O", "-"])
    ])

    def test_check_win(self, board) -> None:
        assert TicTacToe.check_win(board) == Ending.X_WON


class TestCheckWinO:

    @pytest.mark.parametrize("board", [
        (["O", "O", "O", # horizontal top
          "-", "-", "X",
          "-", "-", "X"]),

        (["X", "X", "O", # horizontal middle
          "O", "O", "O",
          "X", "-", "X"]),

        (["O", "X", "O", # horizontal bottom
          "X", "-", "X",
          "O", "O", "O"]),

        (["O", "X", "O", # vertical left
          "O", "-", "X",
          "O", "X", "X"]),

        (["X", "O", "-", # vertical middle
          "X", "O", "X",
          "O", "O", "X"]),

        (["O", "X", "O", # vertical right
          "X", "X", "O",
          "X", "O", "O"]),

        (["O", "X", "O", # diagonal right
          "X", "O", "X",
          "X", "X", "O"]),

        (["O", "X", "O", # diagonal left
          "-", "O", "X",
          "O", "X", "-"])
    ])

    def test_check_win_diagonal_second(self, board) -> None:            
        assert TicTacToe.check_win(board) == Ending.O_WON
    

class TestGetBoard:

    @pytest.mark.parametrize("board, result_board", [
        (["-", "-", "-", # empty
          "-", "-", "-",
          "-", "-", "-"],

          "- | - | -\n " \
          "- | - | -\n " \
          "- | - | -\n "),

        (["X", "-", "-", # normal
          "-", "X", "-",
          "O", "O", "X"],

          "X | - | -\n " \
          "- | X | -\n " \
          "O | O | X\n "),

        (["O", "O", "O", # full
          "O", "X", "X",
          "X", "O", "X"],

          "O | O | O\n " \
          "O | X | X\n " \
          "X | O | X\n "),
    ])
    
    def test_get_board_empty(self, board, result_board) -> None:
        assert TicTacToe.get_board(board) == "\n " + result_board