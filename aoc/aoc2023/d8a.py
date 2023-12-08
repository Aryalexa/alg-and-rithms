
def read_line(line):
	# k: {L:x1, R:x2}
	k, v = line.split(" = ")
	l, r = v[1:-1].split(", ")
	return k, {'L':l, 'R':r}

inst = {}
with open("in") as f:
	lines = f.read().splitlines()
	DIRS = lines[0]
	for line in lines[2:]:
		k, dirs = read_line(line)
		inst[k] = dirs

cur = "AAA"
end = "ZZZ"
res = 0
while cur!=end:
	for d in DIRS:
		cur = inst[cur][d]
		res += 1
		if cur == end:
			break
print(res)
		


