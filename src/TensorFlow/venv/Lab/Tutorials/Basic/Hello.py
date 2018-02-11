import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
with tf.Session() as sess:
    result=sess.run(hello)
    print(result.decode("utf-8"))