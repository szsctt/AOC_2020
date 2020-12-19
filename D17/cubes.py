
import numpy as np
import itertools
import pdb

def main():
	
	# part 1
# 	g = Grid("input")
# 	print(g)
# 	for i in range(6):
# 		g.apply_rules()
# 	print(g)
# 	print(g.count_active_cubes())
# 	

	# part 2
	g = Grid4("input")
	print(g)
	for i in range(6):
		g.apply_rules()
	
	print(g.count_active_cubes())
	


class Grid():
	def __init__(self, input):
		lines = []
		with open(input, 'r') as inhandle:
			for line in inhandle:
				lines.append(line.strip())
		
		self.grid = np.full((len(lines[0]),len(lines),1), ".")
		for y, line in enumerate(lines):
			for x, l in enumerate(line):
				self.grid[x][y][0] = l
				
				
	def __repr__(self):
		"""
		print in same way as in advent of code problem
		"""
		str = ""
		for k in range(self.grid.shape[2]):
			str = str + f"z = {k}\n"
			for j in range(self.grid.shape[1]):
				for i in range(self.grid.shape[0]):
					str = str + self.grid[i][j][k]
				str = str + "\n"
			str = str + "\n"
		return str
				
	def add_new_coords(self, dim, location):
		"""
		add new row/column/slice of '.' at x( or y,z)=0 or x( or y,z)=max
		"""	
		assert location in {'before', 'after'}
		assert dim in {'x', 'y', 'z'}
		
		if dim == 'x':
			ax = 0
			new = np.full((self.grid.shape[1], self.grid.shape[2]), '.')
			loc = self.grid.shape[0]
		elif dim == 'y':
			ax = 1
			new = np.full((self.grid.shape[0], self.grid.shape[2]), '.')
			loc = self.grid.shape[1]	
		elif dim == 'z':
			ax = 2
			new = np.full((self.grid.shape[0], self.grid.shape[1]), '.')
			loc = self.grid.shape[2]
		
		if location == 'before':
			self.grid = np.insert(self.grid, 0, new, axis=ax)
		else:
			self.grid = np.insert(self.grid, loc, new, axis=ax)

	def check_side_active(self, dim, location):
		"""
		check if there is a '#' on the edge of the surface of the current cube
		"""
		assert location in {'before', 'after'}
		assert dim in {'x', 'y', 'z'}
		
		if dim == 'x':
			j = range(self.grid.shape[1])
			k = range(self.grid.shape[2])
			if location == 'before':
				i = [0]
			else:
				i = [self.grid.shape[0]-1]
		elif dim == 'y':
			i = range(self.grid.shape[0])
			k = range(self.grid.shape[2])
			if location == 'before':
				j = [0]
			else:
				j = [self.grid.shape[1]-1]	
		elif dim == 'z':
			i = range(self.grid.shape[0])
			j = range(self.grid.shape[1])
			if location == 'before':
				k = [0]
			else:
				k = [self.grid.shape[2]-1]	
				
		
		for x, y, z in itertools.product(i, j, k):
			if self.grid[x][y][z] == '#':
				return True
		
		return False 		
		
	def add_padding(self):
		"""
		if there is a '#' on the edge of the surface of the current cube, add padding to that side
		"""
		for dim in ('x', 'y', 'z'):	
			for loc in ('before', 'after'):
				if self.check_side_active(dim, loc):
					self.add_new_coords(dim, loc)		
					
	def check_neighbours(self, i, j, k):
		"""
		check how many of the neighbours of the cube at position i, j, k are active
		"""
		sum = 0
		for x, y, z in itertools.product((i-1, i, i+1), (j-1, j, j+1), (k-1, k, k+1)):
			if (x, y, z) == (i, j, k):
				continue
			if x < 0 or y < 0 or z < 0:
				continue
			try:
				if self.grid[x][y][z] == '#':
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
		
		for i, j, k in itertools.product(range(self.grid.shape[0]), range(self.grid.shape[1]), range(self.grid.shape[2])):
			neigbours = self.check_neighbours(i, j, k)
			print(f"cube at position {i}, {j}, {k} is {self.grid[i][j][k]} and has {neigbours} neighbours active")
			if self.grid[i][j][k] == '#':
				if neigbours != 2 and neigbours != 3:
					new_grid[i][j][k] = '.'
			else:
				if neigbours == 3:
					new_grid[i][j][k] = '#'
					
		self.grid = new_grid
		
	def count_active_cubes(self):
		count = 0
		for i in range(self.grid.shape[0]):
			for j in range(self.grid.shape[1]):
				for k in range(self.grid.shape[2]):
					if self.grid[i][j][k] == '#':
						count += 1
		return count

class Grid4():
	def __init__(self, input):
		lines = []
		with open(input, 'r') as inhandle:
			for line in inhandle:
				lines.append(line.strip())
		
		self.grid = np.full((len(lines[0]),len(lines), 1, 1), ".")
		for y, line in enumerate(lines):
			for x, l in enumerate(line):
				self.grid[x][y][0] = l				

	def __repr__(self):
		"""
		print in same way as in advent of code problem
		"""
		str = ""
		for	l in range(self.grid.shape[3]):
			for k in range(self.grid.shape[2]):
				str = str + f"z = {k}, w = {l}\n"
				for j in range(self.grid.shape[1]):
					for i in range(self.grid.shape[0]):
						str = str + self.grid[i][j][k][l]
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