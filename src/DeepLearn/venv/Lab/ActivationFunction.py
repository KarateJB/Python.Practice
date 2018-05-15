import numpy as np
import matplotlib.pylab as plt


def step(x):
    # y = x > 0
    # return y.astype(np.int)
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))    

def relu(x):
    return np.maximum(x,0)

x = np.arange(-5.0, 5.0, 0.1)
# y = step(x) #階層函式
# y = sigmoid(x) #sigmoid
y = relu(x) #ReLU
plt.plot(x, y) 
plt.ylim(-0.1, 1.1) 
plt.show()
