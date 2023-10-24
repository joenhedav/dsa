from pila import * 

pila = Pila() 
pila1 = Pila()

griegos = ['zeus','hades','hera','apolo']

indice = int(input('indice '))
dato = 'atenea' 

for elemento in griegos:
    pila.apilar(elemento)

for i in range(indice):
    pila1.apilar(pila.desapilar())
pila.apilar(dato)

while not pila1.es_vacia():
    pila.apilar(pila1.desapilar())

while not pila.es_vacia():
    data = pila.desapilar()
    print(data)





















