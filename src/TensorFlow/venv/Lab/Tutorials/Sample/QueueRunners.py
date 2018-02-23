"""
QueueRunners and the Coordinator
"""

import tensorflow as tf
    
q = tf.FIFOQueue(capacity=3, dtypes=tf.float32, shapes=[])

dummy_input = tf.random_normal([3], mean=0, stddev=1)
dummy_input = tf.Print(dummy_input, data=[dummy_input], message='Create new dummy inputs: ', summarize=6)
enqueue_op = q.enqueue_many(dummy_input)

# Set a queue runner to handle enqueue_op outside the main thread asynchronously
qr = tf.train.QueueRunner(q, enqueue_ops= [enqueue_op] * 1)
tf.train.add_queue_runner(qr)

data = q.dequeue_many(3)
data = tf.Print(data, data=[q.size(),data], message='How many items are left in queue: ')
# create a fake graph that we can call upon
fg = data + 1

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    enqueue_threads = qr.create_threads(sess, coord=coord, start=True)

    run_option = tf.RunOptions(timeout_in_ms=5000)
    try:
        # sess.run(enqueue_op, options=run_option) # Remove this line
        for i in range(0,5):
            if coord.should_stop(): # coord.should_stop() returns True as soon as coord.request_stop() has been called.
                break
            sess.run(fg, options=run_option)

        # we have to request all threads now stop, then we can join the queue runner
        # thread back to the main thread and finish up
        coord.request_stop()
        # Wait for all the threads to terminate, give them 10s grace period
        coord.join(enqueue_threads, stop_grace_period_secs=10)
            
    except tf.errors.DeadlineExceededError:
        print('Out of range')
    