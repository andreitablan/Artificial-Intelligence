import gymnasium as gym
import numpy as np

gym.make('CliffWalking-v0')


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
            state["occupied"] = False
            break

    score_1 = score_2 = score_3 = -1000000

    if x - 1 >= 0:
        score_1 = Rewards[x - 1][y]
        x = x - 1
    if x + 1 <= 12:
        score_2 = Rewards[x + 1][y]
        if score_2 > score_1:
            x = x + 1
    if y - 1 >= 0:
        score_3 = Rewards[x - 1][y]
        if score_3 > score_2 and score_3 > score_1:
            y = y - 1
    if y + 1 <= 12:
        score_4 = Rewards[x][y + 1]
        if score_4 > score_3 and score_4 > score_2 and score_4 > score_1:
            y = y + 1

    for state in states:
        if state["x"] == x and state["y"] == y:
            state["occupied"] = True
            break

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
    Q = np.zeros((48, 4))
    print(states)
    states = initialize_position(states)
    print(states)
    states = decision(states, Q, Rewards)
    print(states)


if __name__ == '__main__':
    slove_problem()
