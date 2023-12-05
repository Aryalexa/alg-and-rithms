import math
file = "input_d4"

def get_matches(line):
	_, nums = line.strip().split(": ")
	win, have = nums.split(" | ")
	win_set = {x for x in win.split()}
	matches = len([x for x in have.split() if x in win_set])
	# print(line, "- ", 
	# 	[x for x in have.split()], "->",
	# 	win_set,  matches, "\n")
	return matches

suma = 0
lines = []
with open(file, "r") as f:
	lines = f.readlines()
LNUM = len(lines)
cards = {i:1 for i in range(LNUM)}
for i in range(LNUM):
	c_i = cards[i]
	m_i = get_matches(lines[i])
	print(f"card {i}. #:{c_i}, matches:{m_i}")
	for j in range(m_i):
		#print(i, "->", i+1+j)
		cards[i+1+j] += c_i
	# print(line, "- ", 
	# 	[x for x in have.split()], "->",
	# 	win_set,  matches, "\n")
	suma += c_i
print(suma)