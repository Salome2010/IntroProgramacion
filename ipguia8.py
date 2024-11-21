#pila
from queue import LifoQueue as Pila
from queue import Queue as Cola
#1)

def generar_n_al_azar(cantidad:int,desde:int,hasta:int) -> Pila:
    pila= Pila()
    comienzo:int = desde
    for i in range(0,cantidad):
        pila.put(comienzo)
        comienzo+=1 
    return pila

"""res = generar_n_al_azar(2, 1, 3)
#print(res.queue) #ver como es la pila (no hacer en parical)
print("Números generados al azar:")
while not res.empty():
    print(res.get())"""

#2)
def cantidad_de_elementos(p:Pila) -> int:
    contador:int=0
    nuevaP = Pila()
    while not p.empty():
        elemento=p.get()
        nuevaP.put(elemento)
        contador+=1
    while not nuevaP.empty():
        elemento=nuevaP.get()
        p.put(elemento)
    return contador

"""p= Pila()
p.put(1)
p.put(2)
p.put(3)
print(cantidad_de_elementos(p))
while not p.empty(): # ver si p tiene el mismo orden original 
    print(p.get()) """

#3) 
def buscar_el_maximo(p:Pila) -> int:
    maximo:int = 0
    nuevaP = Pila()
    while not p.empty():
        elemento=p.get()
        nuevaP.put(elemento)
        if elemento>=maximo:
            maximo=elemento
        maximo
    while not nuevaP.empty():
        elemento=nuevaP.get()
        p.put(elemento)
    return maximo 

"""p = Pila()
p.put(1)
p.put(8)
p.put(10)
p.put(5)
print(buscar_el_maximo(p))
while not p.empty():
    print(p.get())"""

#4)
def buscar_nota_maxima(p:Pila) -> [str,int]:
    maximo:[str,int]=(None,0)
    nuevaPila = Pila()
    while not p.empty():
        elemento=p.get()
        nuevaPila.put(elemento)
        if elemento[1]>=maximo[1]:
            maximo=elemento
        maximo
    while not nuevaPila.empty():
        elemento=nuevaPila.get()
        p.put(elemento)
    return maximo
    

"""p = Pila()
p.put(["s",10])
p.put(["m",5])
print(buscar_nota_maxima(p))
while not p.empty():
    print(p.get())"""

#5) imp
def esta_bien_balanceada(s:str) -> bool:
    res:bool=True
    contador:int = 0
    p = Pila()
    otraP = Pila()
    for i in range(len(s)):
        otraP.put(s[i])
    while not otraP.empty():
        letra=otraP.get()
        p.put(letra)
    while not p.empty():
        letra_sacada=p.get()
        if letra_sacada=="(":
            contador+=1
        if letra_sacada==")":
            contador-=1
        if contador<0:
             res=False
    if contador>0:
        res=False
    return res


"""print(
esta_bien_balanceada("3*(1x2)-(5-4)"),
esta_bien_balanceada("7((2x7)"),
esta_bien_balanceada("8*(9/3))"),
esta_bien_balanceada("1+)2*3(()")
)
"""

#6) 

#7)
def intercalar(p1:Pila,p2:Pila) -> Pila:
    p = Pila()
    otraP = Pila()
    while not(p1.empty() and p2.empty()):
        elemento1=p1.get()
        elemento2=p2.get()
        otraP.put(elemento2)
        otraP.put(elemento1)
    while not otraP.empty():
        elemento=otraP.get()
        p.put(elemento)
    return p

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
    print(res.get()) """

            
#cola
#8)
def generar_n_al_azar2(cantidad:int,desde:int,hasta:int) -> Cola:
    c = Cola()
    comienzo:int = desde
    for i in range(0,cantidad):
        c.put(comienzo)
        comienzo+=1 
    return c

"""res = generar_n_al_azar2(2, 5, 10)
#print(res.queue) #ver como es la pila (no hacer en parical)
print("Números generados al azar:")
while not res.empty():
    print(res.get())"""

#9)
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
while not c.empty(): # veo que mantenga el orden que arriba
    print(c.get())"""

#10) 
def buscar_max(c:Cola) -> int:
    maximo:int = 0
    nuevaC = Cola()
    while not c.empty():
        elemento=c.get()
        nuevaC.put(elemento)
        if elemento>=maximo:
            maximo=elemento
        maximo
    while not nuevaC.empty():
        elemento=nuevaC.get()
        c.put(elemento)
    return maximo 

"""c = Cola()
c.put(10)
c.put(5)
print(buscar_max(c))
while not c.empty():
    print(c.get())"""

#11)
def buscar_nota_min(c:Cola()) -> int:
    min:int =c.get()
    nuevaC = Cola()
    nuevaC.put(min)
    while not c.empty():
        elemento=c.get()
        nuevaC.put(elemento)
        if elemento[1]<min[1]:
            min=elemento
        min
    while not nuevaC.empty():
        elemento=nuevaC.get()
        c.put(elemento)
    return min[1]
    

"""c = Cola()
c.put(["s",10])
c.put(["m",2])
print(buscar_nota_min(c))
while not c.empty():
    print(c.get())"""

#12)
def intercalarc(c1:Cola,c2:Cola) -> Cola:
    c = Cola()
    nuevaC= Cola()
    # deberia volver a agregar los elementos a c1 y c2
    while not(c1.empty() and c2.empty()):
        elemento1=c1.get()
        elemento2=c2.get()
        c.put(elemento1)
        c.put(elemento2)
    return c

"""c1 = Pila()
c1.put(3)
c1.put(2)
c1.put(1)
c2 = Pila()
c2.put(6)
c2.put(5)
c2.put(4)
res = intercalarc(c1,c2)
while not res.empty():
    print(res.get()) """

#13)
def secuencia_de_bingo() -> Cola():
    c = Cola()
    for i in range(0,100):
        c.put(i)
    return c

"""res = secuencia_de_bingo()
while not res.empty():
    print(res.get())"""

def jugar_carton_del_bingo(carton:[int],bolillero:Cola)->int:  #preguntar
    contador:int=0
    while not bolillero.empty():
        bola=bolillero.get()
        for i in range(len(carton)):
            if carton[i]==bola:
                contador+=1
    return contador

"""bolillero = Cola()
bolillero.put(10)
bolillero.put(5)
bolillero.put(20)
bolillero.put(15)
print(jugar_carton_del_bingo([5,10,15,8],bolillero))"""

#14)
def n_pacientes_urgentes(c:Cola([int,str,str]))-> int:
    contador:int=0
    otraC = Cola()
    while not c.empty():
        paciente=c.get()
        otraC.put(paciente)
        if paciente[0]<=3:
            contador+=1
    while not otraC.empty():
        paciente=otraC.get()
        c.put(paciente)
    return contador

"""c = Cola()
c.put((1,'Jorge','ahi anda'))
c.put((1,'Maria','esta jodida'))
c.put((5,'Alejandro','blabla'))
c.put((4,'Martin','Anda bien dentro de todo'))
print(n_pacientes_urgentes(c))

while not c.empty():
    print(c.get())"""

#15)
def atencion_al_cliente(c:Cola) -> Cola:
    cola:[(str,int,bool,bool)]=Cola()
    otraC:[(str,int,bool,bool)]=Cola()
    cola_prioritaria:[(str,int,bool,bool)]=Cola()
    cola_preferencial:[(str,int,bool,bool)]=Cola()
    cola_resto:[(str,int,bool,bool)]=Cola()
    while not c.empty():
        paciente=c.get()
        otraC.put(paciente)
        if paciente[3]==True:
            cola_prioritaria.put(paciente)
        elif paciente[2]==True:
            cola_preferencial.put(paciente)
        else:
            cola_resto.put(paciente)
    while not otraC.empty():
        paciente=otraC.get()
        c.put(paciente)
    while not cola_prioritaria.empty():
        cola.put(cola_prioritaria.get())
    while not cola_preferencial.empty():
        cola.put(cola_preferencial.get())
    while not cola_resto.empty():
        cola.put(cola_resto.get())
    return cola

"""c=Cola()
c.put(('Jorge',19391293,False,False))
c.put(('Andrea',11523351,True,False))
c.put(('Adelina',7976723,False,True))
c.put(('Roberto',12452413,True,False))
res=atencion_al_cliente(c)
while not res.empty():
    print(res.get()) """

#dicc

#18) 
def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo, "r", encoding='utf8')
    dicc = {}
    for linea in archivo.readlines():
        palabra = ""
        lista=str(linea)
        for i in range(len(lista)):
            if lista[i]!= " " and lista[i]!= "\n":
                palabra+=lista[i]
            else:
                if palabra:  # Verifica si hay una palabra almacenada
                    dicc[len(palabra)] = dicc.get(len(palabra),0) +1 
                    palabra=""
            
    archivo.close()               
    return dicc

"""res = agrupar_por_longitud("hola_soy")
print(res)"""

#17) 
def calcular_promedio_por_estudiante(notas: list) -> dict:
    dicc={}
    for estudiante in notas:
        if not pertenece(estudiante[0], dicc.keys()):
            dicc[estudiante[0]] = promedio(estudiante[0], notas)
    return dicc

def pertenece(estudiante:str, notas:list) -> bool:
    for nota in notas:
        if nota[0] == estudiante:
            return True
    return False

def promedio(estudiante:str, notas:list) -> float:
    sumaNotas:int=0
    cantNotas:int=0
    for nota in notas:
        if estudiante == nota[0]:
            sumaNotas+=nota[1]
            cantNotas+=1
    promedio:float=(sumaNotas/cantNotas)
    return promedio
    

#res = calcular_promedio_por_estudiante([["n",5],["s",5],["n",6],["s",3],["r",7]])
# print(res)

#18)
def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo, 'r', encoding='utf8')
    dicc = {}
    palabras:[str] =[]
    for linea in archivo.readlines():
        palabra=""
        for caracter in linea:
            if caracter!=" " and caracter!="\n":
                palabra+=caracter
            else:
                if palabra:
                    palabras.append(palabra)
                    palabra=""
    for palabra in palabras:
        if not pertenece(palabra, dicc.keys()):
            dicc[palabra] = cantApariciones(palabra, palabras)
    valores = list(dicc.values())
    mayorValor = valores[0]
    for valor in valores:
        if valor > mayorValor:
            mayorValor = valor
        mayorValor
    for clave in dicc.keys():
        if dicc[clave] == mayorValor:
            return clave 


def cantApariciones(palabra:str, palabras:[str]) -> int:
    cantidad:int=0
    for p in palabras:
        if p==palabra:
            cantidad+=1
    return cantidad

#res = la_palabra_mas_frecuente("hola_soy")
#print(res)

#19) no salio
historiales:dict = {}
def pertenece2(usuario: str, usuarios: dict) -> bool:
    return usuario in usuarios

def visitar_sitio(historiales:dict,usuario:str,sitio:str):
    if not pertenece2(usuario, historiales.keys()):
        historiales[usuario] = []
    historiales[usuario].append(sitio)


"""visitar_sitio(historiales, "U1", "google.com")
visitar_sitio(historiales, "U1", "face.com")
visitar_sitio(historiales, "U2", "google.com")

print(historiales)"""

#20)
inventario:dict= {}
def agregar_producto(inventario:dict, nombre:str, precio:float,cantidad:int):
    if nombre not in inventario.keys():
        inventario[nombre] = {'precio':precio, 'cantidad':cantidad}

def actualizar_stock(inventario:dict, nombre:str,cantidad:int):
    if nombre in inventario.keys():
        inventario[nombre]['cantidad'] = cantidad

def actualizar_precio(inventario:dict, nombre:str,precio:float):
    if nombre in inventario.keys():
        inventario[nombre]['precio'] = precio
        
def calcular_valor_inventario(inventario:dict) -> float:
    dineroFinal:float=0
    for nombre in inventario.keys():
        dineroFinal+= (inventario[nombre]['precio'] * inventario[nombre]['cantidad'])
    return dineroFinal


"""agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Pantalon", 40)
actualizar_precio(inventario, "Camisa", 30.0)
res = calcular_valor_inventario(inventario)
print(res)

print(inventario)"""
    


#archivos
#21) repasarrrr

def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo,'r',encoding='utf8')
    contador:int=0
    for linea in archivo.readlines():
        contador+=1
    archivo.close()
    return contador

#res = contar_lineas("hola_soy")
#print(res)

def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    archivo = open(nombre_archivo,'r',encoding='utf8')
    for linea in archivo.readlines():
        if palabra in linea:
            return True
    archivo.close()
    return False

#res = existe_palabra("salo", "hola_soy")
#print(res)

def cantidad_apariciones(palabra:str, nombre_archivo:str) -> int: 
    archivo = open(nombre_archivo,'r', encoding='utf8')
    contador:int=0
    palabras:[str]=[]
    for linea in archivo.readlines():
        unaPalabra = ""
        for caracter in linea:
            if caracter != " " and caracter != '\n':
                unaPalabra += caracter
            else:
                if unaPalabra:
                    palabras.append(unaPalabra)
                    unaPalabra = ""  # Reiniciar para la próxima palabra
    # Contar las apariciones de la palabra buscada
    for unaPalabra in palabras:
        if unaPalabra == palabra:
            contador += 1
    archivo.close()
    return contador

#res = cantidad_apariciones("aa", "hola_soy")
#print(res)

#22)
def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo,'r', encoding='utf8')
    archivo_sin_comentarios=open("archivoClonadoo.py","w")
    for linea in archivo.readlines():
        if linea[0]!="#":
            archivo_sin_comentarios.write(linea) #escribe solo esa linea
    archivo.close()
    archivo_sin_comentarios.close()

#res = clonar_sin_comentarios("hola_soy")
#print(res)

#23)
def invertir_lineas(nombre_archivo:str):
    archivo = open(nombre_archivo,'r', encoding='utf8')
    archivo_reverso = open("reverso.txt",'w')
    lineas = archivo.readlines()
    for linea in range(len(lineas)-1,-1,-1): # ir probando 
        archivo_reverso.write(lineas[linea])
    archivo.close()
    archivo_reverso.close()

#res = invertir_lineas("hola_soy")
#print(res)

#24)
def agregar_frase_al_final(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"a") # el archivo se abre en modo escritura pero para escribir al final del archivo (eso hace "a")
    archivo.write(frase)
    archivo.close()


#res = agregar_frase_al_final("hola_soy","salo")
#print(res)

#25)
def agregar_frase_principio(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,'r+') # abre el archivo en modo lectura y escritura
    contenido = archivo.read()
    archivo.seek(0,0) # posiciona el cursor al principio del archivo 
    archivo.write(frase.rstrip('\r\n') + '\n' + contenido) # frase.rstrip('\r\n') ej: si la frase es "hola mundo\n" entonces agrega solo "hola mundo" luego otro salto de linea y luego el contenido que ya habia en el archivo
    archivo.close()

#26)
def lista_palabras_archivo(nombre_archivo:str) -> list:
    archivo = open(nombre_archivo, 'r', encoding='utf8')
    palabras:[str]=[]
    for linea in archivo.readlines():
        palabra = ""
        for caracter in linea:
            if caracter != " " and caracter != "\n" and caracter!= "_":
                palabra+= caracter
            else:
                if len(palabra)>=5:
                    palabras.append(palabra)
                palabra= "" 
    archivo.close()
    return palabras

#res = lista_palabras_archivo("hola_soy")
#print(res)

#27)  inc 
#def calcular_promedio_por_estudiante(nombre_archivo_notas:str, nombre_archivo_promedio:str):

def promedioEstudiante(lu:str)->float:
    archivo=open('notas.csv','r')
    cantNotas:int=0
    sumaNotas:int=0
    listaEstudiantes:[str,str,str,int]=[]
    for linea in archivo.readlines():
        datos=linea.split(",")
        if datos[0]==lu:
            cantNotas+=1
            sumaNotas+=int(datos[3])
    archivo.close()
    promedio:float = sumaNotas/cantNotas
    return promedio


