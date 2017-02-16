import random, linecache, codecs

from enum import Enum

class Resultado(Enum):
	mayor = 1
	menor = 2
	igual = 3

#Funcion que nos devuelve una palabra aleatoria segun el fichero de palabras que nos han pasado
def get_word(fichero):
	#Primero vamos a contar cuantas filas tiene el fichero
	#Temporalmente voy a fijar el numero de lineas ya que no cambia y sera mas rapido para DEBUG
	with open(fichero,'r',encoding='utf-8') as f:
		num_lines = sum(1 for line in f)
		#num_lines = 15

	#Ahora vamos a elegir una linea aleatoriamente para seleccionar la palabra
	linea_palabra = random.randrange(num_lines)	

	#esta palabra tendra en caracter fin de linea que queremos quitar	
	palabra_con_endline = linecache.getline(fichero, linea_palabra)
	palabra=[]

	for w in range(len(palabra_con_endline) - 1):
		palabra.append(palabra_con_endline[w])

	
	data = {}
	data['palabra'] = palabra
	data['palabra_print'] = palabra_con_endline
	return data

'''
	Funcion que chequea si la palabra es menor, igual o mayor
	mayor = 1
	menor = 2
	igual = 3
	Ademas devolvera en el caso de que no se haya acertado 2 parametros para indicar al
	jugador cuales son las palabras que estan mas cerca de la que queremos buscar
			#Mantengo el estado del numero de letras iguales que hay, esto lo marca el indice del rango
	Estos parametros son:
	letras_iguales: es el primer valor para saber cuanto de cerca esta una palabra de la buscada
	distancia_letra: la primera letra que sea diferente tendra una distancia numerica de la letra
					que se esta buscando
'''
def check_palabra(guess_palabra_t, palabra_t):
	resultado = Resultado.mayor	
	rango = 0
	letras_iguales = 0
	distancia_letra = 30
	guess_palabra = ''
	palabra = ''
	#Quitamos en ambos caso el caracter de salto de linea introducido al obtener
	#los strings desde el JQuery
	palabra = palabra_t.replace('\n','')
	guess_palabra = guess_palabra_t.replace('\n','')	
	
	#Ahora vamos a marcar cual es el rango maximo que debemos buscar
	if len(guess_palabra) < len(palabra):
		rango = len(guess_palabra)
	else:
		rango = len(palabra)

	#Una vez definido el rango a recorrer
	for i in range(rango):
		#print ("loop: " + str(i) +" total: " + str(rango))
		#print(guess_palabra[i] +" "+ palabra[i])

		#Si 2 letras son iguales
		if guess_palabra[i] == palabra[i]:
			#Y ademas estoy en el final del rango
			if i == rango - 1:
				#Y si las 2 palabras tienen el mismo tamaño
				if (len(guess_palabra) == len(palabra)):
					#print("palabra encontrada")
					resultado = Resultado.igual
					break
				#Si no tienen el mismo tamaño entonces voy a ver cual de las 2 palabras
				#es mas grande y dependiendo de esto respondo
				else:
					if len(guess_palabra) < len(palabra):
						#print("la palabra que buscar es MAYOR")
						resultado = Resultado.mayor
					else:
						#print("la palabra que buscar es MENOR")
						resultado = Resultado.menor				
				
			#Si 2 letras son iguales pero todavia no he llegado al final tengo que seguir buscando	
			#else:
			#	print("has acertado alguna letra")
			#por donde voy ahora mismo				
			letras_iguales = i + 1
		#En el caso de que las letras no sean iguales, las comparo para ver si son mayores o menores
		#ademas fuerzo con el BREAK a salir del bucle for, el conteo de letras iguales ya lo tengo
		else:
			if palabra[i] > guess_palabra[i] :
				#print("la palabra que buscas es MAYOR")
				resultado = Resultado.mayor
				distancia_letra = ord(palabra[i]) - ord(guess_palabra[i])
			else:
				#print("la palabra que buscas es MENOR")
				resultado = Resultado.menor
				distancia_letra = ord(guess_palabra[i]) - ord(palabra[i])
			print(distancia_letra)
			break
	
	data = {}
	data['resultado'] = resultado
	data['letras_iguales'] = letras_iguales
	data['distancia_letra'] = distancia_letra
	return data

#En el futuro comprobare que la palabra que se busca esta dentro del Lemario
#El futuro ha llegado
#TODO
def check_diccionario(guess_palabra, fichero):
	resultado = False
	#Primero vamos a contar cuantas filas tiene el fichero
	#Temporalmente voy a fijar el numero de lineas ya que no cambia y sera mas rapido para DEBUG
	num_lines = sum(1 for line in open(fichero))
	#num_lines = 85918	

	with codecs.open(fichero,'r', 'utf-8') as openfile:
		for word in openfile:        
			if guess_palabra in word:
				resultado = True
	
	return resultado
'''
para = False
while not para:
	input_palabra = input('Introduce palabra ')
	resultado = check_palabra(input_palabra)
	if (resultado is Resultado.igual):
		para = True
		print("palabra encontrada TERMINADO")
	elif (resultado is Resultado.mayor):
		print("la palabra que buscas es MAYOR")
	else:
		print("la palabra que buscas es MENOR")
'''

