#!/usr/bin/env python3

import re
from collections import Counter
import pdb

# read in data
pwds = []
with open('input', 'r') as handle:
	for line in handle:
		pwd = dict()
		pwd['line'] = line.strip()
		# split line into fields
		fields = line.strip().split()
		
		# get minium number for appearance of letter
		pwd['pos1'] = int(re.match("(\d+)-", fields[0]).groups()[0])
		
		# get maximum number for appearence of letter
		pwd['pos2'] = int(re.search("-(\d+)$", fields[0]).groups()[0])
		
		# get letter(s)
		pwd['key'] = fields[1].strip(":")
		
		# get password
		pwd['pwd'] = fields[2]
		
		pwds.append(pwd)
		
		
# check passwords
good_passwords = 0
for pwd in pwds:

	pos1, pos2 = False, False
	
	# check position 1
	ind1 = pwd['pos1']
	
	# if the password is long enough, check first position
	if len(pwd['pwd']) >= ind1:
		if pwd['pwd'][ind1 - 1] == pwd['key']:
			pos1 = True
		
		
	# check position 2
	ind2 = pwd['pos2']	
	
	# if the password is long enough, check second position
	if len(pwd['pwd']) >= ind2:
		if pwd['pwd'][ind2 - 1] == pwd['key']:
			pos2 = True

	if (pos1 ^ pos2):
		good_passwords += 1
		

print(f"good passwords: {good_passwords}")