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


"""def divide_a_todos(e:int,s:[int])->bool:
   i=0
   while (0<=i<len(s)):
      if (s[i]%e==0):
         return True
      i+=1
   else:
     return False"""

def divide_a_todos(e:int,s:[int])->bool:
    for i in range(0,len(s)):
        if (s[i]%e==0):
            return True
    
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
      if (len(s[i])>7):
         return True
      
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
    for operacion in operaciones:
        if operacion[0]=="I":
            saldo+=operacion[1]
        if operacion[0]=="R":
            saldo-=operacion[1]
    return saldo 
"""O PONER:
 for i in range(0,len(operaciones)):
        if (operaciones[i][0]=="I"):
            saldo+=operaciones[i][1]
        elif(operaciones[i][0]=="R"):
            saldo-=operaciones[i][1]
    return saldo 
"""
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

"""def vocalesDistintas(palabra:str)-> bool:
    return tieneVocales(palabra)>=3

def tieneVocales(texto:str)-> int:
    sumaVocales=0
    for caracter in texto:
        if caracter=='a' or caracter=='A':
            sumaVocales+=1
        if caracter=='e' or caracter=='E':
            sumaVocales+=1
        if caracter=='i' or caracter=='I':
            sumaVocales+=1
        if caracter=='o' or caracter=='O':
            sumaVocales+=1
        if caracter=='u' or caracter=='U':
            sumaVocales+=1
    return sumaVocales"""
        

# parte 2 
 
def borrarPosicionesPares (s:[int]):
    for i in range (0,len(s)):
        if(i%2==0):
            s[i]=0 # asigna 0 a el numero que hay en la posicion i de s 
    return s 

def borrarPosicionesPares2(s:[int]) -> [int]:
    nuevaLista=[]
    for i in range (0,len(s)):
        if(i%2==0):
           nuevaLista.append(0)
        else: 
            nuevaLista.append(s[i]) 
    return nuevaLista

def borrarVocales(palabra:str)->str:
    nuevaPalabra:str=""
    for caracter in palabra:
        if not es_vocal(caracter):
            nuevaPalabra+=caracter
    return nuevaPalabra

def es_vocal(letra:str)->bool:
    return (letra=="a") or (letra=="e") or (letra=="i") or (letra=="o") or (letra=="u") or (letra=="A") or (letra=="E") or (letra=="I") or (letra=="O") or (letra=="U")

def reemplazaVocales(palabra:[chr])->[chr]:
    nuevaPalabra=[]
    for i in range(0,len(palabra)):
        if (es_vocal(palabra[i])):
            nuevaPalabra+=" "
        else:
            nuevaPalabra+=palabra[i]
    return nuevaPalabra


def da_vuelta_str(palabra:[chr])-> [chr]:
    palabraDadaVuelta=[]
    for i in range(0,len(palabra)):
        palabraDadaVuelta+=palabra[(len(palabra)-i)-1]
    return palabraDadaVuelta 

def eliminar_repetidos(palabra:[chr])->[chr]:
    palabraSinRepetidos=[]
    for i in range(0,len(palabra)):
        if (palabra[i] not in palabraSinRepetidos):
            palabraSinRepetidos+=(palabra[i])
    return palabraSinRepetidos

# 3
def aprobado(notas:[int])->int:
    if todasLasNotasSonMayoresIguales4(notas) and promedioDeNotas(notas)>=7:
        return 1 
    if todasLasNotasSonMayoresIguales4(notas) and 4<=promedioDeNotas(notas)<7:
        return 2
    if not(todasLasNotasSonMayoresIguales4(notas)) and (promedioDeNotas(notas)<4):
        return 3 

def todasLasNotasSonMayoresIguales4(notas:[int])->bool:
    for nota in notas:
        if (nota<4):
            return False
    return True
    
def promedioDeNotas(notas:[int])->float:
    sumaDeNotas=0
    for nota in notas:
        sumaDeNotas+=nota
    promedio=sumaDeNotas//len(notas)
    return promedio 

# ej 4
def listaDeNombres()-> [str]:
    res=[]
    nombre=""
    while(nombre!="listo"):
        print("ingrese un nombre:")
        nombre=input()
        if (nombre!="listo"):
            res.append(nombre)
    return res 


def historialSube()-> [(str,int)]:
    res=[]
    caracter:str=""
    monto:int=0
    dineroActual:int=0
    while(caracter!='X'):
        print("Ingrese una opción(C: Cargar, D: Descontar, X=Cerrar):")
        caracter=input()
        if(caracter=='C'):
            print("Ingrese un monto:")
            monto=int(input())
            dineroActual+=monto
            res.append((caracter,monto))
        elif(caracter=='D'):
            print("Ingrese un monto:")
            monto=int(input())
            dineroActual-=monto
            res.append((caracter,monto))
    print("Terminó con "+str(dineroActual)+" pesos")        
    return res

#def



# EJ 5 
def perteneceACadaUno (e:int,s:[[int]],res:[bool])->None:
    res=[]
    for i in range (0,len(s)):
        if (e not in s[i]):
            res.append(False)
        else: 
            res.append(True)
    return res 


def es_matriz(s:[[int]])->bool:
    for i in range(0,len(s)):
        if (len(s)!=len(s[i])):
            return False
    return True

#mal
def filasOrdenadas(m:[[int]],res:[bool])->None:
    res=[]
    for i in range (0,len(m)):
        if (m[i]+1<m[i]):
            res.append(False)
        else:
            res.append(True)
    print(res)



