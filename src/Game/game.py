from Board.board import Board

class Game:
    def __init__(self, strategy):
        self._board = Board()
        self._strategy = strategy

    @property
    def board(self):
        return self._board

    def human_move(self, x):
        # TODO Change so that human can also play with 'O'
        return self._board.move(x, 'X')

    def computer_move(self):
        return self._strategy.next_move(self._board)
