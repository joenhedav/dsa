from arbol_binario import BinaryTree
from cola import Cola
import random

arbol = BinaryTree()
for i in range(5):
    arbol.insert_node(random.randint(0,50))

# ejercicio 1
# punto a 
#print('preorden')
#arbol.preorden()
#print('\ninorden')
#arbol.inorden()
#print('\npostorden')
#arbol.postorden()
#print('\npor nivel')
#arbol.by_level()
## punto b 
#print('')
#numero = int(input('entre un numero '))
#pos = arbol.search(numero)
#if pos:
#    print(f'{numero} esta cargado en el arbol')
#else:
#    print(f'{numero} no esta cargado en el arbol')
## punto c
#for i in range(3):
#    numero = int(input('numero a eliminar '))
#    valor_eliminado = arbol.delete_node(numero)
#    if valor_eliminado:
#        print(f'el numero {numero} fue eliminado')
#    else:
#        print(f'el numero {numero} no esta en el arbol')
## punto d 
#altura_izquierdo = arbol.altura_subarbol_izq()
#print(f'altura del subarbol izquierdo {altura_izquierdo}')
#altura_derecho = arbol.altura_subarbol_der()
#print(f'altura del subarbol derecho {altura_derecho}')
## punto e 
#ocurrencias = arbol.contar(3)
#print(f'cantidad de ocurrencias {ocurrencias}')
## punto f 
#pares, impares = arbol.contar_pares_impares()
#print(f'pares {pares} impares {impares}')

# ejercicio 4 
arbol = BinaryTree()
arbol.insert_node(10)
arbol.insert_node(5)
arbol.insert_node(15)
print(f'hijo izquierdo {arbol.get_left_child(10)}')
print(f'hijo derecho {arbol.get_right_child(10)}')  

# ejercicio 5
lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()
for value in lista_heroes:
    arbol.insert_node(value['name'].title(), value['heroe'])
print('villanos ordenados alfabeticamente')
arbol.inorden_super_or_villano(False)
print('\ncomienza con C')
arbol.inorden_start_with('C')
cantidad = arbol.contar_heroes()
print(f'cantidad de supereheroes {cantidad}')
print('\nlistado desdendente de supereheroes')
arbol.postorden_superheroe(True)
print('\nrealizando la busqueda por proximidad')
arbol.search_by_coincidence('Do')
value = input('ingrese el nombre que desea modificar ')
indice = arbol.search(value)
if indice:
    is_hero = indice.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese el nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no se encunetra el valor')
# punto g
print('\ngenerar bosque')
bosque = arbol.generar_bosque_s_v()
print('cantidad de nodos en el arbol de supereheroes', bosque['nodos_superheroes'])
print('cantidad de nodos en el arbol de villanos', bosque['nodos_villanos'])

# ejercicio 8 
print('')
arbol = BinaryTree()
for value in range(5):
    arbol.insert_node(random.randint(0,50))
arbol.inorden()
min_value = arbol.find_min()
print(f'minimo valor {min_value}')
max_value = arbol.find_max()
print(f'maximo valor {max_value}')




