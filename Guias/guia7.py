# ej 1 

def pertenece(e:int,seq:[int])->bool: 
    for i in range(0,len(seq),1):
        if (e==seq[i]):
            return True 
    else:
     return False 
    
def pertenece2(e:int,s:[int]) -> bool:
 i=0
 while (0<=i<len(s)):
      if (e==s[i]):
         return True 
      i+=1 
 else: 
    return False

def pertenece3(e:int,s:[int])->bool:
    i=len(s)-1
    while i>=0:
        if(e==s[i]):
            return True
        i-=1
    return False


def divide_a_todos(e:int,s:[int])->bool:
   i=0
   while (0<=i<len(s)):
      if (s[i]%e==0):
         return True
      i+=1
   else:
     return False

def sumaTotal(s:[int])->int:
    contador=0
    for i in range(0,len(s)):
        contador+=s[i]
    return contador


def ordenados1(s: [int]) -> bool:
    i = 0
    while i < len(s) - 1:
        if s[i] > s[i + 1]:
            return False
        i += 1
    return True 

   
def ordenados2(seq:[int])->bool:
    for i in range(0,len(seq)-1):
        if (not(seq[i]<seq[i+1])):
            return False
    return True


def listaPalabras(s:[str]) -> bool:
   for i in range(0,len(s)): 
      if (len(s[i])>=7):
         return True
      i+=1
   return False 

def esPalindromo(palabra:str)->bool:
    l:int=len(palabra) # l es longitud de la palabras
    for i in range(0,l//2): # i va desde 0 hasta la mitad de la palabra
        if(palabra[i]!=palabra[(l-1)-i]): # si la letra en la posicion i no es igual a la letra en (l-1)-i => false
                                          # y si es igual se evalua en la siguiente posicion despues de 0 entre 0 y l//2
            return False
    return True # devuelve true si todas las letras comparadas en if son iguales

# ej 1.7)
def fortalezaContra(contra:str) -> str:
   long=len(contra)
   if (long<5):
      return "ROJO"
   elif (long>8 and  hay_numero(contra) and hay_minuscula(contra) and hay_mayuscula(contra)):
      return "VERDE"
   else:
      return "AMARILLO"
   
def hay_numero(palabra:str)->bool:
    for caracter in palabra: # se fija si cada caracter esta en palabra
        if (caracter>='0') and (caracter<='9'): # los caracteres van del 0 al 9
            return True
    return False
def hay_mayuscula(palabra:str)->bool:
    for caracter in palabra:
        if (caracter>='A') and (caracter<='Z'):
            return True
    return False
def hay_minuscula(palabra:str)->bool:
    for caracter in palabra:
        if (caracter>='a') and (caracter<='z'):
            return True
    return False

# ej 1.8)

def saldoActual(operaciones:[(str,float)])->float:
    saldo=0
    for i in range(0,len(operaciones)):
        if (operaciones[i][0]=="I"):
            saldo+=operaciones[i][1]
        if(operaciones[i][0]=="R"):
            saldo-=operaciones[i][1]
    return saldo 

# 1.9)
def vocalesDistintas(palabra:str)-> bool:
    contadorVocalesDistintas=0
    if(pertenece('a',palabra) or pertenece('A',palabra)):
        contadorVocalesDistintas+=1
    if(pertenece('e',palabra) or pertenece('E',palabra)):
        contadorVocalesDistintas+=1
    if(pertenece('i',palabra) or pertenece('I',palabra)):
        contadorVocalesDistintas+=1
    if(pertenece('o',palabra) or pertenece('O',palabra)):
        contadorVocalesDistintas+=1
    if(pertenece('u',palabra) or pertenece('U',palabra)):
        contadorVocalesDistintas+=1
    return contadorVocalesDistintas>=3
    
