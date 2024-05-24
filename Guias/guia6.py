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



