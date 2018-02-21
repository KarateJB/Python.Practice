"""
tf.argmax
See https://www.tensorflow.org/api_docs/python/tf/argmax
Returns the index with the largest value across axes of a tensor. 
"""

import tensorflow as tf

A = [33,66,11]  
B = [[33,66,11]]  
C = [[1,2,3], [9,8,7]]  
  
with tf.Session() as sess:  
    print(sess.run(tf.argmax(A, 0)))  # 1
    print(sess.run(tf.argmax(B, 1)))  # [1]  
    print(sess.run(tf.argmax(C, 1)))  # [2 0]