import pdb

def main():
	lines = []
	with open("input", "r") as inhandle:
		for line in inhandle:
			lines.append(line.strip())
			
	# part 1
	results = [evaluate_line(l) for l in lines]
	print(sum([int(i) for i in results]))
	
	# part 2
	results = [evaluate_line_part_2(l) for l in lines]
	print(sum([int(i) for i in results]))
	
def evaluate_line_part_2(line):

	terms = line.split()

	# first, evaluate anything inside brackets
	i = 0
	while i < len(terms):
		if "(" in terms[i]:
			inner_terms = get_inner_terms(terms, i)
			terms.insert(i, evaluate_line_part_2(" ".join(inner_terms)))
		i += 1
	
	# next_evaluate '+'
	i = 0
	while i < len(terms):
		if terms[i] == '+':
			a, b = terms[i-1], terms[i+1]
			del terms[i-1:i+2]
			terms.insert(i-1, str(int(a) + int(b)))
			i -= 1
		i += 1
	
	# last, evaluate '*'
	i = 0
	while i < len(terms):
		if terms[i] == '*':
			a, b = terms[i-1], terms[i+1]
			del terms[i-1:i+2]
			terms.insert(i-1, str(int(a) * int(b)))
			i -= 1
		i += 1	
		
	return(terms[0])
	
def evaluate_line(line):
	terms = line.split()
	while True:
		try:
			if "(" in terms[0]:
				inner_terms = get_inner_terms(terms, 0)
				terms.insert(0, evaluate_line(" ".join(inner_terms)))
				continue
			if "(" in terms[2]:
				inner_terms = get_inner_terms(terms, 2)
				terms.insert(2, evaluate_line(" ".join(inner_terms)))
				continue
			a, op, b = terms.pop(0), terms.pop(0), terms.pop(0)			
			if op == '+':
				terms.insert(0, str(int(a) + int(b)))
			elif op == '*':
				terms.insert(0, str(int(a) * int(b)))				
		except IndexError:
			break		
	return terms[0]

def get_inner_terms(terms, j):
	n_open = terms[j].count("(")
	n_closed = terms[j].count(")")
	inner_terms = [terms.pop(j)]
	while n_open != n_closed:
		n_open += terms[j].count("(")
		n_closed += terms[j].count(")")
		inner_terms.append(terms.pop(j))
	inner_terms[0] = inner_terms[0][1:]
	inner_terms[-1] = inner_terms[-1][:-1]
	
	return inner_terms		
		

if __name__ == "__main__":
	main()