"""
Reading data with 
"""

import tensorflow as 
from tensorflow.contrib.learn.python.learn.datasets import mnist
# C:\Users\ppipp\Downloads\Github\Python.Practice\src\TensorFlow\venv\Lab\Lib\site-packages\tensorflow\contrib\learn\python\learn\datasets

# Global parameters
FLAGS = None

def main(unused_argv): 
    # Get data
    data_sets = mnist.read_data_sets(FLAGS.directory, dtype=tf.unit8, reshape=False, validation_size=FLAGS.validation_zie)

    # Convert data to tf.train,Example and write into TFRecords file
    convert_to(data_sets.train, 'train')
    convert_to(data_sets.valiation, 'validation')
    convert_to(data_sets.test, 'test')
    

"""Convert data to tf.train.Example and write into TFRecords file
"""
def convert_to(data_set, name):
    images = data_set.images
    labels = data_set.labels
    num_examples = data_set.num_examples

    if images.shape[0] != num_examples:
        raise ValueError('Images size {0} does not match label size {1}.'.format(images.shape[0], num_examples))

    rows = images.shape[1]
    cols = images.shape[2]
    depth = images.shape[3]

    filename = os.path.join(FLAGS.directory, name + '.tfrecords')
    print('Writing', filename)
    with tf.python_io.TFRecordWriter(filename) as writer:
        for index in range(num_examples):
            features=tf.train.Features(
                feature={
                    
                }
            )
