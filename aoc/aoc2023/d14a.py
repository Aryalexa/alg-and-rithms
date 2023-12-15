
def print_map(m):
	for l in m:
		print(l)
	print()

with open("in") as f:
	lines = f.read().splitlines()
      
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
		elif x == "#":
			load = R-i-1 # row i+1 load
print(ret)