"""BN sample
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# X = tf.placeholder(tf.float32)
X = tf.placeholder_with_default([[[1.]]], shape=[1,1,1], name="X")

fc_mean, fc_var = tf.nn.moments(X,axes=[0],) #Calculate mean and variance

shift = tf.Variable(tf.zeros([1]))
scale = tf.Variable(tf.ones([1]))
epsilon = 0.001
Wx_plus_b = tf.nn.batch_normalization(X, fc_mean, fc_var, shift, scale, epsilon)

# ema = tf.train.ExponentialMovingAverage(decay=0.5)
# def mean_var_with_update():
#     ema_apply_op = ema.apply([fc_mean, fc_var])
#     with tf.control_dependencies([ema_apply_op]):
#         return tf.identity(fc_mean), tf.identity(fc_var)

# mean, var = mean_var_with_update() 
# Wx_plus_b = tf.nn.batch_normalization(tf.Variable(X), mean, var, shift, scale, epsilon)


with tf.name_scope('Sigmoid'):
    fx = tf.sigmoid(Wx_plus_b)
    tf.summary.scalar("f(x)", tf.squeeze(fx))

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

with tf.Session() as sess:

    # Output graph
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("log/Sigmoid/", graph = sess.graph)
    
    # Run the initializer
    sess.run(init)
 
    for step in range(100):
        a = tf.convert_to_tensor(tf.random_uniform([1,1], minval=0.0, maxval=10.0, seed=step))
        a_r = sess.run([a])
        print(sess.run(a), sess.run(fx, feed_dict={X: a_r}))

        sess.run(fx, feed_dict={X: a_r})
        summary = sess.run(merged, feed_dict={X: sess.run([a])})
        writer.add_summary(summary, step)
