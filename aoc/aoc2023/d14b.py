

def print_map(m):
	for l in m:
		print(l)
	print()

def tilt_line_east(s:str):
	str_len = len(s)
	circles_num = s.count('O')
	return (str_len-circles_num)*'.' + circles_num*'O'

def tilt_line_west(s:str):
	str_len = len(s)
	circles_num = s.count('O')
	return circles_num*'O' + (str_len-circles_num)*'.'

def tilt_south(lines):
	cols = list(zip(*lines))
	cols = ["".join(c) for c in cols]

	new_cols = []
	for c in cols:
		parts = [tilt_line_east(p) for p in c.split('#')]
		new_c = "#".join(parts)
		new_cols.append(new_c)
	new_lines = list(zip(*new_cols))
	new_lines = ["".join(c) for c in new_lines]
	return new_lines

def tilt_north(lines):
	cols = list(zip(*lines))
	cols = ["".join(c) for c in cols]

	new_cols = []
	for c in cols:
		parts = [tilt_line_west(p) for p in c.split('#')]
		new_c = "#".join(parts)
		new_cols.append(new_c)
	new_lines = list(zip(*new_cols))
	new_lines = ["".join(c) for c in new_lines]
	return new_lines

def tilt_west(lines):
	new_lines = []
	for c in lines:
		parts = [tilt_line_west(p) for p in c.split('#')]
		new_c = "#".join(parts)
		new_lines.append(new_c)
	return new_lines

def tilt_east(lines):
	new_lines = []
	for c in lines:
		parts = [tilt_line_east(p) for p in c.split('#')]
		new_c = "#".join(parts)
		new_lines.append(new_c)
	return new_lines

def cycle(lines):
	lines = tilt_north(lines)
	lines = tilt_west(lines)
	lines = tilt_south(lines)
	lines = tilt_east(lines)
	return lines

# ---------------

with open("in") as f:
	lines = f.read().splitlines()
W = len(lines[0])
H = len(lines)
print_map(lines)


seen = {}
maps = {}
i = 0
period = 0
map_str = "\n".join(lines)
maps[0] = map_str
seen[map_str] = 0
CYLCLES = 1000000000
for i in range(1, CYLCLES+1, 1):
	lines = cycle(lines)
	map_str = "\n".join(lines)
	if map_str in seen:
		period = i - seen[map_str]
		break
	else:
		seen[map_str] = i
		maps[i] = map_str

map_X = maps[i-period+(CYLCLES - i)%period]

lines =  map_X.splitlines()
R, C = len(lines), len(lines[0])
print_map(lines)

ret = 0
for j in range(C):
	load = R
	for i in range(R):
		x = lines[i][j]
		if x == "O":
			ret += load
		load -= 1
print(ret)






"""
ri - 

"""