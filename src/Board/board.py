from texttable import Texttable
import random


class Board:
    def __init__(self):
        # TODO Have a variable number of rows and columns
        self._rows = 6
        self._columns = 7

        # Empty squares marked with None
        self._data = [[' ' for j in range(self._columns)] for i in range(self._rows)]

    @property
    def row_count(self):
        return self._rows

    @property
    def col_count(self):
        return self._columns

    def get_data(self):
        return self._data

    def get(self, x, y):
        """
        Return symbol at position [x,y] on board

            ' '     -> empty square
            'X', 'O' -> symbols

        """
        return self._data[x][y]

    def is_free(self, x):
        return self.get(0,x) == ' '

    def move(self, x, symbol):
        if self._data[0][int(x)] != ' ':
            print('board is full')
        ok = 0
        # Mark the rest of the choco square to the right and below
        for row in range(self._rows - 1):
            if self._data[row + 1][int(x)] != ' ':
                self._data[row][int(x)] = symbol
                ok += 1
                break
        if ok == 0:
            self._data[self._rows - 1][int(x)] = symbol

        # Mark the new move on the board

    def __str__(self):
        t = Texttable()
        t.header(['1', '2', '3', '4', '5', '6', '7'])
        for row in range(6):
            row_data = []

            for index in self._data[row]:
                if index == ' ':
                    row_data.append(' ')
                else:
                    row_data.append(index)

            t.add_row(row_data)

        return t.draw()

    def checkWin(self,symbol):
        board = self._data
        boardHeight = len(board[0])
        boardWidth = len(board)
        tile = symbol
        # check horizontal spaces
        for y in range(boardHeight):
            for x in range(boardWidth - 3):
                if board[x][y] == tile and board[x + 1][y] == tile and board[x + 2][y] == tile and board[x + 3][y] == tile:
                    return True

        # check vertical spaces
        for x in range(boardWidth):
            for y in range(boardHeight - 3):
                if board[x][y] == tile and board[x][y + 1] == tile and board[x][y + 2] == tile and board[x][
                    y + 3] == tile:
                    return True

        # check / diagonal spaces
        for x in range(boardWidth - 3):
            for y in range(3, boardHeight):
                if board[x][y] == tile and board[x + 1][y - 1] == tile and board[x + 2][y - 2] == tile and board[x + 3][
                    y - 3] == tile:
                    return True

        # check \ diagonal spaces
        for x in range(boardWidth - 3):
            for y in range(boardHeight - 3):
                if board[x][y] == tile and board[x + 1][y + 1] == tile and board[x + 2][y + 2] == tile and board[x + 3][
                    y + 3] == tile:
                    return True

        return False

    def is_full(self):
        for i in range(1,7):
            if self._data[0][i]==' ':
                return False
        return True

