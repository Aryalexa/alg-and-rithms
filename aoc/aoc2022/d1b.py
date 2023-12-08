
#21:42 - 21:57 -> 15 min

elf = []
cal = 0
with open("in") as f:
    for line in f.readlines():
        if line == '\n':
            elf.append(cal)
            cal = 0
        else:
            cal += int(line.strip())
    elf.append(cal)

print(elf)
print(sum(sorted(elf)[-3:]))
        
