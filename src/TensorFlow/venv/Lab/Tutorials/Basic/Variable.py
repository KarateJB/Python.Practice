import tensorflow as tf
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #See https://www.tensorflow.org/api_docs/python/tf/random_uniform
b = tf.Variable(tf.zeros([1])) #See https://www.tensorflow.org/api_docs/python/tf/zeros
init_op=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(W))
    print(sess.run(b))