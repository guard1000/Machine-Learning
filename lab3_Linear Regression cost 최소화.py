import tensorflow as tf
import matplotlib.pyplot as plt #그래프 그려줌
import os       #오류 메시지 안뜨게!
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''
#4 compute_gradient and apply_gradient
X=[1,2,3]
Y=[1,2,3]

W = tf.Variable(5.0)

hypothesis = X*W
gradient = tf.reduce_mean((W*X-Y)*X)*2
cost = tf.reduce_mean(tf.square(hypothesis-Y))

#Minimize : Gradient Decent Magic
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
#Get gradients
gvs = optimizer.compute_gradients(cost)
#Apply_gradients
apply_gradient = optimizer.apply_gradients(gvs)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100):
    print(step, sess.run([gradient,W,gvs]))
    sess.run(apply_gradient)
'''

'''
#3 optimizer를 써보자
X=[1,2,3]
Y=[1,2,3]

W = tf.Variable(-3.0)

hypothesis = X*W
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#Minimize : Gradient Decent Magic
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100):
    print(step, sess.run(W))
    sess.run(train)
'''

'''
#2
x_data=[1,2,3]
y_data=[1,2,3]

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = X*W
cost = tf.reduce_mean(tf.square(hypothesis - Y))

learning_rate = 0.1
gradient = tf.reduce_mean((W*X-Y)*X)
descent = W - learning_rate * gradient
update = W.assign(descent)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(21):
    sess.run(update, feed_dict={X: x_data, Y: y_data})
    print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))
'''



#1
X=[1,2,3]
Y=[1,2,3]

W = tf.placeholder(tf.float32)
# X*W Linear model의 hypothesis
hypothesis = X*W

cost = tf.reduce_mean(tf.square(hypothesis - Y))
#Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())
W_val = []
cost_val = []

# Variables for plotting cost function
for i in range(-30,50):
    feed_W = i*0.1
    curr_cost, curr_W = sess.run([cost, W], feed_dict={W:feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost)

# Show the cost function
plt.plot(W_val, cost_val)
plt.show()
