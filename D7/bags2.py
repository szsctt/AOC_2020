#!/usr/bin/env python

# use networkx to make a directed graph
import networkx as nx
import matplotlib.pyplot as plt
import re
import pdb

def main():
	DG = nx.DiGraph()
	colours = {}
	numbers = {}
	with open("input", 'r') as handle:
		for line in handle:
			# get outer bag
			src = re.match("^([\w ]+?) bags", line.strip()).groups()[0]
			# add to dict if not already seen
			if src not in colours:
				colours[src] = len(colours) + 1
				DG.add_node(colours[src], color=src)
			
			# get inner bag(s)
			dst = re.findall(r"(\d+ [\w ]+?) bag", line.strip())
			for d in dst:
				num = re.search(r"(\d+)", d).groups()[0]
				col = d[len(num)+1:]
				# if we haven't seen this colour before, add node to graph
				if col not in colours:
					colours[col] = len(colours) + 1
					DG.add_node(colours[col], color=d)
				# add connecting edge between src and this colour
				DG.add_edge(colours[src], colours[col])
			
				# keep track of the number of bags involved with this edge
				numbers[(colours[src], colours[col])] = int(num)


	print(f"number of bags inside a shiny gold bag: {num_bags_inside(DG, numbers, colours['shiny gold'])}")

def num_bags_inside(DG, numbers, node):
	"""
	get number of bags inside the specified node
	"""

	num = 0
	# if no bags inside
	if len(list(DG.successors(node))) == 0:
		return num
	
	# if bags inside, return the number of those bags, plus the number of bags inside them
	for s in DG.successors(node):
		# there are this many of these bags inside
		num += numbers[(node, s)]
		# and this many bags inside all of those bags 
		num += numbers[(node, s)] * num_bags_inside(DG, numbers, s)
		
	
	return num

	
		
	
		
if __name__ == "__main__":
	main()
	
		
	
