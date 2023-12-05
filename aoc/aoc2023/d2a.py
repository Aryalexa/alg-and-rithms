
rgb_max = (12, 13, 14)

def get_cubes(handful_str: str):
	r = g = b = 0
	ws = handful_str.split(', ')
	#print("*", ws)
	for w in ws:
		n, color = w.split(' ')
		#print("* ", n, color)
		if color == 'red':
			r = int(n)
		elif color == 'green':
			g = int(n)
		elif color == 'blue':
			b = int(n)
	return (r, g, b)


file = "input_d2"
f = open(file, "r")
suma = 0
for line in f.readlines():
	game, handfuls_line = line.split(':')
	game_id = int(game.split(' ')[1])
	handfuls = handfuls_line.split(';')
	ok = True
	print("\n-", handfuls_line)
	for h in handfuls:
		rgb = get_cubes(h.strip()) #strip leading and trailing spaces
		print (rgb, h.strip())
		if (rgb[0] > rgb_max[0] or
			rgb[1] > rgb_max[1] or
			rgb[2] > rgb_max[2] ):
			ok = False
			break
	print("    -", ok)
	if ok:
		suma += game_id
f.close()
print(suma)
	


