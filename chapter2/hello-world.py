import tensorflow as tf
h = tf.constant('hello')
w = tf.constant(' world!')
hw = h + w
print(hw)

with tf.compat.v1.Session() as sess:
  ans = sess.run(hw)

print(ans)
