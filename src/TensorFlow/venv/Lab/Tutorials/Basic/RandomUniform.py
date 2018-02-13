import tensorflow as tf
import numpy as np
# rnd= tf.Variable(tf.random_uniform([2], 100, 200))
# init = tf.global_variables_initializer()
rnd= tf.random_uniform([2], 100, 200)
X = np.asarray([1.1,2.1,5.122])
print(X.shape[0])
with tf.Session() as sess:
    # sess.run(init)
    print(sess.run(rnd))  # Ouput: [141.38602 158.75304]