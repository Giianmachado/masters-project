import tensorflow as tf

# create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
	#run the tf.constant operation in the session
	output = sess.run(hello_constant)
	print(output)
