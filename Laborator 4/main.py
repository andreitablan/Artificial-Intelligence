def block(matrix, block_i, block_j):
    matrix[block_i][block_j] = -1


def place_Queen(matrix, size, x, y):
    if matrix[x][y] != -1:
        matrix[x][y] = 1
        for i in range(0, size):
            for j in range(0, size):
                if x != i and j != y:
                    if i == x or j == y:
                        matrix[i][j] = -1
                    if x - y == i - j or x + y == i + j:
                        matrix[i][j] = -1
    states = []
    for i in range(size):
        aux = []
        aux.append(i)
        aux.append(matrix[i])
        states.append(aux)
    return states


if __name__ == '__main__':

    size = int(input("Enter number of queens n="))
    matrix = [[0 for x in range(size)] for y in range(size)]
    number_of_constrains = int(input("Enter number of constrains number="))
    for constrain in range(number_of_constrains):
        block_i, block_j = input("Enter 'line column' to constrain").split(' ')
        block(matrix, int(block_i), int(block_j))
    states = []
    # initial state
    for i in range(size):
        aux = []
        aux.append(i)
        aux.append(matrix[i])
        states.append(aux)

    states = place_Queen(matrix, size, 1, 2)
    print(states)
