
def range_in_range(r1, r2):
	"""range = (start, length)
	returns
		- range in 
		- range out lesser, and 
		- range out greater
	"""
	s1,l1 = r1
	s2,l2 = r2
	a,c = s1, s1+l1
	b,d = s2, s2+l2
	if a < b:
		if c <= b:
			return (-1,0), (a, c-a), (-1,0)
		elif c < d:
			return (b,c-b), (a, b-a), (-1,0)
		else:
			return (b,d-b), (a, b-a), (d,c-d)
	elif b <= a < d:
		if c < d:
			return (a, c-a), (-1, 0), (-1,0)
		else:
			return (a,d-a), (-1, 0), (d,c-d)
	else:
		return (-1,0), (-1, 0), (a, c-a)

def as_interv(rng):
	x, r = rng
	return x, x + r -1


def test():
	bd = (50,50)
	acs = [
		(25, 24), (25, 25), (25, 26),
		(25, 74), (25, 75), (25, 76),
		(75, 24), (75, 25), (75, 26),
		(100, 25), (105, 25)
	]
	for ac in acs:
		rs = range_in_range(ac, bd)
		print(ac, bd)
		print(as_interv(ac), 'in', as_interv(bd), "?")
		for r in rs:
			print(r, as_interv(r))
		print()


# -------
file = "input_d5"
lines = []
with open(file, "r") as f:
	lines = f.readlines()

nearest_loc = float("inf")
_, seeds = lines[0].split(": ")
seeds = [int(x) for x in seeds.split()]
last_values = [(x, seeds[i*2+1]) for i, x in enumerate(seeds[::2])]


i = 1
while i < len(lines):
	if not lines[i][0].isdigit():
		i+=1
		continue
	new_values = []
	v_map = [0 for _ in range(len(last_values))]
	print("<", last_values)
	while i < len(lines) and lines[i][0].isdigit():
		#print(lines[i].strip())
		s1, s2, l = [int(x) for x in lines[i].split()]
		for j, (x,r) in enumerate(last_values):
			# print(f"({x},{r}) in ({s2},{l})? {-s2+s1}")
			(in_s,in_l), (o1_s, o1_l), (o2_s, o2_l) = range_in_range((x,r), (s2,l))
			if not v_map[j] and in_l > 0:
				new_values.append((in_s-s2+s1, in_l))
				v_map[j] = 1
				# print(f"({in_s},{in_l})")
				# print(f"({in_s-s2+s1},{in_l})")
				if o1_l > 0:
					last_values.append((o1_s, o1_l))
					v_map.append(0)
					# print(f"({o1_s},{o1_l})")
					# print("*", last_values, v_map)
				if o2_l > 0:
					last_values.append((o2_s, o2_l))
					v_map.append(0)
					# print(f"({o2_s},{o2_l})")
					# print("*", last_values, v_map)

			# print(":",new_values)
		i+=1
	for j, (x,r) in enumerate(last_values):
		if not v_map[j]:
			new_values.append((x,r))
	#print("::",new_values)
	last_values = new_values
	print(">", last_values, "\n")
	i+=1

print(min(x for x,r in last_values))

	
	
