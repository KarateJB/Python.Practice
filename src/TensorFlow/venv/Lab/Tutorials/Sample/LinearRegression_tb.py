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

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")


with tf.name_scope('Weights'):
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='Weight')
    tf.summary.histogram(name = 'Weights', values = W)

with tf.name_scope('Biases'):    
    b = tf.Variable(tf.zeros([1]), name='Bias')
    tf.summary.histogram(name = 'Biases', values = b)

with tf.name_scope('Formula'):    
    y = W * train_X + b

# Minimize the mean squared errors.
with tf.name_scope('Loss'):
    loss = tf.reduce_sum(tf.pow(y-train_Y, 2))/train_X.shape[0]
    # loss = tf.reduce_mean(tf.square(y - train_Y)) # Or use reduce_mean
    tf.summary.scalar('Loss', loss)

with tf.name_scope('Train'): 
    optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    train = optimizer.minimize(loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Output graph
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("log/LinearRegression/", graph = sess.graph)
    
    # Run the initializer
    sess.run(init)

    # Fit all training data
    for step in range(training_epochs):
        sess.run(train)
        if step % display_step == 0:
            stepStr = str(int(step/display_step) + 1) + '.'
            print(stepStr, sess.run(W), sess.run(b))
            
            sess.run(loss, feed_dict={X: train_X, Y:train_Y})
            summary = sess.run(merged, feed_dict={X: train_X, Y:train_Y})
            writer.add_summary(summary, step)
            
            plt.plot(train_X, train_Y, 'go', label='Original data')
            plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
            plt.legend()
            plt.show()
