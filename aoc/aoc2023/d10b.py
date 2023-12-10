def in_map(point):
    xi,xj = point
    return 0<=xi<H and 0<=xj<W

def start_connections(start_p):
    si, sj = start_p
    conns = [] # [(point, origin)]
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
move_pipe = { # symbol: {origin: (step, new_origin)}
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

def start_symbol(dir_a, dir_b):
    def opp_symbol(s):
        return {"N":"S", "S":"N", "W":"E", "E":"W"}[s]
    dir_a = opp_symbol(dir_a)
    dir_b = opp_symbol(dir_b)
    sm = [s for s,dirs in move_pipe.items() 
          if dir_a in dirs and dir_b in dirs][0]
    #print("start symbol", sm)
    return sm


def suma(a, b):
	return a[0]+b[0],a[1]+b[1]
def next_pipe(point_dir):
    p,dir_o = point_dir
    #print(p, symbol(p), dir_o, '-> ', end='') 
    go, new_dir_o = move_pipe[symbol(p)][dir_o]
    new_p = suma(p, go)
    #print(new_dir_o, new_p, symbol(new_p))
    return new_p, new_dir_o


def mark_pipes():
    start = find_start()
    #print("start", start)
    (a,da), (b, db) = start_connections(start)
    #print(da, db)
    ss = start_symbol(da, db)

    pipes[start[0]][start[1]] = ss
    steps = 1
    while a!=start:
        pipes[a[0]][a[1]] = symbol(a)
        a, da = next_pipe((a, da))
        steps += 1
    #print(steps)
    # 14194
    return steps


''' IN=1, OUT=0
F---7 -> 00000
|...| -> 01111
L---J -> 01111
'''
def count_inside_vH():
    def am_i_in(p, iamIN):
        if p in '|LJ':
            return not iamIN
        return iamIN

    inside = 0
    for i in range(H):
        iamIN = False
        for j in range(W):
            p = pipes[i][j]
            iamIN = am_i_in(p, iamIN)
            if p == "0" and iamIN:
                pipes[i][j] = "*" # for visualization
                inside+=1

            print(pipes[i][j], end='')
        print(" ->", inside)
    print('inside vh', inside)
    return inside

# ----------------------------

with open("in") as f:
    mapa = f.read().splitlines()
W = len(mapa[0])
H = len(mapa)
pipes = [["0" for _ in range(W)] for _ in range(H)]

steps = mark_pipes()
# for h in range(H):
#     print(pipes[h])

count_inside_vH()




 

