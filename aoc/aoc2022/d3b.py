#22:33 -44 -58


prios = {}
j = 0
for i, x in enumerate("abcdefghijklmnopqrstuvwxyz", 1):
    prios[x] = i
    j = i + 1
for x in "abcdefghijklmnopqrstuvwxyz".upper():
    prios[x] = j
    j+=1
#print(prios)


ret = 0
grp = []
with open("in") as f:
    for line in f.read().splitlines():
        
        grp.append(set(line))
        #print('grp', len(grp))
        if len(grp) == 3:
            s1,s2,s3 = grp
            x = list(s1.intersection(s2).intersection(s3))[0]
            #print("*", x)
            ret += prios[x]
            grp = []
        
print(ret)
        
        