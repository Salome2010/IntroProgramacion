from queue import LifoQueue as Pila
from queue import Queue as Cola
#### 30/10/23

#1)
def ultima_aparicion(s:[int], e:int) -> int:  #usando for
    ultimo:int=0
    for i in range(len(s)):
        if e==s[i]:
            ultimo=i
    return ultimo 

def ultima_aparicion(s:[int], e:int) -> int: # usando while
    i:int=0
    ultimo:int = 0
    while (i<len(s)):
        if e==s[len(s)-1-i]: #comienza desde atras ya
            ultimo=i
        i+=1
    return ultimo

#res = ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0)
#print(res)

#2)
def elementos_exclusivos(s:[int],t:[int]) -> [int]:
    resu:[int] = []
    for i in range(len(s)):
        if not(pertenece(s[i],t)) and not(pertenece(s[i], resu)):
            resu.append(s[i])
    for j in range(len(t)):
        if not(pertenece(t[j],s)) and not(pertenece(t[j], resu)):
            resu.append(t[j])
    return resu

def pertenece(e:int, lista:[int]) -> bool:
    for i in range(len(lista)):
        if e==lista[i]:
            return True
    return False

#res = elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5])
#print(res)

#3)
def contar_traduciones_iguales(ingles:dict, aleman:dict) -> int:
    contador:int = 0
    for valor in ingles.keys():
        for otroValor in aleman.keys():
            if valor == otroValor and ingles[valor] == aleman[otroValor]:
                contador+=1
    return contador

#res = contar_traduciones_iguales({"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht","salo":"bella"}, {"Pie": "Foot", "Dedo": "Finger","salo":"bella", "Mano": "Hand"})
#print(res)

#4)
def convertir_a_dicc(lista:[int])-> dict:
    dicc = {}
    for i in range(len(lista)):
        if not(verSiEsta(lista[i],list(dicc.keys()))):
            dicc[lista[i]] = cantidadApariciones(lista[i], lista)
    return dicc

def cantidadApariciones(e:int, lista:[int]) -> int:
    contador:int = 0
    for i in range(len(lista)):
        if e==lista[i]:
            contador+=1
    return contador

def verSiEsta(e:int, claves:list) -> bool:
    for i in range(len(claves)):
        if e==claves[i]:
            return True
    return False

#res = convertir_a_dicc([-1,0,4,100,100,-1,-1])
#print(res)

### 6/11/23
#1)
def ind_nesima_aparicion(s:[int], n:int, e:int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if s[i] == e:
            contador+=1
            if contador ==n:
                return i
    return -1

#res = ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3],2,1)
#print(res)

#2)
def mezclar(s1:[int], s2:[int]) -> [int]:
    mezclados:[int] = []
    colaS1 = Cola()
    colaS2 = Cola()
    cola = Cola()
    for i in range(len(s1)):
        colaS1.put(s1[i])
    for j in range(len(s2)):
        colaS2.put(s2[j])
    while not(colaS1.empty() and colaS2.empty()):
        elemento1 = colaS1.get()
        elemento2 = colaS2.get()
        cola.put(elemento1)
        cola.put(elemento2)
    while not cola.empty():
        elemento = cola.get()
        mezclados.append(elemento)
    return mezclados
    
#res = mezclar([1, 3, 0, 1],[4, 0, 2, 3])
#print(res)

#3)
def frecuencia_posiciones_por_caballo(caballos:[str], carreras:dict) -> dict:
    dicc = {}
    for i in range(len(caballos)):
        dicc[caballos[i]] = posiciones(caballos[i],carreras)
    return dicc

def posiciones(caballo:str, carreras:dict) -> [int]:
    longitud = []
    for resultado in carreras.values():
        longitud.append(resultado)
    
    resu:[int] = [0]* (len(longitud[0]))

    for clave in carreras.keys():
        if pertenece(caballo, carreras[clave]):
            resu[posicion(caballo, carreras[clave])]+=1
        else:
            resu[posicion(caballo, carreras[clave])]+=0
    return resu

def pertenece(caballo:str, nombres:[str]) -> bool:
    for i in range(len(nombres)):
        if caballo == nombres[i]:
            return True
    return False

def posicion(caballo:str, lista:[str]) -> int:
    for i in range(len(lista)):
        if caballo == lista[i]:
            return i

#res = frecuencia_posiciones_por_caballo(["linda", "petisa", "mister", "luck" ], {"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]})
#print(res)


#4)
def matriz_capicua(m:[[int]]) -> bool:
    for i in range(len(m)):
        if not(es_capicua(m[i])):
            return False
    return True

def es_capicua(lista:[int]) -> bool:
    mitad: int = len(lista)//2
    for i in range(0,mitad):
        if lista[i] != lista[len(lista)-1-i]:
            return False
    return True

#res = matriz_capicua([[1,2,2,1],[-5,6,6,-5],[0,1,1,0]])
#print(res)

##### 12/06/2024

#1)