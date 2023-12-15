
def hash(s:str):
	cur = 0
	for c in s:
		cur += ord(c)
		cur *= 17
		cur %= 256
	return cur


with open("in") as f:
	text = f.read()
codes = text.split(',')

ret= 0
for code in codes:
	ret += hash(code)

print(ret)
