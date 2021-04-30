import numpy as np
import cv2
# import matplotlib.pyplot as plt

# generating blank output text file
# blank = np.random.randint(245, 256, size=(400, 400))
# np.savetxt('0.txt', blank)
# exit()

n = 400
for k in range(1, 10):
	img = cv2.imread(f'{k}_crop.png')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.uint8)

	imgs = np.zeros((n, 400))
	for i in range(20):
		r = i*49
		for j in range(20):
			c = j*49
			f = cv2.resize(img[r:r+49, c:c+49], (20, 20))
			imgs[i*20 + j] = f.flatten()
			cv2.imwrite(f'{k}/{k}-{i*20+j}.png', f)

	np.savetxt(f'{k}.txt', imgs)

