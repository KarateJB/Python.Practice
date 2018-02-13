import tensorflow as tf
s= tf.square(10)
with tf.Session() as sess:
    print(sess.run(s))  # Ouput: 100