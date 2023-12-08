#21:42

elf = []
cal = 0
max_cal = 0
with open("in") as f:
    for line in f.readlines():
        if line == '\n':
            if cal > max_cal:
                max_cal = cal
            cal = 0
        else:
            cal += int(line.strip())

print(max_cal)
        
