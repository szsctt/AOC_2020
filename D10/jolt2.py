#!/usr/bin/env python3

import pdb

def main():

	# read input
	with open("input", 'r') as input_handle:
		adapters = []
		for line in input_handle:
			adapters.append(int(line.strip()))
			
	# add in lowest joltage - adapter in seat at 0
	adapters.append(0)
	# sort input
	adapters.sort()
	
	# add in highest joltage - three higher than highest
	adapters.append(adapters[-1]+3)
	
	
	# get difference between each adapter
	diffs = [adapters[i]-adapters[i-1] for i in range(1, len(adapters))]

	ones = sum([1 if i == 1 else 0 for i in diffs ])
	threes = sum([1 if i == 3 else 0 for i in diffs ])
	
	print(f"{ones} ones, {threes} threes, product: {ones*threes}")
	
	num_connections = count_leaves(adapters, {})
	print(num_connections)


def count_leaves(adapters, previous_results):
	if len(adapters) == 1:
		return 1
	else:
		# figure out which of the next three are valid and return their sum
		sum = 0
		upper_limit = min(len(adapters), 4)
		for i in range(1,upper_limit):
			if adapters[i] - adapters[0] <= 3:
				dict_key = "_".join([str(i) for i in adapters[i:]])
				if dict_key in previous_results:
					sum += previous_results[dict_key]
				else:
					previous_results[dict_key] = count_leaves(adapters[i:], previous_results)
					sum += previous_results[dict_key]
		return sum
			
				
	
if __name__ == "__main__":
	main()