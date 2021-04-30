import numpy as np
import matplotlib.pyplot as plt
import cv2

 
# crop from -> (48, 22)
# crop to -> (1028, 1002)

for i in range(1, 10):
	img = cv2.imread(f'{i}.png')
	img = img[22:1002, 48:1028]
	cv2.imwrite(f"{i}_crop.png", img)
