import random
from csv import reader

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


def compute_derivative(hidden_layer_scores, expected, X, weights_input_hidden, weights_hidden_output):
    output1 = output(X, weights_input_hidden, weights_hidden_output)
    delta1 = np.multiply(-(expected - hidden_layer_scores), derivative(output1))
    hidden = np.dot(X, weights_input_hidden)
    delta = np.dot(delta1, weights_hidden_output.T) * derivative(hidden)
    activated_hidden = sigmoid(hidden)

    derivative2 = np.dot(activated_hidden.T, delta1)
    derivative1 = np.dot(X.T, delta)
    return derivative1, derivative2


def prepare_mean_error(hidden_layer_scores, expected_scores):
    mean_errors = []
    for index in range(0, len(hidden_layer_scores)):
        mean_errors.append(mean_error(hidden_layer_scores[index], expected_scores))
    return mean_errors


def mean_error(actual, expected):
    return 0.5 * sum((actual - expected) ** 2)


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


def forward_propagation(X, weights_input_hidden, weights_hidden_output):
    hidden = np.dot(X, weights_input_hidden)
    activated_hidden = sigmoid(hidden)
    output = np.dot(activated_hidden, weights_hidden_output)
    activated_output = sigmoid(output)
    return activated_output


def output(X, weights_input_hidden, weights_hidden_output):
    hidden = np.dot(X, weights_input_hidden)
    activated_hidden = sigmoid(hidden)
    output = np.dot(activated_hidden, weights_hidden_output)
    return output


def initialize_parameters():
    size = 11
    input_layer_size = 4
    hidden_layer_size = 4
    output_layer_size = 3
    learning_rate = 0.1
    number_of_ages = 1000
    data = read_from_csv()
    test_data = create_test_data(data)
    data_input = []
    data_output = []
    for iris in data:
        aux_list = []
        aux_list.append(iris.sepal_length)
        aux_list.append(iris.sepal_width)
        aux_list.append(iris.petal_length)
        aux_list.append(iris.petal_width)
        data_input.append(aux_list)
        data_output.append(iris.iris_class)

    X = np.array(data_input, dtype=float)
    Y = np.array(data_output, dtype=type(data[1].iris_class))
    weights_input_hidden = np.random.randn(input_layer_size, hidden_layer_size)
    weights_hidden_output = np.random.randn(hidden_layer_size, output_layer_size)

    hidden_layer_scores = forward_propagation(X, weights_input_hidden, weights_hidden_output)
    print("scores after activation:")
    print(hidden_layer_scores)

    expected_scores = [0.33, 0.66, 0.99]

    error_score = prepare_mean_error(hidden_layer_scores, expected_scores)
    print("error scores for every input:")
    print(error_score)

    derivative1, derivative2 = compute_derivative(hidden_layer_scores, expected_scores, X, weights_input_hidden,
                                                  weights_hidden_output)

    print("derivative1:")
    print(derivative1)
    print("derivative2:")
    print(derivative2)


if __name__ == '__main__':
    initialize_parameters()
