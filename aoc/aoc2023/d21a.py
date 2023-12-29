from functools import cache
DIR = [
	[0,-1], [0,1],
	[-1,0], [1, 0]
]

@cache
def pos_after_1step(cur_pos) -> list:
	cx,cy = cur_pos
	pos_li = [(cx+dx, cy+dy) for dx,dy in DIR
		   if 0<=cx+dx<R and 0<=cy+dy<C and lines[cx+dx][cy+dy]!='#']
	return pos_li

@cache
def get_end_positions(steps):
	if steps == 0:
		return set([start])
	else:
		end_pos = set()
		prev = get_end_positions(steps-1)
		for p in prev:
			new_ps = pos_after_1step(p)
			end_pos = end_pos.union(new_ps)
		return end_pos

# ----
STEPS = 64
lines = []
start = 0,0
with open("in") as f:
	for i, line in enumerate(f.read().splitlines()):
		lines.append(line)
		if 'S' in line:
			start = i,line.index('S')
R, C = len(lines), len(lines[0])
print(R, 'x', C, '. start', start)
ps = get_end_positions(STEPS)
print('STEPS', STEPS, 'res', len(ps))
