from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i
print(digmap)


# line by line
ret = []
with open("in") as f:
    for line in f.read().splitlines():
    	...

# the entire file
with open("in") as f:
    lines = f.read().splitlines()
W = len(lines[0])
H = len(lines)