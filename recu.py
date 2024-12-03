from queue import LifoQueue as Pila
from queue import Queue as Cola
#1)
def ind_nesima_aparicion(s:[int], n:int, e:int) -> int:
    apariciones:int = 0
    for i in range(len(s)):
        if s[i] == e:
            apariciones+=1
            if apariciones >= n:
                return i
    return -1

#res = ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3],2,1)
#print(res)

#2)
def frecuencia_posiciones_por_caballo(caballos:[str], carreras:dict) -> dict:
    dicc = {}
    for i in range(len(caballos)):
        dicc[caballos[i]] = posicion(caballos[i], list(carreras.values()))
    return dicc

def posicion(caballo:str, resultados:[[str]]) -> [int]:
    resu:[int] = [0]*len(resultados[0])
    for i in range(len(resultados)):
        for j in range(len(resultados[i])):
            if resultados[i][j] == caballo:
                resu[j]+=1
    return resu

#res = frecuencia_posiciones_por_caballo(["linda", "petisa", "mister", "luck" ],{"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]})
#print(res)

#3)
def alarma_epidemiologica(registros:[(int,str)], infecciosas:[str], umbral:float) -> dict:
    dicc = {}
    for i in range(len(infecciosas)):
        if not(pertenece(infecciosas[i],list(dicc.keys()))) and porcentaje(infecciosas[i], registros) >= umbral:
            dicc[infecciosas[i]] = porcentaje(infecciosas[i], registros)
    return dicc

def porcentaje(enfermedad:str, historial:[(int,str)]) -> float:
    cantidad:int = 0
    for i in range(len(historial)):
        if historial[i][1] == enfermedad:
            cantidad+=1
    return cantidad/len(historial)

#res = alarma_epidemiologica([(3,"al"),(1,"bm"),(6,"ro"),(5,"fo"),(9,"al"),(2,"ro")],["ro","al","bm"],0.2)
#print(res)

#4)
def nivel_de_ocupacion(camas_por_piso:[[bool]]) -> [float]:
    ocupadas:[float] = []
    for i in range(len(camas_por_piso)):
        ocupadas.append(porcentajeOcupadas(camas_por_piso[i]))
    return ocupadas

def porcentajeOcupadas(piso:[bool]) -> float:
    total:int = 0
    for i in range(len(piso)):
        if piso[i] == True:
            total+=1
    porcentaje =  total / len(piso)
    return porcentaje

#res = nivel_de_ocupacion([[True, False, True],[False,True,True],[True,False,False],[True,True,True],[True,True,True],[False,False,False]])
#print(res)

#5)
def empleados_del_mes(horas:dict) -> [int]:
    resu:[int] = []
    valores = list(horas.values())
    max:int = 0
    for i in range(len(valores)):
        if suma(valores[i]) > max:
            max = suma(valores[i])
    for clave in horas.keys():
        if suma(horas[clave]) >= max:
            resu.append(clave)
    return resu

def suma(lista:[int]) -> int:
    total:int = 0
    for i in range(len(lista)):
        total+=lista[i]
    return total

"""horas_trabajadas = {
    1: [8, 9, 7, 8, 10],
    2: [9, 8, 9, 9, 9],
    3: [8, 8, 8, 8, 8],
    4: [10, 10, 10, 10, 10],
    5: [],
    6: [10, 10, 10, 10, 10],
    7: [10,10,10,10,10]
}

print(empleados_del_mes(horas_trabajadas))"""
#6)
def promedio_de_salidas(registro:dict) -> dict:
    dicc = {}
    for clave in registro.keys():
        dicc[clave] = (cantidadSalasSalio(registro[clave]), promedioSalas(registro[clave]))
    return dicc

def cantidadSalasSalio(lista:[int]) -> int:
    total:int = 0
    for i in range(len(lista)):
        if 0<lista[i]<61 :
            total+=1
    return total

def promedioSalas(lista:[int]) -> float:
    promedio:float = 0.0
    sumaSalio:int = 0
    for i in range(len(lista)):
        if 0<lista[i]<61:
            sumaSalio+=lista[i]
    if cantidadSalasSalio(lista)>0:
        promedio = sumaSalio / cantidadSalasSalio(lista)
    return promedio

"""r1 = {"agus": [0,21,3,61], "leo": [34,0,12,61]} #{"agus":(2,12.0), "leo":(2,23.0)}
print(promedio_de_salidas(r1))
r2 = {"agus": [0,21,3,61], "leo": [61,0,61,61]} #{"agus":(2,12.0), "leo":(0,0.0)}
print(promedio_de_salidas(r2))
r3 = {"agus": [0,61,13,12,45,34,12,61], "leo": [35,46,21,31,21,23,25,38,], "ale": [61,61,61,61,61,61,61,61]}
 #{"agus":(5,23.2), "leo":(8,30.0), "ale":(0,0.0)}
print(promedio_de_salidas(r3))
r4 = {"agus": [58,58,58,0,61,58], "leo": [0,0,0,0,61,54], "ale": [14,13,0,61,10,12]}
# #{"agus":(4,58), "leo":(1,54), "ale":(4,12.25)}
print(promedio_de_salidas(r4))"""
#7)
def racha_mas_larga(tiempos:[int]) -> (int,int):
    longitud:int = 0
    longitudMax:int = 0
    indice:int = 0
    indiceMax:int = 0
    indiceIn:int = 0
    for i in range(len(tiempos)):
        if 0<tiempos[i]<61:
            if longitud == 0:
                indice=i
            longitud+=1
            if longitud>longitudMax:
                longitudMax = longitud
                indiceIn = indice
                indiceMax = i
        else:
            longitud = 0
    return (indiceIn,indiceMax)
    

#res = racha_mas_larga([0, 10, 15, 60, 20, 25, 0, 5, 50, 60, 40,40,30,0, 30, 45])
#print(res)

#8)
def escape_en_solitario(amigos_por_salas:[[int]]) -> [int]:
    resu:[int] = []
    for i in range(len(amigos_por_salas)):
        if soloFue3(amigos_por_salas[i]) and amigos_por_salas[i][2]!=0:
            resu.append(i)
    return resu

def soloFue3(sala:[int]) -> bool:
    for i in range(len(sala)):
        if i!=2 and sala[i]!=0 :
            return False
    return True

#9)
def torneo_de_gallinas(estrategias:dict) -> dict:
    dicc = {}
    for clave in estrategias.keys():
        dicc[clave] = puntajeFinal(clave,estrategias)
    return dicc

def puntajeFinal(jugador:str, jugadas:dict) -> int:
    total:int = 0
    for clave in jugadas.keys():
        if clave!=jugador:
            if jugadas[clave] == "me la banco y no me desvío" and jugadas[jugador] == "me la banco y no me desvío":
                total-=5
            elif jugadas[clave] == "me desvío siempre" and jugadas[jugador] == "me desvío siempre":
                total-=10
            elif jugadas[clave] == "me desvío siempre" and jugadas[jugador] == "me la banco y no me desvío":
                total+=10
            elif jugadas[clave] == "me la banco y no me desvío" and jugadas[jugador] == "me desvío siempre":
                total-=15
    return total

#10)
def quien_gano_el_tateti_facilito(tablero:[str]) -> int:
    tableroTraspuesto:[str] = trasponer(tablero)
    for i in range(len(tableroTraspuesto)):
        for j in range(i+1,len(tableroTraspuesto)):
            if cantidad("X",tableroTraspuesto[i]) == len(tablero) and cantidad("O",tableroTraspuesto[j])<len(tablero):
                return 1
            if cantidad("X",tableroTraspuesto[i]) == len(tablero) and cantidad("O",tableroTraspuesto[j]) == len(tablero):
                return 3
    return 0 

def cantidad(ficha:str, jugada:str) -> int:
    mismaJugada:[str] = list(str(jugada))
    total:int = 0
    for i in range(len(mismaJugada)):
        if mismaJugada[i] == ficha:
            total+=1
    return total

def trasponer(jugadas:[str]) -> [str]:
    traspuestas:[str] = []
    palabra=""
    n:int = 0
    while n<len(jugadas):
        for i in range(len(jugadas)):
            palabra+=jugadas[i][n]
        traspuestas.append(palabra)
        palabra=""
        n+=1
    return traspuestas
            
#11)
def cuantos_sufijos_son_palindromos(texto:str) -> int:
    total:int = 0
    listaSufijos:[str] = []
    mismoTexto:[str] = list(str(texto))
    palabra=""
    while mismoTexto!=[]:
        for i in range(len(mismoTexto)):
            palabra+=mismoTexto[i]
        listaSufijos.append(palabra)
        mismoTexto.pop()
        palabra=""
    for i in range(len(listaSufijos)):
        if esPolindromo(listaSufijos[i]):
            total+=1
    return total

def esPolindromo(texto:str) -> bool:
    mismoTexto:[str] = list(str(texto))
    for i in range(len(mismoTexto)):
        if mismoTexto[i] != mismoTexto[len(mismoTexto)-1-i]:
            return False
    return True

#12)
def un_responsable_por_turno(grilla_horaria:[[str]])->[(bool,bool)]:
    grillaTraspuesta = trasponerG(grilla_horaria)
    resu:[(bool,bool)] = []
    for i in range(len(grillaTraspuesta)):
        primero =  todosIguales(primeraMitad(grillaTraspuesta[i]))
        segundo = todosIguales(segundaMitad(grillaTraspuesta[i]))
        tupla = (primero,segundo)
        resu.append(tupla)
    return resu

def todosIguales(lista:[str]) -> bool:
    for i in range(len(lista)-1):
        if lista[i]!=lista[i+1]:
            return False
    return True

def primeraMitad(lista:[str]) -> [str]:
    laMitad:[str] = []
    mitad = len(lista)//2
    for i in range(0,mitad):
        laMitad.append(lista[i])
    return laMitad

def segundaMitad(lista:[str]) -> [str]:
    laMitad:[str] = []
    mitad = len(lista)//2
    for i in range(mitad,len(lista)):
        laMitad.append(lista[i])
    return laMitad

def trasponerG(grilla:[[str]]) -> [[str]]:
    traspuestas:[[str]] = []
    lista:[str] = []
    n:int = 0
    while n<len(grilla[0]):
        for i in range(len(grilla)):
            lista.append(grilla[i][n])
        traspuestas.append(lista)
        lista = []
        n+=1
    return traspuestas

"""g1 = [["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["algo", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "algo", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"]]
print(un_responsable_por_turno(g1))"""

#13)
def stock_productos(stock_cambios:[(str,int)]) -> dict:
    dicc = {}
    for i in range(len(stock_cambios)):
        if not(pertenece(stock_cambios[i][0], list(dicc.keys()))):
            dicc[stock_cambios[i][0]] = minYMax(stock_cambios[i][0],stock_cambios) 
    return dicc

def minYMax(producto:str, cambios:[(str,int)]) -> (int,int):
    max:int = 0
    min:int = buscarProducto(producto,cambios)
    for i in range(len(cambios)):
        if cambios[i][0] == producto:
            if cambios[i][1] > max:
                max = cambios[i][1] 
            max
    for j in range(len(cambios)):
        if cambios[j][0] == producto:
            if cambios[j][1] < min:
                min = cambios[j][1]
            min
    return (min,max)

def pertenece(producto, productos:[str]) -> bool:
    for i in range(len(productos)):
        if producto == productos[i]:
            return True
    return False

def buscarProducto(producto:str, stock:[(str,int)]) -> int:
    for i in range(len(stock)):
        if stock[i][0] == producto:
            return stock[i][1]


#14)
def subsecuencia_mas_larga(tipos_pacientes_atendidos:[str]) -> int:
    indice:int = 0
    longitud:int = 0
    longitudMax:int = 0
    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == "gato" or tipos_pacientes_atendidos[i] == "perro":
            if longitud==0:
                indice = i
            longitud+=1
            if longitud > longitudMax:
                longitudMax = longitud
        else:
            longitud = 0
    return indice

#15)
def valores_extremos(cotizaciones_diarias:dict) -> dict:
    dicc = {}
    for clave in cotizaciones_diarias.keys():
        dicc[clave] = cotizacionMYM(clave, cotizaciones_diarias)
    return dicc

def cotizacionMYM(empresa:str, cotizaciones:dict) -> (float,float):
    min:float = buscarMin(empresa, cotizaciones)
    max:int = 0
    for clave in cotizaciones.keys():
        if empresa == clave:
            for i in range(len(cotizaciones[clave])):
                if cotizaciones[clave][i][1] > max:
                    max = cotizaciones[clave][i][1]
    for otraClave in cotizaciones.keys():
        if empresa == otraClave:
            for j in range(len(cotizaciones[otraClave])):
                if cotizaciones[otraClave][j][1] < min:
                    min = cotizaciones[otraClave][j][1]
    return (min,max)

def buscarMin(nombre:str, historial:dict) -> float:
    for clave in historial.keys():
        if nombre == clave:
            return historial[clave][0][1]


#16)
def es_sudoku_valido(m:[[int]]) -> bool:
    traspuestas = trasponerM(m)
    for i in range(len(m)):
        if not(todosDistintos(m[i])) or not(todosDistintos(traspuestas[i])):
            return False
    return True

def trasponerM(matriz:[[int]]) -> [[int]]:
    traspuestas:[[int]] = []
    lista:[int] = []
    n:int = 0
    while n<len(matriz):
        for i in range(len(matriz)):
            lista.append(matriz[i][n])
        traspuestas.append(lista)
        lista = []
        n+=1
    return traspuestas

def todosDistintos(lista:[int]) -> bool:
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j] and lista[i]!=0:
                return False
    return True

#17)
def gestion_notas(notas_estudiante_materia:[(str,str,int)]) -> dict:
    dicc = {}
    for i in range(len(notas_estudiante_materia)):
        if not(pertenece(notas_estudiante_materia[i][0], list(dicc.keys()))):
            dicc[notas_estudiante_materia[i][0]] = materias(notas_estudiante_materia[i][0],notas_estudiante_materia)
    return dicc

def materias(estudiante:str, historial:[(str,str,int)]) -> [(str,int)]:
    resu:[(str,int)] = []
    for i in range(len(historial)):
        if estudiante == historial[i][0]:
            resu.append((historial[i][1],historial[i][2]))
    return resu 

#18)
def cantidad_digitos_pares(numeros:[int]) -> int:
    mismosNumeros:[int] = []
    contador:int = 0
    for i in range(len(numeros)):
        mismosNumeros+=(str(numeros[i]))
    for j in range(len(mismosNumeros)):
        if int(mismosNumeros[j])%2==0:
            contador+=1
    return contador

#19)
def reordenar_cola_primero_pesados(paquetes:Cola, umbral:int) -> Cola():
    cola = Cola()
    colaAux = Cola()
    colaPesados = Cola()
    ColaMenosPesados = Cola()
    while not paquetes.empty():
        paquete = paquetes.get()
        colaAux.put(paquete)
        if paquete[1]>umbral:
            colaPesados.put(paquete)
        else:
            ColaMenosPesados.put(paquete)
    while not colaAux.empty():
        paquete = colaAux.get()
        paquetes.put(paquete)
    while not colaPesados.empty():
        paquete = colaPesados.get()
        cola.put(paquete)
    while not ColaMenosPesados.empty():
        paquete = ColaMenosPesados.get()
        cola.put(paquete)
    return cola

#20)
def matriz_pseudo_ordenada(matriz:[[int]]) -> bool:
    for i in range(len(matriz)):
        for j in range(i+1,len(matriz)):
            if minimo(matriz[i]) > minimo(matriz[j]):
                return False
    return True

def minimo(lista:[int]) -> int:
    min:int = lista[0]
    for i in range(len(lista)):
        if lista[i]<min:
            min = lista[i]
    return min

#)
def mezclar(s1:[int], s2:[int]) -> [int]:
    resu:[int] = []
    cola1 = Cola()
    cola2 = Cola()
    for i in range(len(s1)):
        cola1.put(s1[i])
    for j in range(len(s2)):
        cola2.put(s2[j])
    while not cola1.empty() and not cola2.empty():
        elemento1 = cola1.get()
        elemento2 = cola2.get()
        resu.append(elemento1)
        resu.append(elemento2)
    return resu

#)
def empleados_del_mes2(horas:dict) -> [int]:
    resu:[int] = []
    max:int = 0
    for clave in horas.keys():
        if suma(horas[clave]) > max:
            max = suma(horas[clave])
    for mismaClave in horas.keys():
        if suma(horas[mismaClave]) == max:
            resu.append(mismaClave)
    return resu

def suma(lista:[int]) -> int:
    total:int = 0
    for i in range(len(lista)):
        total+=lista[i]
    return total


#)
def verificar_transacciones2(s:str) -> int:
    resultado = 350*(ap_antes_corte("r",s)) - 56*(ap_antes_corte("v",s))
    for i in range(1,ap_antes_corte("v",s)):
        if resultado<0:
            resultado+=56
    return resultado

def ap_antes_corte(c:str, s:str) -> int:
    total:int = 0
    for i in range(len(s)):
        if s[i] == c:
            total+=1
        if s[i] == "x":
            return total
    return total


# tateti guia7
def quien_gana_tateti_dificil(m:[str]) -> int:
    traspuestaM = trasponerM(m)
    diagonal = diagonalM(m)
    for i in range(len(traspuestaM)):
        if cantidadd("O",traspuestaM[i]) == len(traspuestaM) or cantidadd("O",diagonal[i]) == (len(diagonal)+1) :
            return 0
        elif cantidadd("X",traspuestaM[i]) == len(traspuestaM) or cantidadd("X",diagonal[i]) == (len(diagonal)+1):
            return 1
    return 2

def cantidadd(c:str, palabra:str) -> int:
    total:int = 0
    for i in range(len(palabra)):
        if palabra[i] == c :
            total+=1
    return total

def trasponerM(caracteres:[str]) -> [str]:
    traspuestas:[str] = []
    palabra=""
    n:int = 0
    while n<len(caracteres):
        for i in range(len(caracteres)):
            palabra+=caracteres[i][n]
        traspuestas.append(palabra)
        palabra=""
        n+=1
    return traspuestas

def diagonalM(caracteres:[str]) -> [str]:
    diagonales:[str] = []
    palabra=""
    n:int = 0
    while n< len(caracteres):
        for i in range(len(caracteres)):
            palabra+=caracteres[i][n]
            n+=1
        diagonales.append(palabra)
        palabra=""
    n = 2
    while n>=0:
        for j in range(len(caracteres)):
            palabra+=caracteres[j][n]
            n-=1
        diagonales.append(palabra)
    return diagonales


#####################
#21)
def subsecuencia_mas_larga(v:[int]) -> (int,int):
    longitud:int = 0
    longitudMax:int = 0
    indice:int = 0
    indiceIn:int = 0
    indiceMax:int = 0
    for i in range(len(v)-1):
        if abs(v[i] - v[i+1]) == 1:
            if longitud ==0:
                indice=i
            longitud+=1
            if longitud > longitudMax:
                longitudMax = longitud
                indiceIn = indice
                indiceMax = i
        else:
            longitud = 0
    return (longitudMax +1,indiceIn)

#res = subsecuencia_mas_larga([1,2,3,4,8,7,6,3,2,1,1,2,3,4,5,6])
#print(res)

#22)
def mejor_resultado_de_ana(examenes:Cola) -> [int]:
    resu:[int] = []
    colaAux = Cola()
    while not examenes.empty():
        examen = examenes.get()
        colaAux.put(examen)
        if cantidadBool(True,examen) == len(examen)//2 and cantidadBool(False,examen) == len(examen)//2:
            resu.append(len(examen))
        if cantidadBool(True,examen) > len(examen)//2 and cantidadBool(False,examen) < len(examen)//2:
            resu.append(len(examen)//2 + cantidadBool(False,examen))
        if cantidadBool(True,examen) < len(examen)//2 and cantidadBool(False,examen) > len(examen)//2:
            resu.append(len(examen)//2 + cantidadBool(True,examen))
    while not colaAux.empty():
        examen = colaAux.get()
        examenes.put(examen)
    return resu

def cantidadBool(b:bool, lista:[bool]) -> int:
    total:int = 0
    for i in range(len(lista)):
        if lista[i] == b :
            total+=1
    return total

#23)
def cambiar_matriz(A:[[int]]):
    maximoElemento = len(A) * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] % maximoElemento + 1

#24)
def palabras_por_vocales(texto:str) -> dict:
    dicc = {}
    mismoTexto:[str] = sinEspacios(texto)
    for i in range(len(mismoTexto)):
        if cantidadVocales(mismoTexto[i]) not in list(dicc.keys()):
            dicc[cantidadVocales(mismoTexto[i])] = cuantasPalabras(cantidadVocales(mismoTexto[i]),mismoTexto)
    return dicc

def sinEspacios(texto:str) -> [str]:
    palabras:[str] = []
    sinEspacio:[str] = []
    palabra:str=""
    for i in range(len(texto)):
        if texto[i]!=" " and texto[i]!="\n":
            palabra+=(texto[i])
        else:
            palabras.append(palabra)
            palabra=""
    palabras.append(palabra)
    for j in range(len(palabras)):
        if palabras[j]!="":
            sinEspacio.append(palabras[j])
    return sinEspacio

def cantidadVocales(palabra:str) -> int:
    total:int = 0
    for i in range(len(palabra)):
        if palabra[i] == 'a' or palabra[i] == 'e' or palabra[i] == 'i' or palabra[i] == 'o' or palabra[i] == 'u' or palabra[i] == 'A' or palabra[i] == 'E' or palabra[i] == 'I' or palabra[i] == 'O' or palabra[i] == 'U':
            total+=1
    return total 

def cuantasPalabras(n:int, palabras:[str]) -> int:
    total:int = 0
    for i in range(len(palabras)):
        if cantidadVocales(palabras[i]) == n:
            total+=1
    return total

######################
#25)
def multiplos_de_primos(v:[int]) -> dict:
    dicc = {}
    for i in range(len(v)):
        if esPrimo(v[i]) and not(pertenece(v[i], list(dicc.keys()))):
            dicc[v[i]] = cantidadDivisores(v[i],v)
    return dicc

def esPrimo(n:int) -> bool:
    if n==1:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n%2==0 or  n%3==0 or  n%5==0 or  n%7==0:
        return False
    return True 

def cantidadDivisores(n:int , lista:[int]) -> int:
    total:int = 0
    for i in range(len(lista)):
        if lista[i]%n==0:
            total+=1
    return total

#26)
def longitud_mas_grande(A:[[int]]) -> int:
    longitudMax:int = 0
    for i in range(len(A)):
        if longitudUnosMax(A[i]) > longitudMax:
            longitudMax = longitudUnosMax(A[i])
        else:
            longitudMax
    return longitudMax

def longitudUnosMax(lista:[int]) -> int:
    longitud:int = 0
    longitudMax:int = 0
    indice:int = 0
    for i in range(len(lista)):
        if lista[i] == 1:
            if longitud==0:
                indice=i
            longitud+=1
            if longitud > longitudMax:
                longitudMax = longitud
        else:
            longitud = 0
    return longitudMax

#27)
def dame_el_que_falta(s:[(int,int)]) -> (int,int):
    listaCompleta:[(int,int)] = []
    for i in range(len(s)):
        if not(perteneceTupla(s[i],listaCompleta)):
            listaCompleta.append(s[i])
        if not(perteneceTupla(darVuelta(s[i]), listaCompleta)):
            listaCompleta.append(darVuelta(s[i]))
        if not(perteneceTupla((s[i][0],s[i][0]), listaCompleta)):
            listaCompleta.append((s[i][0],s[i][0]))
        if not(perteneceTupla((s[i][1],s[i][1]), listaCompleta)):
            listaCompleta.append((s[i][1],s[i][1]))
    for j in range(len(listaCompleta)):
        if not(perteneceTupla(listaCompleta[j],s)):
            return listaCompleta[j]

def darVuelta(tupla:(int,int)) -> (int,int):
    return (tupla[1],tupla[0])

def perteneceTupla(tupla:(int,int), lista:[(int,int)]) -> bool:
    for i in range(len(lista)):
        if lista[i] == tupla:
            return True
    return False



