# actividad 5 
def RomanoaDecimal(romano):
    '''convierte un numero romano a decimal.'''
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if len(romano) == 1:
        return dic[romano]
    else:
        primero = dic[romano[0]]
        segundo = dic[romano[1]]
        if primero >= segundo:
            return primero + RomanoaDecimal(romano[1:])
        else:
            return segundo - primero + RomanoaDecimal(romano[2:])

print(RomanoaDecimal('DLV'))

# actividad 22
def UsarLaFuerza(mochila,objetos=0):
    '''cuenta la cantidad de objetos sacados uno a la vez de la mochila de un jedi
       hasta encontrar un sable de luz o que no queden objetos en la misma.
    '''
    if len(mochila) == 0:
        return -1  
    elif mochila[0] == 'sable de luz':
        return objetos+1 
    else:
        return UsarLaFuerza(mochila[1:],objetos+1)

arr = ['holocron','brujula estrella','sable de luz','textos']
cantidad = UsarLaFuerza(arr)
if cantidad == -1:
    print('no hay un sable de luz en la mochila')
else:
    print('cantidad de objetos sacados para hallar el sable de luz',cantidad)