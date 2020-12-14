#!/usr/bin/env python3

import pdb
import numpy as np

def main():

	directions = []
	with open("input", "r") as inhandle:
		for line in inhandle:
			directions.append(line.strip())
	
	
	# part 1		
	#NS, WE = follow_directions(directions, 'E')
	#print(f"manhattan distance: {abs(NS) + abs(WE)}")
	
	# part 2
	pos = follow_waypoint_directions(directions, -10, 1)
	print(f"manhattan distance: {abs(pos[0][0]) + abs(pos[1][0])}")
	
	
def follow_waypoint_directions(directions, WE_way, NS_way):
	# matrix transpose((x, y)) where x is W/E direction and y is N/S direction
	coords = np.matrix([[WE_way], [NS_way]]) # waypoint
	pos = np.matrix([[0], [0]]) # current ship position
	
	for dir in directions:
	
		num = int(dir[1:])
		
		# move waypoint by set amount
		if dir[0] == 'N':
			coords[1][0] += num
		elif dir[0] == 'E':
			coords[0][0] -= num
		elif dir[0] == 'S':
			coords[1][0] -= num
		elif dir[0] == 'W':
			coords[0][0] += num
			
		# rotate waypoint
		elif dir[0] == 'L':
			coords = rotate_waypoint(coords, num)
		elif dir[0] == 'R':
			coords = rotate_waypoint(coords, -num)
			
		# move forward
		elif dir[0] == 'F':
			pos = np.add(pos, coords*num)
		
		print(f"direction: {dir}, waypoint coords:\n {coords}, current position:\n {pos}\n\n")
		
	return pos
			
			
			
			
			
			
def rotate_waypoint(coords, deg):
	rad = deg*np.pi/180
	rot_matrix = np.matrix([[np.cos(rad), np.sin(rad)], [-np.sin(rad), np.cos(rad)]])
	print(rot_matrix)
	return np.round(rot_matrix * coords)
		
			
			
def follow_directions(directions, curr_dir):
	WE = 0 # west/east positon, where west is positive and east is negative
	NS = 0 # north/south position, where north is positive and south is negative
	dirs = ['N', 'E', 'S', 'W'] # clockwise order of directions
	for dir in directions:
		if dir[0] in dirs:
			NS, WE = move_direction(NS, WE, dir[0], int(dir[1:]))
		else:
			if dir[0] == 'F':
				NS, WE = move_direction(NS, WE, curr_dir, int(dir[1:]))	
				continue	
			
			num_steps = int(dir[1:])/90 # number of directions to rotate
			curr_i = dirs.index(curr_dir)
			if dir[0] == 'L':
				curr_i = (curr_i - num_steps ) % 4
				curr_dir = dirs[int(curr_i)]
			elif dir[0] == 'R':
				curr_i = (curr_i + num_steps ) % 4	
				curr_dir = dirs[int(curr_i)]
				
		print(f"current dir: {curr_dir}, NS pos {NS}, WE pos {WE}")
		
	return NS, WE
		
			
def move_direction(NS, WE, dir, num):
	if dir == 'N':
		NS += num
	elif dir == 'E':
		WE -= num
	elif dir == 'S':
		NS -= num
	elif dir == 'W':
		WE += num		
		
	return NS, WE		
			
if __name__ == "__main__":
	main()