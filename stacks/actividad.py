from pila import Pila

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


print('')
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


























