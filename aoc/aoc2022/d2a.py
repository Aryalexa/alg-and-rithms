# 21:58 - 22:13

opp = {'A':'rock', 'B':'paper', 'C':'scissors'}

you = {'X':'rock', 'Y':'paper', 'Z':'scissors'}

hand = {'rock':1, 'paper':2, 'scissors':3}

wins = { # (opp, you)
	('rock', 'paper'),
	('scissors', 'rock'),
	('paper', 'scissors'),
	}
win = 6
lost = 0
draw = 3
def points(o, y):
	o = opp[o]
	y = you[y]
	if o == y:
		return hand[y] + draw
	if (o,y) in wins:
		return hand[y] + win
	return hand[y] + lost

ret = 0
with open("in") as f:
	for line in f.readlines():
		o, y = line.strip().split()
		print(o, y)
		score = points(o,y)
		print(score)
		ret += score
print(ret)
