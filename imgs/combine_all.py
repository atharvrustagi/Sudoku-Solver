import numpy as np
import cv2
# import matplotlib.pyplot as plt

combine = np.loadtxt("0.txt").astype(np.uint8)

for i in range(1, 10):
	img = np.loadtxt(f"{i}.txt").astype(np.uint8)
	combine = np.row_stack([combine, img])

np.savetxt("combined.txt", combine)

print(combine.dtype)
cv2.imshow('i', combine[87].reshape(20, 20))
cv2.waitKey()
