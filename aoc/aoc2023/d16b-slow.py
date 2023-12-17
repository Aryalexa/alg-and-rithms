from collections import defaultdict

def print_map(m):
	for l in m:
		if type(l) != str:
			l = ''.join(str(x) for x in l)
		print(l)

def move_one(pos:tuple, _dir:str) -> tuple:
	i,j = pos
	if _dir == 'left':
		return (i, j-1)
	if _dir == 'right':
		return (i, j+1)
	if _dir == 'up':
		return (i-1, j)
	if _dir == 'down':
		return (i+1, j)
	assert False, "wrong"
	
def isinside(pos:tuple) -> bool:
	i, j = pos
	return 0<=i<R and 0<=j<C



def start_beam(pos_ini, _dir_ini):

	def mark_and_continue(new_pos:tuple, new_dir:str):
		if not isinside(new_pos):
			return False
		i,j = new_pos
		energy_map[i][j] = 1
		if new_pos in dirs_dict[new_dir]:
			return False
		dirs_dict[new_dir].append(new_pos)
		return True	
		

	def go_beam_aux(new_pos, new_dir):
		if mark_and_continue(new_pos, new_dir):
			go_beam(new_pos, new_dir)

	def go_beam(pos:tuple, _dir:str):
		i,j = pos
		x = lines[i][j]
		while (x == '.' or 
			(x == '|' and _dir in ('up', 'down')) or
			(x == '-' and _dir in ('left', 'right'))):
			pos = move_one(pos, _dir)
			if not mark_and_continue(pos, _dir):
				break
			i,j = pos
			x = lines[i][j]
			
		if x == '\\':
			new_dirs = {
				'right':'down', 'up':'left', 
				'down':'right', 'left':'up'}
			new_pos = move_one(pos, new_dirs[_dir])
			go_beam_aux(new_pos, new_dirs[_dir])
		elif x == '/':
			new_dirs = {
				'right':'up', 'down':'left', 
				'up':'right', 'left':'down'}
			new_pos = move_one(pos, new_dirs[_dir])
			go_beam_aux(new_pos, new_dirs[_dir])
		elif x == '|' and _dir in ('left', 'right'): 
			# two: up, down
			new_pos = move_one(pos, 'up')
			go_beam_aux(new_pos, 'up')
			new_pos = move_one(pos, 'down')
			go_beam_aux(new_pos, 'down')
		elif x == '-' and _dir in ('up', 'down'):
			# two: left, right
			new_pos = move_one(pos, 'left')
			go_beam_aux(new_pos, 'left')
			new_pos = move_one(pos, 'right')
			go_beam_aux(new_pos, 'right')	

	energy_map = [[0 for _ in range(C)] for _ in range(R)]
	dirs_dict = defaultdict(list) # dir: [pos, pos]
	energy_map[pos_ini[0]][pos_ini[1]] = 1
	dirs_dict[_dir_ini].append(pos_ini)
	go_beam(pos_ini, _dir_ini)
	#print()
	#print_map(energy_map)

	return (sum(sum(r) for r in energy_map))

# -------
with open("in") as f:
	lines = f.read().splitlines()
R, C = len(lines), len(lines[0])
#print_map(lines)

max_energy = 0

i = 0 # first row
for j in range(C):
	energy = start_beam((i,j), 'down')
	print("start:", (i,j), energy)
	max_energy = max(max_energy, energy)
i = R-1 # last row
for j in range(C):
	energy = start_beam((i,j), 'up')
	print("start:", (i,j), energy)
	max_energy = max(max_energy, energy)
j = 0
for i in range(R):
	energy = start_beam((i,j), 'right')
	print("start:", (i,j), energy)
	max_energy = max(max_energy, energy)
j = C-1
for i in range(R):
	energy = start_beam((i,j), 'left')
	print("start:", (i,j), energy)
	max_energy = max(max_energy, energy)
print(max_energy)
# :44 - :46
# 8358