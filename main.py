def initial_board():
    return [
        [ 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R' ],
        [ 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P' ],
        [ 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R' ]
    ]

board = initial_board()

for row in board:
    for cell in row:
        print(f'{cell} ', end='')
    print('')
