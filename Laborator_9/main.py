import gymnasium as gym

gym.make('CliffWalking-v0')


def apply_discount_Qtable(Q, state, states):
    counter = 0
    for aux_state in states:
        if aux_state == state:
            break
        counter += 1

    for line in range(0, len(Q)):
        if line > counter - 1:
            break
        for column in range(0, len(Q[line])):
            Q[line][column] -= 1

    return Q


def print_Qtable(Q):
    for line in range(0, len(Q)):
        print(Q[line])


def update_Qtable(Q, state, states, score_x_minus_1, score_x_plus_1, score_y_minus_1, score_y_plus_1):
    # staga, dreapta, jos, sus
    counter = 0
    for aux_state in states:
        if aux_state == state:
            Q[counter][0] = score_x_minus_1
            Q[counter][1] = score_x_plus_1
            Q[counter][2] = score_y_minus_1
            Q[counter][3] = score_y_plus_1
            break
        counter += 1
    return Q


def initialize_position(states):
    for state in states:
        if state['x'] == 0 and state['y'] == 0:
            state['occupied'] = True
            break
    return states


def decision(states, Q, Rewards):
    x = 0
    y = 0

    for state in states:
        if state["occupied"] is True:
            x = state["x"]
            y = state["y"]
            last_state = state
            state["occupied"] = False
            break

    score_x_minus_1 = score_x_plus_1 = score_y_minus_1 = score_y_plus_1 = -1000000

    if x - 1 >= 0:
        score_x_minus_1 = Rewards[x - 1][y]
        x = x - 1
    if x + 1 <= 12:
        score_x_plus_1 = Rewards[x + 1][y]
        if score_x_plus_1 > score_x_minus_1:
            x = x + 1
    if y - 1 >= 0:
        score_y_minus_1 = Rewards[x - 1][y]
        if score_y_minus_1 > score_x_plus_1 and score_y_minus_1 > score_x_minus_1:
            y = y - 1
    if y + 1 <= 12:
        score_y_plus_1 = Rewards[x][y + 1]
        if score_y_plus_1 > score_y_minus_1 and score_y_plus_1 > score_x_plus_1 and score_y_plus_1 > score_x_minus_1:
            y = y + 1

    for state in states:
        if state["x"] == x and state["y"] == y:
            state["occupied"] = True
            break

    Q = update_Qtable(Q, last_state, states, score_x_minus_1, score_x_plus_1, score_y_minus_1, score_y_plus_1)
    # print_Qtable(Q)

    Q = apply_discount_Qtable(Q, state, states)
    # print_Qtable(Q)
    return states


def slove_problem():
    cliff = -100
    end = 100
    learning_rate = 0.1
    decade = 10
    ages = 30
    states = []
    for y in range(0, 4):
        for x in range(0, 12):
            dictionary = {}
            dictionary["x"] = x
            dictionary["y"] = y
            dictionary["occupied"] = False
            states.append(dictionary)

    Rewards = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, cliff, cliff, cliff, cliff, cliff, cliff, cliff, cliff, cliff, cliff, end]
               ]
    # Q = np.zeros((48, 4))

    Q = [[0 for index in range(0, 4)] for index2 in range(0, 48)]

    print(states)
    states = initialize_position(states)
    print(states)
    states = decision(states, Q, Rewards)
    print(states)


if __name__ == '__main__':
    slove_problem()
