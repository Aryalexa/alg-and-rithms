from tqdm import tqdm

'''
Pick's theorem
A = i + b/2 - 1
i = integers inside -> inside area
b = integers in perimeter

Inside area..
polygon area formula: Shoelace Formula
(to review)
'''

def read_line2(line:str):
	_, _, color = line.split()
	color = color.strip('(#)')
	hexnum, d = color[:-1], color[-1]
	_dir = {'0':'R', '1':'D', '2':'L','3':'U' }[d]
	num = int(hexnum, 16)
	return  _dir, num, color

def read_line(line:str):
	_dir, num, color = line.split()
	return  _dir, int(num), color

inf = 10**18
perim = 0
last_p = (0,0)
points:list = [last_p]
print('reading points...')
with open("in") as f:
	for line in tqdm(f.read().splitlines()):
		_dir, num, color = read_line2(line)
		perim += num
		new_p = last_p
		if _dir in "LR":
			sign = 1 if _dir == 'R' else -1
			new_p = (last_p[0], last_p[1]+ sign*num)
			points.append(new_p)
		else: #"UD"
			sign = 1 if _dir == 'D' else -1
			new_p = (last_p[0]+ sign*num, last_p[1])
			points.append(new_p)
		last_p = new_p

print('done reading')
print('perim', perim)

# for i in range(R0, R+1):
# 	print('*', i, " ", end='')
# 	for j in range(C0, C+1):
# 		if (i,j) in walls:
# 			print('#', end='')
# 		else:
# 			print('.', end='')
# 	print()

def det(p1, p2):
	x1,y1 = p1
	x2,y2 = p2
	# return (y1+y2)*(x2-x1) - max(abs(y1-y2), abs(x1-x2))
	return (y1+y2)*(x2-x1)

print('counting inside...')
inside = 0
for i, p in tqdm(enumerate(points[:-1])):
	p2 = points[i+1]
	inside += det(p, p2)
inside = inside//2

print('done inside', inside)
print(inside, perim, "total:", abs(inside)+perim//2 + 1)