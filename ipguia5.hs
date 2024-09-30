longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs 

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x: principio xs 

reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = ultimo xs: reverso (principio xs) ++ [x]
--reverso (x:xs) = reverso xs ++ [x]

--2)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n==x = True
                   | otherwise = pertenece n xs 

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs) | x==y = todosIguales (y:xs)
                      | otherwise = False 

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:y:xs) | x/=y = todosDistintos(y:xs) && todosDistintos(x:xs)
                        | otherwise = False

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:y:xs) | x==y = True
                      | otherwise = hayRepetidos(x:xs) || hayRepetidos(y:xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n==x = xs
                | otherwise = x: quitar n xs 

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n==x = quitarTodos n xs 
                     | otherwise =x: quitarTodos n xs 

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x: eliminarRepetidos(quitarTodos x xs) 

mismoElementos :: (Eq t) => [t] -> [t] -> Bool
mismoElementos [] [] = True
mismoElementos (x:xs) (y:ys) | pertenece x (y:ys) && pertenece y (x:xs) = mismoElementos xs ys
                             | otherwise = False 

capicua :: (Eq t) => [t] -> Bool
capicua [x] = True
capicua [] = True
capicua (x:xs) | x== ultimo xs = capicua (quitar x xs) 
               | otherwise = False 

--3)

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs)= x + sumatoria xs 

productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x:xs)= x * productoria xs 

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) | x>=y = maximo (x:xs)
                | otherwise = maximo (y:xs)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [n+x]
sumarN n (x:xs) = (n+x): sumarN n xs 

sumarElPrimero :: [Integer] -> [Integer] 
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo xs) (x:xs) 



pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 ==0 = x: pares xs
             | otherwise = pares xs 

multiploDeN :: Integer -> [Integer] -> [Integer]
multiploDeN _ [] = []
multiploDeN n (x:xs) | mod x n == 0 = x: multiploDeN n xs
                     | otherwise = multiploDeN n xs 

ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar (x:xs) | x<minimo xs = [x] ++ ordenar xs 
               | otherwise =  ordenar (xs++[x])

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:xs) | x>= y = minimo(y:xs)
                | otherwise = minimo(x:xs)

--4)
sacarBlancosRepetidos2 :: [Char] -> [Char]
sacarBlancosRepetidos2 [x] = [x]
sacarBlancosRepetidos2 (x:y:xs) | x==' ' && x==y =  sacarBlancosRepetidos2 (y:xs)
                               | otherwise = x: sacarBlancosRepetidos2 (y:xs)


-- dificil 
{-contarPalabras :: [Char] -> Integer
contarPalabras xs = contarEspacios(sacarEspacioInicio(sacarEspacioFin(sacarBlancosRepetidos xs))) + 1-}

sacarEspacioInicio :: [Char] -> [Char]
sacarEspacioInicio (x:xs) | x==' ' = xs
                           | otherwise = (x:xs)

sacarEspacioFin :: [Char] -> [Char]
sacarEspacioFin [] = []
sacarEspacioFin (x:[]) | x==' '=[] 
                       | otherwise = [x]
sacarEspacioFin (x:xs) = x:(sacarEspacioFin xs)
       

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x== ' ' = 1 + contarEspacios xs 
                      | otherwise = contarEspacios xs 


{-palabra :: [Char] -> [[Char]]
palabra [] = []
palabra xs = primeraPalabra xs : palabra(sacarPrimeraPalabra(sacarEspacioInicio(sacarEspacioFin(sacarBlancosRepetidos xs))))
-}
primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x ==' ' =[]
                      | otherwise = x:primeraPalabra xs


sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] =[]
sacarPrimeraPalabra (x:xs) | x==' ' = xs
                           | otherwise = sacarPrimeraPalabra xs
-- ej [['h'],['h'],[' '],['h']] = "hh h"
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs 

{-palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:xs) = laMasLarga(sacarEspacioInicio(sacarEspacioFin(sacarBlancosRepetidos xs)))-}

laMasLarga :: [Char] -> [Char]
laMasLarga xs | sacarPrimeraPalabra xs == [] = primeraPalabra xs 
              | length(primeraPalabra xs) > length(laMasLarga xs) = primeraPalabra xs
              | otherwise = laMasLarga(sacarPrimeraPalabra xs )

-- ej [['h'],['h'],[' '],['h']] = "h h  h "
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ ' ' : aplanarConBlancos xs 


aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _= []
aplanarConNBlancos (x:xs) n= x ++ nBlancos n ++ aplanarConNBlancos xs n


nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos  n = ' ': nBlancos (n-1) 

--5)
sumaAcumulada  :: (Num t) => [t] -> [t]
sumaAcumulada [x] = [x]
sumaAcumulada (x:xs) = sumaAcumuladaAux (x:xs) 0

sumaAcumuladaAux :: (Num t) => [t] -> t -> [t]
sumaAcumuladaAux [] _ = []
sumaAcumuladaAux (x:xs) n = [n+x] ++ sumaAcumuladaAux xs (n+x)



descomponerEnPrimos :: [Integer] -> [[Integer]] 
descomponerEnPrimos [x] = [(descomponerEnPrimosAux x 2)]
descomponerEnPrimos (x:xs) = [(descomponerEnPrimosAux x 2)] ++ descomponerEnPrimos xs 

descomponerEnPrimosAux :: Integer -> Integer -> [Integer]
descomponerEnPrimosAux x n | x<n = []
                           | mod x n == 0 = n : descomponerEnPrimosAux (div x n) n 
                           | otherwise = descomponerEnPrimosAux x (n+1)


