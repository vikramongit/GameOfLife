def check_neighbour(self, check_row, check_column):
    search_min = -1
    search_max = 2

    neighbour_list = []
    for row in range(search_min, search_max):
        for column in range(search_min, search_max):
            neighbour_row = check_row + row
            neighbour_column = check_column + column

            valid_neighbour = True

            if neighbour_row == check_row and neighbour_column == check_column:
                valid_neighbour = False
            if neighbour_row < 0 or neighbour_row >= self._rows:
                valid_neighbour = False

            if neighbour_column < 0 or neighbour_column >= self._columns:
                valid_neighbour = False

            if valid_neighbour:
                neighbour_list.append(self._grid[neighbour_row][neighbour_column])
    return neighbour_list
