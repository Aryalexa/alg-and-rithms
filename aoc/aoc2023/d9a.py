
def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def all_zeros(seq):
	return all(x == 0 for x in seq)

def predict(seq):
	if all_zeros(seq):
		return 0
	difs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
	return seq[-1] + predict(difs)

ret = 0
with open("in") as f:
	for line in f.read().splitlines():
		seq = ints(line)
		new_v = predict(seq)
		print(seq, new_v)
		ret += new_v
print(ret)

