var = 'mundo'
num = 1234
num2 = 5678

flotante = 123.4
flotante2 = 456.31
carac = 'c'
carac2 = 'd'

bol = True
bol2 = False
bol3 = None

print (var)
print (carac + carac2)
print (var + carac)

print (num + num2)
print (flotante + flotante2)

print (not bol)
print (not bol2)
print (bol or bol2)
print (bol and bol2)


if 10 > 5:
	print ('10 es mayor que 5')
elif 10 < 5:
	print ('Eso es imposible viejo')

if bol:
	print ('Usamos la variable bol')

if True:
	print ('Es verdadero')

if not False:
	print ('La negacion de falso')

var_rapida = 0

while bol != bol2:
	if var_rapida >= 10:
		bol = False
	print(var_rapida)	
	var_rapida += 2

if type(var_rapida) is int:
	print('Es un entero')

if type(var) is str:
	print('Es una cadena')

if type(flotante) is float:
	print('Es flotante')

if type(flotante) is int:
	print('Es entero')

arreglo_num = [0, 1, 2, 3]
arreglo_car = ['c', 'h', 'a', 'r']  

print(arreglo_car[0])
print(arreglo_car[1])
print(arreglo_car[3])
print(len(arreglo_car))
print(arreglo_car[len(arreglo_car) - 1])


for cualquiernombredevariable in arreglo_num:
	print(cualquiernombredevariable)


for i in range(5):
	print(var[i])

for i in var:
	print(i)

gen = (i for i in range(100) if i % 2 != 0)

for x in gen:
	print(x)

arreglo_num.append(4)
arreglo_num.extend([5, 6])
print(arreglo_num)


tupla = (1, 2, 3)
print(tupla)

comp = [i + 1 for i in range(100) if i % 2!= 0]
comp.append(101)
print(comp)


dic = {'color': 'red', 'size': 123, 'width': 405.60}
if 'color' in dic:
	print(dic['color'])

for key in dic:
	print(key)
	print(dic[key])

	if 'color' in dic:
		print(dic['color'])


def multiplicacion(a1, a2):
	return a1 * a2

def mult(a1, a2, i = 0, acc = 0):
	if i < a2:
		return mult(a1, a2, i + 1, a1 + acc)
	else:
		return acc
		
def mult2(*args):
	res = 1
	for i in args:
		res *= i
	
	return res


def mult3(**kwargs):
	res = 1
	for key in kwargs:
		print(key)
		res *= kwargs[key]

	return res


def mult4(*args, **kwargs):
	res = 1
	for key in kwargs:
		print(key)
		res *= kwargs[key]
	
	for i in args:
		res *= i
	
	return res

print(multiplicacion(2,6))

print(mult(2,6))

print(mult2(2,6))

print(mult2(2,6,4,3))

print(mult3(num1 = 2, num2 =6))

print(mult3(num1 = 2, num2 = 6, num3 = 4, num4 = 3))
 
print(mult4(4, 3, num1 = 2, num2 = 6))

#Lectura de archivos
file = open('archivo1.txt', 'r')
print(file.readlines())
file.close()

#Escritura
file2 = open('archivo2.txt', 'w')
file2.write('Archivo2 prueba DE NUEVO')
file2.close()

#Append
file3 = open('archivo3.txt', 'a')
file3.write('Archivo3 prueba DE NUEVO')
file3.close()


try:
	file4 = open('archivo4.txt', 'a')
	file4.write('\nNueva linea de texto')
	file4.close()
except Exception as e:
	print('Ocurrio un error: ', e)
finally:
	print('Se intento abrir el archivo')

def abreArchivo():
	with open('archivo4.txt', 'r') as f:
		yield f.readlines()

for line in abreArchivo():
	print(line)