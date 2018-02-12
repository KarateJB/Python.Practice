import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Parameters
learning_rate = 0.2
training_epochs = 201
display_step = 20

# 用 numpy 亂數產生 100 個點，並且
train_X = np.random.rand(100).astype(np.float32)
train_Y = train_X * 0.1 + 0.3

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.) 
# 等等 tensorflow 幫我們慢慢地找出 fitting 的權重值

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * train_X + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - train_Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.global_variables_initializer()

# Launch the graph.
with tf.Session() as sess:
    sess.run(init)

    # Fit the line.
    for step in range(training_epochs):
        sess.run(train)
        if step % display_step == 0:
            print(step, sess.run(W), sess.run(b))
            plt.plot(train_X, train_Y, 'ro', label='Original data')
            plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
            plt.legend()
            plt.show()

# Learns best fit is W: [0.1], b: [0.3]