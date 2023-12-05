import math
file = "input_d4"


suma = 0
with open(file, "r") as f:
	for line in f.readlines():
		card, nums = line.strip().split(": ")
		win, have = nums.split(" | ")
		win_set = {x for x in win.split()}
		matches = len([x for x in have.split() if x in win_set])
		# print(line, "- ", 
		# 	[x for x in have.split()], "->",
		# 	win_set,  matches, "\n")
		suma += pow(2, matches-1) if matches > 0 else 0
print(suma)