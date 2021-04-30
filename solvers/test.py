import numpy as np
import cv2
import matplotlib.pyplot as plt
from time import perf_counter as pf

# im = cv2.imread('sudokus.jpg')
# plt.imshow(im)
# plt.show()
# exit()

t = pf()

# im = cv2.imread('sudokus.jpg')[350:1400, 600:1650]
im = cv2.imread('sudokus.jpg')[1330:2450, 470:1635]
im = cv2.resize(im, (500, 500))
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 155, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for c in contours:
    ar = cv2.contourArea(c)
    if ar<200000 and ar>180000:
        cv2.drawContours(im, [c], 0, (128, 255, 0), 1)
        a = np.array(c)

aminx, aminy = np.argmin(a[..., 0]), np.argmin(a[..., 1])
amaxx, amaxy = np.argmax(a[..., 0]), np.argmax(a[..., 1])

cv2.circle(im, tuple(a[aminx, 0]), 5, (0,0,255), 3)
cv2.circle(im, tuple(a[aminy, 0]), 5, (0,0,255), 3)
cv2.circle(im, tuple(a[amaxx, 0]), 5, (0,0,255), 3)
cv2.circle(im, tuple(a[amaxy, 0]), 5, (0,0,255), 3)
img_siz = 405
grid_siz = img_siz//9
pts1 = np.float32([a[aminx, 0], a[aminy, 0], a[amaxx, 0], a[amaxy, 0]])
pts2 = np.float32([[0, img_siz], [0, 0], [img_siz, 0], [img_siz, img_siz]])
M = cv2.getPerspectiveTransform(pts1,pts2)
im2 = cv2.warpPerspective(imgray, M, (img_siz,img_siz))
for i in range(grid_siz, img_siz, grid_siz):
    cv2.line(im2, (i, 0), (i, img_siz), 0, 2)
    cv2.line(im2, (0, i), (img_siz, i), 0, 2)

im3 = np.where(im2 > 160, 255, im2)

grid = np.zeros((400, 81), np.uint8)
border = 4
for i in range(9):
	for j in range(9):
		g = im3[i*grid_siz+border:(i+1)*grid_siz-border, 
				j*grid_siz+border:(j+1)*grid_siz-border]
		g = np.pad(g, (10, 10), constant_values=(245, 245))
		grid[:, i*9 + j] = cv2.resize(g, (20, 20)).flatten()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_prop(X):
	# X.shape = (400, m)
	Z1 = W1.dot(X) + b1		# (25, 400)x(400, m) -> (25, m)
	A1 = sigmoid(Z1)
	Z2 = W2.dot(A1) + b2	# (10, 25)x(25, m) -> (10, m)
	A2 = sigmoid(Z2)
	return A2

hidden_nodes = 30
W1 = np.loadtxt("neural_network/W1.txt")
W2 = np.loadtxt("neural_network/W2.txt")
b1 = np.loadtxt("neural_network/b1.txt").reshape(hidden_nodes, 1)
b2 = np.loadtxt("neural_network/b2.txt").reshape(10, 1)

preds = forward_prop(grid)
preds = np.argmax(preds, axis=0).reshape(9, 9)
print(preds)
print(preds.shape)

print(f"Time taken: {round(pf()-t, 4)}")

cv2.imshow('b&w', imgray)
# cv2.imshow('im2', im2)
cv2.imshow('im3', im3)
cv2.imshow('sm0l', grid[:, 11].reshape(20, 20))
cv2.waitKey()
