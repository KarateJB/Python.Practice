"""
FIFOQueue
See https://www.tensorflow.org/api_docs/python/tf/FIFOQueue
"""

import tensorflow as tf
    
dummy_input = tf.random_normal([3], mean=0, stddev=1)
# shp = [3]
# dummy_input = tf.placeholder("float", shp)
dummy_input = tf.Print(dummy_input, data=[dummy_input], message='Create new dummy inputs: ', summarize=6)

q = tf.FIFOQueue(capacity=3, dtypes=tf.float32)
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
        for i in range(0,3):
            sess.run(fg, options=run_option)
    except tf.errors.DeadlineExceededError:
        print('Out of range')
    
    
    
