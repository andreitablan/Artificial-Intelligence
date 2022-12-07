import random

import gymnasium as gym

gym.make('CliffWalking-v0')

list_counter = []


def clear_tables(states):
    for state in states:
        if state['x'] == 11 and state['y'] == 3:
            state['occupied'] = False
        if state['x'] == 3 and state['y'] == 0:
            state['occupied'] = True

    Q = [[0 for index in range(0, 4)] for index2 in range(0, 48)]
    return states, Q


def is_final(states):
    for state in states:
        if state['x'] == 11 and state['y'] == 3 and state['occupied'] is True:
            return True
    return False


def update_global_list(element):
    global list_counter
    list_counter.append(element)


def apply_discount_Qtable(Q, decade):
    global list_counter
    for element in list_counter:
        Q[element][0] -= decade
        Q[element][1] -= decade
        Q[element][2] -= decade
        Q[element][3] -= decade
    return Q


def print_Qtable(Q):
    for line in range(0, len(Q)):
        print(Q[line])


def update_Qtable(Q, state, states, score_x_minus_1, score_x_plus_1, score_y_minus_1, score_y_plus_1):
    # staga, dreapta, sus, jos
    counter = 0
    for aux_state in states:
        if aux_state == state:
            Q[counter][0] = score_x_minus_1
            Q[counter][1] = score_x_plus_1
            Q[counter][2] = score_y_minus_1
            Q[counter][3] = score_y_plus_1
            break
        counter += 1
    update_global_list(counter)
    return Q


def initialize_position(states):
    for state in states:
        if state['x'] == 0 and state['y'] == 3:
            state['occupied'] = True
            break
    return states


def decision_loop(states, Q, Rewards, decade):
    if not is_final(states):
        counter = 0
        while not is_final(states):
            counter += 1
            states, Q, Rewards = decision(states, Q, Rewards, decade)
        print(states)
        return counter
    return 0


def decision(states, Q, Rewards, decade):
    Q = apply_discount_Qtable(Q, decade)

    initial_x = 0
    initial_y = 0

    for state in states:
        if state["occupied"] is True:
            initial_x = state["x"]
            initial_y = state["y"]
            last_state = state
            state["occupied"] = False
            break
    score_x_minus_1 = score_x_plus_1 = score_y_minus_1 = score_y_plus_1 = -1000000

    if initial_x - 1 >= 0:
        score_x_minus_1 = Rewards[initial_y][initial_x - 1]

    if initial_x + 1 < 12:
        score_x_plus_1 = Rewards[initial_y][initial_x + 1]

    if initial_y - 1 >= 0:
        score_y_minus_1 = Rewards[initial_y - 1][initial_x]
    if initial_y + 1 < 4:
        score_y_plus_1 = Rewards[initial_y + 1][initial_x]

    list_dict = []
    dictionary_scores1 = {}
    dictionary_scores2 = {}
    dictionary_scores3 = {}
    dictionary_scores4 = {}

    max_score = max(score_x_plus_1, score_x_minus_1, score_y_plus_1, score_y_minus_1)
    if max_score == score_x_plus_1:
        dictionary_scores1["score_x_plus_1"] = max_score
        dictionary_scores1["x"] = initial_x + 1
        dictionary_scores1["y"] = initial_y
        list_dict.append(dictionary_scores1)
    if max_score == score_x_minus_1:
        dictionary_scores2["score_x_minus_1"] = max_score
        dictionary_scores2["x"] = initial_x - 1
        dictionary_scores2["y"] = initial_y
        list_dict.append(dictionary_scores2)

    if max_score == score_y_plus_1:
        dictionary_scores3["score_y_plus_1"] = max_score
        dictionary_scores3["x"] = initial_x
        dictionary_scores3["y"] = initial_y + 1
        list_dict.append(dictionary_scores3)

    if max_score == score_y_minus_1:
        dictionary_scores4["score_y_minus_1"] = max_score
        dictionary_scores4["x"] = initial_x
        dictionary_scores4["y"] = initial_y - 1
        list_dict.append(dictionary_scores4)

    dictionary = random.choice(list_dict)
    x = dictionary["x"]
    y = dictionary["y"]

    for state in states:
        if state["x"] == x and state["y"] == y:
            state["occupied"] = True
            break

    Q = update_Qtable(Q, last_state, states, score_x_minus_1, score_x_plus_1, score_y_minus_1, score_y_plus_1)

    return states, Q, Rewards


def run_ages(ages, states, Q, Rewards, decade):
    age = 0
    while age < ages:
        age += 1
        states, Q = clear_tables(states)
        print(decision_loop(states, Q, Rewards, decade))


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

    Q = [[0 for index in range(0, 4)] for index2 in range(0, 48)]

    #(states)
    states = initialize_position(states)

    run_ages(ages, states, Q, Rewards, decade)


if __name__ == '__main__':
    slove_problem()
