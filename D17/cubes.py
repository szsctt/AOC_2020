
import numpy as np
import itertools
import pdb

def main():
	
	# part 1
	g = GridN("input", 3)
	#print(g)
	for i in range(6):
		g.apply_rules()
	#print(g)
	print(g.count_active_cubes())

	# part 2
	g = GridN("input", 4)
	#print(g)
	for i in range(6):
		g.apply_rules()
	#print(g)
	print(g.count_active_cubes())
	


class GridN():
	def __init__(self, input, n=4):
		assert n > 1
		lines = []
		with open(input, 'r') as inhandle:
			for line in inhandle:
				lines.append(line.strip())
		
		grid_size = [len(lines[0]),len(lines)] + [1 for i in range(n-2)]
		self.grid = np.full(grid_size, ".")
		for y, line in enumerate(lines):
			for x, l in enumerate(line):
				self.grid[x][y][0] = l				

	def __repr__(self):
		"""
		print in same way as in advent of code problem
		"""
		if len(self.grid.shape) > 4:
			return f"grid with shape {self.grid.shape}"
		
		str = ""
		ranges = [range(i) for i in self.grid.shape[2:]]
		dims = ("z", "w")
		for coords in itertools.product(*ranges):
			str = str + ", ".join([f"{dims[i]} = {coords[i]}" for i in range(len(coords))]) + "\n"
			for i in range(self.grid.shape[0]):
				for j in range(self.grid.shape[1]):
					coords_2 = [i, j] + list(coords)
					str = str + self.get_value_at_coords(coords_2, self.grid)
				str = str + "\n"
			
			str = str + "\n"
		
		return str

	def add_new_coords(self, dims, locs):
		"""
		add new slice of '.' at location in dimension
		"""	
		assert len(dims) == len(locs)
		for d in dims:
			assert d in range(len(self.grid.shape))
		for i, l in enumerate(locs):
			assert l in range(-self.grid.shape[dims[i]], self.grid.shape[dims[i]])
		
		# make new array of '.' with dimensions added
		new_shape = [i for i in self.grid.shape]
		for i in dims:
			new_shape[i] += 1
		new = np.full(new_shape, '.')
		
		# transfer old data to new array
		ranges = [list(range(i)) for i in new.shape]
		for i in range(len(dims)):
			ranges[dims[i]].pop(locs[i])
			
		for coords in itertools.product(*[range(i) for i in self.grid.shape]):
			new_coords = []

			for i, c in enumerate(coords):
				new_coords.append(ranges[i][c])
			val = self.get_value_at_coords(coords, self.grid)
			new = self.set_value_at_coords(new_coords, val, new)

			
		self.grid = new

	def get_value_at_coords(self, coords, grid):
		base_type = type(grid)
		curr = grid
		for i in coords:
			curr = curr[i]
			if not isinstance(curr, base_type):
				return curr
	
	def set_value_at_coords(self, coords, value, grid):
		base_type = type(self.grid)
		curr = grid
		for i in coords:
			last = curr
			curr = curr[i]
			if not isinstance(curr, base_type):
				last[i] = value
				return grid
			
	def check_side_active(self, dim, loc):
		"""
		check if there is a '#' on the edge of the surface of the current cube
		"""
		assert dim in range(len(self.grid.shape))
		assert loc in range(-self.grid.shape[dim], self.grid.shape[dim])
		
		ranges = [range(self.grid.shape[i]) for i in range(len(self.grid.shape)) if i != dim]				
		ranges.insert(dim, [loc])
		for coords in itertools.product(*ranges):
			if self.get_value_at_coords(coords, self.grid) == '#':
				return True
		
		return False 	

	def add_padding(self):
		"""
		if there is a '#' on the edge of the surface of the current cube, add padding to that side
		"""
		dims = []
		locs = []
		for dim, loc in itertools.product(range(len(self.grid.shape)), (0, -1)):	
			if self.check_side_active(dim, loc):
				dims.append(dim)
				locs.append(loc)
		self.add_new_coords(dims, locs)
					
	def check_neighbours(self, coords):
		"""
		check how many of the neighbours of the cube at position i, j, k are active
		"""
		sum = 0
		ranges = [(i-1, i, i+1) for i in coords]
		for i_coords in itertools.product(*ranges):
			if i_coords == coords:
				continue
			if any([i < 0 for i in i_coords]):
				continue
			try:
				if self.get_value_at_coords(i_coords, self.grid) == "#":
					sum += 1
			except IndexError:
				pass
				
		return sum							
		
	def apply_rules(self):
		"""
		apply rules:
		
    	If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
    	Otherwise, the cube becomes inactive.
    	If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
    	Otherwise, the cube remains inactive.

		"""
		self.add_padding()
		
		new_grid = np.copy(self.grid)
		ranges = [range(i) for i in self.grid.shape]
		
		for coords in itertools.product(*ranges):
			neigbours = self.check_neighbours(coords)
#			print(f"cube at position {coords} is {self.get_value_at_coords(coords, self.grid)} and has {neigbours} neighbours active")
			if self.get_value_at_coords(coords, self.grid) == '#':
				if neigbours != 2 and neigbours != 3:
					new_grid = self.set_value_at_coords(coords, '.', new_grid)
			else:
				if neigbours == 3:
					new_grid = self.set_value_at_coords(coords, '#', new_grid)
					
		self.grid = new_grid
		
	def count_active_cubes(self):
		count = 0
		ranges = [range(i) for i in self.grid.shape]		
		for coords in itertools.product(*ranges):
			if self.get_value_at_coords(coords, self.grid) == '#':
				count += 1
		
		return count
if __name__ == "__main__":
	main()