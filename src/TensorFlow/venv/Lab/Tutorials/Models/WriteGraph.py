"""
tf.train.write_graph
See https://www.tensorflow.org/api_docs/python/tf/train/write_graph
"""
import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants
import os

a = tf.Variable([[1],[2]], dtype=tf.float32, name='a')
b = tf.Variable(3, dtype=tf.float32, name='b')

output = tf.add(a, b, name='out') # Tensor must have a name

graph_dir = "./graph_dir"
if not os.path.exists(graph_dir):
    os.makedirs(graph_dir)


# Save graph file
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    # Convert Variable to constant, "out" is the name of the tensor
    graph = convert_variables_to_constants(sess, sess.graph_def, ["out"])
    tf.train.write_graph(graph, graph_dir,'graph.pb', as_text=False)


# Restore graph file
with tf.Session() as sess:
    # with open(os.path.join(graph_dir,'graph.pb'), 'rb') as f:
    with tf.gfile.FastGFile(os.path.join(graph_dir,'graph.pb'),'rb') as f:
        graph_def=tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        output = tf.import_graph_def(graph_def, return_elements=['out:0'])
        print(sess.run(output))