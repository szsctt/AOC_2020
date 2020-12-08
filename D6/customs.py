#!/usr/bin/env python


count = 0
group = set()
with open("input", 'r') as handle:
	for line in handle:
		if line == "\n":
			count += len(group)
			group = set()
		else:
			for let in line.strip():
				group.add(let)

print(count)