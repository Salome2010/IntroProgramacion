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








    
