from typing import Tuple


def atoi(s:str) -> Tuple[int, int]:
	n:int = 0
	length:int = 0
	for c in s:
		if c.isdigit():
			n = n*10 + int(c)
			length += 1
		else:
			return n, length
	return n, length


def explore_line(num, _nline:int, pos_ini:int, pos_fin:int):
	
	for pos in range(pos_ini-1, pos_fin+2, 1):
		#print(f"\tcheck ({_nline}, {pos}) in ({0}, {line_len})")
		if pos >= 0 and pos < L_LEN:
			#print("\t\tvalid")
			if lines[_nline][pos] == '*':
				#print("\t\t%")
				gears[(_nline, pos)] = sum([gears.get((_nline, pos), []), [n]],[])
				

def check_number(num, _nline:int, pos_ini:int, pos_fin:int):
	# look up, look sides, look down
	if _nline > 0:
		explore_line(num, _nline - 1, i, npos)
	explore_line(num, _nline, i, npos)
	if _nline < L_NUM - 1:
		explore_line(num, _nline + 1, i, npos)


file = "input_d3"
with open(file, "r") as f:
	txt = f.read()

lines = txt.split("\n")
L_LEN = len(lines[0])
L_NUM = len(lines)
suma = 0
gears = dict()

for nline, line in enumerate(lines):
	#print(nline, line)
	i = 0
	while i < len(line):
		n, l = atoi(line[i:])
		if n>0: # theres number
			npos = i + l - 1
			#print(line, "->", n, f"({i}, {npos})")
			check_number(n, nline, i, npos)
			i += l
		else:
			i+=1
for g, nums in gears.items():
	if len(nums) == 2:
		suma += nums[0] * nums[1]
print(suma)
