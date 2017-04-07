import tensorflow as tf
import Get_Database


def Classified(path):
    data = Get_Database.base(path, False)
    x = tf.placeholder(tf.float32, [None, 1600])
    W = tf.Variable(tf.zeros([1600, 26]))
    b = tf.Variable(tf.zeros([26]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    sess = tf.Session()
    saver = tf.train.Saver()
    saver.restore(sess, "D:\Code\Python\Valified_Code_Classify\Classified\model\model.ckpt")
    print("Model restored.")
    result = sess.run(y, feed_dict={x: data})
    code = ""
    for i in result:
        temp = list(i)
        code += chr(temp.index(max(temp)) + 97)
    return code


path = "D:\Code\Python\Valified_Code_Classify\\Network_training\Dataset\\test_set"
print(Classified(path))
