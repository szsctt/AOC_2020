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

def seat_id(id):
	col = column(id[0:7])
	row = row(id[7:])
	return row*8+col
	
def col(col_str):
	num = 0b1111111
	for i in range(6, 0, -1):
		if col_str[i] == 'F':
			num = num << 1
	print(f"{col_str}, {bin(num)}, {num}")
	return num
	
col('BFFFBBF')
col('FFFBBBF')
col('BBFFBBF')
