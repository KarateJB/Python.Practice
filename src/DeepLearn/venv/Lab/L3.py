import numpy as np
from ActivationFunction import *


def init_network():
    network = {}
    network['w1'] = np.array([[1, 2, 3], [4, 5, 6]])  # (2,3)
    network['b1'] = np.array([0.1, 0.2, 0.3])  # (3)
    network['w2'] = np.array([[1, 2], [3, 4], [5, 6]])  # (3,2)
    network['b2'] = np.array([0.1, 0.2])  # (2)
    network['w3'] = np.array([[1, 2], [4, 5]])  # (2),)2)
    network['b3'] = np.array([0.1, 0.2]) # (2,2)
    return network

def identify(y):
    return y

def forward(network, x):
    w1, w2, w3 = network['w1'],network['w2'],network['w3']
    b1, b2, b3 = network['b1'],network['b2'],network['b3']
    y1 = np.dot(x, w1) + b1
    z1 = sigmoid(y1)
    y2 = np.dot(z1, w2) + b2
    z2 = sigmoid(y2)
    y3 = np.dot(z2, w3) + b3
    z3 = sigmoid(y3)
    y = identify(z3)
    return y

if __name__ == '__main__':
    network = init_network()
    x = np.array([1, 2])
    y = forward(network, x)
    print(y)
