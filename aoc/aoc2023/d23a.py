
with open("in") as f:
	lines = f.read().splitlines()
R, C = len(lines), len(lines[0])

print(R, 'x', C)

START = 0,lines[0].index('.')
END = R-1, lines[-1].index('.')
print('START', START, '. END', END)

DIR = {'^': [-1,0], 'v':[1,0],
	   '>':[0,1], '<':[0,-1]}

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
### CHECK recursive using SEEN

def longest_IT():
	longest = 0
	stack:list[tuple[tuple, int, list]] = [(START, 0, [])]
	while stack:
		cp, clen, cpath = stack.pop()
		if cp == END:
			print('end', clen)
			if clen > longest:
				longest = clen
		else:
			cx, cy = cp
			moves = [DIR[lines[cx][cy]]] if lines[cx][cy] in DIR else (DIR.values())
			for move in moves:
				dx, dy = move
				nx, ny = (cx+dx, cy+dy)
				if lines[nx][ny] != '#' and (nx,ny) not in cpath:
					stack.append(((nx,ny), clen +1, cpath+[(nx,ny)]))
	print(longest)

longest_IT()				



