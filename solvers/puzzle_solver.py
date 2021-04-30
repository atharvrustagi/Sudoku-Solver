import numpy as np
from time import perf_counter as pf

grid = np.zeros((50, 9, 9), dtype=np.uint8)
f = open("puzzles.txt")
m = i = j = 0
for i, row in enumerate(f):
	if row[0]!='G':
		for j, c in enumerate(row[:-1]):
			grid[i//10, i%10-1, j] = int(c)
f.close()
# exit()

def is_available(r, c, val, grid):
	if np.any(grid[r]==val):
		return False
	if np.any(grid[:, c]==val):
		return False
	r = r - r%3
	c = c - c%3
	if np.any(grid[r:r+3, c:c+3]==val):
		return False

	return True

def solve_cell(r, c, grid):
	global solved
	if (r==9):
		return
	r_new = r+1 if c==8 else r
	c_new = (c+1)%9
	if (grid[r, c]):
		solve_cell(r_new, c_new, grid)
	else:
		for val in range(9, 0, -1):
			if is_available(r, c, val, grid):
				grid[r, c] = val
				solve_cell(r_new, c_new, grid)
				if solved:
					return
		if grid[rlast, clast]:
			solved = True
		else:
			grid[r, c] = 0

def check_grid(grid):
	if np.any(np.sum(grid, axis=0)!=45) or np.any(np.sum(grid, axis=1)!=45):
		return False

	# 3x3 grid check left
	return True

solved = False
rlast = clast = 0
found = False
count = 0
t = pf()
for m in range(50):
	t1 = pf()
	solved = False
	rlast = clast = 0
	found = False
	for i in range(8, -1, -1):
		for j in range(8, -1, -1):
			if not grid[m, i, j]:
				rlast = i
				clast = j
				found = True
				break
		if found:
			break
	solve_cell(0, 0, grid[m])
	if check_grid(grid[m]):
		count += 1
		print(f"{m+1}. Solved in {round(pf()-t1, 4)} seconds. ({count} / 50)")
	else:
		print("Not solved. F")
t = pf()-t
print(f"\nAll solved in {t} seconds.")
