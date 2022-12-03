import gymnasium as gym
import numpy as np

gym.make('CliffWalking-v0')


def decision(states, Q, Rewards):
    x = 0
    y = 0
    for state in states:
        if state["occupied"] is True:
            x = state["x"]
            y = state["y"]
            state["occupied"] = False
            break
    max_score = max(Rewards[x - 1][y - 1], Rewards[x + 1][y + 1], Rewards[x - 1][y], Rewards[x][y - 1])
    if max_score == Rewards[x - 1][y - 1]:
        x = x - 1
        y = y - 1
    elif max_score == Rewards[x + 1][y + 1]:
        x = x + 1
        y = y + 1
    elif max_score == Rewards[x - 1][y]:
        x = x - 1
        y = y
    else:
        x = x
        y = y - 1

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


if __name__ == '__main__':
    slove_problem()
