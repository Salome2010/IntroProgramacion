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
def alarma_epidemiologica (registros:[(int, str)], infecciosas:[str], umbral: float) -> dict:
    dicc = {}
    for i in range(len(registros)):
        if pertenece(registros[i][1], infecciosas) and cantidad(registros[i][1], registros) >= umbral:
            dicc[registros[i][1]] = (cantidad(registros[i][1], registros)) / len(registros)
    return dicc

def pertenece(enfermedad:str, enfermedades:[str]) -> bool:
    for i in range(len(enfermedades)):
        if enfermedad == enfermedades[i]:
            return True
    return False

def cantidad(enfermedad:str, regist:[(int,str)]) -> int:
    total:int = 0
    for i in range(len(regist)):
        if enfermedad == regist[i][1]:
            total+=1
    return total

#res = alarma_epidemiologica([(3,"al"),(1,"bm"),(6,"ro"),(5,"fo"),(9,"al"),(2,"ro")],["ro","al","bm"],0.5)
#print(res)

#2)
def orden_de_atencion(urgentes:Cola, postergables:Cola) -> Cola():
    cola = Cola()
    colaU = Cola()
    colaP = Cola()
    while not(urgentes.empty() and postergables.empty()):
        pacienteU= urgentes.get()
        colaU.put(pacienteU)
        cola.put(pacienteU)
        pacienteP = postergables.get()
        colaP.put(pacienteP)
        cola.put(pacienteP)
    while not colaU.empty():
        paciente = colaU.get()
        urgentes.put(paciente)
    while not colaP.empty():
        paciente = colaP.get()
        postergables.put(paciente)
    return cola

"""urgentes = Cola()
urgentes.put(2)
urgentes.put(3)
urgentes.put(4)
postergables = Cola()
postergables.put(5)
postergables.put(6)
postergables.put(7)
res = orden_de_atencion(urgentes, postergables)
while not res.empty():
    print(res.get())
while not urgentes.empty():
    print(urgentes.get())"""

#3)
def nivel_de_ocupacion(camas_por_piso:[[bool]]) -> [float]:
    ocupadas:[float] = []
    for i in range(len(camas_por_piso)):
        ocupadas.append((cantidad_camas(camas_por_piso[i]))/len(camas_por_piso[i]))
    return ocupadas

def cantidad_camas(piso:[bool]) -> int:
    total:int = 0
    for i in range(len(piso)):
        if piso[i] == True:
            total+=1
    return total

#res = nivel_de_ocupacion([[True, False, True],[False,True,True],[True,False,False],[True,True,True],[True,True,True],[False,False,False]])
#print(res)

#4) verr
def empleados_del_mes(horas:dict) -> [int]:
    totasLasHoras:[[int]] = []
    max:int = 0
    masHoras:[int] = []
    for id in horas.keys():
        totasLasHoras.append(horas[id])
    for i in range(len(totasLasHoras)):
        if suma(totasLasHoras[i]) > max:
            max=i
        max
    claves = list(horas.keys())
    for i in range(len(claves)):
        if i == max:
            masHoras.append(claves[i])
    return masHoras

def suma(lista:[int]) -> int:
    total:int = 0
    for i in range(len(lista)):
        total+=lista[i]
    return total

"""horas_trabajadas = {
    1: [8, 9, 7, 8, 10],
    2: [9, 8, 9, 9, 9],
    3: [8, 8, 8, 8, 8],
    4: [10, 9, 10, 10, 10],
    5: [],
    6: [10, 9, 10, 10, 10]
}

print(empleados_del_mes(horas_trabajadas))"""

## 12/06/2024

#1)
def promedio_de_salidas(registro: dict) -> dict:
    dicc = {}
    for clave in registro.keys():
        dicc[clave] = verPromedio(registro[clave])
    return dicc

def verPromedio(valores:[int]) -> dict:
    dic = {}
    cantidadSalas:int = 0
    cantidadMayor0: int = 0
    for i in range(len(valores)):
        if  0<valores[i]<61:
            cantidadSalas+=1
    
    for j in range(len(valores)):
        if  0<valores[j]<61:
            cantidadMayor0+=valores[j]
    promedio:float = 0.0
    if cantidadMayor0>0 and cantidadSalas>0:
        promedio = (cantidadMayor0 / cantidadSalas)
    if cantidadSalas not in dic.keys():
        dic[cantidadSalas] = promedio
    return dic
    
"""r1 = {"agus": [0,21,3,61], "leo": [34,0,12,61]} #{"agus":(2,12.0), "leo":(2,23.0)}
print(promedio_de_salidas(r1))
r2 = {"agus": [0,21,3,61], "leo": [61,0,61,61]} #{"agus":(2,12.0), "leo":(0,0.0)}
print(promedio_de_salidas(r2))
r3 = {"agus": [0,61,13,12,45,34,12,61], "leo": [35,46,21,31,21,23,25,38,], "ale": [61,61,61,61,61,61,61,61]}
 #{"agus":(5,23.2), "leo":(8,30.0), "ale":(0,0.0)}
print(promedio_de_salidas(r3))
r4 = {"agus": [58,58,58,0,61,58], "leo": [0,0,0,0,61,54], "ale": [14,13,0,61,10,12]}
# #{"agus":(4,58), "leo":(1,54), "ale":(4,12.25)}
print(promedio_de_salidas(r4))   """

#2)
def tiempo_mas_rapido(tiempo_salas:[int]) -> int:
    masRapido:int = primeroDistintodDe0(tiempo_salas)
    indice:int = 0
    for i in range(0,len(tiempo_salas)):
        if (0<tiempo_salas[i]<61) and tiempo_salas[i]<masRapido:
            masRapido = tiempo_salas[i]
            indice = i
    return indice



def primeroDistintodDe0(tiempos:[int]) -> int:
    for i in range(len(tiempos)):
        if tiempos[i] != 0:
            return tiempos[i]


"""print(tiempo_mas_rapido([12,14,90,45,10])) #4
print(tiempo_mas_rapido([12,10,90,45,10])) #1
print(tiempo_mas_rapido([0,61,7,12,54,23])) #2
print(tiempo_mas_rapido([0,0,0,60,61])) #2 falla
print(tiempo_mas_rapido([1,23,34,1,1,1,0,61])) #0
print(tiempo_mas_rapido([0,0,61,0,61,12,2])) #6"""

#3)
def racha_mas_larga(tiempos:[int]) -> (int,int):
    indiceIn:int = 0
    indice:int = 0
    longitud:int = 0
    indiceMax:int = 0
    longitudMax:int = 0
    for i in range(len(tiempos)):
        if 0<tiempos[i]<61:
            if longitud == 0:
                indice = i
            longitud+=1
            if longitud>longitudMax:
                longitudMax = longitud
                indiceIn = indice
                indiceMax = i
        else:
            longitud = 0
    return (indiceIn, indiceMax)

#res = racha_mas_larga([0, 10, 15, 60, 20, 25, 0, 5, 50, 60, 0, 30, 45])
#print(res)

#4)
def escape_en_solitario(amigos_por_sala:[[int]]) -> [int]:
    solo3:[int] = []
    for i in range(len(amigos_por_sala)):
        if salaSoloFue3(amigos_por_sala[i]) and 0<amigos_por_sala[i][2]<=61:
            solo3.append(i)
    return solo3

def salaSoloFue3(sala:[int]) -> bool:
    for i in range(len(sala)):
        if i!=2:
            if sala[i]!=0:
                return False
    return True

"""aps1 = [[0,0,1,4],
         [0,0,21,0]]
print(escape_en_solitario(aps1)) #[1]
aps2 = [[0,0,1,0],
         [0,0,21,0],
         [1,2,54,1],
         [0,0,5,1]]
print(escape_en_solitario(aps2)) #[0,1]
aps3 = [[0,0,61,61],
         [12,32,0,0],
         [35,21,26,21]]
print(escape_en_solitario(aps3)) #[]
aps4 = [[0,0,0,0],
         [0,0,61,0],
         [0,0,21,0],
         [0,0,0,0]]
print(escape_en_solitario(aps4)) #[1,2]
aps5 = [[0,0,34,0],
         [0,0,61,0],
         [0,0,21,0],
         [0,0,54,0]]
print(escape_en_solitario(aps5)) #[0,1,2,3] """

##2023

#1)
def acomodar(s:[str]) -> [str]:
    acomodado:[str]= []
    for i in range(len(s)):
        if s[i] == "UP":
            acomodado.append(s[i])
    for j in range(len(s)):
        if s[j] == "LLA":
            acomodado.append(s[j])
    return acomodado

#res = acomodar(["LLA","UP","UP","LLA","UP","LLA","LLA","UP"])
#print(res)

#2)
def pos_umbral(s:[int], u:int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if s[i]>0:
            contador+=s[i]
            if contador> u:
                return i 
    return -1 

"""print(pos_umbral([1,-2,0,5,-7,3], 5))
print(pos_umbral([1,0,-2,1,-1,0,2], 7))
print(pos_umbral([1,0,-2,5,2,-3], 7))"""

#3)
def columnas_repetidas(matriz:[[int]]) -> bool:
    for i in range(len(matriz)):
        if not(mitadIgual(matriz[i])):
            return False
    return True

def mitadIgual(lista:int) -> bool:
    primeraMitad:[int] = []
    segundaMitad:[int] = []
    mitad:int = len(lista)//2
    for i in range(0,mitad):
        primeraMitad.append(lista[i])
    for j in range(mitad,len(lista)):
        segundaMitad.append(lista[j])
    return primeraMitad == segundaMitad

"""m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
print(columnas_repetidas(m))
m2 = [[1,2,1,2],[-5,6,-5,6],[0,1,0,2]]
print(columnas_repetidas(m2))
m3 = [[1,2,1,2,1,2],[-5,6,-5,6,-5,6],[0,1,0,1,0,1]]
print(columnas_repetidas(m3))
m4 = [[1,2,1,1,2,1],[-5,6,-5,-5,6,-5],[0,1,0,0,1,0]]
print(columnas_repetidas(m4))"""

#4)
def cuenta_posiciones_por_nacion(naciones:[str], torneos:dict) -> dict:
    dicc = {}
    for i in range(len(naciones)):
        dicc[naciones[i]] = posicion(naciones[i], list(torneos.values()))
    return dicc

def posicion(nacion:str, valores:[[str]]) -> [int]:
    resu:[int] = [0]*len(valores[0])
    for i in range(len(valores)):
        for j in range(len(valores[i])):
            if nacion == valores[i][j]:
                resu[j]+=1
    return resu

"""naciones = ["arg", "aus", "nz", "sud"]
torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
print(cuenta_posiciones_por_nacion(naciones, torneos))"""

#10/06/2024
#1)
def reordenar_cola_priorizando_vips(filaClientes:Cola) -> Cola():
    cola:[str] = Cola()
    colaComun:[str] = Cola()
    colaVip:[str] = Cola()
    colaAux:[(str,str)] = Cola()
    while not filaClientes.empty():
        cliente = filaClientes.get()
        colaAux.put(cliente)
        if cliente[1] == "vip":
            colaVip.put(cliente[0])
        else:
            colaComun.put(cliente[0])
    while not colaAux.empty():
        cliente = colaAux.get()
        filaClientes.put(cliente)
    while not colaVip.empty():
        cliente = colaVip.get()
        cola.put(cliente)
    while not colaComun.empty():
        cliente = colaComun.get()
        cola.put(cliente)
    return cola

"""filaClientes: Cola = Cola()
filaClientes.put(("juan", "vip")) #1
filaClientes.put(("ana", "vip")) #2
filaClientes.put(("seba", "comun")) #5
filaClientes.put(("rodo", "vip")) #3
filaClientes.put(("aejo", "comun")) #6
filaClientes.put(("leo", "comun")) #7
filaClientes.put(("bale", "vip")) #4
res = reordenar_cola_priorizando_vips(filaClientes)
while not res.empty():
    print(res.get())
while not filaClientes.empty():
    print(filaClientes.get())"""

#2)
def torneo_de_gallinas(estrategias: dict) -> dict:
    dicc = {}
    for clave in estrategias.keys():
        dicc[clave] = estrategia(clave,estrategias)
    return dicc

def estrategia(jugador:str, jugadas:dict) -> int:
    contador:int = 0
    for clave in jugadas.keys():
        if clave != jugador:
            if jugadas[jugador] == "no me desv" and jugadas[clave] == "no me desv":
                contador-=5
            if jugadas[jugador] == "me desv" and jugadas[clave] == "me desv":
                contador-=10
            if (jugadas[clave] == "no me desv" and jugadas[jugador] == "me desv"):
                contador-=15
            if (jugadas[jugador] == "no me desv" and jugadas[clave] == "me desv"):
                contador+=10
    return contador

"""e1 = {"leo": "me desv", "rodo": "no me desv"}
# leo = -15
# rodo = 10
print(torneo_de_gallinas(e1))
e2 = {"leo": "me desv", "rodo": "no me desv", "bale": "me desv"}
# leo = -25
# rodo = 20
# bale = -25
print(torneo_de_gallinas(e2))
e3 = {"leo": "me desv", "rodo": "no me desv", "bale": "me desv", "nico": "no me desv"}
# leo = -40
# rodo = 15
# bale = -40
# nico = 15
print(torneo_de_gallinas(e3))
e4 = {"leo": "me desv", "rodo": "no me desv", "bale": "me desv", "nico": "no me desv", "ale": "no me desv"}
# leo = -55 
# rodo = 10
# bale = -55
# nico = 10
# ale = 10
print(torneo_de_gallinas(e4))"""


#3) MAALLLL
def quien_gano_el_tateti_facilito(tablero:[str]) -> int:
    traspuestas:[str] = trasponer(tablero)
    for i in range(len(traspuestas)):
        if (contadorX(traspuestas[i]) == len(traspuestas[i])):
            if VerSiHayO(traspuestas):
                return 3
    for j in range(len(traspuestas)):
        if not(contadorX(traspuestas[j]) == len(traspuestas[j])):
            if not(VerSiHayO(traspuestas)):
                return 0
    for l in range(len(traspuestas)):
        if (contadorX(traspuestas[l]) == len(traspuestas[l])):
            if not(VerSiHayO(traspuestas)):
                return 1

def VerSiHayO(traspues:[str]) -> bool:
    for i in range(len(traspues)):
        if traspues[i] == "O"*len(traspues[i]):
            return True
    return False


def trasponer(tablero:[str]) -> [str]:
    fin:[str] = []
    n:int = 0
    palabra=""
    while n<len(tablero[0]):
        for i in range(len(tablero)):
            palabra+=tablero[i][n]
        fin.append(palabra)
        palabra=""
        n+=1
    return fin

def contadorX(traspuest:str) -> int:
    contador:int = 0
    for i in range(len(traspuest)):
        if traspuest[i] == "X":
            contador+=1
    return contador


"""t1 = [["X","","O","",""],["X","O","","",""],["X","","","","O"]] #1
print(quien_gano_el_tateti_facilito(t1))
t2 = [["","O","","","",""],["","X","","","O",""],["","X","","","",""],["","X","O","","",""]]
print(quien_gano_el_tateti_facilito(t2)) #1
t3 = [["","O","","X","",""],["","","O","","","X"],["","O","","","",""],["X","","","","",""]]
print(quien_gano_el_tateti_facilito(t3)) #2
t4 = [["","O","","X","",""],["","","O","","","X"],["","","","","O",""],["X","","","","",""]]
print(quien_gano_el_tateti_facilito(t4)) #2
t5 = [["","X","","","","","O"],["X","","O","","","",""],["","","","","O","X","X"],["O","","","","","","X"]] #2
print(quien_gano_el_tateti_facilito(t5))
t6 = [["X","","","","",""],["X","","","O","",""],["X","","","O","",""],["","","","O","",""]] #3
print(quien_gano_el_tateti_facilito(t6))
t7 = [["","","","","","O"],["","","X","O","",""],["X","O","X","","",""],["","","X","","","O"]] #1
print(quien_gano_el_tateti_facilito(t7))"""


#4)
def cuantos_sufijos_son_palindromos(texto:str) -> int:
    total:int = 0
    listaSufijo:[str] = []
    lista = list(str(texto))
    palabra=""
    while len(lista)>0:
        for i in range(len(lista)):
            palabra+=lista[i]
        listaSufijo.append(palabra)
        lista.pop(0)
        palabra=""
    for j in range(len(listaSufijo)):
        if espalindromo(listaSufijo[j]):
            total+=1
    return total

def espalindromo(palabra:str) -> bool:
    lista = list(str(palabra))
    mitad = len(lista)//2
    for i in range(0,mitad):
        if lista[i] != lista[len(lista)-1-i]:
            return False
    return True

#res = cuantos_sufijos_son_palindromos("sos")
#print(res)

## otro 10/06
#1)
def filtrar_codigos_primos(codigo_barras:[int]) -> [int]:
    primos:[int] = []
    for i in range(len(codigo_barras)):
        if cantidadDig(codigo_barras[i]) == 3 and (esPrimo(codigo_barras[i]) or (ultimos3(codigo_barras[i]))== ('002' or '005' or '007')) :
            primos.append(codigo_barras[i])
        if cantidadDig(codigo_barras[i]) > 3 and (esPrimo(ultimos3(codigo_barras[i])) or (ultimos3(codigo_barras[i])) == ('002' or '005' or'007')) :
            primos.append(ultimos3(codigo_barras[i]))
    return primos

def cantidadDig(numero:int) -> int:
    cantidad:int = 0
    lista = list(str(numero))
    for i in range(len(lista)):
        cantidad+=1
    return cantidad

def esPrimo(numero:int) -> bool:
    if numero == 2 or numero ==3 or numero==5 or numero==7:
        return True
    if int(numero)%2 == 0 or int(numero)%3==0 or int(numero)%5 == 0 or  int(numero)%7==0:
        return False
    return True

def ultimos3(numero:int) -> int:
    lista = list(str(numero))
    numero:int = ''
    while len(lista)>3:
        lista.pop(0)
    for i in range(len(lista)):
        numero+=lista[i] 
    return numero 

"""c1 = [11111002, 214013, 849032, 38491005,102011]
print(filtrar_codigos_primos(c1))
c2 = [101, 38435028, 4742019, 95472986]
print(filtrar_codigos_primos(c2))"""

#2)
def stock_productos(stock_cambios:[(str,int)]) -> dict:
    dicc = {}
    for i in range(len(stock_cambios)):
        if not(pertenece(stock_cambios[i][0], list(dicc.keys()))):
            dicc[stock_cambios[i][0]] = tuplaMinMax(stock_cambios[i][0], stock_cambios)
    return dicc

def pertenece(producto, productos:[str]) -> bool:
    for i in range(len(productos)):
        if producto == productos[i]:
            return True
    return False

def  tuplaMinMax(producto:str, stock:[(str,int)]) -> (int,int):
    max:int = 0
    verMin:int = buscarProducto(producto,stock)
    min:int = verMin[0][1]
    for i in range(len(stock)):
        if producto == stock[i][0]:
            if stock[i][1]>max:
                max = stock[i][1]
            max
    for j in range(len(verMin)):
        if verMin[j][1] < min:
            min = verMin[j][1]
        min
    return (min,max)

def buscarProducto(prod: str, lista:[(str,int)]) -> [(str,int)]:
    res:[(str,int)] = []
    for i in range(len(lista)):
        if prod == lista[i][0]:
            res.append(lista[i])
    return res

"""sc1 = [("galletita", 12),("galletita", 10),("galletita", 1),("hueso",120),("hueso",3),("hueso",10)] #{"galletita":(1,12), "hueso":(3,120)}
print(stock_productos(sc1))
sc2 = [("pato", 12),("pato",0),("pato",13),("collar",300),("collar",20),("collar",17),("comida",100),("comida",29)]
#{"pato":(0,13), "collar":(17,300), "comida": (29,100)}
print(stock_productos(sc2))
sc3 = [("correa", 10),("comida",140),("comida",49),("shampoo",2),("shampoo",39),("shampoo",50)]
#{"correa": (10,10), "comida":(49,140), "shampoo": (2,50)}
print(stock_productos(sc3))"""

#3) no salio
def un_responsable_por_turno(grilla_horaria:[[str]]) -> [(bool,bool)]:
    traspuestas = (trasponerNombres(grilla_horaria))
    res: [(bool,bool)] = []
    dia0: bool = True
    dia1: bool = True
    res: [(bool,bool)] = []
    i:int = 0
    while i< len(traspuestas):
        for j in range(0, len(traspuestas[i])//2) :
            if traspuestas[i][j] != traspuestas[i][j+1]:
                dia0 = False
        dia0
        for k in range(len(traspuestas[i])//2, len(traspuestas[i])-1):
            if traspuestas[i][k] != traspuestas[i][k+1]:
                dia1 = False
        dia1 
        res.append((dia0,dia1))
        i+=1
    return res

def trasponerNombres(nombres: [[str]]) -> [[str]]:
    traspuesta:[[str]] = []
    res = []
    n:int = 0
    while n < len(nombres[0]):
        for i in range(len(nombres)):
            res.append(nombres[i][n])
        traspuesta.append(res)
        res = []
        n+=1
    return  traspuesta
    

"""g1 = [["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["algo", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "algo", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"]]
print(un_responsable_por_turno(g1))"""

#4)
def subsecuencia_mas_larga(mascotas:[str]) -> int:
    longitud:int = 0
    longitudMax: int = 0
    indice:int = 0
    for i in range(len(mascotas)):
        if mascotas[i] == "perro" or mascotas[i] == "gato":
            if longitud == 0:
                indice = i
            longitud+=1
            if longitud > longitudMax:
                longitudMax = longitud
        else:
            longitud = 0
    return indice
    

#res = subsecuencia_mas_larga(["perro","gato","algo","algo","perro","gato","perro"])
#print(res)

# recuperatorio.py 
#1)
def ap_antes_corte(c:str, s:str) -> int:
    total:int = 0
    for i in range(len(s)):
        if c == s[i]:
            if s[i] == "r" :
                total+=1
            elif s[i] == "v":
                total+=1
        elif  s[i] == "x":
                return total
    return total

def verificar_transacciones(s: str) -> int:
    resultado = 350*(ap_antes_corte("r",s)) - 56*(ap_antes_corte("v",s))
    for i in range(1, ap_antes_corte("v",s)):
        if resultado < 0:
            resultado+=56
    return resultado
    
#res = verificar_transacciones("ssrvvrrvvsvvsxrvvv")
#print(res)

#2)
def valor_minimo(s:[(float,float)]) -> float:
    min:float = s[0][0]
    for i in range(len(s)):
        if s[i][0] < min:
            min = s[i][0]
        else:
            min
    return min

#res = valor_minimo([(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)])
#print(res)

#3)
def valores_extremos(cotizaciones_diarias:dict) -> dict:
    dicc = {}
    for clave in cotizaciones_diarias.keys():
        dicc[clave] = buscarMaxMin(clave,cotizaciones_diarias)
    return dicc

def buscarMaxMin(empresa:str, cotizaciones:dict) -> float:
    max:float = 0
    min:float = buscarEmpresa(empresa, cotizaciones)[0][1]
    for nombre in cotizaciones.keys():
        if empresa == nombre:
            for j in range(len(cotizaciones[nombre])):
                if cotizaciones[nombre][j][1] > max:
                    max = cotizaciones[empresa][j][1]
                max
    for nombre in cotizaciones.keys():
        if empresa == nombre:
            for k in range(len(cotizaciones[nombre])):
                if cotizaciones[nombre][k][1] < min:
                    min = cotizaciones[empresa][k][1]
                min
    return (min,max)

def buscarEmpresa(e:str, c:dict) -> [(float,float)]:
    for clave in c.keys():
        if e == clave:
            return c[clave]

#res = valores_extremos({"YPF" : [(1,10),(15, 3),(31,100)], "ALUA" : [(1,0), (20, 50),(31,30)], "MELI" : [(1,40), (5,10),(27, 9)]})
#print(res)

#4)
def es_sudoku_valido(m:[[int]]) -> bool:
    traspuesta = trasponerSodu(m)
    for i in range(len(m)):
        if hayRepetidos(m[i]):
            return False
    for j in range(len(traspuesta)):
        if hayRepetidos(traspuesta[j]):
            return False
    return True

def trasponerSodu(m:[[int]]) -> [[int]]:
    resu:[[int]] = []
    t:[int] = []
    n:int = 0
    while n< len(m):
        for i in range(len(m)):
            t.append(m[i][n])
        resu.append(t)
        t = []
        n+=1
    return resu

def hayRepetidos(lista:[int]) -> bool:
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j] and lista[i] != 0:
                return True
    return False

"""res = es_sudoku_valido([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]])
print(res)"""

##recuperatorio2024_tema1.py
#1)
def gestion_notas(notas_estudiante_materia:[(str,str,int)]) -> dict:
    dicc = {}
    for i in range(len(notas_estudiante_materia)):
        if not(pertenece(notas_estudiante_materia[i][0], list(dicc.keys()))):
            dicc[notas_estudiante_materia[i][0]] = materiaYNota(notas_estudiante_materia[i][0], notas_estudiante_materia)
    return dicc

def materiaYNota(estudiante:str, historial:[(str,str,int)]) -> [(str,int)]:
    resu:[(str,int)] = []
    for i in range(len(historial)):
        if estudiante == historial[i][0]:
            resu.append((historial[i][1],historial[i][2]))
    return resu

#res = gestion_notas([("Pedro", "Geografía", 1), ("Lucía", "Historia", 10)])
#print(res)

#simulacro

def gestion_ventas(ventas_empleado_producto:[(str,str,int)]) -> dict:
    dicc = {}
    for i in range(len(ventas_empleado_producto)):
        if not(pertenece(ventas_empleado_producto[i][0], list(dicc.keys()))):
            dicc[ventas_empleado_producto[i][0]] = productoYCantidad(ventas_empleado_producto[i][0], ventas_empleado_producto)
    return dicc

def productoYCantidad(empleado:str, historial:[(str,str,int)]) -> [(str,int)]:
    resu:[(str,int)] = []
    for i in range(len(historial)):
        if historial[i][0] == empleado:
            resu.append((historial[i][1],historial[i][2]))
    return resu

#res = gestion_ventas([("mica", "pantalon", 2),("salo", "pantalo", 1),("mica", "saco",1),("mica","camisa",3),("salo", "camisa", 2)])
#print(res)




    
    
        