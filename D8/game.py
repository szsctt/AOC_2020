#!/usr/bin/env python3

import re
import pdb

def main():
	# read in instructions
	instruct = []
	with open("input", 'r') as handle:
		for line in handle:
			num = int(re.search('[+|-]\d+$', line.strip()).group())
			if 'nop' in line:
				instruct.append({'type': 'nop'})
			elif 'acc' in line:
				instruct.append({'type': 'acc', 'num': num})
			elif 'jmp' in line:
				instruct.append({'type': 'jmp', 'num': num})			

	last_instruct = run_instructions(instruct)
	if last_instruct  == len(instruct):
		print(f"finished last instruction")
		
	for i in range(len(instruct)):
		# copy instruction i
		op_i = instruct[i].copy()
		# replace instruction i with nop
		instruct[i] = {'type': 'nop'}
		last_instruct, acc = run_instructions(instruct)
		if last_instruct == len(instruct):
			print(f"finished last instruction after changing instruction {i+1} - accumulator was ")
			break
		# replace operation i
		instruct[i] = op_i

def run_instructions(instruct):
	# start executing instructions
	acc = 0
	i = 0 # current position
	seen = set()

	
	while i not in seen:
		try:
			print(i)	
			seen.add(i)
			inst = instruct[i]
			if inst['type'] == 'nop':
				i += 1
			elif inst['type'] == 'jmp':
				i += inst['num']
			elif inst['type'] == 'acc':
				i += 1
				acc += inst['num']
		except IndexError:
			break

	print(f"accumultor was {acc}, last instruction was number {i}")
	return i, acc
	
if __name__ == "__main__":
	main()