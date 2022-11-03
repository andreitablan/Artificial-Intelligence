# Leagan Dan; Tablan Andrei; Laborator 5 - AI
class Move:
    def __init__(self, player1, player2, move_player1, move_player2, output):
        self.player1 = player1
        self.player2 = player2
        self.move_player1 = move_player1
        self.move_player2 = move_player2
        self.output = output

    def print(self):
        print(self.player1, self.player2, self.move_player1, self.move_player2, self.output)


def read_input():
    with open("game.txt", "r") as myfile:
        data = myfile.read().splitlines()
    players = {}
    values = []
    for line in range(0, len(data)):
        if line < 2:
            line_split = data[line].split("\t")
            moves = []
            for move in range(1, len(line_split)):
                moves.append(line_split[move])
            players[line_split[0]] = moves
        else:
            line_split = data[line].split("\t")
            for output_value in range(0, len(line_split)):
                values.append(line_split[output_value])

    list_of_moves = []
    index = 0
    for move1 in players['PlayerA']:
        for move2 in players['PlayerB']:
            split_output = values[index].split("/")
            move = Move("PlayerA", "PlayerB", move1, move2, (int(split_output[0]), int(split_output[1])))
            list_of_moves.append(move)
            index += 1

    for listed_move in list_of_moves:
        listed_move.print()
    return list_of_moves


def calculate_dominant_strategy(list_of_moves):
    player1_scores = {}
    player2_scores = {}
    for move in list_of_moves:
        if move.move_player1 not in player1_scores:
            player1_scores[move.move_player1] = move.output[0]
        else:
            player1_scores[move.move_player1] += move.output[0]

        if move.move_player2 not in player2_scores:
            player2_scores[move.move_player2] = move.output[1]
        else:
            player2_scores[move.move_player2] += move.output[1]

    max1 = -1
    for key in player1_scores:
        if player1_scores[key] > max1:
            max1 = player1_scores[key]
            dominaint_move_1 = key

    max2 = -1
    for key in player2_scores:
        if player2_scores[key] > max2:
            max2 = player2_scores[key]
            dominaint_move_2 = key

    return (dominaint_move_1, dominaint_move_2)


def calculate_Nash_equilibrum(list_of_moves):
    nash=0
    for move in list_of_moves:
        print("Another move:", move.output)
        maxim_player_1 = -1
        maxim_player_2 = -1
        for move1 in list_of_moves:
            if move != move1:
                if move.move_player1 == move1.move_player1:
                    print("---Compare:", move.move_player1, "-", move.move_player2, ":", move.output[1], ' ',
                          move1.move_player1, "-",
                          move1.move_player2, ":", move1.output[1])
                    if move1.output[1] > maxim_player_2:
                        maxim_player_2 = move1.output[1]
                    if move.output[1] > maxim_player_2:
                        maxim_player_2 = move.output[1]
                if move.move_player2 == move1.move_player2:
                    print("---Compare:", move.move_player1, "-", move.move_player2, ":", move.output[0], ' ',
                          move1.move_player1, "-",
                          move1.move_player2, ":", move1.output[0])
                    if move1.output[0] > maxim_player_1:
                        maxim_player_1 = move1.output[0]
                    if move.output[0] > maxim_player_1:
                        maxim_player_1 = move.output[0]
        print("The maximum for the pure strategy is: ", maxim_player_2, maxim_player_2)
        if move.output[0] == maxim_player_1 and move.output[1] == maxim_player_2:
            nash = move.output
    if nash==0:
        return "Nu exista!"
    else:
        return nash


if __name__ == '__main__':
    print("The input is:")
    list_of_moves = read_input()
    print("A dominant strategy is:")
    print(calculate_dominant_strategy(list_of_moves))
    print("A Nash equilibrium for pure strategies is:")
    print("Nash:", calculate_Nash_equilibrum(list_of_moves))
