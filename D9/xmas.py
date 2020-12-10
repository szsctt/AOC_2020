#!/usr/bin/env python3

import pdb


preamble_length = 25

def main():
	nums = []
	with open('input', 'r') as handle:
		for line in handle:
			if len(nums) < preamble_length:
				nums.append(int(line.strip()))
				continue
				
			if not valid_number(nums[-preamble_length:], int(line.strip())):
				print(f"number {line.strip()} is not a valid number")
				num = int(line.strip())
				break
			
			nums.append(int(line.strip()))
			
			#print(f"line: {line.strip()}, preamble: {nums[-preamble_length:]}")
			
			
			
	# find contiugous range for part2
	contig_nums = find_contiguous_range(nums, num)
	
	# encryption weakness is smallest + largest number
	contig_nums.sort()
	weakness = contig_nums[0] + contig_nums[-1]
	
	print(f"nums: {contig_nums}, weakness: {weakness}")

def find_contiguous_range(nums, num):
	"""
	find a contiguous range of numbers that add up to number
	"""
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if sum(nums[i:j]) == num:
				return nums[i:j]
			if sum(nums[i:j]) > num:
				break


def valid_number(preamble, number):
	"""
	check if any two numbers from the preamble sum to give the number
	"""
	for num1 in preamble:
		for num2 in preamble:
			if num1 + num2 == number:
				return True
	
	return False


if __name__ == "__main__":
	main()