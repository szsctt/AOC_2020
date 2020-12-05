#!/usr/bin/env python3

import math

def main():
	grid = []
	height = 0
	with open("input", 'r') as handle:
		for line in handle:
			grid.append(line.strip())
			height += 1

	trees = []		
	trees.append(count_trees(grid, 1, 1))
	trees.append(count_trees(grid, 3, 1))
	trees.append(count_trees(grid, 5, 1))
	trees.append(count_trees(grid, 7, 1))
	trees.append(count_trees(grid, 1, 2))

	print(f"tree counts: {trees}")
	print(f"product: {math.prod(trees)}")

def count_trees(grid, horiz_step, vert_step):
	i, j, trees = 0, 0, 0
	
	while i < len(grid) :
		j_pos = j % len(grid[i])
		if grid[i][j_pos] == '#':
			trees += 1
		i += vert_step
		j += horiz_step
	
	return trees
	
if __name__ == "__main__":
	main()