def in_map(point):
    xi,xj = point
    return 0<=xi<H and 0<=xj<W

def start_connections(si, sj):
    conns = []
    N = (si-1, sj)
    if in_map(N) and mapa[N[0]][N[1]] in "|7F":
        conns.append((N,'S'))
    S = (si+1, sj)
    if in_map(S) and mapa[S[0]][S[1]] in "|JL":
        conns.append((S,'N'))
    W = (si, sj-1)
    if in_map(W) and mapa[W[0]][W[1]] in "-LF":
        conns.append((W, 'E'))
    E = (si, sj+1)
    if in_map(E) and mapa[E[0]][E[1]] in "-J7":
        conns.append((E, 'W'))
    assert len(conns) == 2, "S with 2 conns? no"
    return conns

def find_start():
    for i in range(H):
        for j in range(W):
            if mapa[i][j] == 'S':
                return i, j
    raise Exception("no start found")


goN = (-1, 0)
goS = (1, 0)
goW = (0, -1)
goE = (0, 1)
move_pipe = {
    '|' : {'S':(goN, 'S'), 'N':(goS, 'N')},
    '-' : {'W':(goE, 'W'), 'E':(goW, 'E')},
    '7' : {'S':(goW, 'E'), 'W':(goS,'N')},
    'F' : {'S':(goE, 'W'), 'E':(goS,'N')},
    'L' : {'N':(goE, 'W'), 'E':(goN,'S')},
    'J' : {'N':(goW, 'E'), 'W':(goN,'S')},
}
def symbol(point):
    xi,xj = point
    return mapa[xi][xj]

def suma(a, b):
	return a[0]+b[0],a[1]+b[1]
def next_pipe(point_dir):
    p,dir_o = point_dir
    print(p, symbol(p), dir_o, '-> ', end='') 
    go, new_dir_o = move_pipe[symbol(p)][dir_o]
    new_p = suma(p, go)
    print(new_dir_o, new_p, symbol(new_p))
    return new_p, new_dir_o
        

    
with open("in") as f:
    mapa = f.read().splitlines()
W = len(mapa[0])
H = len(mapa)

si, sj = find_start()
print("start", si,sj)
(a,da), (b, db) = start_connections(si, sj)
print(a, b)
steps = 1
while a!=b:
    a, da = next_pipe((a, da))
    b, db = next_pipe((b, db))
    steps += 1
print(steps)
#7097    

