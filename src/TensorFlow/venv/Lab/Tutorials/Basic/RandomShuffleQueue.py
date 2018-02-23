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

    run_option = tf.RunOptions(timeout_in_ms=5000)
    try:
        # sess.run(enqueue_op, feed_dict={dummy_input: [10.,20.,30.]}, options=run_option)
        sess.run(enqueue_op, options=run_option)
        for i in range(0,9):
            sess.run(fg, options=run_option)
    except tf.errors.DeadlineExceededError:
        print('Out of range')
    
    
    
