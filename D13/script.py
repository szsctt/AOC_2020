#!/usr/bin/env python3
import pdb
import numpy as np
import math

def main():
	
	# read input
	with open("input", 'r') as inhandle:
		arrival = int(next(inhandle).strip())
		busses = next(inhandle).strip().split(",")
		

	#least_min_waited, earliest_bus_number = find_earliest_bus(arrival, busses)
	#print(f"min waited: {least_min_waited}, bus num: {earliest_bus_number}, product: {least_min_waited*earliest_bus_number}")
	
	a = []
	n = []
	for i, bus in enumerate(busses):
		if bus == 'x':
			continue
		print(f"bus {bus} at time t + {i}")
		a.append(i)
		n.append(int(bus))
	
	# check pairwaise coprime
	for i in n:
		for j in n:
			if i == j:
				continue
			if np.gcd(i, j) != 1:
				print(f"{i}, {j} are not coprime")
	
	i = satisfy_constraints(busses)
	print(int(i))
	print()
	 




	
# https://brilliant.org/wiki/chinese-remainder-theorem/
def satisfy_constraints(busses):
	sum = 0
	
	bus_nums = [int(i) for i in busses if i != 'x']
	N = int(np.prod(bus_nums))
	
	for i, num in enumerate(busses):
		if num == 'x':
			continue 

		remainder = int(num) - i
		
		
		
		y = int(N / int(num))
		
		z = pow(y, -1, int(num))
		sum += remainder * y * z
		
	return sum % N


def find_earliest_bus(arrival, busses):
	earliest_bus_number = None
	least_min_waited = 10000000
	for bus_num in busses:
		if bus_num == 'x':
			continue
		bus_num = int(bus_num)
		min_waited = bus_num - (arrival % bus_num) 
		if min_waited < least_min_waited:
			least_min_waited = min_waited
			earliest_bus_number = bus_num


	return least_min_waited, earliest_bus_number
	
if __name__ == "__main__":
	main()