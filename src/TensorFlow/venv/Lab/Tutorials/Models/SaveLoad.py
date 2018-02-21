"""Save and Load model sample
See https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/4_Utils/save_restore_model.py
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import os

# Initialize random weights
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

# Define model
def model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden): 
    # 1st fully connected layer
    X = tf.nn.dropout(X, p_keep_input) # Apply dropout to hidden layer
    h = tf.nn.relu(tf.matmul(X, w_h))
    
    
    h = tf.nn.dropout(h, p_keep_hidden)  # Apply dropout to hidden layer
    
    # 2nd fully connected layer
    h2 = tf.nn.relu(tf.matmul(h, w_h2))
    h2 = tf.nn.dropout(h2, p_keep_hidden)  # Apply dropout to hidden layer

    return tf.matmul(h2, w_o)


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels

X = tf.placeholder("float", [None, 784])
Y = tf.placeholder("float", [None, 10])

#Initialize weights
w_h = init_weights([784, 625]) # weight for 1st layer
w_h2 = init_weights([625, 625]) # Weight for 2nd layer
w_o = init_weights([625, 10]) 



p_keep_input = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")

# Create neural network model and get log probabilities
py_x = model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden)

# Calculate the loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=py_x, labels=Y))

# Train
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(loss) # See https://www.tensorflow.org/api_docs/python/tf/train/RMSPropOptimizer
predict_op = tf.argmax(py_x, 1)  # Returns the index with the largest value

# Define the store-model directory
ckpt_dir = "./ckpt_dir"
if not os.path.exists(ckpt_dir):
    os.makedirs(ckpt_dir)

# Set a global step with trainable = false
global_step = tf.Variable(0, name='global_step', trainable=False)

# Call this after declaring all tf.Variables.
saver = tf.train.Saver()

# This variable won't be stored, since it is declared after tf.train.Saver()
non_storable_variable = tf.Variable(777)


# Launch the graph in a session
with tf.Session() as sess:
    # you need to initialize all variables
    tf.global_variables_initializer().run()

    # Load last train state
    ckpt = tf.train.get_checkpoint_state(ckpt_dir) # Returns CheckpointState proto from the "checkpoint" file
    if ckpt and ckpt.model_checkpoint_path:
        print(ckpt.model_checkpoint_path)
        saver.restore(sess, ckpt.model_checkpoint_path) # restore all variables

    start = global_step.eval() # get last global_step
    print("Start from:", start)

    for i in range(start, 100):
        for start, end in zip(range(0, len(trX), 128), range(128, len(trX)+1, 128)):
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                          p_keep_input: 0.8, p_keep_hidden: 0.5})

        global_step.assign(i+1).eval() # set and update(eval) global_step with index, i
        saver.save(sess, ckpt_dir + "/model.ckpt", global_step=global_step)
        print(i, np.mean(np.argmax(teY, axis=1) ==
                         sess.run(predict_op, feed_dict={X: teX, 
                                                         p_keep_input: 1.0,
                                                         p_keep_hidden: 1.0})))


        # If you want to only save the graph in to binary file
        tf.train.write_graph(sess.graph_def, '/tmp/tfmodel','train.pbtxt')
