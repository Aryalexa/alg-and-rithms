import numpy as np


def ints(s, split=' '):
	return [int(x) for x in s.split(split) if x]
def as_array_ofdimN(x,n) -> np.ndarray:
	return np.array(list(x)[:n])

lines = []
with open("in") as f:
	for line in f.read().splitlines():
		x_str, v_str = line.split(' @ ')
		x = as_array_ofdimN(ints(x_str, ', '), 2)
		v = as_array_ofdimN(ints(v_str, ', '), 2)
		lines.append((x,v))

N = len(lines)
print(N)
AREA_MIN = 200000000000000
AREA_MAX = 400000000000000

def int_in_the_past(t1,t2):
	return False
	if t1 <0 and t2 < 0:
		print('int in the past for both')
		return False
	elif t1 < 0:
		print('int in the past for A')
		return False
	elif t2 < 0:
		print('int in the past for B')
		return False

def get_slope_and_origin(x,y,dx,dy):
	m = dy/dx
	n = y - m*x
	return m,n

def intersection_using_slopes(m1, n1, m2, n2):
	if m1 == m2:
		return False, 0,0
	x = (n2-n1)/(m1-m2)
	y = m1*x+n1
	return True, x,y

def intersection_infuture(xa:np.ndarray, va:np.ndarray, xb:np.ndarray, vb:np.ndarray):
	x1,y1 = xa
	x2,y2 = xb
	dx1, dy1 = va
	dx2, dy2 = vb

	m1, n1 = get_slope_and_origin(*xa, *va)
	m2, n2 = get_slope_and_origin(*xb, *vb)
	exist, i1,i2 = intersection_using_slopes(m1, n1, m2, n2)
	if not exist:
		print('parallel')
		return False, (0,0)
	# times
	t1 = (i1 -x1)/dx1
	t2 = (i1 -x2)/dx2
	print('t1', t1)
	if t1 <0 or t2 < 0:
		return int_in_the_past(t1,t2), (i1,i2)
	print('inters', (i1,i2))
	return True, (i1,i2)

cnt = 0
for i, lin1 in enumerate(lines):
	for j, lin2 in enumerate(lines):
		if i < j:
			print()
			print(lin1, 'and')
			print(lin2)
			exist, (p1,p2) = intersection_infuture(*lin1, *lin2)
			if not exist:
				continue
			if AREA_MIN<=p1<=AREA_MAX and AREA_MIN<=p2<=AREA_MAX:
				cnt+=1
print('counter', cnt)
			

