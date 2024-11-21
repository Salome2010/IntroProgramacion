from queue import LifoQueue as Pila
from queue import Queue as Cola
### 1) tema2
def gestion_ventas(ventas_empleado_producto: list) -> dict:
    dicc:dict = {}
    for empleado, producto, cantidad in ventas_empleado_producto:
        if empleado in dicc.keys():
            dicc[empleado].append((producto,cantidad))
        else:
            dicc[empleado]=[(producto,cantidad)]
    return dicc

#res = gestion_ventas([("mica", "pantalon", 2),("salo", "pantalo", 1),("mica", "saco",1),("mica","camisa",3),("salo", "camisa", 2)])
#print(res)

### 2)
def cantidad_digitos_imp(numeros:[int]) -> [int]:
    contador:int=0
    lista:[int] = []
    for i in range(len(numeros)):
        lista+=str(numeros[i])
    for i in range(len(lista)):
        if int(lista[i]) % 2 == 1:
            contador+=1
    return contador

#res = cantidad_digitos_imp([57, 2383, 812, 246,8,957])
#print(res)

### 3)
def reordenar_cola(carpetas:Cola, umbral:int) -> Cola():
    cola:[(str,int)] = Cola()
    colaAux:[(str,int)] = Cola()
    colaMayores:[(str,int)] = Cola()
    colaMenores:[(str,int)] = Cola()
    while not carpetas.empty():
        carpeta:(str,int) = carpetas.get()
        colaAux.put(carpeta)
        if carpeta[1]>umbral:
            colaMayores.put(carpeta)
        else:
            colaMenores.put(carpeta)
    while not colaAux.empty():
        carpeta = colaAux.get()
        carpetas.put(carpeta)
    while not colaMayores.empty():
        carpeta = colaMayores.get()
        cola.put(carpeta)
    while not colaMenores.empty():
        carpeta = colaMenores.get()
        cola.put(carpeta)
    return cola
"""
carpetas = Cola()
carpetas.put(("A123", 10))
carpetas.put(("A124", 5))
carpetas.put(("A125", 12))
carpetas.put(("A126", 3))
carpetas.put(("A127", 7))
res = reordenar_cola(carpetas,6)
while not res.empty():
    print(res.get())
"""

#4)
def matriz_cuasi_decre(matriz:[[int]])-> bool:
    maximo:int=0
    for i in range(0,len(matriz)-1):
        if buscar_max(matriz[i]) < buscar_max(matriz[i+1]):
            return False
    return True
    
def buscar_max(lista:[int]) -> int:
    max:int=0
    for i in range(len(lista)):
        if lista[i]>max:
            max=lista[i]
        max
    return max

#res = matriz_cuasi_decre([[10,5,2],[8,2,9],[12,6,7],[1,4,3]])
#print(res)

#### tema 1
#1)

def gestion_notas(notas_estudiante_materia: list) -> dict:
    dicc = {}
    for estudiante, materia, nota in notas_estudiante_materia:
        if estudiante in dicc.keys():
            dicc[estudiante].append((materia, nota))
        else:
            dicc[estudiante] = [(materia, nota)]
    return dicc

#res = gestion_notas([("mica", "lengua", 2),("salo", "lengua", 1),("mica", "mate",1),("mica","geo",3),("salo", "geo", 2)])
#print(res)

#2)
def cant_digitos_pares(numeros:[int]) -> int:
    contador:int=0
    lista:[int] = []
    for i in range(len(numeros)):
        lista+=(str(numeros[i]))
    for j in range(len(lista)):
        if int(lista[j])%2==0:
            contador+=1
    return contador

#res =  cant_digitos_pares([22,456,789,431])
#print(res)
#3)
def reordenar_cola_primero_pesados(paquetes:Cola, umbral:int) -> Cola():
    cola:[(str,int)] = Cola()
    colaAux:[(str,int)] = Cola()
    colaMayores:[(str,int)] = Cola()
    colaMenores:[(str,int)] = Cola()
    while not paquetes.empty():
        paquete = paquetes.get()
        colaAux.put(paquete)
        if paquete[1] > umbral:
            colaMayores.put(paquete)
        else:
            colaMenores.put(paquete)
    while not colaAux.empty():
        paquete = colaAux.get()
        paquetes.put(paquete)
    while not colaMayores.empty():
        paquete = colaMayores.get()
        cola.put(paquete)
    while not colaMenores.empty():
        paquete = colaMenores.get()
        cola.put(paquete)
    return cola

"""paquetes = Cola()
paquetes.put(("A123", 10))
paquetes.put(("A124", 5))
paquetes.put(("A125", 12))
paquetes.put(("A126", 3))
paquetes.put(("A127", 7))
res = reordenar_cola_primero_pesados(paquetes,6)
while not res.empty():
    print(res.get())"""

#4)
def matriz_minimos(matriz:[[int]]) -> bool:
    for i in range(0,len(matriz)-1):
        if minimo(matriz[i]) > minimo(matriz[i+1]):
            return False
    return True

def minimo(lista:[int]) -> int:
    min:int = lista[0]
    for i in range(len(lista)):
        if lista[i]<= min:
            min=lista[i]
        min 
    return min 

#res = matriz_minimos([[0,5,8],[1,2,6],[4,5,7],[0,1,2]])
#print(res)

    



        
    



