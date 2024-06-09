#1))
def ultima_aparicion(s:[int],e:int)->int:
    for i in range(0,len(s)):
        if e==s[(len(s)-1)-i]:
            return (len(s)-1)-i
        
#2))
def elementos_exclusivos(s:[int],t:[int])-> [int]:
    res=[]
    syt:list= s+t
    for elemento in syt:
        if not perteneceAAmbos(elemento,s,t):
            if not pertenece(elemento,res):
                res.append(elemento)
    return res

def pertenece(n:int,s:[int])->bool:
    for i in range(0,len(s)):
        if n==s[i]:
            return True
    return False
    
def perteneceAAmbos(elemento:int,l:[int],m:[int])->bool:
    return pertenece(elemento,l) and pertenece(elemento,m)

#3)
def contar_traducciones_iguales(ing:dict,alem:dict)->int:
    contador=0
    for palabra in ing.keys():
        if pertenece(palabra,alem.keys()) and ing[palabra]==alem[palabra]:
            contador+=1
    return contador 

#4)
def cantidad_de_apariciones(n:int,s:list)->int:
    contador=0
    for i in range(0,len(s)):
        if n==s[i]:
            contador+=1
    return contador 

def convertir_a_dic(lista:[int])->dict:
    res={}
    for numero in lista:
        res[numero]=cantidad_de_apariciones(numero,lista)
    return res


#parcial
#1
def acomodar(s:[str])->[str]:
    res=[]
    for boleta in s:
        if boleta=="UP":
            res.append(boleta)
    for boleta in s:
        if boleta=="LLA":
            res.append(boleta)
    return res 


#2
def pos_umbral2(s:[int],u:int)->int:
    for i in range(0,len(s)):
        if i<u:
            if s[i]>=u:
                return i
    return -1

#3
def columnas_repetidas(mat:[[int]])->bool:
    res=True
    for columna in mat:
        if not columna_simetrica(columna):
            return False
    return res 

def columna_simetrica(s:[int])->bool:
    primera_mitad=[]
    segunda_mitad=[]
    for i in range(0,len(s)//2):
        primera_mitad.append(s[i])
    for j in range(len(s)//2,len(s)):
        segunda_mitad.append(s[j])

    return  primera_mitad==segunda_mitad

#4 
def cuenta_pos_por_nacion(naciones:[str],torneos:dict)->dict:
    res={}
    for nacion in naciones:
        res[nacion]=[0]*len(naciones)
    for ano in torneos.keys():
        for i in range(len(torneos[ano])):
            res[torneos[ano][i]][i]+=1
    return res