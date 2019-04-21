import tensorflow as tf
import Get_Database

trainset_path = "D:\Code\Python\Valified_Code_Classify\Dataset\\train_set"
testset_path = "D:\Code\Python\Valified_Code_Classify\Dataset\\test_set"
# testset_path = "D:\Code\Python\Valified_Code_Classify\Dataset\\train_set"
data = Get_Database.Data(trainset_path, testset_path)

x = tf.placeholder(tf.float32, [None, 1600])
W = tf.Variable(tf.zeros([1600, 26]))
b = tf.Variable(tf.zeros([26]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder("float", [None, 26])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cross_entropy)
sess = tf.Session()
if(tf.__version__.startswith("0.") and int(tf.__version__.split(".")[1])<12): ### For tf version < 0.12.0
    init = tf.initialize_all_variables()
else: ### For tf version >= 0.12.0
    init = tf.global_variables_initializer()

# saver = tf.train.Saver()
# saver.restore(sess, "D:\Code\Python\model.ckpt")
sess.run(init)
for i in range(10000):
    batch_xs, batch_ys = data.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    if i % 100 == 0:
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys}))
print(sess.run(accuracy, feed_dict={x: data.test_images, y_: data.test_labels}))
saver = tf.train.Saver()
model_path = "D:\Code\Python\Valified_Code_Classify\Classified\model.ckpt"
save_path = saver.save(sess, model_path)
print("Model saved in file: %s" % save_path)
