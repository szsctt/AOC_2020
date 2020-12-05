#!/usr/bin/env python3

import re
from collections import Counter

# read in data
pwds = []
with open('input', 'r') as handle:
	for line in handle:
		pwd = dict()
		pwd['line'] = line.strip()
		# split line into fields
		fields = line.strip().split()
		
		# get minium number for appearance of letter
		pwd['min'] = int(re.match("(\d+)-", fields[0]).groups()[0])
		
		# get maximum number for appearence of letter
		pwd['max'] = int(re.search("-(\d+)$", fields[0]).groups()[0])
		
		# get letter(s)
		pwd['key'] = fields[1].strip(":")
		
		# get password
		pwd['pwd'] = fields[2]
		
		pwds.append(pwd)
		
		
# check passwords
bad_passwords = 0
for pwd in pwds:
	# simplest case - letter not in password
	if pwd['key'] not in pwd['pwd']:
		bad_passwords += 1
		continue
	
	# count letters in string
	count = 0
	for let in pwd['pwd']:
		if let == pwd['key']:
			count += 1
	
	# check count
	if count < pwd['min'] or count > pwd['max']:
		bad_passwords += 1


print(f"bad passwords: {bad_passwords}, good passwords: {len(pwds) - bad_passwords}")