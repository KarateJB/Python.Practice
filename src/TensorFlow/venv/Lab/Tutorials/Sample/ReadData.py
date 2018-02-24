"""
Reading data with 
"""

import tensorflow as tf

def main(unused_argv): 
    data_sets = mnist.read_data_sets(FLAGS.directory, dtype=tf.unit8, reshape=False, validation_size=FLAGS.validation_zie)

    # Convert data to tf.train,Example and write into TFRecords file
    convert_to(data_sets.train, 'train')
    convert_to(data_sets.valiation, 'validation')
    convert_to(data_sets.test, 'test')
    