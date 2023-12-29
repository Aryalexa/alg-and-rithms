import heapq
from collections import defaultdict
from functools import total_ordering


def ints(s, split=' ') -> list:
	return [int(x) for x in s.split(split) if x]

@total_ordering
class P:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y
	def __str__(self) -> str:
		return f"P({self.x},{self.y})"
	def __repr__(self) -> str:
		return self.__str__()
	def vals(self):
		return [self.x, self.y]
	def sum_axis(self, val, axis):
		dx, dy, dz = {'x':[1,0,0], 'y':[0,1,0], 'z':[0,0,1]}[axis]
		np = P(self.x + val*dx, self.y+val*dy) # , self.z+val*dz)
		return np
	def __eq__(self, other) -> bool:
		return self.x == other.x and self.y == other.y
	def __lt__(self, other) -> bool:
		return self.vals() < other.vals()
	def __hash__(self) -> int:
		return self.x*10000 + self.y


@total_ordering
class Brick:
	def __init__(self, name, e1:P,h1, e2:P,h2) -> None:
		self.name = name
		if [*e1.vals(), h1] <= [*e2.vals(), h2]:
			self.base1:P = e1
			self.h1 = h1
			self.base2:P = e2
			self.h2 = h2
		else:
			self.base1:P = e2
			self.h1 = h2
			self.base2:P = e1
			self.h2 = h1

	def __str__(self) -> str:
		return f"{self.name}[{self.base1}{self.h1},{self.base2}{self.h2}]"
	def __repr__(self) -> str:
		return self.__str__()
	def on_the_ground(self)->bool:
		return self.h1 == 1 or self.h2 == 1
	@property
	def min_z(self):
		return self.h1 #min(self.h1, self.h2)
	@property
	def max_z(self):
		return self.h2 #max(self.h1, self.h2)
	def size(self):
		dist = max(abs(t-o) for t,o in zip(
			[*self.base1.vals(), self.h1],
			[*self.base2.vals(), self.h2]))
		return dist + 1
	def orientation(self):
		if self.size() == 1:
			return 'x'
		x1,y1 = self.base1.vals()
		x2,y2 = self.base2.vals()
		if x1 != x2:
			return 'x'
		elif y1 != y2:
			return 'y'
		else:
			return 'z'

	def base(self):
		if self.base1.vals() == self.base2.vals():
			return [self.base1]
		li = [self.base1]
		o = self.orientation()
		for i in range(1, self.size()):
			li.append(self.base1.sum_axis(i, o))
		assert li[-1].vals() == self.base2.vals(), f'bad body sum {li}'
		return li
	def height(self):
		return self.max_z - self.min_z +1

	def fall(self, how_much):
		if how_much < 1:
			return 
		# print('before',how_much,  self)
		self.base1 = self.base1.sum_axis(-how_much, 'z')
		self.base2 = self.base2.sum_axis(-how_much, 'z')
		# print('after',how_much,  self)
	
	def __gt__(self, other):
		return self.min_z > other.min_z



def load_bricks():
	global R
	global C
	with open("in") as f:
		for i, line in enumerate(f.read().splitlines()):
			e1_s, e2_s = line.split('~')
			x1,y1,z1 = ints(e1_s, ',')
			x2,y2,z2 = ints(e2_s, ',')
			b = Brick(f'B{i}', P(x1,y1), z1, P(x2,y2), z2)
			heapq.heappush(falling, (b.min_z, b))
			R, C = max([R, x1, x2]), max([C, y1, y2])
	R=R+1
	C=C+1

class FloorCell():
	def __init__(self, height, brick_name) -> None:
		self.height = height
		self.brick = brick_name
	def __str__(self) -> str:
		return f'[h={self.height},{self.brick}]'
	def __repr__(self) -> str:
		return self.__str__()

class Node:
	def __init__(self, name:str, brick:Brick) -> None:
		self.name = name
		self.brick = brick
		self.above = []
		self.below = []
	def add_above(self, b_name):
		self.above.append(b_name)
	def add_below(self, b_name):
		self.below.append(b_name)
	def has_2ormore_below(self):
		return len(self.below) >= 2
	def has_above(self):
		return len(self.above) > 0
	def allabove_morethan1below(self):
		print('\n\t', 'above:', )
		for b in self.above:
			print('\t', brick_nodes[b])
			if len(brick_nodes[b].below) == 1:
				return False
		return True
	def __str__(self) -> str:
		return f'N({self.name}. below:{self.below}, above:{self.above})'

def process_falling():
	def update_floor_heights(cur_b:Brick, fh):
		for p in cur_b.base():
			floor[p].height = fh + cur_b.height()
			floor[p].brick = cur_b.name

	aboves = defaultdict(list)
	brick_nodes['F'] = Node('F', Brick('F', P(0,0), 0, P(0,0), 0))
	while falling:
		_, cb = heapq.heappop(falling) # lowest brick
		print('* <', cb)
		n = Node(cb.name, cb)
		fh = max(floor[p].height for p in cb.base())
		below = [floor[p].brick for p in cb.base() if floor[p].height == fh]
		n.below = list(set(below))
		for b in below:
			aboves[b].append(cb.name)
		brick_nodes[cb.name] = n
		print('  >', n)
		update_floor_heights(cb, fh)
		print('  > floor', end=' ')
		for k in sorted(floor.keys()):
			print(f'{k}:{floor[k]}', end='; ')
		print()
	for b, ch in aboves.items():
		n = brick_nodes[b]
		n.above = list(set(ch))
		brick_nodes[b] = n
		


visited = []
def desintegrate_1(brick_name):
	if brick_name not in visited:
		n = brick_nodes[brick_name]
		print('NODE *',n, len(res), end='')
		if not n.has_above():
			res.append(n.name)
		elif n.allabove_morethan1below():
			# if all above has more than 1 below, add me
			res.append(n.name)
		print('->',len(res))
		for ch in n.above:
			desintegrate_1(ch)
	visited.append(brick_name)
	


# ---
R = 0
C = 0
floor = defaultdict(lambda:FloorCell(0,'F'))
brick_nodes:dict[str, Node] = {}
falling:list[tuple[int, Brick]] = []
load_bricks()
print(R, 'x', C)
print('**falling', falling)
process_falling()
res = list()
desintegrate_1('F')
res_set = {x for x in res} 
count = len(res_set)
# print('res')
# for b in res_set:
# 	print(brick_nodes[b].brick)
print('res',count)

