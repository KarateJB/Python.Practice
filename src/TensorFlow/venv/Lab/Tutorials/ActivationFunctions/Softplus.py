"""Relu
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# X = tf.placeholder(tf.float32)

# with tf.name_scope('Relu'):
#     fx = tf.nn.relu(X)
#     tf.summary.scalar("f(x)", tf.squeeze(fx))

# init = tf.global_variables_initializer()

# with tf.Session() as sess:

#     # Output graph
#     merged = tf.summary.merge_all()
#     writer = tf.summary.FileWriter("log/Relu/", graph = sess.graph)
    
#     # Run the initializer
#     sess.run(init)
 
#     for step in range(-10,11):
#         a = tf.convert_to_tensor(step, dtype=tf.float32)
#         a_r = sess.run([a])
#         print(sess.run(a), sess.run(fx, feed_dict={X: a_r}))

#         sess.run(fx, feed_dict={X: a_r})
#         summary = sess.run(merged, feed_dict={X: sess.run([a])})
#         writer.add_summary(summary, step)

with tf.Session() as sess:
    
    for step in range(-10,11):
        X = tf.convert_to_tensor(step, dtype=tf.float32)
        # X = tf.random_uniform([1,1], minval=1.0, maxval=3.0, seed=step) //Or use random number
        print(sess.run(X), sess.run(tf.nn.softplus(X)))