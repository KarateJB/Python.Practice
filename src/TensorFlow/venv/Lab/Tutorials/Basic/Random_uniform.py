import tensorflow as tf
rnd= tf.Variable(tf.random_uniform([2], 100, 200))
init = tf.global_variables_initializer()
# rnd= tf.random_uniform([2], 100, 200)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(rnd))  # Ouput: [141.38602 158.75304]