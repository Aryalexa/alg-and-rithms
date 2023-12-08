import math

def read_line(line):
	# k: {L:x1, R:x2}
	k, v = line.split(" = ")
	l, r = v[1:-1].split(", ")
	return k, {'L':l, 'R':r}

def is_end(cur):
	return cur.endswith("Z")

def follow_dirs(cur):
	steps = 0
	while not is_end(cur):
		for d in DIRS:
			cur = inst[cur][d]
			steps += 1
			if is_end(cur):
				break
	return (steps)

def lcm(nums):
	lcm = 1
	for i in range(len(nums)):
		lcm = math.lcm(lcm, nums[i])
	return lcm

inst = {}
inis = []
with open("in") as f:
	lines = f.read().splitlines()
	DIRS = lines[0]
	for line in lines[2:]:
		k, dirs = read_line(line)
		inst[k] = dirs
		if k.endswith("A"):
			inis.append(k)

curs = inis
print(curs)
steps_li = []
for cur in curs:
	steps_li.append(follow_dirs(cur))
print(steps_li)
res = lcm(steps_li)
print(res)
		


