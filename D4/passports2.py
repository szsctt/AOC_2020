#!/usr/bin/env python

import re
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

	print(f"found {valid} valid passports")

def check_valid_passport(mandatory, optional, pas):

	# check for no duplicate fields
	if 'duplicate' in pas:
		return False
		
	# check for all mandatory fields
	if len(mandatory.difference(pas)) > 0:
		return False
	
	# check for correct number of fields
	if len(pas) != 7 and len(pas) != 8:
		return False
	
	# check birth year
	if not check_yr(pas['byr'], 1920, 2002):
		return False
		
	# check issue year
	if not check_yr(pas['iyr'], 2010, 2020):
		return False	
	
	# check expiration year
	if not check_yr(pas['eyr'], 2020, 2030):
		return False			
	
	# check height
	if not check_height(pas['hgt']):
		return False
	
	# check hair colour
	if not check_hcl(pas['hcl']):
		return False
		
	# check eye color
	if not check_ecl(pas['ecl']):
		return False	
		
	# check pid		
	print(f"pid: {pas['pid']}, ok: {check_pid(pas['pid'])}")
	if not check_pid(pas['pid']):
		return False		
			
	return True

def check_ecl(ecl):
	"""
	exactly one of: amb blu brn gry grn hzl oth
	"""
	if ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
		return False
		
	return True

def check_hcl(hcl):
	"""
	a # followed by exactly six characters 0-9 or a-f.
	"""
	# check length
	if len(hcl) != 7:
		return False
		
	# check hexadecimal
	if not re.search("^#[0-9a-f]+$", hcl):
		return False
		
	return True

def check_height(hgt):
	"""
	(Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
	"""
	# check for a number followed by either cm or in
	num = re.search("^(\d+)(in|cm)$", hgt)
	if not num:
		return False
	
	# get numeric value
	ht = int(num.groups()[0])
	# check for cm valid values
	if num.groups()[1] == 'cm':
		if ht < 150 or ht > 193:
			return False
	
	elif num.groups()[1] == 'in':
		if ht < 59 or ht > 76:
			return False		
	
	return True

def check_pid(pid):
	"""
	a nine-digit number, including leading zeroes
	"""
	# check for length
	if len(pid) != 9:
		return False
	# check for int
	try:
		int(pid)
	except ValueError:
		return False
		
	return True

def check_yr(yr, min, max):
	"""
	byr: four digits; at least 1920 and at most 2002.
	iyr: four digits; at least 2010 and at most 2020.
	eyr: four digits; at least 2020 and at most 2030.
	return True of OK, False if not
	"""
	# check length
	if len(yr) != 4:
		return False
	# check digits
	try:
		num = int(yr)
	except ValueError:
		return False
	# check minimum
	if num < min:
		return False
	# check maximum
	if num > max:
		return False
	return True



def parse_passport(lines):
	p = {}
	
	for line in lines:
		# get fields from line
		for field in line.split():
			# get info from field
			colon = field.find(":")
			if field[:colon] in p:
				p.add('duplicate')
			p[field[:colon]] = field[colon+1:]

	return p

if __name__ == "__main__":
	main()