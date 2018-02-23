"""
FIFOQueue
See https://www.tensorflow.org/versions/r1.2/api_docs/python/tf/RandomShuffleQueue
"""

import tensorflow as tf
    
# shp = [10]
# dummy_input = tf.placeholder("float", shp)
dummy_input = tf.random_normal([10], mean=0, stddev=1)
dummy_input = tf.Print(dummy_input, data=[dummy_input], message='Create new dummy inputs: ', summarize=6)

q = tf.RandomShuffleQueue(capacity=10, min_after_dequeue=2, dtypes=tf.float32)
enqueue_op = q.enqueue_many(dummy_input)

data = q.dequeue()
data = tf.Print(data, data=[q.size(),data], message='How many items are left in queue: ')
# create a fake graph that we can call upon
fg = data + 1

with tf.Session() as sess:
    # sess.run(enqueue_op, feed_dict={dummy_input: [10.,20.,30.]})
    sess.run(enqueue_op)
    for i in range(0,8):
        sess.run(fg)
    
    
