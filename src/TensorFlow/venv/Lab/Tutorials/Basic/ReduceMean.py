# See https://www.tensorflow.org/api_docs/python/tf/reduce_mean
import tensorflow as tf

x = tf.constant([[2., 3.], [4., 1.]])

with tf.Session() as sess:
    all = tf.reduce_mean(x) #reduces all dimensions
    dm0 = tf.reduce_mean(x, axis=0) #reduces dimension 0, that will be on 2 and 4, 3 and 1
    dm1 = tf.reduce_mean(x, axis=1) #reduces dimension 1, that will be on 2 and 3, 4 and 1

    print(sess.run(all)) # Result: 2.5
    print(sess.run(dm0)) # Result: [3. 2.]
    print(sess.run(dm1)) # Result: [2.5 2.5]
