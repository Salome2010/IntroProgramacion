#1)
def pertenece(s:[int],e:int) -> bool:
    i:int=0
    while (i<len(s)):
        if e==s[i]:
            return True
        i+=1
    return False
    
    """for i in range(0,len(s),1):
        if e==s[i]:
            return True
    return False"""

 
#res = pertenece([1,2,3,4],3)
#print(res)

def divide_a_todos(s:[int],e:int)->bool:
    i:int=0
    while(i<len(s)):
        if (s[i]%e!=0):
            return False
        i+=1
    return True

    """for i in range(len(s)):
        if(s[i]%e!=0):
            return False
    return True"""
    
#res= divide_a_todos([4,2,4,4],4)
#print(res)

def suma_total(s:[int]) -> int:
    suma:int=0
    i:int=0
    while(i<len(s)):
        suma+=s[i]
        i+=1
    return suma

    """suma:int=0
    for i in range(len(s)):
        suma+=s[i]
    return suma"""

#res= suma_total([1,3,4,5])
#print(res)

def maximo(s:[int]) -> int:
    i:int=0
    max:int=0
    while(i<len(s)):
        if(s[i]>=max):
            max=s[i]
        max
        i+=1
    return max

    """max:int=0
    for i in range(len(s)):
        if(s[i]>=max):
            max=s[i]
        max
    return max"""

#res= maximo([20,3,2,4,6,12,0,15,50])
#print(res)

def minimo(s:[int]) -> int:
    min:int=s[0]
    i:int=0
    while(i<len(s)):
        if(s[i]<=min):
            min=s[i]
        min
        i+=1
    return min

#res = minimo([7,2,1,6,5])
#print(res)

def ordenados(s:[int]) -> bool:
    i:int=0
    while(i<(len(s)-1)):
        if(s[i]>s[i+1]):
            return False
        i+=1
    return True

    """for i in range(len(s)-1):
        if(s[i]>s[i+1]):
            return False
    return True"""

#res= ordenados([3,5,2,7])
#print(res)

def pos_maximo(s:[int]) -> int: #pos_minimo se hace igual
    if len(s) == 0:
        return -1
    max = s[0]  # Asumimos que el primer elemento es el mayor inicialmente
    pos = 0  # Posición del mayor
    for i in range(len(s)):
        if s[i] > max:
            max = s[i]  # Actualizamos el mayor encontrado
            pos = i  # Actualizamos la posición del mayor
    return pos
    
#res = pos_maximo([5,7,2,7,8,8])
#print(res)

def lista_palabras(s:[str]) -> bool:
    for palabra in s:
        if(len(palabra)>7):
            return True
    return False

#res = lista_palabras(["salo","mica","y","sa"])
#print(res)

def palindromo(palabra:str) -> bool: #IMPPPPPP
    mitad=len(palabra)//2
    for i in range(mitad):
        if (palabra[i] != palabra[len(palabra)-1 - i]):
            return False
    return True
             
#res= palindromo("abshsba")
#print(res) 

def recorrer(s:[int])-> bool:
    for i in range(len(s)-2):
        if(s[i]==s[i+1]==s[i+2]):
            return True
    return False

#res = recorrer([1,5,5,2,2,2])
#print(res)

def vocales_dist(palabra:str)-> bool:
    contador:int=0
    for letra in palabra:
        if (letra=="a" or letra=="A" or letra=="e" or letra=="E" or letra=="i" or letra=="I" or letra=="o" or letra=="O" or letra=="u" or letra=="U"):
            contador+=1
    return contador>=3

#res = vocales_dist("ebigga") 
#print(res)

#def

def cantidad_digitos_impares(numeros:[int])-> int:
    contador:int=0
    lista:[int]=[]
    for numero in numeros:
        if numero==0:
            contador+=1
    for numero in numeros:
        lista+=(str(numero))
    for num in lista:
        if(int(num)%2!=0):
            contador+=1
    return contador
        
#res = cantidad_digitos_impares([57, 2383, 812, 246,0])
#print(res)

#2)

def ceroEnPosPares(s:[int]):
    i:int=0
    while(i<len(s)):
        if(i%2==0):
            s[i]=0
        i+=1
    return s

#res= ceroEnPosPares([1,2,3,4])
#print(res)

def ceroEnPosPares2(s:[int]) -> [int]:
    lista:[int] = []
    i:int=0
    while(i<len(s)):
        if(i%2==0):
            lista.append(0)
        else:
            lista.append(s[i])
        i+=1
    return lista

#res= ceroEnPosPares2([1,2,3,4])
#print(res)

def cadenaSinVocales(palabra:str) -> str:
    nuevo:str=""
    for letra in palabra:
        if(letra!='a' and letra!="A" and letra!="e" and letra!="E" and letra!="i" and letra!="I" and letra!="o" and letra!="O" and letra!="U" and letra!="u" ):
            nuevo+=letra
    return nuevo

#res = cadenaSinVocales("adfio")
#print(res)

def remplaza_vocales(s:str) -> str:
    nuevo:str=""
    for letra in s:
        if(letra!='a' and letra!="A" and letra!="e" and letra!="E" and letra!="i" and letra!="I" and letra!="o" and letra!="O" and letra!="U" and letra!="u" ):
            nuevo+=letra
        else:
            nuevo+=" "
    return nuevo

#res= remplaza_vocales("adfoji")
#print(res)

def dar_vuelta_str(s:str) -> str: 
    vuelta:str=""
    for i in range(len(s)):
        vuelta+=s[len(s)-i-1]
    return vuelta

#res = dar_vuelta_str("asdf")
#print(res)

def eliminar_repetidos(s:str) -> str:
    sinRep:str=""
    for letra in s:
        if(letra not in sinRep):
            sinRep+=letra
    return sinRep

#res = eliminar_repetidos("aasfdfs")
#print(res)

def resultadoMaterias(notas:[int]) -> int:
    if notasMayoresA4(notas) and promedio(notas)>=7:
        return 1
    if notasMayoresA4(notas) and 4<=promedio(notas)<7:
        return 2
    if not(notasMayoresA4(notas)) or promedio(notas)>=7:
        return 3

def notasMayoresA4(notas:[int]) -> bool:
    for nota in notas:
        if nota<4:
            return False
    return True

def promedio(notas:[int]) -> int:
    suma:int=0
    cantNotas:int=0
    for nota in notas:
        suma+=nota
        cantNotas+=1
    promedio:int= (suma//cantNotas)
    return promedio 

#res =  resultadoMaterias([4,5,8])
#print(res)

def saldoPorHistorial(hist:[(str,int)]) -> int:
    saldoFin:int=0
    for operacion in hist:
        if operacion[0]=="I":
            saldoFin+=operacion[1]
        if operacion[0]=="R":
            saldoFin-=operacion[1]
    return saldoFin

#res = saldoPorHistorial([("I",200),("R",100),("I",500)])
#print("el saldo final es: " + str(res))

#3)
def pertenece_a_cada_uno_version_1(s:[[int]], e:int,resu:[bool]):
    resu:[bool]=[]
    for lista in s:
        if pertenece(lista,e):
            resu.append(True)
        resu.append(False)
    return resu
   
#res = pertenece_a_cada_uno_version_1([[1,2,3],[2,3,4],[5,7,8],[5],[]],5,[])
#print(res)

#def 

def pertenece_a_cada_uno_version_3(s:[[int]], e:int) -> [bool]:
    resu:[bool]=[]
    for lista in s:
        if not(pertenece(lista,e)):
            resu.append(False)
        else:
            resu.append(True)
    return resu

#res = pertenece_a_cada_uno_version_3([[1,2,3],[2,3,4],[5,7,8],[5],[]],5)
#print(res)   

def es_matriz(matriz:[[int]])-> bool:
    if (len(matriz)>0 and len(matriz[0])>0 and todasFilasMismasLong(matriz)):
        return True
    return False 

def todasFilasMismasLong(matriz:[[int]])-> bool:
    i:int=0
    primeraFila:int=matriz[0]
    while(i<len(matriz)):
        if(len(matriz[i])!=len(primeraFila)):
            return False
        i+=1
    return True

#res = es_matriz([[1,2,3],[2,3,4],[],[2,3,5]])
#print(res)

def filas_ordenadas(m:[[int]],resu:[bool]):
    resu:[bool]=[]
    for fila in m:
        if (ordenados(fila)):
            resu.append(True)
        else:
            resu.append(False)
    return resu 

#res = filas_ordenadas([[1,2,3],[3,4,5],[2,2,2],[1,4,1]],[])
#print(res)

def columna(m:[[int]],c:int) -> [int]:
    for i in range(len(m)):
        if (i==c):
            return m[i]

#res = columna([[1,2,3],[2,4,5],[4,7]],2)
#print(res)

def columnas_ordenadas(m:[[int]])-> [bool]:
    resu:[bool]=[]
    for i in range(len(m)):
        if ordenados(columna(m,i)):
            resu.append(True)
        else:
            resu.append(False)
    return resu

#res = columnas_ordenadas([[1,2,3],[2,4,5],[4,7]])
#print(res)

def trasponer(m:[[int]])-> [[int]]: #IMPP
    resu:[[int]]=[]
    for i in range(len(m[0])):
        poner:[int]=[]
        for j in range(len(m)):
            poner.append(m[j][i])
        resu.append(poner)
    return resu

#res = trasponer([[1,2,3],[1,2,3],[1,2,3]])
#print(res)

def quien_gana_tateti(m:[str])-> int: #MUY DIF
    i:int=0
    #HORIZONTAL
    for fila in m:
        if (contarXO(fila)[0][0])==3:
            return 1
        if (contarXO(fila)[0][1])==3:
            return 0
    #VERTICAL
    while(i<len(m)):
        if contarXO(trasponer(m)[i])[0][0]==3:
            return 1
        i+=1
    k:int=0
    while(k<len(m)):
        if contarXO(trasponer(m)[k])[0][1]==3:
            return 0
        k+=1
    #DIAGONAL
    if mitad(m)[0]==mitad(m)[l]==mitad(m)[2]=="X":
        return 1
    if mitad(m)[0]==mitad(m)[l]==mitad(m)[2]=="O":
            return 0
    #NO CUMPLE NINGUNO    
    return 2


def contarXO(m:str)-> [int]:
    contadorx=0
    contadoro=0
    contador=[]
    for caracter in m:
        if caracter=="X":
            contadorx+=1  # Contar "X" en la fila
        else:
            contadoro+=1   # Contar "O" en la fila
    contador.append((contadorx, contadoro))
    return contador
    
def mitad(m:[[int]])-> [int]: #IMPP
    resu:[int]=[]
    for j in range(len(m)):
        resu.append(m[j][1])
    return resu


#res = quien_gana_tateti(["XOX","XOO","XXO"])
#print(res)