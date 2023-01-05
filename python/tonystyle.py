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

def update_matrix(): 
    return matrix

matrix = init_matrix()

def print_matrix(matrix):
    D = {0: '-', 1: 'O'}
    for i in range(len(matrix)):
        print(''.join([D[e] for e in matrix[i]]))

def update_matrix():
    return 0

while True:
    print_matrix(matrix)
    matrix = update_matrix(matrix)
