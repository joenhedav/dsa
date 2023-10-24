from pila import *
import random
from random import choice 
import string

pila = Pila()
pila1 = Pila()
for n in range(5):
    pila.apilar(random.randint(1,50))

#valor = int(input('valor '))
#count = 0
#while not pila.es_vacia():
#    data = pila.desapilar()
#    if data == valor:
#        count+=1
#print('ocurrencias de',valor,count)

#while not pila.es_vacia():
#    data = pila.desapilar()
#    print(data)
#    if data % 2==0:
#        pila1.apilar(data)
#pila = pila1
#while not pila1.es_vacia():
#    print(pila1.desapilar())

#valor = int(input('valor '))
#reemplaza = int(input('reemplazar '))
#while not pila.es_vacia():
#    data = pila.desapilar()
#    if data == valor:
#        data = reemplaza 
#    pila1.apilar(data)
#pila = pila1 
#while not pila.es_vacia():
#    print(pila.desapilar())

#print('mi pila')
#while not pila.es_vacia():
#    data = pila.desapilar()
#    print(data) 
#    pila1.apilar(data)
#print('invertida')
#while not pila1.es_vacia():
#    print(pila1.desapilar())

#pila = Pila()
#palabra = str(input('palabra '))
#invertida = ''
#for letra in palabra:
#    pila.apilar(letra)
#while not pila.es_vacia():
#    letra = pila.desapilar()
#    invertida += letra
#if invertida == palabra:
#    print('palidormo')

# eliminar data del indice n 
#pila = Pila()
#pila1 = Pila()
#palabras = ['ola','mar','uva','te','sol']
#indice = int(input('indice debajo de la pila '))
#for palabra in palabras:
#    pila.apilar(palabra)
#for i in range(indice):
#    pila1.apilar(pila.desapilar())
#pila.desapilar()
#while not pila1.es_vacia():
#    pila.apilar(pila1.desapilar())
#while not pila.es_vacia():
#    print(pila.desapilar())

# inserta dato en indice x 
#pila = Pila() 
#pila1 = Pila()
#griegos = ['zeus','hades','hera','apolo']
#indice = int(input('indice '))
#dato = 'atenea' 
#for elemento in griegos:
#    pila.apilar(elemento)
#while not pila.es_vacia():
#    print(pila.desapilar())
#for i in range(indice):
#    pila1.apilar(pila.desapilar())
#pila.apilar(dato)
#while not pila1.es_vacia():
#    pila.apilar(pila1.desapilar())
#while not pila.es_vacia():
#    print(pila.desapilar())

#pila = Pila()
#vocales=['a','e','i','o','u']
#count = 0
#for i in range(5):
#    letra = random.choice(string.ascii_lowercase)
#    pila.apilar(letra)
#while not pila.es_vacia():
#    data = pila.desapilar()
#    print(data)
#    if data in vocales:
#        count +=1 
#print('vocales',count)

#pila = Pila()
#pila1 = Pila()
#valores = ['yoda','darth vader','r2d2','c3po','kylo ren','leila organa','boba fett','grogu','chewbacca','han solo','obi-wan']
#for i in range(5):
#    valor = random.choice(valores)
#    pila.apilar(valor)
#    valores.remove(valor) # para evitar valores duplicados en la pila 
#hallado = False
#while not pila.es_vacia():
#    data = pila.desapilar()atooine", "Jabba the Hutt", 100
#    print(data)
#    pila1.apilar(data)
#    if data == 'boba fett' or data == 'leila organa':
#        hallado = True
#while not pila1.es_vacia():
#    pila.apilar(pila1.desapilar())
#if hallado:
#    print('se encontro a boba fett o leila organa')


#class Traje:
#    def __init__(self,modelo,pelicula,estado):
#        self.modelo = modelo
#        self.pelicula = pelicula
#        self.estado = estado
#
#    def __str__(self):
#        return self.modelo + ' ' + self.pelicula + ' ' + self.estado
#
#pila = Pila()
#pila1 = Pila()
#insertar = True
#estados = ['dañado','destruido','impecable']
#
#trajes = [
#        {'model':'mark I','film':'iron man','estate':choice(estados)},
#        {'model':'mark II','film':'iron man ','estate':choice(estados)},
#        {'model':'mark VII','film':'avengers','estate':choice(estados)},
#        {'model':'mark XLIV','film':'spider-man: homecoming','estate':choice(estados)},
#        {'model':'mark XLVI','film':'captain america: civil war','estate':choice(estados)}, 
#        {'model':'mark LXXXV','film':'iron man','estate':choice(estados)},
#    ]
#
#for traje in trajes:
#    data = Traje(traje['model'],
#                 traje['film'],
#                 traje['estate'])
#    pila.apilar(data)
#    print(data)
#
#film = str(input('pelicula donde se uso el modelo mark LXXXV '))
#while not pila.es_vacia():
#    data = pila.desapilar()
#    if data.modelo == 'mark XLIV': # a
#        print(f'el modelo {data.modelo} se uso en la pelicula {data.pelicula}')
#    if data.estado == 'dañado': # b 
#        print(f'{data.modelo} resultó dañado') 
#    if data.estado != 'destruido': # c 
#        pila1.apilar(data) 
#    if data.modelo == 'mark LXXXV' and data.pelicula == film: # e 
#        insertar = False
#    if data.pelicula in ['spider-man: homecoming','captain america: civil war']:
#        print(f'en la pelicula {data.pelicula} se uso el modelo {data.modelo}')
#
#if insertar:
#    nuevo_dato = Traje('mark LXXXV',film,choice(estados))
#    pila.apilar(nuevo_dato)
#
#while not pila1.es_vacia():
#    pila.apilar(pila1.desapilar())
#print('')
#while not pila.es_vacia():
#    print(pila.desapilar())

#pila = Pila()
#for i in range(5):
#    data = pila.apilar_creciente(random.randint(1,999))
#while not pila.es_vacia():
#    print(pila.desapilar())


# interseccion dadas dos pilas  
#episodio_v = ['darth vader','luke skywalker','yoda','sheev palpatine']
#episodio_vii = ['kylo ren','luke skywalker','yoda','han solo']
#
#pila = Pila()
#pila1 = Pila()
#interseccion = Pila()
#
#for data in episodio_v:
#    pila.apilar(data)
#for data in episodio_vii:
#    pila1.apilar(data)
#
#while not pila.es_vacia() and not pila1.es_vacia():
#    data = pila.desapilar()
#    data1 = pila1.desapilar()
#    if data == data1:
#        interseccion.apilar(data)
#
#print('mi pila interseccion')
#while not interseccion.es_vacia():
#    print(interseccion.desapilar())


# actividad 22 
#class Info:
#    def __init__(self,planeta,captura,costo):
#        self.planeta = planeta
#        self.captura = captura
#        self.costo = costo
#    def __str__(self):
#        return self.planeta + ' ' + self.captura + ' ' + str(self.costo)
#
#nave_bobafett = Pila()
#nave_dindjarin = Pila() 
#
#info_bobafett = [
#        {'planeta':'tatooine','captura':'luke skywalker','costo':15000},
#        {'planeta':'bespin','captura':'chewbacca','costo':30000},
#        {'planeta':'coruscant','captura':'han solo','costo':15550},
#        ]
#
#info_dindjarin = [
#        {'planeta':'nevarro','captura':'greef karga','costo':9500},
#        {'planeta':'tython','captura':'grogu','costo':3000},
#        {'planeta':'tatooine','captura':'moff gideon','costo':4000},
#        ]
#
#for info in info_bobafett:
#    data = Info(info['planeta'],
#                info['captura'],
#                info['costo'],  
#                )
#    nave_bobafett.apilar(data)
#
#for info in info_dindjarin:
#    data = Info(info['planeta'],
#                info['captura'],
#                info['costo'],  
#                )
#    nave_dindjarin.apilar(data)
#
#
#planetas_bobafett = Pila()  
#planetas_dindjarin = Pila() 
#auxiliar = Pila() 
#
#mision = 1 
#posicion = None
#
#creditos_bobafett = 0  
#creditos_dindjarin = 0 
#capturas = {'boba fett':0,'din djarin':0}
#while not nave_dindjarin.es_vacia() and not nave_bobafett.es_vacia():
#    # punto a 
#    data0 = nave_bobafett.desapilar()
#    planetas_bobafett.apilar(data0.planeta)
#    data1 = nave_dindjarin.desapilar()
#    planetas_dindjarin.apilar(data1.planeta)
#    # punto b 
#    creditos_bobafett += data0.costo  
#    creditos_dindjarin += data1.costo
#    # punto c
#    if data0.captura == 'han solo':
#        posicion = mision
#    mision += 1 
#    # punto d 
#    capturas['boba fett'] += 1 
#    capturas['din djarin'] += 1 
#
#print('planetas visitados por din djarin')
#while not planetas_dindjarin.es_vacia():
#    print(planetas_dindjarin.desapilar())
#print('planetas visitados por boba fett')
#while not planetas_bobafett.es_vacia():
#    print(planetas_bobafett.desapilar())
#
#if creditos_bobafett>creditos_dindjarin:
#    print('boba fett tiene mayor fortuna que din djarin')
#elif creditos_dindjarin>creditos_bobafett:
#    print('din djarin tiene mayor fortuna que boba fett')
#else:
#    print('ambos tienen la misma cantidad de creditos')
#
#if posicion is not None:
#    print('han solo capturado en mision',posicion,'desde el fondo de la pila')
#
#print('boba fett realizó {} capturas y din djarin realizó {} capturas'.format(capturas["boba fett"], capturas["din djarin"]))


# actividad 24
class Personaje:
    def __init__(self,name,films):
        self.name = name
        self.films = films
    
    def __str__(self):
        return f'{self.name} {self.films}'

pila=Pila()

personajes = [
        {'name':'groot','films':3},
        {'name':'doctor strange','films':2},
        {'name':'rocket raccoon','films':3},
        {'name':'iron man','films':10},
        {'name':'captain america','films':9}, 
        {'name':'black widow','films':7},
        {'name':'ant-man','films':4},
        ]

for personaje in personajes:
    pila.apilar(Personaje(personaje['name'].title(),
                          personaje['films'],
                          ))

groot = 1 
rocketraccoon = 1 
while not pila.es_vacia():
    data = pila.desapilar()
    # punto a 
    if data.name == 'groot'.title():
       print(f'{data.name} esta en la posicion {groot}')
    groot+=1 
    if data.name == 'rocket raccoon'.title():
        print(f'{data.name} esta en la posicion {rocketraccoon}')
    rocketraccoon +=1 
    # punto b 
    if data.films>5:
        print(f'{data.name} participo en mas de 5 peliculas {data.films}')
    # punto c 
    if data.name == 'black widow'.title():
        print(f'{data.name} participo en {data.films} peliculas')
    # punto d 
    if data.name[0] == 'C' or data.name[0] == 'G' or data.name[0] == 'D':
        print(f'su nombre comienza con C G o D {data.name}')


# actividad 19 
class Pelicula:
    def __init__(self,titulo,estudio,estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.estreno = estreno
    def __str__(self):
        return f'{self.titulo} - {self.estudio} - {self.estreno}'

peliculas = [
        {'titulo':'interstellar','estudio':'paramount pictures','estreno':2014},
        {'titulo':'guardians of the galaxy','estudio':'marvel studios','estreno':2014},
        {'titulo':'avengers: infinity war','estudio':'marvel studios','estreno':2018},
        {'titulo':'deadpool','estudio':'marvel studios','estreno':2016},
        {'titulo':'upgrade','estudio':'blumhouse productions','estreno':2018},
        {'titulo':'hacksaw ridge','estudio':'summit entertainment','estreno':2018},
        ]

pila=Pila()
for pelicula in peliculas:
    pila.apilar(Pelicula(pelicula['titulo'].title(),
                         pelicula['estudio'].title(),
                         pelicula['estreno'],
                         ))

count = 0 
while not pila.es_vacia():
    data = pila.desapilar()
    # punto a 
    if data.estreno == 2014:
        print(f'{data.titulo} fue estrenada en 2014')
    # punto b 
    if data.estreno == 2018:
        count += 1 
    # punto c 
    if data.estudio == 'marvel studios'.title() and data.estreno == 2016:
        print(f'estrenada en 2016 por Marvel Studios {data.titulo}')
print(f'cantidad de peliculas estrenadas en 2018 {count}')








