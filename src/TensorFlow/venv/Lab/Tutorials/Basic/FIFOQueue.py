"""
FIFOQueue
See https://www.tensorflow.org/api_docs/python/tf/FIFOQueue
"""

import tensorflow as tf
    

# shp = [4]
# inp = tf.placeholder("float")
# inp1 = tf.placeholder("float")
# queue = tf.FIFOQueue(20, dtypes="float")

dummy_input = tf.random_normal([3], mean=0, stddev=1)
dummy_input = tf.Print(dummy_input, data=[dummy_input], message='New dummy inputs have been created: ', summarize=6)

q = tf.FIFOQueue(capacity=3, dtypes=tf.float32)
enqueue_op = q.enqueue_many(dummy_input)

data = q.dequeue()
data = tf.Print(data, data=[q.size(),data], message='This is how many items are left in q: ')
# create a fake graph that we can call upon
fg = data + 1

with tf.Session() as sess:
    # first load up the queue
    sess.run(enqueue_op)
    for i in range(0,3):
        sess.run(fg)
    
    
