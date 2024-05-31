# ej 1
def contar_lineas(nombre_archivo:str)->int:
    archivo = open (nombre_archivo,"r") #abre el archivo en modo lectura
    totalLineas:int=0
    for linea in archivo.readlines(): #readLines() lee las lineas del archivo
        totalLineas+=1
    archivo.close() #salir del archivo
    return totalLineas


def existe_palabra( palabra : str,  nombre_archivo : str) -> bool:
    res=False
    archivo=open(nombre_archivo,"r")
    for linea in archivo.readlines():
        if palabra in linea:
            return True
    archivo.close()
    return res 

def cantidad_apariciones(nombre_archivo:str,palabra:str)->int:
    totalApariciones:int=0
    archivo=open(nombre_archivo,'r')
    contenidoDelArchivo=archivo.read() # lee el contenido 
    palabrasDelArchivo=contenidoDelArchivo.split() #divide el contenido de un archivo de texto en palabras individuales y las guarda en una lista
    for palabraDelArchivo in palabrasDelArchivo: #se fija cada palabra del archivo en el contenido del archivo 
        if palabra==palabraDelArchivo:
            totalApariciones+=1
    archivo.close()
    return totalApariciones

#2
def clonar_sin_comentarios(nombre_archivo : str):
    archivo=open(nombre_archivo,"r")
    archivo_sin_comentarios=open("archivoClonado.py","w")
    for linea in archivo.readlines():
        if not linea.strip()[0]=="#": # strip() separaba palabra por palabra => linea.strip()[0] es la primera palabra de la linea
            archivo_sin_comentarios.write(linea)
    archivo.close()
    archivo_sin_comentarios.close()

# 3
def invertir_lineas(nombre_archivo:str):
    archivo=open(nombre_archivo,"r")
    archivo_reverso=open("reverso.txt","w")
    for linea in archivo.readlines()[::-1]: # el [::-1] indica que comienza desde la ultima linea de archivo
        archivo_reverso.write(linea)
    archivo.close()
    archivo_reverso.close()

# 4
def agregar_frase_al_final(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"a") # el archivo se abre en modo escritura pero para escribir al final del archivo (eso hace "a")
    archivo.write(frase)
    archivo.close()

#5 
def agregar_frase_principio(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,'r+') # abre el archivo en modo lectura y escritura
    contenido = archivo.read()
    archivo.seek(0,0) # posiciona el cursor al principio del archivo 
    archivo.write(frase.rstrip('\r\n') + '\n' + contenido) # frase.rstrip('\r\n') ej: si la frase es "hola mundo\n" entonces agrega solo "hola mundo" luego otro salto de linea y luego el contenido que ya habia en el archivo
    archivo.close()

# ej 6

# ej 7 INC.
def promedioEstudiante(lu:str)->float:
    archivo=open('notas.csv','r')
    contador:int=0
    notaAcumulada:int=0
    for linea in archivo.readlines():
        datos=linea.split(",")
        if datos[0]==lu:
            contador+=1
            notaAcumulada+=int(datos[3])

    archivo.close()
    promedio:float = notaAcumulada/contador
    return promedio

# inc def calcular_promedio_por_estudiante(nombre_archivo_notas : str):
    archivos_promedio=open("promedios.csv","w")
    archivos_promedio.write(promedioEstudiante)
    archivos_promedio.close()

# pila
# 8
from queue import LifoQueue as Pila
import random

def generar_nros_al_azar(n:int,desde:int,hasta:int)->Pila:
    pila= Pila()
    for i in range(0,n):
        pila.put(random.randint(desde,hasta)) # pila.put apila los 5 numeros que encontro desde-hasta 
    return pila

# ej 9 no entendi
def cantidad_elementos(p:Pila)->int:
    contenido=[]
    contador:int=0
    while not p.empty():
        contenido.append(p.get()) # agrega a contenido el elemento mas reciente agregado a p 
        contador+=1
    for elemento in contenido[::-1]: # debe empezar desde el ultimo 
        p.put(elemento)
    return contador




# 10

def buscar_el_maximo(p:Pila)->int:
    maximo:int=p.get() #Inicializamos la variable maximo con el primer elemento de la pila usando p.get()
    while not p.empty: 
        nuevo_elemento=p.get()
        if nuevo_elemento > maximo:
            maximo=nuevo_elemento
    return maximo 

# 11 no entendi bien 
def esta_bien_balanceada(s:str)->bool:
    res:bool=True
    p=Pila()
    parentesis_abiertos:int=0
    for letra in s[::-1]: # recorre s de atras hacia delante 
        p.put(letra) #Para cada carácter letra en la cadena s (en orden inverso), 
                     #se coloca ese carácter en la pila p utilizando el método put() de la pila. 
                     #Esto significa que los caracteres se apilan en orden inverso en la pila
    while not p.empty():
        letra_sacada=p.get()
        if letra_sacada=="(":
            parentesis_abiertos+=1
        if letra_sacada==")":
            parentesis_abiertos-=1
        if parentesis_abiertos<0:
            res=False
    if parentesis_abiertos>0:
        res=False
    return res

#12 

# COLAS
# 13
from queue import Queue as Cola
def generar_nros_al_azar_cola(n:int,desde:int,hasta:int)->Cola:
    c=Cola()
    p:Pila=generar_nros_al_azar(n,desde,hasta)
    for i in range (0,n):
        c.put(p.get()) #Agrega elementos a la cola utilizando el método put(), 
                       #obtenidos de la pila p utilizando el método get().
    return c


#14
def cantidad_elementos(c:Cola)->int:
    contenido=[]
    contador:int=0
    while not c.empty():
        contenido.append(c.get())
        contador+=1
    for elemento in contenido:
        c.put(elemento)
    return contador

#15
def buscar_el_maximo(c:Cola)->int:
    maximo:int=c.get()
    while not c.empty():
        nuevo_elemento=c.get()
        if nuevo_elemento > maximo:
            maximo=nuevo_elemento
    return maximo

"""c=Cola()
c.put(9)
c.put(2)
c.put(7)
c.put(10)
print(buscar_el_maximo(c))"""

#16 




# dic
#19
def agrupar_por_longitud(nombre_archivo:str)->dict:
    archivo=open(nombre_archivo,'r',encoding='utf8')
    res:dict[int]={}
    for linea in archivo.readlines():
        palabras=linea.split()
        for palabra in palabras:
            longitud=len(palabra)
            if longitud in res:
                res[longitud]+=1
            else:
                res[longitud]=1
    archivo.close()
    return res








