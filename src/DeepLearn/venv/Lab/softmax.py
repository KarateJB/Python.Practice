import numpy as np
import matplotlib.pyplot as plt


def softmax_overflow(a): 
    ''' Thissoftmax will cause overflow
    '''
    #輸入訊號的指數
    exp = np.exp(a)

    #輸入訊號的指數函數和
    sum_exp = np.sum(exp)

    y = exp/sum_exp
    return y

def softmax(a):

    #1. Set a constantant, which is the max value from input values
    #2. Set the new inut as a-c to avoid overflow
    c = np.max(a)
    a_new = a - c

    #輸入訊號的指數
    exp = np.exp(a_new)

    #輸入訊號的指數函數和
    sum_exp = np.sum(exp)

    y = exp/sum_exp
    return y


if __name__ == '__main__':
    a = np.array([.3,2.9,4.0])
    # a = np.array([1000,2000,3000])
    
    y =softmax(a)
    print(y)
    print(np.sum(y))
