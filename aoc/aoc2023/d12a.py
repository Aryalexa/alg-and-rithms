from copy import deepcopy

# backtracking - not good enough for second part

def read_springs(str):
    springs, damaged_groups_str = str.split(' ')
    damaged_groups = [int(x) for x in damaged_groups_str.split(',')]
    return springs, damaged_groups


def update_damages(springs, damages, i):
    while (i < len(springs) and springs[i] != '?'):
        x = springs[i]
        if x == '#':
            damages[-1] += 1
        if x == '.' and damages[-1] > 0:
            damages.append(0)        
        i+=1
    return i

def promising(cur_damages, damages):
    # cur_damages is start of damages?
    cd = [x for x in cur_damages if x >0]
    #print("promising", cur_damages, cd, damages)
    len_cd = len(cd)
    if len_cd == 0:
        return True
    if len_cd > len(damages):
        return False
    i = 0
    while i < len_cd - 1:
        if cd[i] != damages[i]:
            return False
        i+=1
    #print(i)
    if cd[i] > damages[i]:
        return False
    return True

def possible_arrangements(springs, damaged_groups):
    count = 0
    i = 0
    cur_damages = [0]
    if '?' in springs:
        count = possible_arrangements_BT(springs, damaged_groups,
                             cur_damages, i)
    return count
  
def possible_arrangements_BT(springs, damages, cur_damages, i):
    #print("round", i, springs, damages)
    
    i = update_damages(springs, cur_damages, i)
    #print(i, cur_damages)
    if not promising(cur_damages, damages):
        return 0

    if i == len(springs):
        cd = [x for x in cur_damages if x >0]
        #print("final", cd, damages, cd == damages)
        return int(cd == damages)
    count = 0
    for s in ".#":
        springs = list(springs)
        springs[i] = s
        springs = ''.join(springs)
        cur_damages_cpy = deepcopy(cur_damages)
        count += possible_arrangements_BT(springs, damages, cur_damages_cpy, i)
    return count
    

ret = 0
with open("in") as f:
    for line in f.read().splitlines():
        springs, damaged_groups = read_springs(line)
        possible_arrgs = possible_arrangements(springs, damaged_groups)
        print(springs, damaged_groups, possible_arrgs)
        ret += possible_arrgs
print(ret)
# 7653