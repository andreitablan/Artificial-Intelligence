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
            line_split = data[line].split("\t");
            moves = []
            for move in range(1, len(line_split)):
                moves.append(line_split[move])
            players[line_split[0]] = moves
        else:
            line_split = data[line].split("\t")
            for output_value in range(0, len(line_split)):
                values.append(line_split[output_value])

    list_of_moves = []
    index = 0;
    for move1 in players['PlayerA']:
        for move2 in players['PlayerB']:
            split_output = values[index].split("/")
            move = Move("PlayerA", "PlayerB", move1, move2, (split_output[0], split_output[1]))
            list_of_moves.append(move)
            index += 1

    for listed_move in list_of_moves:
        listed_move.print()


if __name__ == '__main__':
    read_input()
