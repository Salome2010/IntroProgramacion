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
    cantNotas:int=0
    sumaNotas:int=0
    for linea in archivo.readlines():
        datos=linea.split(",")
        if datos[0]==lu:
            cantNotas+=1
            sumaNotas+=int(datos[3])

    archivo.close()
    promedio:float = sumaNotas/cantNotas
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

"""resultado = generar_nros_al_azar(5, 1, 10)
print("Números generados al azar:")
while not resultado.empty():
    print(resultado.get())""" 

# ej 9 
def cantidad_elementos(p:Pila)->int:
    contenido1=Pila()
    contador:int=0
    while not p.empty():
        elemento=p.get()
        contenido1.put(elemento) # agrega a contenido elemento de p 
        contador+=1
    while not contenido1.empty():
        elemento=contenido1.get()
        p.put(elemento)
    return contador

"""p=Pila()
p.put(1)
p.put(2)
p.put(3)
print(cantidad_elementos(p))
#Esto para chequear que la pila sigue igual que al principio
while not p.empty():
    print(p.get())"""

# 10

def buscar_el_maximo(p:Pila)->int:
    maximo:int=p.get() #Inicializamos la variable maximo con el primer elemento de la pila usando p.get()
    while not p.empty(): 
        nuevo_elemento=p.get()
        if nuevo_elemento > maximo:
            maximo=nuevo_elemento
    return maximo 
"""p=Pila()
p.put(1)
p.put(7)
p.put(5)
print(buscar_el_maximo(p))"""


# 11 
def esta_bien_balanceada(s:str)->bool:
    res:bool=True
    p=Pila()
    p_aux=Pila()
    parentesis_abiertos:int=0
    for letra in s: 
        p_aux.put(letra) 
    while not p_aux.empty():
        letra=p_aux.get()
        p.put(letra)
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

"""print(
esta_bien_balanceada("3*(1x2)-(5-4)"),
esta_bien_balanceada("7((2x7)"),
esta_bien_balanceada("8*(9/3))")
)"""


#12 

# COLAS
# 13
from queue import Queue as Cola
def generar_nros_al_azar_cola(n:int,desde:int,hasta:int)->Cola:
    c=Cola()
    for i in range (0,n):
        c.put(random.randint(desde,hasta)) #Agrega elementos a la cola utilizando el método put(), 
                       #obtenidos de la pila p utilizando el método get().
    return c

"""c:Cola=generar_nros_al_azar_cola(5,1,10)
while not c.empty():
    print(c.get())"""



#14
def cantidad_elementos_cola(c:Cola)->int:
    c_aux=Cola()
    totalElementos=0
    while not c.empty():
        c_aux.put(c.get())
        totalElementos+=1
    while not c_aux.empty():
            c.put(c_aux.get())
    return totalElementos 

"""c=Cola()
c.put(1)
c.put(2)
c.put(5)
print(cantidad_elementos_cola(c))
while not c.empty():
    print(c.get())"""


#15
def buscar_el_maximo(c:Cola)->int:
    maximo=c.get()
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

#16 mal inc
def armar_sec_bingo()->Cola:
    c=Cola()
    lista=list(range(1,100))
    for elemento in lista:
        c.put(elemento)
    return c 

#17 
def n_pacientes_urgentes(c:Cola([int,str,str]))-> int:
    contador=0
    cola_aux=Cola()
    while not c.empty():
        paciente:[int,str,str]=c.get()
        cola_aux.put(paciente)
        if paciente[0] in [1,2,3]:
            contador+=1
    while not cola_aux.empty():
        paciente:[int,str,str]=cola_aux.get()
        c.put(paciente)
    return contador 

"""c=Cola()
c.put((1,'Jorge','ahi anda'))
c.put((1,'Maria','esta jodida'))
c.put((5,'Alejandro','blabla'))
c.put((4,'Martin','Anda bien dentro de todo'))
print(n_pacientes_urgentes(c))
while not c.empty():
    print(c.get())"""

#18
def atencion_a_clientes(c:Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
    cola_prioritaria:[(str,int,bool,bool)]=Cola()
    cola_preferencial:[(str,int,bool,bool)]=Cola()
    cola_resto:[(str,int,bool,bool)]=Cola()
    cola_aux:[(str,int,bool,bool)]=Cola()
    cola_ordenada:[(str,int,bool,bool)]=Cola()
    while not c.empty():
        cliente:[(str,int,bool,bool)]=c.get()
        cola_aux.put(cliente)
        if cliente[3]:
            cola_prioritaria.put(cliente)
        elif cliente[2]:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)
    while not cola_aux.empty():
        cliente:[(str,int,bool,bool)]=cola_aux.get()
        c.put(cliente)
    while not cola_prioritaria.empty():
        cola_ordenada.put(cola_prioritaria.get())
    while not cola_preferencial.empty():
        cola_ordenada.put(cola_preferencial.get())
    while not cola_resto.empty():
        cola_ordenada.put(cola_resto.get())

    return cola_ordenada

"""c=Cola()
c.put(('Jorge',19391293,False,False))
c.put(('Andrea',11523351,True,False))
c.put(('Adelina',7976723,False,True))
c.put(('Roberto',12452413,True,False))
cola_ordenada=atencion_a_clientes(c)
while not cola_ordenada.empty():
    print(cola_ordenada.get())"""




# dic
#19
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo=open(nombre_archivo, 'r', encoding='utf8')
    res={}
    for linea in archivo.readlines():
        palabra = ""
        for caracter in linea:
            if caracter != " " and caracter != "\n":
                palabra += caracter
            else:
                if palabra:  # Verifica si hay una palabra almacenada
                     res[len(palabra)] = res.get(len(palabra), 0) + 1
                     palabra=""
                     
    archivo.close()               
    return res


#*Ejercicio 20
def promedio_alumnos()->dict:
    archivo=open('notas.csv','r')
    promedios:dict={}
    for linea in archivo.readlines():
        data=linea.rstrip('\n').split(',')
        lu:str=data[0]
        #Si el alumno no esta en el diccionario de promedios, calculo su promedio y lo añado
        if lu not in promedios:
            promedios[lu]=promedioEstudiante(lu)

    archivo.close()
    return promedios










