# A live cell dies if it has fewer than two live neighbors.
# A live cell with two or three live neighbors lives on to the next generation.
# A live cell with more than three live neighbors dies.
# A dead cell will be brought back to live if it has exactly three live neighbors.

def init_matrix():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
]

matrix = init_matrix()

def count_live_neighbours(matrix, i, j):
    return 0

def print_matrix(matrix):
    D = {0: '-', 1: 'O'}
    for i in range(len(matrix)):
        print(''.join([D[e] for e in matrix[i]]))

def update_matrix():
    new_matrix = [[0 for e in line] for line in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count_live_neighbours = count_live_neighbours(matrix, i, j)
            if matrix[i][j] == 1:
                if count_live_neighbours == 0 or count_live_neighbours == 1:
                    new_matrix[i][j] = 0
                elif count_live_neighbours >= 4:
                    new_matrix[i][j] = 0
                else:
                    new_matrix[i][j] = 1
            else:
                if count_live_neighbours == 3:
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0
    return new_matrix

def update_matrix():
    return 0

while True:
    print_matrix(matrix)
    matrix = update_matrix(matrix)
