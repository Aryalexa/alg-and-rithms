#22:33 -44


prios = {}
j = 0
for i, x in enumerate("abcdefghijklmnopqrstuvwxyz", 1):
    prios[x] = i
    j = i + 1
for x in "abcdefghijklmnopqrstuvwxyz".upper():
    prios[x] = j
    j+=1
print(prios)


ret = 0
with open("in") as f:
    for line in f.read().splitlines():
        n = len(line)
        s1, s2 = set(line[:n//2]), set(line[n//2:])
        x = list(s1.intersection(s2))[0]
        ret += prios[x]
        
print(ret)
        
        