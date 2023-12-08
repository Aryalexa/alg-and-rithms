# 21:58 - 22:13 - 22:28 -> 15, 15

opp = {'A':'rock', 'B':'paper', 'C':'scissors'}
#you = {'X':'rock', 'Y':'paper', 'Z':'scissors'}
strat = {'X': 'lose', 'Y' :'draw', 'Z': 'win'}

hand = {'rock':1, 'paper':2, 'scissors':3}

wins = { # (opp, you)
	('rock', 'paper'),
	('scissors', 'rock'),
	('paper', 'scissors'),
	}
win = 6
lost = 0
draw = 3

def get_hand(o, strategy):
	if strategy == 'lose':
		return [loser for (loser, w) in wins if w==o][0]
	if strategy == 'win':
		return [w for (loser, w) in wins if loser==o][0]
	return o

def points(o, y):
	# o = opp[o]
	# y = you[y]
	if o == y:
		return hand[y] + draw
	if (o,y) in wins:
		return hand[y] + win
	return hand[y] + lost

ret = 0
with open("in") as f:
	for line in f.readlines():
		o, s = line.strip().split()
		y = get_hand(opp[o], strat[s])
		score = points(opp[o],y)
		#print(opp[o], strat[s], y, score)
		ret += score
print(ret)
