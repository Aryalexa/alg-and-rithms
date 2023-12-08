from functools import cmp_to_key
from collections import Counter

POWER_C = "J23456789TQKA"
POWER_H = [
	'High card',
	'One pair',
	'Two pair',
	'Three of a kind',
	'Full house',
	'Four of a kind',
	'Five of a kind',
]
joker = 'J'

def best_J(h):
	c = Counter(h)
	li = sorted([(n, v) for v, n in c.items()], reverse=True)
	print(li)
	for n, v in li:
		if v!=joker:
			return v
	return joker


def get_hand_type(h):
	x = best_J(h)
	newh = h.replace(joker, x) if joker in h else h
	print("*",h, x, newh)
	vs = list(Counter(newh).values())
	if 5 in vs:
		return 'Five of a kind'
	if 4 in vs:
		return 'Four of a kind'
	if 3 in vs and 2 in vs:
		return 'Full house'
	if 3 in vs: 
		return 'Three of a kind'
	if vs.count(2) == 2:
		return 'Two pair'
	if 2 in vs:
		return 'One pair'
	return 'High card'

def compare(h1, h2):
	h1, b1 = h1
	h2, b2 = h2
	print(h1, "-", h2)
	ht1 = get_hand_type(h1)
	ht2 = get_hand_type(h2)
	print(ht1, "-", ht2)
	cmp= POWER_H.index(ht1) - POWER_H.index(ht2)
	if cmp != 0:
		return cmp
	for i in range(5):
		cmp = POWER_C.index(h1[i]) - POWER_C.index(h2[i])
		if cmp != 0:
			return cmp
	return 0

hands = []
with open("in") as f:
	for line in f.read().splitlines():
		hands.append(line.split())

ranking = sorted(hands, key=cmp_to_key(compare))
#print(hands)
ret = 0
for i, h in enumerate(ranking, 1):
	_, b = h
	ret += i*int(b)
	#print(i, h)
print(ret)
