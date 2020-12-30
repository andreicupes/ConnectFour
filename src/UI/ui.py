from Strategy.strategy import *
from Game.game import *


class UI:
    def __init__(self):
        self._strategy = RandomMoveStrategy()
        self._game = Game(self._strategy)

    def read_human_move(self):
        # TODO Add error handling
        coord = input('where to play>')
        right=False

        while not right:
            if '1'<=coord<='7':
                row = int(coord)
                return row
            else:
                print('Wrong input!')
                coord = input('where to play>')

    def start(self):
        finished = False
        human_turn = True

        while not finished:
            # Print the board state
            if self._game.board.checkOWin() is True:
                print('Computer wins')
                print(self._game.board)
                return
            elif self._game.board.checkXWin() is True:
                print('You win')
                print(self._game.board)
                return
            else:
                print(self._game.board)

            if human_turn:
                coord = self.read_human_move()
                # print(coord)
                if self._game.human_move(coord) is False:
                    print('You wins!')

                    return
            else:
                if self._game.computer_move() is False:
                    print('All you base are belong to us!')

                    return
            human_turn = not human_turn


ui = UI()
ui.start()