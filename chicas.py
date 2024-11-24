"""def torneo_gallinas(estrategias:dict) -> dict:
    dicc = {}
    listaValores:[str] = []
    for clave1 in estrategias.keys():
        listaValores.append(estrategias[clave1])
    for clave in estrategias.keys():
        dicc[clave] = quePaso(dicc[clave], listaValores)
    return dicc

def quePaso(valor:str, lista:[str]) -> int:
    totalFinal:int = 0
    for i in range(len(lista)):"""

def quien_gano_el_tateti_facilito(tablero:[str]) -> int:
    traspuestas:[str]= []
    for i in range(len(tablero)):
        traspuestas.append(trasponer(tablero[i]))
    for j in range(len(traspuestas)):
        if contadorX(traspuestas[j]) == len(traspuestas[j]) and contadorO(traspuestas[j+1]) == len(traspuestas[j+1]):
            return 3
        elif contadorX(traspuestas[j]) == len(traspuestas[j]) and not(contadorO(traspuestas[j+1]) == len(traspuestas[j+1])):
            return 1
    return 0


def trasponer(m:[str])-> [str]: #IMPP
    resu:[str]=[]
    for i in range(len(m[0])-1):
        poner:[int]=[]
        for j in range(len(m)):
            poner.append(m[j][i])
        resu.append(poner)
    return resu


def contadorX(traspuest:str) -> int:
    contador:int = 0
    for i in range(len(traspuest)):
        if traspuest[i] == "X":
            contador+=1
    return contador

def contadorO(traspuest:str) -> int:
    contador:int = 0
    for i in range(len(traspuest)):
        if traspuest[i] == "O":
            contador+=1
    return contador


res =  quien_gano_el_tateti_facilito([["","O","O","O","X"],["O","O","","X",""],["O","O","X","X","O"],["O","O","","X",""]])
print(res)
    




        
    