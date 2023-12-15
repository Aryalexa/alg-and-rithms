from collections import OrderedDict, defaultdict

def hash(s:str):
	cur = 0
	for c in s:
		cur += ord(c)
		cur *= 17
		cur %= 256
	return cur

class Box:
	def __init__(self) -> None:
		self.lens: OrderedDict[str,int] = OrderedDict()
	
	def __str__(self) -> str:
		d = [f"{k}:{v}" for k,v in self.lens.items()]
		return f"Box({','.join(d)})"
	
	def focusing_power(self, num:int) -> int:
		lenses_power = 0
		for i, (label,v) in enumerate(self.lens.items(),1):
			lenses_power += num*i*v
		return lenses_power


# -------------------

with open("in") as f:
	text = f.read()

codes = text.split(',')
boxes = defaultdict(Box)
ret = 0

for code in codes:
	if '=' in code:
		label, num = code.split("=")
		print(code, hash(label))
		boxes[hash(label)].lens[label] = int(num)
	if '-' in code:
		label = code[:-1]
		if label in boxes[hash(label)].lens:
			del boxes[hash(label)].lens[label]

power = 0
for n, b in boxes.items():
	power += b.focusing_power(n+1)
	print(n, b, power)

print(power)
