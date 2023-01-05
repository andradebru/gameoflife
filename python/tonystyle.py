# game of life rules
# A live cell dies if it has fewer than two live neighbors.
# A live cell with two or three live neighbors lives on to the next generation.
# A live cell with more than three live neighbors dies.
# A dead cell will be brought back to live if it has exactly three live neighbors.

def init_matrix():
    return [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
]

matrix = init_matrix()

def print_matrix(matrix):
    D = {0: '-', 1: 'O'}
    for i in range(len(matrix)):
        print(''.join([D[e] for e in matrix[i]]))

def count_alive_neighbours(matrix, i, j):
    possible_neighbour_position = [
            (-1,-1), (-1,0), (-1,1), # (o--) (-o-) (--o)
            (0,-1), (0,1),
            (1,-1), (1,0), (1,1)
        ]
    neighbour_position = [
        (i+pnp[0], j+pnp[1])
        for pnp in possible_neighbour_position
        if 0 <= i+pnp[0] < len(matrix)
        and 0 <= j+pnp[1] < len(matrix[0])
    ]
    return len([1 for np in neighbour_position if matrix[np[0]][np[1]] == 1])

def update_matrix(matrix):
    new_matrix = [[0 for e in line] for line in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            alive_neighbours = count_alive_neighbours(matrix, i, j)
            if matrix[i][j] == 1:
                if alive_neighbours == 0 or alive_neighbours == 1:
                    new_matrix[i][j] = 0
                elif alive_neighbours >= 4:
                    new_matrix[i][j] = 0
                else:
                    new_matrix[i][j] = 1
            else:
                if alive_neighbours == 3:
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0
    return new_matrix

while True:
    print_matrix(matrix)
    matrix = update_matrix(matrix)
