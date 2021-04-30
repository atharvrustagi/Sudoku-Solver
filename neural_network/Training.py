import numpy as np
from time import perf_counter as pf

"""
number of examples -> m
input size -> (400, m)
hidden layers -> 1 (25 units)
output layer -> 10 units
"""


# dataset
X = np.loadtxt("training_set.txt") / 255		# normalizing
Y = np.loadtxt("training_labels.txt").astype(bool)
m = X.shape[0]
np.random.seed(0)
shuffle = np.arange(m)
np.random.shuffle(shuffle)
X = X[shuffle]
Y = Y[shuffle]

ntest = 500
X_test = X[:ntest].T
Y_test = Y[:ntest].T
X = X[ntest:]
Y = Y[ntest:]
shf2 = np.arange(m-ntest)
np.random.seed(np.random.randint(0, 1000))
np.random.shuffle(shf2)
X = X[shf2].T
Y = Y[shf2].T

# print(X.shape, Y.shape, X_test.shape, Y_test.shape)
print(f"Verifying seed [2230  668 3616 2363  142]=={shuffle[:5]}")
print(f"Verifying random : {shf2[:5]}")


# weights and biases
hidden_nodes = 30
# initialize
# W1 = np.random.randn(hidden_nodes, 400)
# b1 = np.zeros((hidden_nodes, 1))
# W2 = np.random.randn(10, hidden_nodes)
# b2 = np.zeros((10, 1))

# load
W1 = np.loadtxt("W1.txt")
W2 = np.loadtxt("W2.txt")
b1 = np.loadtxt("b1.txt").reshape(hidden_nodes, 1)
b2 = np.loadtxt("b2.txt").reshape(10, 1)


def sigmoid(x):
	return 1/(1+np.exp(-x))

def forward_prop(X):
	# X.shape = (400, m)
	Z1 = W1.dot(X) + b1		# (25, 400)x(400, m) -> (25, m)
	A1 = sigmoid(Z1)
	Z2 = W2.dot(A1) + b2	# (10, 25)x(25, m) -> (10, m)
	A2 = sigmoid(Z2)
	return A1, A2


def backward_prop(X, A1, A2, Y, W1, W2):
	dA2 = A2-Y					# (10, m)
	dW2 = dA2.dot(A1.T) / m		# (10, 25)
	db2 = np.mean(dA2, axis=1, keepdims=True)
	dA1 = W2.T.dot(dA2) * A1 * (1-A1)
	dW1 = dA1.dot(X.T) / m
	db1 = np.mean(dA1, axis=1, keepdims=True)
	cost = -(np.sum((Y.dot(np.log(A2.T)) + (1-Y).dot(np.log(1-A2.T))).diagonal()) + 0.5 * lam * (np.sum(W1**2) + np.sum(W2**2))) / m
	return cost, dW1, db1, dW2, db2


# _, out = forward_prop(X)
# accuracy = np.mean(np.argmax(out, axis=0)==np.argmax(Y, axis=0))
# print(f"Accuracy before training: {accuracy*100}%")

lr = 0.05
lam = 0.02
iterations = 1
for i in range(1, iterations+1):
	A1, A2 = forward_prop(X)
	cost, dW1, db1, dW2, db2 = backward_prop(X, A1, A2, Y, W1, W2)
	W1 -= lr * (dW1 + lam/m * W1)
	W2 -= lr * (dW2 + lam/m * W2)
	b1 -= lr * db1
	b2 -= lr * db2

	if i%50==0:
		print(f"Iteration {i}: Cost: {cost}")

# _, A2 = forward_prop(X)
accuracy = np.mean(np.argmax(A2, axis=0)==np.argmax(Y, axis=0))
print(f"Accuracy on training set: {accuracy*100}%")
_, A2 = forward_prop(X_test)
accuracy = np.mean(np.argmax(A2, axis=0)==np.argmax(Y_test, axis=0))
print(f"Accuracy on test set: {accuracy*100}%")

# saving weights
np.savetxt( "W1.txt", W1)
np.savetxt( "W2.txt", W2)
np.savetxt( "b1.txt", b1)
np.savetxt( "b2.txt", b2)
