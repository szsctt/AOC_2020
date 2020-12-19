import pdb

def main():
	with open('input', 'r') as inhandle:
		starting_numbers = next(inhandle).strip().split(",")
		
	starting_numbers = [int(i) for i in starting_numbers]
	print(starting_numbers)


	#[print(get_ith_number(starting_numbers, i)) for i in range(10)]
	
	
	print(get_ith_number(starting_numbers, 2020))
	
	print(get_ith_number(starting_numbers, 30000000))	


def get_ith_number(starting_numbers, desired_number):

	
	# key = number, value = turn on which number was last spoken
	spoken = {}
	for i, num in enumerate(starting_numbers[:-1]):
		spoken[num] = i + 1
	
	last_spoken = starting_numbers[-1]
	
	turn = len(starting_numbers)
	while turn < desired_number + 1:
		
		# if last number not already said
		if last_spoken not in spoken.keys():
			spoken[last_spoken] = turn
			last_spoken = 0
		
		# if last number already said
		else:
			last_spoken_turn = spoken[last_spoken]
			spoken[last_spoken] = turn
			last_spoken = turn - last_spoken_turn
			
		turn += 1
		
	# find number spoken on turn - 1 in dict
	for num, num_turn in spoken.items():
		if num_turn == desired_number:
			return num
	

if __name__ == "__main__":
	main()