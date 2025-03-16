# easy:
board = [
    [5, 4, 6, 2, None, 7, None, 8, None],
    [None, 1, None, 8, 4, 5, 2, 3, None],
    [None, 3, 8, None, None, None, 4, None, 7],
    [1, None, 4, 5, 7, None, None, 2, None],
    [9, 7, None, None, None, 6, None, None, 3],
    [None, 5, None, None, 9, 2, None, 6, None],
    [None, None, None, None, 1, 4, 3, None, None],
    [None, 8, None, 3, None, None, None, None, 5], 
    [None, None, 7, None, None, None, 1, None, 2]
]


# board = [
#     [4, None, 8, None, None, None, None, 2, 1],
#     [None, None, 1, None, 9, None, None, None, None],
#     [None, None, 3, None, None, 4, None, None, 7],
#     [None, None, 5, None, None, None, 8, None, None],
#     [None, 2, None, None, 1, 3, None, None, None],
#     [None, None, None, None, None, 5, None, 7, 4],
#     [None, None, None, None, None, None, 7, None, None],
#     [None, None, None, 7, 2, None, 6, 5, None],
#     [None, 8, None, None, 3, None, None, None, None]
# ]

symbols = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def get_row_nums(r): # O(n)
    usable_nums = symbols - set(board[r]) - {"-"}
    return usable_nums

def get_col_nums(c): # O(n)
    column = {row[c] for row in board}
    usable_nums = symbols - column - {"-"}
    return usable_nums

def get_square_nums(r, c): # O(n)
    corner_r = (r // 3) * 3
    corner_c = (c // 3) * 3

    square = {
        board[corner_r][corner_c], board[corner_r][corner_c + 1], board[corner_r][corner_c + 2],
        board[corner_r + 1][corner_c], board[corner_r + 1][corner_c + 1], board[corner_r + 1][corner_c + 2],
        board[corner_r + 2][corner_c], board[corner_r + 2][corner_c + 1], board[corner_r + 2][corner_c + 2],
    }

    usable_nums = symbols - square - {"-"}
    return usable_nums


# print(get_square_nums(0, 6))
possible_values_map = {}

def fill_solo(possible_values_map):

    iter = 0
    change_made = False

    while iter == 0 or change_made == True:
        
        change_made = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == None:
                    possible_values = get_row_nums(i) & get_col_nums(j) & get_square_nums(i, j)
                    possible_values_map[(i,j)] = possible_values
                    # print(f"{i, j}: {possible_values}")
                    if len(possible_values) == 1:
                        board[i][j] = possible_values.pop()
                        del possible_values_map[(i,j)]
                        change_made = True
        iter += 1
    return possible_values_map

possible_values_map = fill_solo(possible_values_map)
if len(possible_values_map) == 0:
    print("complete")
    print(board)