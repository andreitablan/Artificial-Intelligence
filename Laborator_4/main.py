import copy


def block(matrix, block_i, block_j):
    matrix[block_i][block_j] = -1


def priority(states, size):
    prior = {}
    for queen in range(0, size):
        number_of_0 = 0
        for index in range(0, size):
            if states[queen][index] == 0:
                number_of_0 += 1
        prior[queen] = number_of_0
    return sorted(prior.values())


def place_queen(aux_states, size, x, y):
    states2 = aux_states.copy()
    if states2[x][y] != -1:
        states2[x][y] = 1
        for i in range(0, size):
            for j in range(0, size):
                if states2[i][j] != 1:
                    if x != i and j != y:
                        if x - y == i - j or x + y == i + j:
                            if states2[i][j] != 2:
                                states2[i][j] -= 1
                    if i == x or j == y:
                        if states2[i][j] != 2:
                            states2[i][j] -= 1
    return states2


def remove_queen(aux_states, size, x, y):
    states2 = aux_states.copy()
    states2[x][y] = 2
    for i in range(0, size):
        for j in range(0, size):
            if states2[i][j] < 0:
                if x != i and j != y:
                    if x - y == i - j or x + y == i + j:
                        states2[i][j] += 1
                if i == x or j == y:
                    states2[i][j] += 1
    return states2


def print_states(states1, size1):
    for i in range(0, size1):
        print(states1[i])


def is_domain_empty(states, size, queen):
    for j in range(0, size):
        if states[queen][j] == 0:
            return False
    return True


def is_domain_final(states, size, queen):
    for j in range(0, size):
        if states[queen][j] == 1:
            return True
    return False


def select_value_forward_checking(size, aux_states, states, queen):
    while not is_domain_empty(aux_states, size, queen):

        print("o noua iteratie")
        for j in range(0, size):
            if aux_states[queen][j] == 0:
                position = j
                break
        aux_states = copy.deepcopy(place_queen(aux_states, size, queen, position))

        print("----------------")
        print_states(aux_states, size)

        k = queen + 1
        while k < size:
            for j in range(0, size):
                if aux_states[queen][j] == 0:
                    position = j
                    break
            placed = 0
            for b in range(0, size):
                if aux_states[k][b] == 0:
                    aux_states = copy.deepcopy(place_queen(aux_states, size, k, b))
                    print("--")
                    print_states(aux_states, size)
                    placed = 1
                    break
            if placed == 0:
                for b in range(0, size):
                    if aux_states[k - 1][b] == 1:
                        aux_states = copy.deepcopy(remove_queen(aux_states, size, k - 1, b))
                k -= 1
                print("am resetat:")
                print_states(aux_states, size)
            else:
                k += 1
        ok = True
    for queen in range(0, size):
        if not is_domain_final(aux_states, size, queen):
            ok = False
            break
    if ok is True:
        return position
    print("am returnat none")
    return None


def generalized_lookahead(size, states):
    index = 0
    while size > index >= 0:
        aux_states = copy.deepcopy(states)
        j = select_value_forward_checking(size, aux_states, states, index)
        if j is None:
            index -= 1
            for index1 in range(index + 1, size):
                aux_states[index1] = states[index1]
        else:
            print("am primit pozitia ", index, j)
            states = copy.deepcopy(place_queen(states, size, index, j))
            index += 1
            print("noul meu states: ")
            print_states(states, size)

    for i in range(0, size):
        for j in range(0, size):
            if aux_states[i][j] < 0:
                aux_states[i][j] = -1
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
    for i in range(size):
        states.append(board[i])

    print(generalized_lookahead(size, states))
