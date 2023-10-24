from cola import *
from pila import *
import random
from random import randint,choice
import string

cola = Cola()
for i in range(5):
    cola.arribo(random.randint(1,11))

#cola1 = Cola()
#vocales = ['a','e','i','o','u']
#for i in range(5):
#    letra = random.choice(string.ascii_lowercase)
#    cola.arribo(letra)
#
#while not cola.es_vacia():
#    data = cola.atencion()
#    if data not in vocales:
#        cola1.arribo(data)
#cola = cola1
#while not cola1.es_vacia():
#    print(cola1.atencion())

#cola = Cola()
#pila = Pila()
#for valor in range(5):
#    cola.arribo(valor)
#while not cola.es_vacia():
#    pila.apilar(cola.atencion())
#while not pila.es_vacia():
#    cola.arribo(pila.desapilar())
#while not cola.es_vacia():
#    print(cola.atencion())

#cola = Cola()
#pila = Pila()
#valor = str(input('palabra '))
#invertida = ''
#for letra in valor:
#    cola.arribo(letra)
#while not cola.es_vacia():
#    pila.apilar(cola.atencion())
#while not pila.es_vacia():
#    letra = pila.desapilar()
#    invertida += letra
#if invertida == valor:
#    print(valor,'es un palidormo')

#cola = Cola()
#pila = Pila()
#for i in range(5):
#    pila.apilar(i)
#while not pila.es_vacia():
#    cola.arribo(pila.desapilar())
#while not cola.es_vacia():
#    pila.apilar(cola.atencion())

#valor = int(input('dame un valor '))
#count = 0
#while not cola.es_vacia():
#    data = cola.atencion()
#    print(data)
#    if data == valor:
#        count += 1 
#print('ocurrencias',count)
#


#notificaciones = [
#        {'app':'facebook','hora':'14:30','mensaje':'nuevo mensaje de asdasd'},
#        {'app':'twitter','hora':'11:30','mensaje':'hola mundo en python'},
#        {'app':'telegram','hora':'15:00','mensaje':'asdasda'},
#        ]
#
#cola = Cola()
#cola1 = Cola()
#pila  = Pila()
#
#for notificacion in notificaciones:
#    cola.arribo(notificacion)
#while not cola.es_vacia():
#    data = cola.atencion()
#    if data['app'] != 'facebook':
#        cola1.arribo(data)
#while not cola1.es_vacia():
#    cola.arribo(cola1.atencion())
#for i in range(cola.tamano()):
#    data = cola.mover_al_final()
#    if data['app'] == 'twitter' and 'python' in data['mensaje']:
#        print(data['hora'],data['app'],data['mensaje'])
#for i in range(cola.tamano()):
#    data = cola.mover_al_final()
#    if data['hora'] >= '11:43' and data['hora'] <= '15:57':
#        pila.apilar(data)
#print('cantidad de notificaciones en la pila',pila.tam())
#while not cola.es_vacia():
#    print(cola.atencion())


# actividad 11

#class Personaje:
#    def __init__(self,nombre,planeta):
#        self.nombre = nombre
#        self.planeta = planeta 
#    def __str__(self):
#        return f'{self.nombre} {self.planeta}'
#
#cola_star_wars = Cola()
#cola = Cola()
#personajes = [
#        {'nombre':'han solo','planeta':'corellia'},
#        {'nombre':'luke skywalker','planeta':'tatooine'},
#        {'nombre':'jar jar binks','planeta':'naboo'},
#        {'nombre':'wicket w. warrick','planeta':'endor'},
#        {'nombre':'leila organa','planeta':'alderaan'},
#        {'nombre':'yoda','planeta':'desconocido'},
#        {'nombre':'chewbacca','planeta':'kashyyyk'},
#        ]
#
#for personaje in personajes:
#    cola_star_wars.arribo(Personaje(personaje['nombre'],
#                          personaje['planeta'],
#                          ))
#
#nuevo_personaje = Personaje('r2d2','asdasd')
#while not cola_star_wars.es_vacia():
#    data = cola_star_wars.atencion()
#    if data.planeta == 'alderaan' or data.planeta == 'endor' or data.planeta == 'tatooine':
#        print(f'{data.planeta} {data.nombre}')
#    if data.nombre == 'luke skywalker' or data.nombre == 'han solo':
#        print(f'{data.nombre} originario de {data.planeta}')
#    if data.nombre == 'yoda':
#        cola.arribo(nuevo_personaje)
#        cola.arribo(data)
#    else:
#        cola.arribo(data)
#while not cola.es_vacia():
#    cola_star_wars.arribo(cola.atencion())
#while not cola_star_wars.es_vacia():
#    data = cola_star_wars.atencion()
#    if data.nombre == 'jar jar binks':
#        cola.arribo(data)
#        cola_star_wars.atencion()
#    else:
#        cola.arribo(data)
#print('')
#print(f'se inserto a {nuevo_personaje} antes que yoda y se elimino al personaje ubicado luego de jar jar binks')
#while not cola.es_vacia():
#    print(cola.atencion())
#


cola = Cola()
class Superheroe:
    def __init__(self,nombre,personaje,sexo):
        self.nombre = nombre
        self.personaje = personaje 
        self.sexo = sexo

    def __str__(self):
        return f'{self.nombre}  {self.personaje}  {self.sexo}' 

personajes = [
        {'name':'tony stark','nick':'iron man','sex':'m'},
        {'name':'steve rogers','nick':'captian america','sex':'m'},
        {'name':'natasha romanoff','nick':'black widow','sex':'f'},
        {'name':'peter parker','nick':'spiderman','sex':'m'},
        {'name':'scott lang','nick':'ant man','sex':'m'},
        {'name':'carol danvers','nick':'captain marvel','sex':'f'},
        ]

for personaje in personajes:
    cola.arribo(Superheroe(personaje['name'].title(),
                       personaje['nick'].title(),
                       personaje['sex'].title(),
                       ))

encontrado = False
while not cola.es_vacia():
    data = cola.atencion()
    if data.personaje == 'captain marvel'.title():
        print(f'el nombre de {data.personaje} es {data.nombre}')
    if data.sexo == 'F':
        print(f'personaje femenino {data.personaje}')
    if data.sexo == 'M':
        print(f'personaje masculino {data.personaje}')
    if data.nombre == 'scott lang'.title():
        print(f'{data.nombre} es el superheroe {data.personaje}')
    if data.personaje[0] == 'S':
        print(f'comienza con S {data.personaje}')
    if data.nombre == 'carol danvers'.title():
        encontrado = True
        nombre = data.nombre
        superheroe = data.personaje

if encontrado:
    print(f'{nombre} esta en la cola su nombre de superheroe es {superheroe}')
else:
    print('{nombre} no esta en la cola')