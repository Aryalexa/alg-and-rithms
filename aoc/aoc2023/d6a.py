import math
'''sqrt solution'''

def previous_integer(n:float) -> int:
	if math.floor(n) == n:
		return int(n) - 1
	return math.floor(n)

def next_integer(n:float) -> int:
	return math.floor(n)+1


file = "in"
lines = []
with open(file, "r") as f:
	lines = f.readlines()

time = [int(x) for x in lines[0].split(": ")[1].strip().split()]
print(time)
distance = [int(x) for x in lines[1].split(": ")[1].strip().split()]
print(distance)
N = len(time)

prod = 1
for i in range(N):
	t  = time[i] 
	d = distance[i]
	x1 = (-t + math.sqrt(t*t - 4*d))/(-2)
	x2 = (-t - math.sqrt(t*t - 4*d))/(-2)
	print(t, d, "->", x1, x2)
	w1 = next_integer(x1)
	w2 = previous_integer(x2)
	print("->", w1, w2, "-", w2 - w1 + 1)
	prod *= w2 - w1 + 1
print(prod)


""""

7s 9m
1 {2,3,4,5} 6,7 (4)

15, 40
1 - 3 {4 - 11} 12 - 15 (8)
b 1-15
40 - 15 = 25s -> 25m/s -> 

30 - 200
1 - 10 {11 - 19} 20 - 30 (9)

---

7s 9m
1 {2,3,4,5} 6,7 (4)
b			  rem_t * v
1s -> 1m/s -> (7-1) * 1
2s -> 2m/s -> (7-2) * 2 = 10
3s -> 3m/s -> (7-3) * 3 = 12
(T-x)*x > record when x in [1-T]
Tx - x2 - rec = 0
-x2 + Tx - rec = 0
	a = -1 < 0 (neg)
	b = T = 7
	c = -rec = -9, rec = 9
x = (-T +- sq(T2 - 4*rec))/(-2)
x = (-7 +- sq(49 - 36))/(-2)
x = (-7 +- sq(13))/(-2)
x = (-7 +- 3.6)/(-2)
x1 = (-7+3.6)/(-2) = 3.4/2 = 1.7 (L)-ceil-> 2
x2 = (-7-3.6)/(-2) = 10.6/2 = 5.3 (G)-floor-> 5 
	x in [x1,x2], res >= rec
	x in (x1,x2), res > rec
	x1 < x < x2 -> ceil(x) <= x <= floor(x2)

"""