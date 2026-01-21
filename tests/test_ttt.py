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

    def test_check_win_X(self, board: list) -> None:
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

    def test_check_win_O(self, board: list) -> None:            
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
    
    def test_get_board(self, board: list, result_board: str) -> None:
        assert TicTacToe.get_board(board) == "\n " + result_board


class TestGetEmptyPos:
    
    @pytest.mark.parametrize("board, result", [
        
        (["-", "-", "-", # empty board, should return full list
          "-", "-", "-",
          "-", "-", "-"],
          list(range(0, 9))), 
        
        (["O", "-", "O", 
          "-", "X", "-",
          "X", "O", "-"],
          [1, 3, 5, 8]), 

        (["X", "X", "O", # full board, should return empty list
          "O", "O", "X",
          "X", "O", "O"],
          []), 

    ])

    def test_get_empty_pos(self, board: list, result: list) -> None:
        assert TicTacToe.get_empty_pos(board) == result


class TestEvaluate:
    @pytest.mark.parametrize("board, ai_symbol, human_symbol, result", [
        
        (["O", "O", "O",
          "X", "O", "X",
          "O", "X", "X"], 
          "O", "X", 10),

        (["X", "O", "O",
          "O", "X", "X",
          "O", "X", "O"], 
          "X", "O", 0),

        (["X", "O", "O",
          "X", "X", "O",
          "O", "X", "O"], 
          "X", "O", -10),

    ])

    def test_evaluate(self, board: list, ai_symbol: str, human_symbol: str, result: int) -> None:
        assert TicTacToe.evaluate(board, ai_symbol, human_symbol) == result


class TestMinimax:
      
    # in the test method, is_maximizing is given False. Thus simulating that the next move would be the players.
    @pytest.mark.parametrize("board, result", [ 
        
        (["O", "-", "O",
          "O", "X", "X",
          "-", "-", "X"], 10),

        (["O", "X", "O",
          "O", "-", "X",
          "X", "O", "X"], 0),

        (["O", "-", "O",
          "O", "X", "X",
          "X", "-", "X"], -10),

    ])

    def test_minimax(self, board: list, result: int) -> None:
        assert TicTacToe.minimax(board, "O", "X", False) == result