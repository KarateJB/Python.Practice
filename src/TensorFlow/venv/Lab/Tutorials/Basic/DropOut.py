"""
dropout
See https://www.tensorflow.org/api_docs/python/tf/nn/dropout
Make some elements become 0 in a tensor，others will become 1/keep_prob.
"""

import tensorflow as tf

keepProb = tf.placeholder(tf.float32)
x = tf.Variable(tf.ones([5, 5]))
y = tf.nn.dropout(x, keepProb)

init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(y, feed_dict = {keepProb: 0.4}))