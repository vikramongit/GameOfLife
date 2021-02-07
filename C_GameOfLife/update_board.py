def update_board(self):
    print('updating board')
    goes_alive = []
    gets_killed = []

    for row in range(len(self._grid)):
        for column in range(len(self._grid[row])):

            check_neighbour = self.check_neighbour(row, column)

            living_neighbours_count = []

            for neighbour_cell in check_neighbour:
                if neighbour_cell.is_alive():
                    living_neighbours_count.append(neighbour_cell)

            cell_object = self._grid[row][column]
            status_main_cell = cell_object.is_alive()

            if status_main_cell:
                if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                    gets_killed.append(cell_object)

                if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                    goes_alive.append(cell_object)

            else:
                if len(living_neighbours_count) == 3:
                    goes_alive.append(cell_object)

    for cell_items in goes_alive:
        cell_items.set_alive()

    for cell_items in gets_killed:
        cell_items.set_dead()
