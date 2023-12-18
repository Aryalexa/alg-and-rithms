import heapq

def print_map(m):
	for l in m:
		if type(l) != str:
			l = ''.join(str(x) for x in l)
		print(l)
	print()

def ints(s):
	return [int(x) for x in s if x]

def isinside(pos:tuple) -> bool:
	i, j = pos
	return 0<=i<R and 0<=j<C

def hcost(i, ik, j, jk):
	if ik:
		sign = 1 if ik>0 else -1
		return sum(grid[i+sign*k][j] for k in range(1, abs(ik)+1))
	if jk:
		sign = 1 if jk>0 else -1
		return sum(grid[i][j+sign*k] for k in range(1, abs(jk)+1))
	assert "error cost"

def next_moves(pos, _dir):
	i,j = pos
	# CHANGES FOR PART 2 HERE
	UD = (
		[((i-k, j), '^', hcost(i, -k, j, 0)) for k in range(4,11) if isinside((i-k, j))] + 
		[((i+k, j), 'v', hcost(i, k, j, 0)) for k in range(4,11) if isinside((i+k, j))] )
	LR = (
		[((i, j-k), '<', hcost(i, 0, j, -k)) for k in range(4,11) if isinside((i, j-k))] +
		[((i, j+k), '>', hcost(i, 0, j, k)) for k in range(4,11) if isinside((i, j+k))] )
	
	poss = {
		'>': UD, '<': UD, 
		'^': LR, 'v': LR, 
	}
	opp = {'<':'>', '>':'<', '^':'v', 'v':'^', '-':'-'}[_dir]
	return [(p, d, cost) for p, d, cost in poss[_dir] 
			 if d!=opp and isinside(p)]

inf = 10**17
def dijkstra_distances(start_pos):
	distances = {(start_pos, '>'): 0, (start_pos, 'v'): 0}
	priority_queue:list[tuple[int, tuple]] = [(0, (start_pos, '>')), (0, (start_pos, 'v'))]
	while priority_queue:
		cur_dist, (cur_pos, cur_dir) = heapq.heappop(priority_queue)
		# print(cur_pos, cur_dir)
		if cur_dist > distances.get((cur_pos, cur_dir), inf):
			continue
		for neighbor, _dir, cost in next_moves(cur_pos, cur_dir):
			dist = cur_dist + cost
			if dist < distances.get((neighbor, _dir), inf):
				distances[(neighbor, _dir)] = dist
				heapq.heappush(priority_queue, (dist, (neighbor, _dir)))
	return distances


# --------------
grid = []
with open("in") as f:
	for line in f.read().splitlines():
		grid.append(ints(line))
R, C = len(grid), len(grid[0])
print_map(grid)

ini_pos = (0,0)

ds = dijkstra_distances(ini_pos)
print(min([v for (p,d), v in ds.items() if p == (R-1, C-1)]))



