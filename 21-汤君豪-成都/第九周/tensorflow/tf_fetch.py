import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input1, input2)
multi = tf.multiply(intermed, input3)

with tf.Session() as sess:
    # 需要获取的多个 tensor 值，在 op 的一次运行中一起获得（而不是逐个去获取 tensor）。
    print(sess.run([multi, intermed]))