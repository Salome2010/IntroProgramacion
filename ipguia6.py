import math
#1)

def hola_mundo():
    x:str  = "Hola Mundo"
    print(x)

# llamar a la funcion 
hola_mundo()

def un_verso():
    x:str = "Hola\nMundo"
    print(x)

#
#un_verso()

def factoria_2():
    x:int = math.factorial(2)
    print(x)

#
#factoria_2()

def raiz_2():
    x:float = round(math.sqrt(2), 4)
    print(x)

#
#raiz_2()

def perimetro() -> float:
    x:float = 2*(math.pi)
    print(x)

#
#perimetro()

#2)
def imprimir_saludo(nombre: str):
    x:str = "hola " + str(nombre) 
    return x 

#res = imprimir_saludo("salo")
#print(res)

def raiz_cuadrada_de(numero: int):
    x:int = math.sqrt(numero)
    return x

#res= raiz_cuadrada_de(25)
#print(res)

def fahrenheit_a_celsius(t: float) -> float:
    x:float = ((t - 32) * 5)/9
    return x

#res = fahrenheit_a_celsius(68)
#print(res)

def imprimir_dos_veces(estribillo: str):
    estribillo*=2
    return estribillo

#res = imprimir_dos_veces("hola")
#print(res)

def es_multiplo_de(n:int , m: int) -> bool:
    if (n%m ==0):
        return True
    return False # otra manera es solo poner en la linea 69: return (n%m ==0)
       

#res = es_multiplo_de(10,2)
#print(res)

def es_par(n:int) -> bool:
    if (es_multiplo_de(n,2)): 
        return True
    return False # podria simplificarse igual que linea 71

#res = es_par(7)
#print(res)

def cantidad_pizzas(comensales: int, porciones:int):
    x:int = math.ceil((comensales*porciones)/8)
    return x 

#res = cantidad_pizzas(10,5)
#print(res)

#3)
def alguno_es_0(n: float, m:float) -> bool:
    return (n==0 or m==0)

#res = alguno_es_0(0,1)
#print(res)

def ambos_son_0(n: float, m:float) -> bool:
    return (n==0 and m==0)

def es_nombre_largo(nombre: str) -> bool:
    return (3<=len(nombre)<=8)

#res = es_nombre_largo("salo")
#print(res)

def es_bisiesto(año: int) -> bool:
    return (es_multiplo_de(año, 400) or (es_multiplo_de(año,4) and not(es_multiplo_de(año,100))))

#res = es_bisiesto(2016)
#print(res)

#4)
def peso_pino(altura: int) -> int: 
    if (altura<=300):
        return altura * 3 
    else: 
        return 300*3 + ((altura - 300)*2)

#res = peso_pino(700)
#print(res)

def es_peso_util(peso: int) -> bool:
    return 400<= peso <=1000

#res = es_peso_util(300)
#print(res)

def sirve_pino(altura:int) -> bool:
    if(altura<=300):
        return (400<=(altura * 3)<=1000)
    else:
        return (400<=(300 * 3 + ((altura - 300)*2))<=1000)
        
#res = sirve_pino(400)
#print(res)

def sirve_pino2(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))

#5)
def devolver_el_doble_si_es_par(numero: int) -> int:
    if es_par(numero):
        return numero * 2
    else: 
        return numero 

#res = devolver_el_doble_si_es_par(4) 
#print(res)

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    if not(es_par(numero)):  #o usar solo else: return numero + 1
        return numero + 1

#res = devolver_valor_si_es_par_sino_el_que_sigue(3)
#print(res)

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if es_multiplo_de(numero,3):
        return numero * 2
    elif es_multiplo_de(numero,9): # tambien puede ser if
        return numero * 3
    else: 
        return numero

#res = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18)
#print(res)

def lindo_nombre(nombre: str):
    if len(nombre)>=5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

#res = lindo_nombre("salo")
#print(res)

def el_rango(numero: int):
    if numero<5:
        return "Menor a 5"
    if (10<numero<20):
        return "entre 10 y 20"
    if numero>20: # o elif 
        return "el numero es mayor a 20"
    else:
        return "el numero pertenece a otro rango"

#res = el_rango(5)
#print(res)

def depende_tu_edad(genero: str, edad: int):
    if genero=="F":
        if (edad>=60 or edad<18):
            return "Anda de vacaciones :)"
        else:
            return "Te toca trabajar :( "
    if genero=="M":
        if (edad>=65 or edad<18):
            return "Anda de vacaciones :)"
        else:
            return "Te toca trabajar :( "

#res = depende_tu_edad("F",50)
#print(res)

#6)
def del_1_al_10():
    i:int=1
    while (i<=10):
        print(i)
        i+=1

# del_1_al_10() (si uso res .... y print(res) entonces al final de la lista tira un None)


def pares_10_al_40():
    i:int=10
    while (i<=40):
        print(i)
        i+=2

#pares_10_al_40()

def eco():
    i:int = 1
    while(i<=10):
        print("Eco")
        i+=1

#eco()

def cohete_1():
    i:int=10
    while(i>=1):
        print(i)
        i-=1
    print("Despegue")

#cohete_1()

def viaje_en_el_tiempo(partida: int, llegada:int):
    i:int= partida-1
    while (i>=llegada):
        print("viajamos 1 año al pasado, estamos en el año " + str(i))
        i-=1
    print("llegamoss")

#viaje_en_el_tiempo(2010,2005)

def aristoteles(partida:int):
    i:int= partida
    while(i>=384):
        print("vamos a viajar de a 20 años en cada salto, estamos en el año " + str(i))
        i-=20
    print("falta poco para conocer a Aristoteles :)")

#aristoteles(2000)

#7)
def del_1_al_10_2():
    for i in range(1,11,1):
        print(i)

#del_1_al_10_2() 


def pares_10_al_40_2():
    for i in range(10,41,2):
        print(i)
    
#pares_10_al_40_2()

def eco_2():
    for i in range(1,11,1):
        print("Eco")
    
#eco_2()

def cohete():
    for i in range(10,0,-1):
        print(i)
    print("Depegue")

#cohete()

def viaje_en_el_tiempo_2(partida: int, llegada:int):
    for i in range(partida-1,llegada-1,-1):
        print("viajamos 1 año al pasado, estamos en el año " + str(i))
    print("llegamoss")

#viaje_en_el_tiempo_2(2010,2005)

def aristoteles_2(partida:int):
    for i in range(partida,385,-20):
        print("vamos a viajar de a 20 años en cada salto, estamos en el año " + str(i))
    print("falta poco para conocer a Aristoteles :)")

#aristoteles_2(2000)


#9)
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

#res = ro(1)
#res = ro(1)
#res = ro(1)
#print(res)