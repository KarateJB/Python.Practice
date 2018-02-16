"""Sigmoid
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# a = np.arange(-10,11,1)

with tf.name_scope('Sigmoid'):
    tf.summary.scalar('Loss', loss)
    
init = tf.global_variables_initializer()
# Start training
with tf.Session() as sess:
    
    # Output graph
    writer = tf.summary.FileWriter("log/Sigmoid/", graph = sess.graph)
    
    # Run the initializer
    sess.run(init)
 
    for step in range(-10,10):
        a = tf.convert_to_tensor(step, dtype=tf.float32)
        # a = tf.random_uniform([1,1], minval=1.0, maxval=3.0, seed=step)
        stepStr = str(step + 1) + '.'
        print(stepStr, sess.run(tf.constant(step)), sess.run(tf.sigmoid(a)))

