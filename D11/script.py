#!/usr/bin/env python3

import pdb
import itertools

def main():
	
	# read in chair layout
	chairs = []
	with open("input", 'r') as inhandle:
		for line in inhandle:
			chairs.append([let for let in line.strip()])
	
	# part 1
# 	chairs, num_changes = apply_rules(chairs)
# 	
# 	while num_changes > 0:
# 		chairs, num_changes = apply_rules(chairs)
# 	print(f"there are {count_occupied(chairs)} occupied chairs")
	
	# part 2
	print_chairs(chairs)
	chairs, num_changes = apply_part_2_rules(chairs)
	print_chairs(chairs)
	
	while num_changes > 0:
		chairs, num_changes = apply_part_2_rules(chairs)
		print_chairs(chairs)
	print(f"there are {count_occupied(chairs)} occupied chairs")
	
def apply_part_2_rules(chairs):
	"""
	consider the first seat they can see in each of those eight directions (up, down, left, right, diagonal)
	
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
	"""
	num_changes = 0
	new_chairs = []
	for i in range(len(chairs)):
		row = chairs[i]
		new_chairs.append(list(chairs[i]))
		for j in range(len(row)):
			# chair unoccupied
			if chairs[i][j] == 'L':	
				# check number of adjacent occupied chairs
				occupied = num_seen_occupied(i, j, chairs)
				if occupied == 0:
					new_chairs[i][j] = '#'
					num_changes += 1
			# chair occupied
			if chairs[i][j] == '#':
				occupied = num_seen_occupied(i, j, chairs)
				if occupied >= 5:
					new_chairs[i][j] = 'L'
					num_changes += 1
					
	return new_chairs, num_changes	
	

def num_seen_occupied(i, j, chairs):
	"""
	count the number of occupied chairs that can be seen from chair i, j
	consider the first seat they can see in each eight directions (up, down, left, right, diagonal)
	"""
	occupied = 0
	# check seat above (i-1, j)
	for x, y in itertools.product(["inc", "no", "dec"], ["inc", "no", "dec"]):
		if x == "no" and y == "no":
			continue
		if seen_in_direction(i, j, x, y, chairs):
			occupied += 1
			
	return occupied	
	
	
def seen_in_direction(i, j, i_direction, j_direction, chairs):
	"""
	check if there is an occupied chair visible from chair i, j, if we increment/decrement i and j as specified
	"""
	# increment or decrement i
	if i_direction == "inc":
		new_i = i + 1
	elif i_direction == "dec":
		new_i = i - 1
	else:
		new_i = i
	# increment or decrement j
	if j_direction == "inc":
		new_j = j + 1
	elif j_direction == "dec":
		new_j = j - 1
	else:
		new_j = j
	# if we're off the grid, there's no seen chair
	if new_i < 0 or new_i >= len(chairs):
		return False
	if new_j < 0 or new_j >= len(chairs[i]):
		return False
		
	# if chair is occupied
	if chairs[new_i][new_j] == '#':
		return True
	
	# if chair is unoccupied:
	elif chairs[new_i][new_j] == 'L':
		return False
		
	# if floor, keep going:
	else:
		return seen_in_direction(new_i, new_j, i_direction, j_direction, chairs)
		

def apply_rules(chairs):
	"""
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
	"""
	num_changes = 0
	new_chairs = []
	for i in range(len(chairs)):
		row = chairs[i]
		new_chairs.append(list(chairs[i]))
		for j in range(len(row)):
			# chair unoccupied
			if chairs[i][j] == 'L':	
				# check number of adjacent occupied chairs
				occupied = num_adjacent_occupied(i, j, chairs)
				if occupied == 0:
					new_chairs[i][j] = '#'
					num_changes += 1
			# chair occupied
			if chairs[i][j] == '#':
				occupied = num_adjacent_occupied(i, j, chairs)
				if occupied >= 4:
					new_chairs[i][j] = 'L'
					num_changes += 1
					
	return new_chairs, num_changes

def num_adjacent_occupied(i, j, chairs):
	occupied = 0
	# check seat above (i-1, j)
	for x, y in itertools.product([i-1, i, i+1], [j-1, j, j+1]):
		if x == i and y == j:
			continue
		if chair_occupied(x, y, chairs):
			occupied += 1
			
	return occupied

def chair_occupied(i, j, chairs):
	if i >= 0 and i < len(chairs):
		if j >= 0 and j < len(chairs[i]):
			if chairs[i][j] == '#':
				return True
	return False

def print_chairs(chairs):
	[print("".join(line)) for line in chairs]
	print()

def count_occupied(chairs):
	occupied = 0
	for i in range(len(chairs)):
		for j in range(len(chairs[i])):
			if chairs[i][j] == "#":
				occupied += 1
	return occupied

if __name__ == "__main__":
	main()