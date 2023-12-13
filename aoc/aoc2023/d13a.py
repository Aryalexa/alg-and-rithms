from typing import List

def print_map(m):
	for l in m:
		print(l)

def transpose(matrix: List[str]) -> List[str]:
	H = len(matrix)
	W = len(matrix[0])
	return ["".join([(matrix[i][j]) for i in range(H)]) for j in range(W)]
		
def hor_mirror(m, H):
	for r1,r2 in [(row, row+1) for row in range(H-1)]:
		k = min(r1-0+1, (H-1)-r2+1)
		if all(m[r1-x] == m[r2+x] for x in range(k)):
			#print("found ", r1+1, r2+1) ##
			return r1+1
	return -1

def ver_mirror(m, W):
	mT = transpose(m)
	return hor_mirror(mT, W)

def solve_mirrors(m):
	H = len(m)
	W = len(m[0])
	n1 = hor_mirror(m, H)
	if n1 > 0:
		above_of_horizontal = 100*n1
		return above_of_horizontal
	else:
		n1 = ver_mirror(m, W)
		left_of_vertical = n1
		return left_of_vertical

m = []
res = 0
with open("in") as f:
	for line in f.read().splitlines():
		if line == "":
			res += solve_mirrors(m)
			m = []
		else:
			m.append(line)
print(res)
# 35232