#!/usr/bin/env python3

exp = []
with open("D1_P1_input.txt", 'r') as handle:
	for line in handle:
		exp.append(int(line.strip()))
		
print(len(exp))
print(exp[0:5])

for i in range(len(exp)):
	for j in range(len(exp)):
		for k in range(len(exp)):
			if exp[i] + exp[j] + exp[k]  == 2020:
				print(f"num1: {exp[i]}, num2: {exp[j]}, num3: {exp[k]}, product: {exp[i]*exp[j]*exp[k]}")
				break