import math
from queue import LifoQueue as Pila
from queue import Queue as Cola

############ gui6 ###############

def imprimir_un_saludo(nombre:str):
    return  "hola " +  str(nombre)

#res = imprimir_un_saludo("salo")
#print(res)

def es_multiplo_de(n:int,m:int) -> bool:
    if n%m==0:
        return True
    return False

#res = es_multiplo_de(4,2)
#print(res) 

def cant_pizzas(comensales:int,cant:int) -> int:
    return math.ceil((comensales*cant)/8)

#res = cant_pizzas(3,5)
#print(res)

def peso_pino(altura:int) -> int:
    if altura<=300:
        return altura*3
    else:
        return 900 + (altura-300)*2

def viaje_en_el_tiempo(partida: int, llegada:int):
    inicio:int= partida - 1
    while(inicio>=llegada):
        print("Viajó un año al pasado, estamos en el año: " + str(inicio))
        inicio-=1
    print("llegamos")

#viaje_en_el_tiempo(2010,2005)

############ gui7 ###############

"""def ordenados(s:[int]) -> bool:
    primero:int=0
    i:int=1
    while(i<len(s)-1):
        if s[i]>s[i+1]:
            return False
        i+=1
    return True"""

def ordenados(s:[int]) -> bool:
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return False
    return True


#res = ordenados([1,4,3,4])
#print(res)

def pos_maximo(s:[int]) -> int:
    if len(s)==0:
        return -1
    max:int=s[0]
    pos:int=0
    for i in range(len(s)):
        if s[i]>=max:
            max=s[i]
            pos=i
        max
        pos
    return pos


#res = pos_maximo([5,7,2,7,8,8])
#print(res)

def pos_min(s:[int]) -> int:
    if len(s)==0:
        return -1
    min:int=s[0]
    pos:int=0
    for i in range(len(s)):
        if s[i]<=min:
            min=s[i]
            pos=i
        min
        pos
    return pos

#res = pos_min([5,7,2,1,1,1])
#print(res)

def lista_palabras(s:[str]) -> bool:
    for i in range(len(s)):
        if(len(s[i])>7):
            return True
    return False

#res = lista_palabras(["salo","micahjkg","y","sa"])
#print(res)

def palindromo(palabra:str) -> bool:
    mitad:int=len(palabra)//2
    for i in range(mitad):
        if palabra[i]!=palabra[len(palabra)-1-i]:
            return False
    return True

#res= palindromo("abshsba")
#print(res) 

def recorrer(s:[int])-> bool:
    for i in range(len(s)-2):
        if(s[i]==s[i+1]==s[i+2]):
            return True
    return False

#res = recorrer([1,5,5,2,2,6,6,6])
#print(res)

def vocales_dist(palabra:str)-> bool:
    contador:int=0
    for i in range(len(palabra)):
        if (palabra[i]=="a" or palabra[i]=="A" or palabra[i]=="e" or palabra[i]=="E" or palabra[i]=="i" or palabra[i]=="I" or palabra[i]=="o" or palabra[i]=="O" or palabra[i]=="u" or palabra[i]=="U"):
            contador+=1
    return contador>=3

#res = vocales_dist("ebigg") 
#print(res)

def cantidad_digitos_impares(numeros:[int])-> int:
    contador:int=0
    lista:[int]=[]
    for i in range(len(numeros)):
        lista+=str(numeros[i])
    for j in range(len(lista)):
        if int(lista[j])%2==1:
            contador+=1
    return contador

#res = cantidad_digitos_impares([57, 2383, 812, 246,0])
#print(res)

def eliminar_repetidos(s:str) -> str:
    sinRep:str=""
    for i in range(len(s)):
        if not pertenece(sinRep, s[i]):
            sinRep+=s[i]
    return sinRep

def pertenece(s:str, e:str) -> bool:
    for i in range(len(s)):
        if s[i]==e:
            return True
    return False

#res = eliminar_repetidos("mmhklññ")
#print(res)

def pertenece_a_cada_uno_version_1(s:[[int]], e:int,resu:[bool]):
    for i in range(len(s)):
        if pertenece(s[i],e):
            resu.append(True)
        else:
            resu.append(False)
    return resu
   
#res = pertenece_a_cada_uno_version_1([[1,2,3],[2,3,4],[5,7,8],[5],[]],5,[])
#print(res)

def es_matriz(matriz:[[int]])-> bool:
    if (len(matriz)>0 and len(matriz[0])>0 and todasFilasMismasLong(matriz)):
        return True
    return False 

def todasFilasMismasLong(matriz:[[int]]) -> bool:
    primera:[int] = matriz[0]
    for i in range(len(matriz)):
        if len(matriz[i])!=len(primera):
            return False
    return True

#res = es_matriz([[],[2,3,4],[1,2,3],[2,3,5]])
#print(res)

def filas_ordenadas(m:[[int]],resu:[bool]):
    for i in range(len(m)):
        if (ordenados(m[i])):
            resu.append(True)
        else:
            resu.append(False)
    return resu 

def columna(m:[[int]],c:int) -> [int]:
    secuencia:[int]=[]
    for i in range(len(m)):
        if (i==c):
            secuencia+=m[i]
    return secuencia

#res = columna([[1,2,3],[2,4,5],[4,7]],2)
#print(res)

def trasponer(m:[[int]]) -> [[int]]:
    traspuesta:[[int]] = []
    for i in range(len(m)):
        poner:[int]=[]
        for j in range(len(m)):
            poner.append(m[j][i])
        traspuesta.append(poner)
    return traspuesta

#res = trasponer([[1,2,3],[1,2,3],[1,2,3]])
#print(res)

############### guia8 ###############

def cant_elementos(p:Pila)-> int:
    otraP = Pila()
    cantidad:int=0
    while not p.empty():
        elemento=p.get()
        otraP.put(elemento)
        cantidad+=1
    while not otraP.empty():
        elemento=otraP.get()
        p.put(elemento)
    return cantidad

"""p = Pila()
p.put(1)
p.put(2)
p.put(3)
res = cant_elementos(p)
print(res)
while not p.empty():
    print(p.get())"""

def buscar_maxi(p:Pila)-> int:
    max= p.get()
    otraP = Pila()
    otraP.put(max)
    while not p.empty():
        elemento=p.get()
        otraP.put(elemento)
        if elemento>max:
            max=elemento
        max
    while not otraP.empty():
        elemento=otraP.get()
        p.put(elemento)
    return max

"""p = Pila()
p.put(1)
p.put(4)
p.put(3)
res = buscar_max(p)
print(res)
while not p.empty():
    print(p.get())"""

def buscar_nota_maxima(p:Pila) -> [str,int]:
    maximo:[str,int]= p.get()
    otraP = Pila()
    otraP.put(maximo)
    while not p.empty():
        elemento=p.get()
        otraP.put(elemento)
        if elemento[1]>maximo[1]:
            maximo=elemento
        maximo
    while not otraP.empty():
        elemento=otraP.get()
        p.put(elemento)
    return maximo

"""p = Pila()
p.put(["s",10])
p.put(["m",5])
print(buscar_nota_maxima(p))
while not p.empty():
    print(p.get())"""

def intercalar(p1:Pila,p2:Pila) -> Pila:
    pila = Pila()
    otraP = Pila()
    while not (p1.empty() and p2.empty()):
        elemento2=p2.get()
        elemento1=p1.get()
        otraP.put(elemento2)
        otraP.put(elemento1)
    while not otraP.empty():
        elemento=otraP.get()
        pila.put(elemento)
    return pila

"""p1 = Pila()
p1.put(3)
p1.put(2)
p1.put(1)
p2 = Pila()
p2.put(6)
p2.put(5)
p2.put(4)
res = intercalar(p1,p2)
while not res.empty():
    print(res.get())"""

def cant_elementos(c:Cola) -> int:
    otraC= Cola()
    contador:int=0
    while not c.empty():
        elemento=c.get()
        otraC.put(elemento)
        contador+=1
    while not otraC.empty():
        elemento=otraC.get()
        c.put(elemento)
    return contador

"""c = Cola()
c.put(1)
c.put(2)
c.put(3)
print(cant_elementos(c))
while not c.empty(): 
    print(c.get())"""

def buscar_max(c:Cola) -> int:
    maximo = c.get()
    nuevaC = Cola()
    nuevaC.put(maximo)
    while not c.empty():
        elemento=c.get()
        nuevaC.put(elemento)
        if elemento>maximo:
            maximo=elemento
        maximo
    while not nuevaC.empty():
        elemento=nuevaC.get()
        c.put(elemento)
    return maximo

"""c= Cola()
c.put(10)
c.put(5)
res = buscar_max(c)
print(res)
while not c.empty():
    print(c.get())"""


def secuencia_bingo() -> Cola:
    cola = Cola()
    for i in range(0,100):
        cola.put(i)
    return cola 

"""res = secuencia_bingo()
while not res.empty():
    print(res.get())"""

"""def jugar_carton_bingo(carton:[int], bolillero:Cola) -> Pila:
    contador:int=0
    carton2 = Cola()
    carton3=Pila()
    while not bolillero.empty():
        bola=bolillero.get()
        for i in range(len(carton)):
            if carton[i]==bola:
                contador+=1
    return contador

bolillero = Cola()
bolillero.put(12)
bolillero.put(7)
bolillero.put(23)
bolillero.put(5)
bolillero.put(42)
bolillero.put(8)
bolillero.put(1)
bolillero.put(17)
bolillero.put(99)
bolillero.put(98)
print(jugar_carton_bingo([5,17,23,42,8],bolillero))"""


def n_pacientes_urgente(c:Cola) -> int:
    cantidad:int=0
    otraC = Cola()
    while not c.empty():
        paciente:[int,str,str]=c.get()
        otraC.put(paciente)
        if (paciente[0]<=3):
            cantidad+=1
    while not otraC.empty():
        paciente:[int,str,str]=otraC.get()
        c.put(paciente)
    return cantidad

############# dicccc

def agrupar_por_long(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo, "r", encoding='utf8')
    dicc = {}
    for linea in archivo.readlines():
        palabra=""
        lista = str(linea)
        for i in range(len(lista)):
            if lista[i]!=" " and lista[i]!="\n":
                palabra+=lista[i]
            else:
                if palabra:
                    dicc[len(palabra)]=dicc.get(len(palabra),0)+1
                    palabra=""
    archivo.close()
    return dicc

#res = agrupar_por_long("hola_soy")
#print(res)

def calcular_promedio_estudiante(notas:list) -> dict:
    dicc = {}
    for i in range(len(notas)):
        estudiante=notas[i][0]
        if not(pertenece(estudiante, list(dicc.keys()))):
            dicc[estudiante]= promedio(estudiante, notas)
    return dicc

def pertenece(estudiante:str, claves:list) -> bool:
    for i in range(len(claves)):
        if claves[i]==estudiante:
            return True
    return False

def promedio(estudiante:str, notas:list) -> float:
    suma:int=0
    cantidad:int=0
    for i in range(len(notas)):
        if estudiante==notas[i][0]:
            suma+=notas[i][1]
            cantidad+=1
    promedio:float = suma/cantidad
    return promedio

#res = calcular_promedio_estudiante([["s", 10],["mo",8],["s",5],["romi",5],["mo",6]])
#print(res)

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    dicc = {}
    listaPalabras:[str] = []
    archivo = open(nombre_archivo, "r", encoding = 'utf8')
    for linea in archivo.readlines():
        palabra=""
        lista=str(linea)
        for i in range(len(lista)):
            if lista[i]!=" " and lista[i]!="\n":
                palabra+=lista[i]
            else:
                if palabra:
                    listaPalabras.append(palabra)
                    palabra=""
    for i in range(len(listaPalabras)):
        if not(pertenece(listaPalabras[i], list(dicc.keys()))):
            dicc[listaPalabras[i]]= cantidadApariciones(listaPalabras[i], listaPalabras)
    valores = list(dicc.values())
    mayorValor = valores[0]
    for i in range(len(valores)):
        if valores[i]> mayorValor:
            mayorValor=valores[i]
        mayorValor
    for clave in dicc.keys():
        if dicc[clave] == mayorValor:
            return clave

def cantidadApariciones(palabra:str, listaPalabras:[str]) -> int:
    apariciones:int=0
    for i in range(len(listaPalabras)):
        if palabra==listaPalabras[i]:
            apariciones+=1
    return apariciones 


#res = la_palabra_mas_frecuente("hola_soy")
#print(res)

inventario = {}
def agregar_producto(inventario:dict, nombre:str, precio:float, cantidad:int):
    if not(pertenece(nombre, list(inventario.keys()))):
        inventario[nombre] = {'precio':precio, 'cantidad':cantidad}

def actualizar_stock(inventario:dict, nombre:str, cantidad:int):
    if pertenece(nombre, list(inventario.keys())):
        inventario[nombre]['cantidad'] = cantidad

def actualizar_precio(inventario:dict, nombre:str, precio:float):
    if pertenece(nombre, list(inventario.keys())):
        inventario[nombre]['precio'] = precio

def calcular_valor_inventario(inventario: dict) -> float:
    total:float = 0
    for valor in inventario.keys():
        total+=((inventario[valor]['precio'])*(inventario[valor]['cantidad']))
    return total
    
"""agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Pantalon", 40)
actualizar_precio(inventario, "Camisa", 30.0)
res = calcular_valor_inventario(inventario)
print(res)"""



    dicc = {}
    for i in range(len(ventas_empleado_producto)):
        empleado = ventas_empleado_producto[i][0]
        producto = ventas_empleado_producto[i][1]
        if not(pertenece(empleado, list(dicc.keys()))):
            dicc[empleado] = []
        if not(pertenece(producto, list(dicc.values())[0])):
            dicc[empleado].append((producto,cantidadProducto(producto, ventas_empleado_producto))) 
    return dicc


def pertenece(empleado:str, claves:list) -> bool:
    for i in range(len(claves)):
        if empleado==claves[i]:
            return True
    return False

def cantidadProducto(producto:str, historial:[(str,str,int)]) -> int:
    cantidad:int = 0
    for i in range(len(historial)):
        if producto == historial[i][1]:
            cantidad+=historial[i][2]
    return cantidad
