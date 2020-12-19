import re
import pdb

def main():
	with open("input", 'r') as inhandle:
		instructions = []
		for line in inhandle:
			instructions.append(line.strip())
		
	# part 1
	mem = apply_instructions(instructions)
	print(sum([i for i in mem.values()]))
	
	# part 2
	mem = apply_instructions_2(instructions)
	print(sum([i for i in mem.values()]))

def apply_instructions_2(instructions):
	memory = {}
	for i in instructions:
		if i[0:4] == "mask":
			mask, floating = generate_bitmasks(i[-36:])
		else:
			nums = re.match("mem\[(\d+)\] = (\d+)", i)
			addresses = apply_bitmasks_2(mask, floating, int(nums.groups()[0]))
			for addr in addresses:
				memory[addr] = int(nums.groups()[1])
			
	return memory
	
def apply_bitmasks_2(mask, floating, num):
	
	# first, apply mask
	addresses = [num | mask]
	
	# then change floating bits
	for i in floating:
		new_addr = []
		for addr in addresses:
			# if this bit is set, need to add unset bit
			if addr & (1 << i):
				new_addr.append(addr - (1 << i))
			# if this bit is unset, need to add unset bit
			else:
				new_addr.append(addr + (1 << i))
		addresses += new_addr
				
	return addresses
	
def generate_bitmasks(bitmask):
	"""
    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.
	"""
	mask = 0
	floating = []
	for i, bit in enumerate(reversed(bitmask)):
		if bit == '1':
			mask = mask + (1 << i) 
		if bit == 'X':
			floating.append(i)
			
			
	return mask, floating
	
def apply_instructions(instructions):
	memory = {}
	for i in instructions:
		if i[0:4] == "mask":
			current_mask = i[-36:]
		else:
			nums = re.match("mem\[(\d+)\] = (\d+)", i)
			memory[nums.groups()[0]] = apply_bitmask(current_mask, nums.groups()[1])
			
	return memory

def apply_bitmask(mask, value):
	onemask = "".join(['1' if i == '1' else '0' for i in mask])
	zeromask = "".join(['0' if i == '0' else '1' for i in mask])
	
	return (int(value) | int(onemask, 2)) & int(zeromask, 2)
	
	
if __name__ == "__main__":
	main()