def fibu(n):
    '''calcula la suseción de fibunacci de un n-esimo termino'''
    if n == 0 or n == 1:
        return n
    return fibu(n-1) + fibu(n-2)

def fact(n):
    '''calcula el factorial de un numero entero'''
    if n == 1:
        return 1
    return n * fact(n-1)

def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)

def producto(n1,n2):
    if n1 == 0 or n2 == 0:
        return 0
    return n1 + producto(n1,n2-1)

def potencia(base,exp):
    if exp == 0:
        return 1 
    return base * potencia(base,exp-1)

def RomanoaDecimal(romano):
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

print(RomanoaDecimal('LILCMD'))

def invertirCadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertirCadena(cadena[1:]) + (cadena[0])
print(invertirCadena('alpha centauri'))

def cantDigitos(num):
    if num < 10:
        return 1
    else:
        return 1 + cantDigitos(num//10)

print('cantidad de digitos de',cantDigitos(123))

def h(num):
    if num==1:
        return 1
    else:
        return h(num-1) + 1/num

def logEntero(n,b):
    if n<b:
        return 0
    else:
        return logEntero(n//b,b)+1

def binario(decimal):
    if decimal <= 1:
        return str(decimal)
    else:
        return binario(decimal//2)+str(decimal%2)

def euclides(num1,num2):
    if num2==0:
        return num1
    else:
        return euclides(num2,num1%num2)

def mcm(num1,num2):
    return (num1*num2)/euclides(num1,num2)

def invertirNumero(num,res=0):
    if num == 0:
        return res
    else:
        res = (res*10)+(num%10)
        num = num // 10
        return invertirNumero(num,res)

num = 12345
print('el numero invertido de',num,'es',invertirNumero(num))

def SumDigitos(n):
    if n == 0:
        return 0
    else:
        return n%10 + SumDigitos(n//10)

def progresionGeometrica(n):
    if n==1:
        return 2
    else:
        return -3 * progresionGeometrica(n-1)
n=3
for valor in range(1,n+1):
    print("a{} = {}".format(valor,progresionGeometrica(valor)))

def ArrayInverso(a,index):
    if index >= 0:
        print(a[index])
        ArrayInverso(a,index-1)

arr = [1,2,3,4,5]
ArrayInverso(arr,len(arr)-1)

def busquedaBinariaRecursiva(arr,valor,l,r):
    if l>r:
        return -1    
    mid = (l+r)//2 
    if arr[mid] == valor:
        return mid
    if valor<arr[mid]:
        return busquedaBinariaRecursiva(arr,valor,l,mid-1)
    else:
        return busquedaBinariaRecursiva(arr,valor,mid+1,r)
valores = [1,3,5,23]
valor = 3
indice = busquedaBinariaRecursiva(valores,valor,0,len(arr)-1)
if indice == -1:
    print(valor,'no esta en la lista')
else:
    print(valor,'esta en el indice',indice)


def UsarLaFuerza(mochila,objetos=0):
    if len(mochila) == 0:
        return -1  # no encuentra nada
    elif mochila[0] == 'sable de luz':
        return objetos + 1  # encuentra el sable de luz
    else:
        return UsarLaFuerza(mochila[1:],objetos+1)  # sigue buscando

arr = ['holocron','brujula estrella','sable de luz','textos']
print('cantidad de objetos sacados',UsarLaFuerza(arr))