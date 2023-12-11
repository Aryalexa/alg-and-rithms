skymap = []
empty_rows = []
empty_cols = []
galaxies = []

# galaxies and empty rows
i = 0
with open("in") as f:
	for line in f.read().splitlines():
		skymap.append(line)
		gal_r = [(i,j) for j,x in enumerate(line)
				if x=="#"]
		if len(gal_r) == 0:
			empty_rows.append(i)
		galaxies += gal_r
		i += 1

# empty cols
W = len(skymap[0])
H = len(skymap)
for j in range(W):
	gal_c = [i for i in range(H) 
		  if skymap[i][j]=="#"]
	if len(gal_c) == 0:
		empty_cols.append(j)

# distances
FACTOR = 2 # i knew...
dists = 0
for i, (x1,y1) in enumerate(galaxies, 1):
	for j, (x2,y2) in enumerate(galaxies[i:], i+1):
		dx = abs(x2-x1) + len([x for x in empty_rows if x1<x<x2 or x2<x<x1])*(FACTOR-1)
		dy = abs(y2-y1) + len([y for y in empty_cols if y1<y<y2 or y2<y<y1])*(FACTOR-1)
		dists += dx + dy
print(dists)

