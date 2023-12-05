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

def issymbol(c:str):
	return (not c.isdigit() and c != '.')

def check_line(_nline:int, pos_ini:int, pos_fin:int) -> bool:
	
	for pos in range(pos_ini-1, pos_fin+2, 1):
		#print(f"\tcheck ({_nline}, {pos}) in ({0}, {line_len})")
		if pos >= 0 and pos < L_LEN:
			#print("\t\tvalid")
			if issymbol(lines[_nline][pos]):
				#print("\t\t%")

				return True
	return False

def check_number(_nline:int, pos_ini:int, pos_fin:int) -> bool:
	return ( # look up, look sides, look down
		(_nline > 0 and 
	 		check_line(_nline - 1, i, npos)) or
		check_line(_nline, i, npos) or
		(_nline < L_NUM - 1 and 
	 		check_line(_nline + 1, i, npos))
		)


file = "input_d3"
with open(file, "r") as f:
	txt = f.read()

lines = txt.split("\n")
L_LEN = len(lines[0])
L_NUM = len(lines)
suma = 0

for nline, line in enumerate(lines):
	#print(nline, line)
	i = 0
	while i < len(line):
		n, l = atoi(line[i:])
		if n>0: # theres number
			npos = i + l - 1
			#print(line, "->", n, f"({i}, {npos})")
			if check_number(nline, i, npos):
				#print("*")
				suma += n
			i += l
		else:
			i+=1
print(suma)
