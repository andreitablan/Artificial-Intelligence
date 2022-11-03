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


if __name__ == '__main__':
    size = 11
    neural_network = [[0 for x in range(size)] for y in range(size)]
    input_layer_size = 4
    hidden_layer_size = 4
    output_layer_size = 3
    learning_rate = 0.01
    number_of_ages = 30
    data = read_from_csv()
    test_data = []
    random.shuffle(data)
    for flower in range(0, int((10 / 100) * len(data))):
        test_data.append(data.pop(flower))
        
    for row in range(0, size):
        for column in range(0, size):
            if row < column:
                if row == 0 or row == 1 or row == 2 or row == 3:
                    neural_network[row][4] = neural_network[4][row] = round(random.uniform(-1,1),2)
                    neural_network[row][5] = neural_network[5][row] = round(random.uniform(-1,1),2)
                    neural_network[row][6] = neural_network[6][row] = round(random.uniform(-1,1),2)
                    neural_network[row][7] = neural_network[7][row] = round(random.uniform(-1,1),2)
                if row == 8 or row == 9 or row == 10:
                    neural_network[row][4] = neural_network[4][row] = round(random.uniform(-1,1),2)
                    neural_network[row][5] = neural_network[5][row] = round(random.uniform(-1,1),2)
                    neural_network[row][6] = neural_network[6][row] = round(random.uniform(-1,1),2)
                    neural_network[row][7] = neural_network[7][row] = round(random.uniform(-1,1),2)

    for row in range(0, size):
        print(neural_network[row])
