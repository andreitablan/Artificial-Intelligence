def block(matrix, block_i, block_j):
    matrix[block_i][block_j] = -1


def place_queen(states, size, x, y):
    if states[x][y] != -1:
        states[x][y] = 1
        for i in range(0, size):
            for j in range(0, size):
                if states[i][j] != 1:
                    if x != i and j != y:
                        if x - y == i - j or x + y == i + j:
                            states[i][j] = -1
                    if i == x or j == y:
                        states[i][j] = -1
                        #idee talban schimbam imediat

    return states


def print_states(states, size):
    for i in range(0, size):
        print(states[i])


def is_domain_empty(states, size, queen):
    for j in range(0, size):
        if states[queen][j] == 0:
            return False
    return True


def select_value_forward_checking(board, size, aux_states, states, queen):

    while not is_domain_empty(aux_states, size, queen):
        for j in range(0, size):
            if aux_states[queen][j] == 0:
                position = j
                break

        place_queen(aux_states,size,queen,position)
        print("position " , j)

        empty_domain = False

        for k in range(queen + 1, size):
            for b in range(0, size):
                if aux_states[k][b] == 0:
                    aux_states = place_queen(aux_states, size, k, b)
                    print_states(aux_states,size)
                    break

            empty_domain = True
            for b in range(0, size):
                if aux_states[k][b] != -1:
                    empty_domain = False
                    print("linia ", k, "am gasit un nr diferit de -1", k, b)
                    break

            if not empty_domain:
                break

        if empty_domain:
            for k in range(queen + 1, size):
                aux_states[k] = states[k]
            #queen=queen+1
            print("------------------")
            print_states(aux_states)
        else:
            return position
    return None


def generalized_lookahead(board, size, states):
    aux_states = states
    index = 0
    while size > index >= 0:
        j = select_value_forward_checking(board, size, aux_states, states, index)
        if j is None:
            index -= 1
            for index1 in range(index + 1, size):
                aux_states[index1] = states[index1]
        else:
            aux_states = place_queen(aux_states, size, index, j)
            index += 1

    if index == 0:
        return False, aux_states
    else:
        return True, aux_states


if __name__ == '__main__':

    size = int(input("Enter number of queens n="))
    board = [[0 for x in range(size)] for y in range(size)]
    number_of_constrains = int(input("Enter number of constrains number="))
    for constrain in range(number_of_constrains):
        block_i, block_j = input("Enter 'line column' to constrain").split(' ')
        block(board, int(block_i), int(block_j))
    states = []
    # initial state
    for i in range(size):
        states.append(board[i])

    print(states)

    print(generalized_lookahead(board, size, states))
