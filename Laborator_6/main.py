from csv import reader
import random
import numpy as np


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, iris_class):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.iris_class = iris_class

    def print(self):
        print(self.sepal_length, self.sepal_width, self.petal_length, self.petal_width, self.iris_class)


def read_from_csv():
    data = []
    with open('iris.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            iris = Iris(row[0], row[1], row[2], row[3], row[4])
            data.append(iris)
    return data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def mean_squared_error(act, pred):
    diff = pred - act
    differences_squared = diff ** 2
    mean_diff = differences_squared.mean()

    return mean_diff


def create_test_data(data):
    data_i1 = []
    data_i2 = []
    data_i3 = []

    for line in data:
        if line.iris_class == 'Iris-setosa':
            data_i1.append(line)
    for line in data:
        if line.iris_class == 'Iris-versicolor':
            data_i2.append(line)
    for line in data:
        if line.iris_class == 'Iris-virginica':
            data_i3.append(line)

    test_data = []
    random.shuffle(data_i1)
    for flower in range(0, int((10 / 100) * len(data_i1))):
        test_data.append(data_i1.pop(flower))
    random.shuffle(data_i2)
    for flower in range(0, int((10 / 100) * len(data_i2))):
        test_data.append(data_i2.pop(flower))
    random.shuffle(data_i3)
    for flower in range(0, int((10 / 100) * len(data_i3))):
        test_data.append(data_i3.pop(flower))

    return test_data


def populate_neural_network(size):
    neural_network = [[0 for x in range(size)] for y in range(size)]
    for row in range(0, size):
        for column in range(0, size):
            if row < column:
                if row == 0 or row == 1 or row == 2 or row == 3:
                    neural_network[row][4] = neural_network[4][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][5] = neural_network[5][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][6] = neural_network[6][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][7] = neural_network[7][row] = round(random.uniform(-1, 1), 2)
                if row == 8 or row == 9 or row == 10:
                    neural_network[row][4] = neural_network[4][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][5] = neural_network[5][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][6] = neural_network[6][row] = round(random.uniform(-1, 1), 2)
                    neural_network[row][7] = neural_network[7][row] = round(random.uniform(-1, 1), 2)
    return neural_network


def initialize_parameters():
    size = 11
    input_layer_size = 4
    hidden_layer_size = 4
    output_layer_size = 3
    learning_rate = 0.01
    number_of_ages = 30
    data = read_from_csv()
    test_data = create_test_data(data)
    neural_network = populate_neural_network(size)
    # for row in range(0, size):
    #   print(neural_network[row])


if __name__ == '__main__':
    initialize_parameters()
