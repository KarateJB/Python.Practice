# See https://www.tensorflow.org/api_docs/python/tf/reduce_sum
import tensorflow as tf

x = tf.constant([[2, 3], [4, 1]])

with tf.Session() as sess:
    print(sess.run(tf.reduce_sum(x))) # Result: 2+3+4+1=10
    print(sess.run(tf.reduce_sum(x, 0))) # Result: [6 4]
    print(sess.run(tf.reduce_sum(x, 1))) # Result: [5 5]
    print(sess.run(tf.reduce_sum(x, 1, keepdims=True))) # Result: [[5], [5]]
    print(sess.run(tf.reduce_sum(x, [0, 1]))) # Result: 10
    
