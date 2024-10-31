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


