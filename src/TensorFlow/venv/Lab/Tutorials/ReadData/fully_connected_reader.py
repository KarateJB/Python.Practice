import argparse
import os.path
import sys
import time

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import mnist

FLAGS = None

TRAIN_FILE = 'trina.tfrecords'
VALIDATION_FILE = 'validation.tfrecords'

def decode(serialized_example):
    """Parses an image and lable from the given serialized_example"""
    features = tf.parse_single_example(
        serialized_example,
        features={
            'image_raw': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64)
        }
    )

image = tf.decode_raw(features['image_raw'], tf.uint8)
image.set_shape((mnist.IMAGE_PIXELS))

