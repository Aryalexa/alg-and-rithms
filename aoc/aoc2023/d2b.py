
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
	print("\n-", handfuls_line)
	r = g = b = 0
	for h in handfuls:
		rgb = get_cubes(h.strip()) #strip leading and trailing spaces
		print (rgb, h.strip())
		if rgb[0] > r:
			r = rgb[0]
		if rgb[1] > g:
			g = rgb[1]
		if rgb[2] > b:
			b = rgb[2]
	power = r*g*b
	print ("power", r, g, b, "->", power)
	suma += power
f.close()
print(suma)
	


