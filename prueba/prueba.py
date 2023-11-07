from arbol_binario import BinaryTree
from grafo import Grafo

# ejercicio 1
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemons = [
    {'name': 'pikachu', 'number': 25, 'type': ['electrico']},
    {'name': 'charizard', 'number': 6, 'type': ['fuego', 'volador']},
    {'name': 'bulbasaur', 'number': 1, 'type': ['tierra']},
    {'name': 'jolteon', 'number': 3, 'type': ['fuego', 'tierra']},
    {'name': 'lycanroc', 'number': 5, 'type': ['electrico']},
    {'name': 'tyrantrum', 'number': 4, 'type': ['acero']},
 ]

for data in pokemons:
    names = data['name']
    numbers = data['number']
    types = data['type']

    arbol_nombre.insert_node(names, data)
    arbol_numero.insert_node(numbers, data)
    for type in types:
        arbol_tipo.insert_node(type, data)

# punto b
num = 25
value = arbol_numero.search(num)
if value:
    print(value.other_values) 
else:
    print(f'no hay pokemon con el numero {num}')

print('\nbusqueda por coincidencia')
nombre_buscado = arbol_nombre.search_by_coincidence('bul')
if nombre_buscado:
    print('pokémons encontrados por nombre')
    for pokemon in nombre_buscado:
        print('nombre', pokemon.value)
        print('datos', pokemon.other_values)

# punto c
tipo = 'electrico'
print(f'\npokemons de tipo {tipo}')
arbol_tipo.inorden_tipos_pokemon(tipo)

# punto d
print('\nlistado por numero ascendente')
arbol_numero.postorden()
print('\nlistado ascendente nombre ')
arbol_nombre.postorden()
print('\nlistado por nivel nombre')
arbol_nombre.by_level()

# punto e 
print('\ndatos de jolteon')
node = arbol_nombre.search('jolteon')
if node:
    print(node.other_values)
else:
    print('no se encuentra jolteon')

print('\ndatos de lycanroc')
node = arbol_nombre.search('lycanroc')
if node:
    print(node.other_values)
else:
    print('no se encuentra lycanroc')

print('\ndatos de tyrantrum')
node = arbol_nombre.search('tyrantrum')
if node:
    print(node.other_values)
else:
    print('no se encuentra tyrantrum')

# punto f
print('\ncantidad de pokemons de tipo electrico')
cantidad =  arbol_tipo.contar_electrico_pokemon()
print(cantidad)
print('\ncantidad de pokemons de tipo acero')
cantidad = arbol_tipo.contar_acero_pokemon()
print(cantidad)


# ejercicio 2
grafo = Grafo()
grafo.insert_vertice('luke skywalker')
grafo.insert_vertice('boba fett')
grafo.insert_vertice('c-3po')
grafo.insert_vertice('rey')
grafo.insert_vertice('kylo ren')
grafo.insert_vertice('chewbacca')
grafo.insert_vertice('han solo')
grafo.insert_vertice('r2-d2')
grafo.insert_vertice('bb-8')
grafo.insert_vertice('yoda')
grafo.insert_vertice('darth vader')
grafo.insert_vertice('leila')

# aristas
grafo.insert_arist("luke skywalker", "leila", 4)
grafo.insert_arist("luke skywalker", "yoda", 3)
grafo.insert_arist("boba fett", "darth vader", 2)
grafo.insert_arist("c-3po", "r2-d2", 6)
grafo.insert_arist("rey", "kylo ren", 7)
grafo.insert_arist("chewbacca", "han solo", 5)
grafo.insert_arist("han solo", "leila", 4)
grafo.insert_arist("r2-d2", "bb-8", 3)
grafo.insert_arist("yoda", "darth vader", 2)


# punto b
arbol_expancion_min = grafo.kruskal()
for arista in arbol_expancion_min:
    print(arista)

contiene_yoda = False
for arista in arbol_expancion_min:
    if 'yoda' in arista[0] or 'yoda' in arista[1]:
        contiene_yoda = True

if contiene_yoda:
    print('contiene a yoda')
else:
    print('no contiene a yoda')

# punto c 
max_episodios = 0
personajes_max_episodios = []

for i in range(grafo.size()):
    vertice = grafo.get_element_by_index(i)
    aristas = vertice[1]
    for j in range(aristas.size()):
        arista = aristas.get_element_by_index(j)
        if arista.peso > max_episodios:
            max_episodios = arista.peso
            personajes_max_episodios = [vertice[0], arista.vertice]
        elif arista.peso == max_episodios:
            personajes_max_episodios.append(vertice[0])
            personajes_max_episodios.append(arista.vertice)

print('número máximo de episodios compartidos:', max_episodios)
print('personajes involucrados en el máximo de episodios compartidos:', personajes_max_episodios)
