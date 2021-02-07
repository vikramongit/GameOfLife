from board import Board


def main():
    user_rows = int(input('how many rows? '))
    user_columns = int(input('how many columns? '))

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


main()
