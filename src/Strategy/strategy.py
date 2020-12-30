import random

class Strategy:
    """
    Class decides computer's next move
    Basic implementation of the strategy design pattern - https://refactoring.guru/design-patterns/strategy
    """

    def next_move(self, board):
        """
        Return the computer's next move
        """
        # TODO Acts like an abstract base class
        raise Exception('Subclass strategy in order to implement computer play!')



class RandomMoveStrategy(Strategy):
    def next_move(self, board):
        """
        Make a random, but valid move
        """
        # Store possible moves here
        available_moves = []

        for col in range(board.col_count):  # 0 - 6
                if board.is_free( col):
                    available_moves.append(col)
        # Pick one of the available moves
        move = random.choice(available_moves)
        #print(move)
        return board.move(move, 'O')
