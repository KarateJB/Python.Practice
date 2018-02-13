"""Linear Regression
https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_linear_regression_works.html
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Parameters
learning_rate = 0.2
training_epochs = 201
display_step = 20

# Create 100 training data
train_X = np.random.rand(100).astype(np.float32)
train_Y = train_X * 0.1 + 0.3

# Try to find values for W and b that compute train_Y = W * train_X + b
# TensorFlow will learns, and best fit is W: [0.1], b: [0.3]
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * train_X + b

# Minimize the mean squared errors.
# MMSE reference:
# https://en.wikipedia.org/wiki/Minimum_mean_square_error
# http://allenluadvance.blogspot.tw/2014/01/sine-wave-estimation-mmse-estimator-ml.html
# https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/more-on-regression/v/proof-part-1-minimizing-squared-error-to-regression-line
loss = tf.reduce_mean(tf.square(y - train_Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for step in range(training_epochs):
        sess.run(train)
        if step % display_step == 0:
            stepStr = str(int(step/display_step) + 1) + '.'
            print(stepStr, sess.run(W), sess.run(b))
            plt.plot(train_X, train_Y, 'go', label='Original data')
            plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
            plt.legend()
            plt.show()
