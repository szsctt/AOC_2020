#!/usr/bin/env python

# use networkx to make a directed graph
import networkx as nx
import matplotlib.pyplot as plt
import re
import pdb

DG = nx.DiGraph()
colours = {}
numbers = {}
with open("small_input", 'r') as handle:
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
			DG.add_edge(colours[col], colours[src])


p = [a for a in nx.bfs_predecessors(DG, colours['shiny gold'])]

print(colours)
print("predecessors:")
print(p)
print(f"number of predecessors: {len(p)}")


nx.draw_networkx(DG, with_labels = True)
plt.show()


		
	
