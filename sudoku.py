grid = [
	[5, 3, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_puzzle(g):
        print("----------------------------")
	for i in range(9):
		if (i % 3 == 0 and i != 0):
			print("----------------------------")
	
		for j in range(9):
			if (j % 3 == 0):
				print("| "),

			if (g[i][j] == 0):
				print(" "),
			else:
				print(g[i][j]),
		
		print("|")
	print("----------------------------")         

def find_empty(g):
	for i in range(9):
		for j in range(9):
			if (g[i][j] == 0):
				return (i, j)

	return -1, -1

def possible_answers(g, c, r):
	#c, r = find_empty(g)

	possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	#searching all columns at index r
	for i in range(9):
		if (g[i][r] != 0):
			possible[g[i][r] - 1] = 0
	
	#searching row c at all indices
	for j in range(9):
		if (g[c][j] != 0):
			possible[g[c][j] - 1] = 0

	return possible

def attempt(g, c, r):
	#column, row = find_empty(g)

	p = possible_answers(grid, c, r)

	for i in range(9):
		if (p[i] != 0):
			grid[c][r] = p[i];
			break;

def solve(g):
	column, row = find_empty(g)
	backtrack = [[column, row]] 

	while(column != -1 and row != -1):
		attempt(grid, column, row)
		column, row = find_empty(g)
		entry = [column, row]
		backtrack.insert(0,entry)

#Declarations#
print("Sudoku puzzle: ")
print_puzzle(grid)
solve(grid)
print("Attempt 1: ")
print_puzzle(grid)

