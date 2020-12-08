#!/usr/bin/env python

# advent of code 2020, day 5

#Here are some other boarding passes:
#    BFFFBBFRRR: row 70, column 7, seat ID 567.
#    FFFBBBFRRR: row 14, column 7, seat ID 119.
#    BBFFBBFRLL: row 102, column 4, seat ID 820.

# B == binary '1'
# F == binary '0'

# R == binary '1'
# L == binary '0'

#BFFFBBF
#1000110
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
# In this example, the seat has ID 44 * 8 + 5 = 357.

import pdb

def main():
	max_id = 0
	ids = []
	with open('input', 'r') as handle:
		# get ids for each seat in list
		for row in handle:
			sid = seat_id(row.strip())
			max_id = max(max_id, sid)
			ids.append(sid)
			
	print(f"the maximum seat id was {max_id}")
	
	# sort list and check for diff of 2
	ids = sorted(ids)
	i = ids[0]
	for j in sorted(ids[1:]):
		if i != j-1:
			print(f"gap at seat {i}, so seat is {i+1}")
		i = j

def seat_id(id):
	rownum = row(id[0:7])
	colnum = column(id[7:])
	return rownum*8+colnum
	
def row(row_str):
	"""
	convert row string to binary number where 'F' is 0 and 'B' is 1
	this gives row number
	"""
	num = 0
	for i in range(len(row_str)):
		if row_str[i] == 'B':
			num += 1 << (len(row_str) - i - 1)
	return num
	
def column(col_str):
	"""
	convert column string to binary number where 'L' is 0 and 'R' is 1
	this gives column number
	"""
	num = 0
	for i in range(len(col_str)):
		if col_str[i] == 'R':
			num += 1 << (len(col_str) - i - 1)
	return num

if __name__ == "__main__":
	main()