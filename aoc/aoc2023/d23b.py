
from collections import defaultdict


with open("in") as f:
	lines = f.read().splitlines()
R, C = len(lines), len(lines[0])
print(R, 'x', C)
lines = [[c for c in r] for r in lines]


START = 0,lines[0].index('.')
END = R-1, lines[-1].index('.')
print('START', START, '. END', END)

DIR = {'^': [-1,0], 'v':[1,0],
	   '>': [0,1], '<':[0,-1]}

dist = defaultdict(dict)
points = set([START, END])

# process intersections: save starting points
for i in range(R):
	for j in range(C):
		arrows_cnt = 0
		for move in DIR.values():
			dx, dy = move
			if 0<=i+dx<R and 0<=j+dy<C and lines[i+dx][j+dy] in '^v<>':
				arrows_cnt+=1
		if arrows_cnt >= 3:
			lines[i][j] = 'I' # intersection
			for move in DIR.values():
				dx, dy = move
				if 0<=i+dx<R and 0<=j+dy<C and lines[i+dx][j+dy] in '^v<>':
					points.add((i+dx,j+dy))
					dist[i,j][i+dx,j+dy] = 1
					dist[i+dx,j+dy][i,j] = 1

print('1-',dist)

# dist matrix for all points - only connected are calculated
def calc_dist_dfs(x,y,sx,sy,fx,fy, r):
	if x==fx and y==fy:
		dist[sx,sy][fx,fy] = r
	else:
		for dx,dy in DIR.values():
			nx,ny = x+dx, y+dy
			if 0<=nx<R and 0<=ny<C and lines[nx][ny] not in "#I" and (nx,ny) not in seen:
				seen.add((nx,ny))
				calc_dist_dfs(nx,ny,sx,sy,fx,fy,r+1)
				seen.discard((nx,ny))

for sx,sy in points:
	seen = set([(sx,sy)])
	for fx,fy in points:
		if sx!=fx or sy!=fy:
			calc_dist_dfs(sx,sy,sx,sy,fx,fy,0)
print('2-',dist)

# longest path len using only what we saved in dist (S, E, intersections and points)
def longest_path_till_end(x, y, cur_len):
	global longest
	if (x,y) == END:
		if cur_len > longest:
			longest = cur_len
			print('longer', longest)
	else:
		for nx,ny in dist[x,y]:
			if 0<=nx<R and 0<=ny<C and lines[nx][ny] != "#" and (nx,ny) not in seen:
				seen.add((nx,ny))
				longest_path_till_end(nx,ny,cur_len+dist[x,y][nx,ny])
				seen.discard((nx,ny))

longest = 0
seen = set([START])
longest_path_till_end(*START, 0)
print(longest)


"""
# WHY SEEN?

If (nx, ny) is already in the seen set, it means that the DFS has already
explored the path from the starting position to (nx, ny). 
# Optimizing Depth-First Search
Depth-first search can potentially explore the same position multiple 
times through different paths. The seen set helps to optimize the DFS 
traversal by ensuring that each position is visited at most once from 
a given starting point
# Avoiding Infinite Loops
"""






# def longest_BT(cp, cpath, clen):
# 	if cp == END:
# 		print('end', clen)
# 		if clen > longest:
# 			longest = clen
# 	else:
# 		cx, cy = cp
# 		moves = [DIR[lines[cx][cy]]] if lines[cx][cy] in DIR else (DIR.values())
# 		for move in moves:
# 			dx, dy = move
# 			nx, ny = (cx+dx, cy+dy)
# 			if lines[nx][ny] != '#' and (nx,ny) not in cpath:
# 				longest_BT((nx,ny), cpath+[(nx,ny)], clen+1)

def longest_IT():
	longest = 0
	stack:list[tuple[tuple, int, list]] = [(START, 0, [])]
	max_until_now = {} # bad idea
	while stack:
		cp, clen, cpath = stack.pop()
		if cp == END:
			print('end', clen)
			if clen > longest:
				longest = clen
		else:
			if cp in max_until_now and max_until_now[cp] > clen:
				continue
			max_until_now[cp] = clen
			cx, cy = cp
			moves = list(DIR.values())
			for move in moves:
				dx, dy = move
				nx, ny = (cx+dx, cy+dy)
				if lines[nx][ny] != '#' and (nx,ny) not in cpath:
					stack.append(((nx,ny), clen +1, cpath+[(nx,ny)]))
	print(longest)

#longest_IT()				



