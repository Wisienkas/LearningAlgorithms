import random
from matplotlib import pyplot

learning_rate = 0.001

class Unit:

    def __init__(self):
        self.w = 0.5


class Threshold:

    def __init__(self):
        self.threshold = 1

    def predict(self, ):
        if input < self.threshold:
            return -1
        else:
            return 1

class Perceptron:

    def __init__(self, inputs):
        self.units = []
        self.threshold = Unit()
        for i in range(0, inputs):
            self.units.append(Unit())

    def train(self, inputs, result):
        if len(inputs) != len(self.units):
            raise Exception("Invalid inputs")

        predicted = self.predict(inputs)
        self.adapt(predicted, result, inputs)

    def predict(self, inputs):
        result = []
        for i, unit_i in enumerate(self.units):
            result.append(unit_i.w * inputs[i])

        return result

    def adapt(self, predicted, result, inputs):
        for i, unit_i in enumerate(self.units):
            unit_i.w += learning_rate * (result[i] - predicted[i]) * inputs[i]

    def print_network(self):
        for i, node in enumerate(self.units):
            print("Node: {}, Weight: {}".format(i, node.w))

perceptron = Perceptron(2)

and_set = [
    ([0, 0], [0, 0]),
    ([0, 1], [0, 5]),
    ([1, 0], [5, 0]),
    ([1, 1], [5, 5]),
]
from math import sqrt


def distance(a, b):
    sum = 0
    for i in range(0, len(a)):
        sum += (a[i] - b[i])**2
    return sqrt(sum)

def evaluate():
    mean_error = 0
    for set in and_set:
        mean_error += distance(set[1], perceptron.predict(set[0]))
        print("input: {}, output: {}, error: {}".format(set[0], perceptron.predict(set[0]), mean_error))

    mean_sqrt_error = 0.5 * mean_error
    print("Mean squared error is: {}".format(mean_sqrt_error))

for e in range(0, 10000):
    if e % 100 == 0: evaluate()
    for set in and_set:
        perceptron.train(set[0], set[1])

perceptron.print_network()