

perim = 0
walls:set[tuple[int, int]] = {(0,0)}
last_p = (0,0)
with open("in") as f:
	for line in f.read().splitlines():
		_dir, num, color = line.split()
		num = int(num)
		perim += num  # +1
		new_p = last_p
		if _dir in "LR":
			sign = 1 if _dir == 'R' else -1
			for k in range(1,num+1):
				new_p = (last_p[0], last_p[1]+ sign*k)
				walls.add(new_p)
		else: #"UD"
			sign = 1 if _dir == 'D' else -1
			for k in range(1,num+1):
				new_p = (last_p[0]+ sign*k, last_p[1])
				walls.add(new_p)
		last_p = new_p

R0 = min(i for (i,_) in walls)
C0 = min(i for (i,_) in walls)
R = max(i for (i,_) in walls)
C = max(j for (_,j) in walls)

print(R-R0+1,"x",C-C0+1)
print('perim', perim)

for i in range(R0, R+1):
	print('*', i, " ", end='')
	for j in range(C0, C+1):
		if (i,j) in walls:
			print('#', end='')
		else:
			print('.', end='')
	print()

inside = 0
for ri in range(R0, R):
	walls_ri = sorted([j for (i,j) in walls if i == ri])
	print('*',ri, " ", end='')
	ins = False
	last_w = walls_ri[0] - 1
	holes = 0
	for wj in walls_ri:
		if ins:
			holes+= wj - last_w - 1
		down = (ri+1,wj)
		if down in walls:
			ins = not ins
		last_w = wj
	inside += holes
	print(" ", ri, '->', holes, inside)

print(inside, perim, inside+perim)