from tqdm import tqdm
from collections import defaultdict
import heapq

def read_line(line:str):
	_, _, color = line.split()
	color = color.strip('(#)')
	hexnum, d = color[:-1], color[-1]
	_dir = {'0':'R', '1':'D', '2':'L','3':'U' }[d]
	num = int(hexnum, 16)
	return  _dir, num, color

inf = 10**18
perim = 0
walls:defaultdict[int, list[int]] = defaultdict(list)
last_p = (0,0)
R0, R, C0, C = inf, -inf, inf, -inf
print('reading, getting walls...')
with open("in") as f:
	for line in tqdm(f.read().splitlines()):
		_dir, num, color = read_line(line)
		perim += num
		new_p = last_p
		if _dir in "LR":
			sign = 1 if _dir == 'R' else -1
			for k in range(1,num+1):
				new_p = (last_p[0], last_p[1]+ sign*k)
				R0, R, C0, C = min(R0, new_p[0]), max(R, new_p[0]), min(C0, new_p[1]), max(C, new_p[1])
				heapq.heappush(walls[new_p[0]], new_p[1])
		else: #"UD"
			sign = 1 if _dir == 'D' else -1
			for k in range(1,num+1):
				new_p = (last_p[0]+ sign*k, last_p[1])
				R0, R, C0, C = min(R0, new_p[0]), max(R, new_p[0]), min(C0, new_p[1]), max(C, new_p[1])
				heapq.heappush(walls[new_p[0]], new_p[1])
		last_p = new_p
print('done reading')

print(R-R0+1,"x",C-C0+1)
print('perim', perim)

# for i in range(R0, R+1):
# 	print('*', i, " ", end='')
# 	for j in range(C0, C+1):
# 		if (i,j) in walls:
# 			print('#', end='')
# 		else:
# 			print('.', end='')
# 	print()

print('counting inside...')
inside = 0
for ri in tqdm(range(R0, R)):
	walls_ri = walls[ri]
	ins = False
	last_w = walls_ri[0] - 1
	holes = 0
	while walls_ri:
		wj = heapq.heappop(walls_ri)
		if ins:
			holes+= wj - last_w - 1
		# look point below = (ri+1,wj)
		if wj in walls[ri+1]:
			ins = not ins
		last_w = wj
	inside += holes
print('done inside', inside)
print(inside, perim, "total:", inside+perim)