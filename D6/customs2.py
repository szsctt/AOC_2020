#!/usr/bin/env python

import pdb

count = 0
group = {}
group_n = 0
with open("input", 'r') as handle:
	for line in handle:
		if line == "\n":
			count += sum([1 for let, count in group.items() if count == group_n])
			group = {}
			group_n = 0
		else:
			for let in line.strip():
				if let in group:
					group[let] += 1
				else:
					group[let] = 1
			group_n += 1

print(count)