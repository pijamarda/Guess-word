from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.utils import timezone

import linecache
import json
from datetime import datetime

from . import tools
from .models import Palabra, Intento, Reportada, Rendicion

def index(request):

	#Este es el nombre del fichero que vamos a utilizar para configurar la ruta utilizamos el fichero
	#settings.py donde ya hemos configurado una ruta con los ficheros del sistema
	FICHERO_LEMARIO = settings.LEMARIO_FOLDER +'lemario-20101017.txt'
	#Llamamos a la funcion que nos devolvera una palabra aleatoriamente cada vez que refresquemos
	#la pantalla principal
	palabra = tools.get_word(FICHERO_LEMARIO)
	
	#Creamos un diccionario para pasar todos los datos que vayamos necesitando al template
	#El primero de ellos es la palabra
	#OJO que este string tendra un caracter de fin de linea \n
	data={}	
	data['palabra_guess'] = palabra['palabra_print']
	return render(request, 'game/index.html', data)

#API REST Function que comprueba si la palabra introducida es la correcta
def check_guess(request):
	FICHERO_LEMARIO = settings.LEMARIO_FOLDER +'lemario-20101017.txt'
	guess = None
	palabra = ''
	
	#Comprobamos que venimos de un GET y si es asi cojemos las 2 variables
	#En un futuro habria que ocultar la palabra a adivinar ya que esta en claro
	#en la peticion
	if request.method == 'GET':		
		guess = request.GET['guess']
		palabra = request.GET['palabra']

	#Resultado guardara si la palabra buscada es mayor, menor o igual
	#si no es ninguna de ellas se toma por defecto que la palabra buscada no 
	#esta en el diccionario
	resultado = 4
	
	#La funcion check_diccionario es la que busca la palabra en el listado de palabras
	if (tools.check_diccionario(guess, FICHERO_LEMARIO)):
		data = tools.check_palabra(guess, palabra)		
		resultado = data['resultado']
		return HttpResponse(json.dumps({
						        "resultado": resultado.value, 					        
						        "letras_iguales": data['letras_iguales'],
						        "distancia_letra": data['distancia_letra']}),
						    	content_type="application/json")
	#
	else:
		return HttpResponse(json.dumps({"resultado": resultado}),
						    	content_type="application/json")
	
#Funcion auxuliar que no estoy utilizando, por ahora pagina en blanco del template
def resultado(request):
	
	data={}		
	return render(request, 'game/resultado.html', data)

#API REST function que permite guardar los resultados del jugador en funcion de las palabras
#y los intentos
def save(request, intentos, palabra):
	
	p = Palabra.objects.filter(word=palabra)
	if not p:				
		p = Palabra(word=palabra)
		p.save()
	else:
		p = Palabra.objects.get(word=palabra)
	i = Intento(palabra=p,intentos=intentos, fecha=timezone.now())
	i.save()
	data=0	
	return HttpResponse(data)

#Funcion que permite reportar palabras que el usuario cree que deberian existir pero que no aparecen
#en la lista que tenemos
def reportar(request, palabra):
	
	p = Reportada.objects.filter(word=palabra)
	if not p:				
		p = Reportada(word=palabra, veces=1)
		p.save()
	else:
		p = Reportada.objects.get(word=palabra)
		num_veces = p.veces
		num_veces = num_veces + 1
		p.veces = num_veces
		p.save()
	data = {}
	return render(request, 'game/reportar.html', data)

#API REST function que permite guardar cuando el jugador se rinde en funcion de las palabras
#y los intentos
def merindo(request, intentos, palabra):
	
	p = Palabra.objects.filter(word=palabra)
	if not p:				
		p = Palabra(word=palabra)
		p.save()
	else:
		p = Palabra.objects.get(word=palabra)
	i = Rendicion(palabra=p,intentos=intentos, fecha=timezone.now())
	i.save()
	data=0	
	return HttpResponse(data)
