#!/usr/bin/env python

import pdb

def main():
	mandatory = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
	optional = {'cid'}

	lines = []
	valid = 0
	with open("input", 'r') as handle:

		for line in handle:
			# new passport is coming up
			if line.strip() == '':
				p = parse_passport(lines)
				if check_valid_passport(mandatory, optional, p):
					valid += 1
					
				lines = []
				continue
		
			# store lines
			lines.append(line.strip())

	print(p)
	print(f"found {valid} valid passports")

def check_valid_passport(mandatory, optional, pas):

	if 'duplicate' in pas:
		return False
		
	# check for all mandatory fields
	if len(mandatory.difference(pas)) > 0:
		return False
	
	if len(pas) != 7 and len(pas) != 8:
		return False
	
	return True

def parse_passport(lines):
	p = set()
	
	for line in lines:
		# get fields from line
		for field in line.split():
			# get info from field
			colon = field.find(":")
			if field[:colon] in p:
				p.add('duplicate')
			p.add(field[:colon])

	return p

if __name__ == "__main__":
	main()