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
	print("-"*28);
	for i in range(len(grid[0])):
		if (i % 3 == 0 and i != 0):
			print("-"*28);

		for j in range(len(grid[0])):
			if (j % 3 == 0):
				print("| "),

			if (g[i][j] == 0):
				print(" "),
			else:
				print(g[i][j]),
		
		print("|")
	print("-"*28);

def find_empty(g):
	for i in range(len(grid[0])):
		for j in range(len(grid[0])):
			if (g[i][j] == 0):
				return (i, j)

	return -1, -1

def possible_answers(g, c, r):
	possible = []

	for i in range(len(grid[0])):
		possible.append(i + 1);

	#searching all columns at index r
	for i in range(len(grid[0])):
		if (g[i][r] != 0):
			possible[g[i][r] - 1] = 0
	
	#searching row c at all indices
	for j in range(len(grid[0])):
		if (g[c][j] != 0):
			possible[g[c][j] - 1] = 0

	start_c = c / 3;
	start_r = r / 3;

	start_c = start_c * 3;
	start_r = start_r * 3;

	spacing = len(grid[0]) / 3;

	for a in range(spacing):
		for b in range(spacing):
			if (g[a + start_c][b + start_r] != 0):
				possible[g[a + start_c][b + start_r] - 1] = 0			

	return possible

def solve(g):
	column, row = find_empty(g)

	entry = [column, row]
	backtrack = [entry]

	p_arr = possible_answers(grid, column, row)
	b_poss = [p_arr]

	while(column != -1 and row != -1):
		i = 0

		while (i < len(grid[0])):
			if (b_poss[0][i] != 0):
				grid[column][row] = b_poss[0][i];
				b_poss[0][i] = 0;
				break;

			if (i == (len(grid[0]) - 1)):
				grid[column][row] = 0;

			i += 1

		if (grid[column][row] == 0):
			#means something went wrong, we need to backtrack
			backtrack.pop(0)
			column = backtrack[0][0]
			row = backtrack[0][1]
			b_poss.pop(0)

		else:	
			column, row = find_empty(g)
			entry = [column, row]
			backtrack.insert(0, entry)
			p_arr = possible_answers(grid, column, row)
			b_poss.insert(0, p_arr)


#Declarations#
print("Sudoku puzzle: ")
print_puzzle(grid)
solve(grid)
print("Solution: ")
print_puzzle(grid)

