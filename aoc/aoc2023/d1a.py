

# leer archivo
# leer linea a linea
#pra cada linea:
# 	calcular el primero y el ultimo digito
# 	crear el numero de dos digitos y guardarlo
# sumamos todos

numbers = {
	0:"zero",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine"
}

def first_digit(line):
	if line[0] in "0123456789":
		return int(line[0]), 1
	for num, word in numbers.items():
		if line.startswith(word):
			return num, len(word)
	return -1, 0
	
## TODO: schange to day 1 A
def get_digits(line):
	d1 = ""
	dn = ""
	for i in range(len(line)):
		d, l = first_digit(line[i:])
		if d != -1 and d1 == "":
			d1 = d
		if d != -1:
			dn = d
		i += l
	if dn == "":
		print("error")
	return d1, dn
			


file = "input_d1"
f = open(file, "r")
suma = 0
for line in f.readlines():
	d1, dn = get_digits(line)
	n = int(d1)*10 + int(dn)
	print(line, n)
	suma += n
print(suma)