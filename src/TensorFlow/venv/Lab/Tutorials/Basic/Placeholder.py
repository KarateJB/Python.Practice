import tensorflow as tf
num1=tf.placeholder(tf.int32)
num2=tf.placeholder(tf.int32)
result=num1+num2
with tf.Session() as sess:
    result=sess.run(result,{num1:10, num2:20})
    print(result)  # Output: 30