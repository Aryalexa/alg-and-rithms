
file = "input_d5"

lines = []
with open(file, "r") as f:
	lines = f.readlines()

nearest_loc = float("inf")
_, seeds = lines[0].split(": ")
last_values = [int(x) for x in seeds.split()]
N = len(last_values)
i = 1
while i < len(lines):
	if not lines[i][0].isdigit():
		#print("pass", lines[i])
		i+=1
		continue
	v_map = [0 for _ in range(N)]
	#print("<", last_values)
	while i < len(lines) and lines[i][0].isdigit():
		#print(lines[i].strip())
		s1, s2, l = [int(x) for x in lines[i].split()]
		for j, v in enumerate(last_values):
			if s2 <= v < s2+l and not v_map[j]:
				last_values[j] = s1 + v - s2
				v_map[j] = 1
		i+=1
	print(">", last_values)
	i+=1

print(min(last_values))

	
	

