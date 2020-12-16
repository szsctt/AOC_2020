import pdb

def main():

	rules = {}
	ticket = []
	other_tickets = []
	
	seen_mine = False
	with open("input", 'r') as inhandle:
		for line in inhandle:
			if line.strip() == "nearby tickets:":
				continue
			if line.strip() == "":
				continue
			if line.strip() == "your ticket:":
				ticket = next(inhandle).strip().split(",")
				seen_mine = True
			# if it's another ticket
			elif seen_mine:
				other_tickets.append(line.strip().split(","))
			# if it's a rule
			else:
				field_name = line.strip().split(": ")[0]
				ruledef = line.strip().split(": ")[1]
				ruledef = ruledef.split(" or ")
				ruledef = [(int(i.split("-")[0]), int(i.split("-")[1]))for i in ruledef]
				rules[field_name] = ruledef
				
	print(rules)
	print(ticket)
	#print(other_tickets)
	
	# part 1
	all_range = get_valid_range_all(rules)
	invalid_fields = []
	for t in other_tickets:
		invalid_fields += check_valid(all_range, t)
	#print(invalid_fields)
	print(sum(invalid_fields))
	
	# part 2
	# discard invalid tickets
	remove = []
	for i in reversed(range(len(other_tickets))):
		if len(check_valid(all_range, other_tickets[i])) != 0:
			other_tickets.pop(i)
			
	# check each field against ranges
	assigned_fields = {name:[] for name in rules.keys()}
	for field in rules.keys():
		field_ranges = rules[field]
		
		for i in range(len(rules)):
			# get values from all tickets from first, second, thrid, etc fields in turn
			all_tickets = [t[i] for t in other_tickets]
			
			# check if these values are in the specified range for this field
			if len(check_valid(field_ranges, all_tickets)) == 0:
				assigned_fields[field].append(i)
				
	print(assigned_fields)

	# for some fields there are multiple options, for others there are only one
	# check for fields with only one option, and remove those from all other fields
	# repeat until there is only one option for all fields
	while any([len(val) > 1 for val in assigned_fields.values()]):
		for field in assigned_fields.keys():
			# if this field has a list with length 1
			if len(assigned_fields[field]) == 1:
				val = assigned_fields[field][0]
				# remove this field from all other lists
				for f in assigned_fields.keys():
					if f == field:
						continue
					if val in assigned_fields[f]:
						assigned_fields[f].remove(val)
		print(assigned_fields)
		print()
			
	# get departure fields
	dep_fields = {k:v for k, v in assigned_fields.items() if 'departure' in k}
	print(dep_fields)
	
	# multiply values together for ticket
	product = 1
	for f in assigned_fields.keys():
		if 'departure' not in f:
			continue
		fn = assigned_fields[f][0]
		product *= int(ticket[fn])
		
	print(product)
	
def get_valid_range_all(rules):
	# combine a nested list of ranges to get one flattened list of ranges
	ranges = [list(rules.values())[0][0]]
	for rule in rules.values():
		for rule_range in rule:
			overlapped = False
			for i in range(len(ranges)):
				if overlap(rule_range, ranges[i]):
					overlapped = True
					ranges[i] = (min(rule_range[0], ranges[i][0]), max(rule_range[1], ranges[i][1]))
					break
			if not overlapped:
				ranges.append(rule_range)
	return ranges
	

def check_valid(all_range, ticket):
	# return all invalid values in ticket (those that aren't in any of the ranges in all_range)
	invalid = []
	for field in ticket:
		f = int(field)
		if not any([overlap((f, f), r) for r in all_range]):
			invalid.append(f)
	return invalid


def overlap(r1, r2):
	assert r1[0] <= r1[1]
	assert r2[0] <= r2[1]
	# r1 completetly to the left of r2
	if r1[1] < r2[0]:
		return False
	# r1 completely to the right of r2 
	if r1[0] > r2[1]:
		return False
	return True

if __name__ == "__main__":
	main()