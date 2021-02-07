from cell import Cell
from random import randint


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self):
        print('\n' * 1)
        print('printing board')
        for row in self._grid:
            for column in row:
                print(column.get_print_character(), end='')
            print()

    def _generate_board(self):
        for row in self._grid:
            for column in row:
                chance_number = randint(0, 2)
                if chance_number == 1:
                    column.set_alive()


class Solution:
    pass
