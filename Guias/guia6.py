#ej 1

import math


def imprimir_hola_mundo ():
    x= "hola mundo"
    print(x)


def imprimir_un_verso():
    print("ggggghjjjjjj\njfjfjjfjfj") 

def raizDe2() -> float:
    return round(math.sqrt(2),4) # math.sqrt calcula la raiz de 2 y con el round obtengo solo 4 decimales de esa raiz

def  factorial_2() -> int: 
    return math.factorial(2)

def perimetro() -> float:
   res= 2*math.pi # 2 por el numero pi 
   return(res) 

# ej 2

def imprime_saludo(nombre: str):
    print("hola" + nombre) 

def raiz_cuadrada_de(numero) -> float:
    return math.sqr(numero) #raiz cuadrada 

def fahrenheit_a_celsius(temp_far:float) -> float:
    return((temp_far -32)*5)/9 

def imprimir_dos_veces(estribillo:str):
    estribillo *=2
    print("estribillo repetido:" + estribillo )

#def imprimir_dos_veces(estribillo:str)->None:
#     print(estribillo*2)

def es_multiplo_de(n:int,m:int) -> bool:
    return(n%m==0) #modulo

def es_par(numero:int) -> bool:
    return (es_multiplo_de(numero,2)) #devuelve true si el numero es multiplo de 2 => es par

def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int)->int:
     return math.ceil((comensales*min_cant_de_porciones)/8) # math.ceil redonde el numero hacia arriba al entero mas cercano
                                                            # si return=4.3 => devuelve 5 

#ej 3
def alguno_es_0(numero1:float,numero2:float)->bool:
    return (numero1==0) or (numero2==0)

def ambos_son_0(numero1:float,numero2:float)->bool:
    return (numero1==0) and (numero2==0)

def es_nombre_largo(nombre:str) -> bool:
    return(3<= len(nombre)>=8) # len es longitud 

def es_bisiesto(año:int) -> bool:
    return ((año%4==0) and ((año%100!=0)) or (año%400==0))

# ej 4

def peso_pino(altura:int) -> int:
    if(altura<=300): # 3 metros = 300 cm
     return altura*3 
    else:
     return 900+ 2*(altura-300) 
    
def es_peso_util(peso:int) -> bool:
    return (400<= peso<=1000)

def sirve_pino1(altura:int) -> bool:
    return (150<=altura<=350)

def sirve_pino2(altura:int)->bool:
    return es_peso_util(peso_pino(altura)) # me da el peso del pinto y se fija que este entre 400 y 1000

# ej 5

def devolver_el_doble_si_es_par(numero:int) -> int:
    if(numero%2==0): # o poner if(es_par(numero))
        return numero*2
    else:
        return numero 
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if(numero%2==0): # o poner if(es_par(numero))
        return numero
    else:
        return numero + 1 

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    if(numero%9==0): # o podia poner if(es_multiplo_de(numero,3))
        return numero*3 
      
    elif(numero%3==0):
        return numero*2
    else: 
        return numero

def lindo_nombre(nombre:str) -> str:
    if(len(nombre)>=5):
        return "Tu nombre tiene muchas letras!" 
    else: 
        return "tu nombre tiene menos de 5 caracteres"
    
def elRango(numero:int)->None:
    if(numero<5):
        print("Menor a 5")
    elif(10<=numero<=20):
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

def depende_tu_edad(genero:str,edad:int) -> str:
    if(genero=="F"):
     if(18<=edad<60):
         return "te toca trabajar"
     else: 
         return "anda de vacaciones"
    if(genero=="M"):
        if(18<=edad<65):
            return "te toca trabajar"
        else:
            return "anda de vacaciones"

# ej 6

def numeros_1_al_10():
    i=1
    while (i<=10):
        print(i)
        i+=1

def numeros_pares_10_al_40():
    i=10
    while(i<=40):
        print(i)
        i+=2 

def palabra_eco():
    i= 1
    while(i<=10):
        print("eco")
        i+=1 

def cohete(numero:int):
    while (numero>=1):
        print(numero)
        numero-=1
    print ("Despegue")

def viajeEnElTiempo(añoSalida:int,añoLlegada:int):
    añoSalida-=1 # como viaja un año atras entonces debe ser 2009 y luego hace el resto 
    while(añoSalida>=añoLlegada):
        print("Viajó un año al pasado, estamos en el año "+str(añoSalida))
        añoSalida-=1

def conocerAAristoteles(añoDeSalida:int):
    while(añoDeSalida>=384):
        print("Viajó 20 años al pasado, estamos en el "+ str(añoDeSalida))
        añoDeSalida-=20
    if(añoDeSalida>=374):
        print("Viajó 20 años al pasado, estamos en el "+ str(añoDeSalida)) 
    print("faltan 4 años para conocer a Aristoteles!!")

# ej 7 
def numeros_del_1_al_10_v2(): 
 for i in range(1,11,1):
    print (i)

def pares_del_10_al_40_v2(): 
 for i in range(10,41,2):
    print (i)

def eco_v2(): 
 for i in range(1,11,1):
    print ("eco")

def cohete_v2(numero:int): 
 for i in range(numero,0,-1):
    print (i)
 print("Despegue") 
  
def viajeEnElTiempoV2(añoSalida:int,añoLlegada:int):
 añoSalida-=1 
 for i in range(añoSalida,añoLlegada-1,-1):
     print("Viajó un año al pasado, estamos en el año "+str(i))
 añoSalida-=1

def conocerAAristotelesV2(añoSalida:int):
 for i in range(añoSalida,384,-20):
     print("Viajó 20 años al pasado, estamos en el año "+str(i))
 añoSalida-=20

 for i in range(añoSalida,374,-20):
     print("Viajó 20 años al pasado, estamos en el año "+str(i))
 añoSalida-=20

 print("falta 4 años para conocer a Aristoteles!!")




