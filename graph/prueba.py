from grafo import Grafo

# ejercicio 14

# punto a
lista = ['cocina','comedor','cochera','quincho','bano1','bano2','hab1','hab2', 'sala_estar','terraza','patio']

grafo_casa = Grafo(dirigido=False)

for vertice in lista:
    grafo_casa.insert_vertice(vertice)

# punto b
# cocina
grafo_casa.insert_arist("cocina", "comedor", 3, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cocina", "cochera", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cocina", "hab1", 5, criterio_vertice='nombre', criterio_arista='vertice')
#comedor
grafo_casa.insert_arist("comedor", "quincho", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("comedor", "terraza", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("comedor", "sala_estar", 9, criterio_vertice='nombre', criterio_arista='vertice')
# cochera
grafo_casa.insert_arist("cochera", "quincho", 6, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cochera", "hab2", 5, criterio_vertice='nombre', criterio_arista='vertice')
# quincho
grafo_casa.insert_arist("quincho", "sala_estar", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("quincho", "terraza", 7, criterio_vertice='nombre', criterio_arista='vertice')
# baño 1
grafo_casa.insert_arist("bano1", "hab1", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano1", "sala_estar", 6, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano1", "terraza", 5, criterio_vertice='nombre', criterio_arista='vertice')
# baño 2
grafo_casa.insert_arist("bano2", "terraza", 4, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano2", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano2", "comedor", 5, criterio_vertice='nombre', criterio_arista='vertice')
# habitacion 1
grafo_casa.insert_arist("hab1", "bano2", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab1", "terraza", 4, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab1", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
# habitacion 2
grafo_casa.insert_arist("hab2", "sala_estar", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab2", "terraza", 3, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab2", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
# sala estar
grafo_casa.insert_arist("sala_estar", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("sala_estar", "hab1", 4, criterio_vertice='nombre', criterio_arista='vertice')
# terraza
grafo_casa.insert_arist("terraza", "patio", 4, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("terraza", "cochera", 8, criterio_vertice='nombre', criterio_arista='vertice')
# patio
grafo_casa.insert_arist("patio", "cochera", 5, criterio_vertice='nombre', criterio_arista='vertice')

# punto c
bosque = grafo_casa.kruskal()
for arbol in bosque:
    print('\narbol de expansion minima')
    for nodo in arbol.split(';'):
        print(nodo)

longitud = 0
for arbol in bosque:
    for arista in arbol.split(';'):
        distancia = int(arista.split('-')[-1])
        longitud += distancia
print(f'longitud total de cables necesaria para conectar todos los ambientes; {longitud} metros.')

# punto d
ori = 'hab1'
des = 'sala_estar'
longitud = 0
origen = grafo_casa.search_vertice(ori, criterio='nombre')
destino = grafo_casa.search_vertice(des, criterio='nombre')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo_casa.has_path(ori, des, criterio='nombre')):
        camino_mas_corto = grafo_casa.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
           value = camino_mas_corto.pop()
           if fin == value[0]:
                print(value[0], value[1])
                longitud+=value[1]
                fin = value[2]
print(f'total de metros de cable de red necesarios para conectar el router con el smart tv; {longitud} metros')


# ejercicio 15 
class Maravilla:    
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
   
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'

mi_grafo = Grafo(dirigido=False)

# arquitectonicas
mi_grafo.insert_vertice(Maravilla('gran muralla', 'china', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('machu picchu', 'peru', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('chichen itza', 'mexico', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('la petra', 'jordania', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('cristo redentor', 'brasil', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('coliseo', 'italia', 'arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('ciudad prohibida', 'china', 'arquitectonica'), criterio='nombre')
# naturales
mi_grafo.insert_vertice(Maravilla('isla de jeju', 'corea del sur', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('parque nacional de komodo', 'indonesia', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('gran barrera de coral', 'australia', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('el gran cañon', 'estados unidos', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('cataratas de iguazu', 'brasil argentina', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('montaña de la mesa', 'sudafrica', 'natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla('boque de piedra', 'china', 'natural'), criterio='nombre')

# punto b
# arquitectonicas
mi_grafo.insert_arist('gran muralla', 'machu picchu', 2, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'chichen itza', 4, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'la petra', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'cristo redentor', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'coliseo', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('gran muralla', 'ciudad prohibida', 3, criterio_vertice='nombre')

mi_grafo.insert_arist('machu picchu', 'chichen itza', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'la petra', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'cristo redentor', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'coliseo', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('machu picchu', 'ciudad prohibida', 4, criterio_vertice='nombre')

mi_grafo.insert_arist('chichen itza', 'la petra', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'cristo redentor', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'coliseo', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('chichen itza', 'ciudad prohibida', 8, criterio_vertice='nombre')

mi_grafo.insert_arist('la petra', 'cristo redentor', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('la petra', 'coliseo', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('la petra', 'ciudad prohibida', 8, criterio_vertice='nombre')

mi_grafo.insert_arist('cristo redentor', 'coliseo', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('cristo redentor', 'ciudad prohibida', 7, criterio_vertice='nombre')

mi_grafo.insert_arist('coliseo', 'ciudad prohibida', 6, criterio_vertice='nombre')

# naturales
mi_grafo.insert_arist('isla de jeju', 'parque nacional de komodo', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('isla de jeju', 'gran barrera de coral', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('isla de jeju', 'el gran cañon', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('isla de jeju', 'cataratas de iguazu', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('isla de jeju', 'montaña de la mesa', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('isla de jeju', 'boque de piedra', 5, criterio_vertice='nombre')

mi_grafo.insert_arist('parque nacional de komodo', 'gran barrera de coral', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('parque nacional de komodo', 'el gran cañon', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('parque nacional de komodo', 'cataratas de iguazu', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('parque nacional de komodo', 'montaña de la mesa', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('parque nacional de komodo', 'boque de piedra', 4, criterio_vertice='nombre')

mi_grafo.insert_arist('gran barrera de coral', 'el gran cañon', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'cataratas de iguazu', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'montaña de la mesa', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('gran barrera de coral', 'boque de piedra', 5, criterio_vertice='nombre')

mi_grafo.insert_arist('el gran cañon', 'cataratas de iguazu', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('el gran cañon', 'montaña de la mesa', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('el gran cañon', 'boque de piedra', 7, criterio_vertice='nombre')

mi_grafo.insert_arist('cataratas de iguazu', 'montaña de la mesa', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('cataratas de iguazu', 'boque de piedra', 5, criterio_vertice='nombre')

mi_grafo.insert_arist('montaña de la mesa', 'boque de piedra', 4, criterio_vertice='nombre')

# punto c
for i in range(mi_grafo.size()):
    vertice = mi_grafo.get_element_by_index(i)[0]
    if vertice.tipo == 'arquitectonica':
        bosque = mi_grafo.kruskal()
        for arbol in bosque:
            print('\narbol expansion minima arquitectonicas')
            for nodo in arbol.split(';'):
                print(nodo)
        break 
               
for i in range(mi_grafo.size()):
    vertice = mi_grafo.get_element_by_index(i)[0]
    if vertice.tipo == 'natural':
        bosque = mi_grafo.kruskal()
        for arbol in bosque:
            print('\narbol expansion minima naturales')
            for nodo in arbol.split(';'):
                print(nodo)
        break

# punto d
arquitectonicas = set()
naturales = set()

for i in range(mi_grafo.size()):
    vertice = mi_grafo.get_element_by_index(i)[0]
    if vertice.tipo == 'arquitectonica':
        arquitectonicas.add(vertice.pais)
    elif vertice.tipo == 'natural':
        naturales.add(vertice.pais)

ambos = arquitectonicas.intersection(naturales)
print('\npaises que tienen maravillas de ambos tipos')
for i in ambos:
    print(i)

# punto e
maravillas = {}
for i in range(mi_grafo.size()):
    vertice = mi_grafo.get_element_by_index(i)[0]
    pais = vertice.pais
    tipo = vertice.tipo

    data = f'{pais}-{tipo}'
    if data not in maravillas:
        maravillas[data] = 1
    else:
        maravillas[data] += 1

for data, count in maravillas.items():
    if count > 1:
        pais, tipo = data.split('-')
        print(f'{pais} tiene más de una maravilla del tipo {tipo}')