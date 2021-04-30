import subprocess
from time import perf_counter as pf

# sudoku = [	"3 6 1 0 2 5 9 0 0",
# 			"0 8 0 9 6 0 0 1 0",
# 			"4 0 0 0 0 0 0 5 7",
# 			"0 0 8 0 0 0 4 7 1",
# 			"0 0 0 6 0 3 0 0 0",
# 			"2 5 9 0 0 0 8 0 0",
# 			"7 4 0 0 0 0 0 0 5",
# 			"0 2 0 0 1 8 0 6 0",
# 			"0 0 5 4 7 0 3 2 9"	]

# hardest
sudoku = [	"3 0 0 0 0 0 0 0 0",
			"0 0 5 0 0 9 0 0 0",
			"2 0 0 5 0 4 0 0 0",
			"0 2 0 0 0 0 7 0 0",
			"1 6 0 0 0 0 0 5 8",
			"7 0 4 3 1 0 6 0 0",
			"0 0 0 8 9 0 1 0 0",
			"0 0 0 0 6 7 0 8 0",
			"0 0 0 0 0 5 4 3 7"	]

grid = " ".join(sudoku)
print(grid)

n = 1
t = pf()
for _ in range(n):
	output = subprocess.run([r'.\sudoku_solver'], input=grid, 
		stdout = subprocess.PIPE, universal_newlines=True).stdout[1:90]

t = pf()-t
print(f"\nTime taken for {n} solve(s): {t} seconds.")
print(output)

