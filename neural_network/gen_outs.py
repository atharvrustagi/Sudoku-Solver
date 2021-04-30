import numpy as np

f = open('outs.txt', 'w')

for i in range(10):
	st = i*"0 " + "1 " + (9-i)*"0 " + '\n'
	for _ in range(400):
		f.write(st)

f.close()

