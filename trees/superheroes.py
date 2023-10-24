from arbol_binario import BinaryTree

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

