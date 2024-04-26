

--Ejercicio 1
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
{-# HLINT ignore "Evaluate" #-}
{-# HLINT ignore "Redundant bracket" #-}
--a)
longitud :: [t] -> Integer 
longitud [] = 0
longitud (x:xs) = 1 + longitud xs 

--a)
ultimo :: [t] -> t 
ultimo [x] = x 
ultimo (x:xs) = ultimo xs

--b)
principio::[t]->[t]
principio [x] = []
principio (x:xs) = x : principio xs

--d)
reverso :: [t] -> [t] 
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]
{-ej: reverso (3,4,5), reverse [4,5] ++ [2]
                        reverse [4] ++ [5] ++ [2]
                        reverse [] ++ [4] ++ [5] ++ [2]
                        []++ [4]++[5]++[2
                        [4,5,2]
 -} 

 --Ejercicio 2 
 --a) 
pertenece ::(Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys

--pertenece ::(Eq t) => t -> [t] -> Bool
--pertenece _ [] = False
--pertenece x (y:ys) | x == y  = True 
--                   | otherwise = pertenece x ys 

--b)
todosIguales :: (Eq t) => [t] -> Bool 
todosIguales (x:xs)| longitud (x:xs) == 1 = True
                   | x == head xs = True && todosIguales xs
                   | otherwise = False

--c)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True 
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs 

--d)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = False
                    | otherwise = hayRepetidos xs 

--e)
quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n==x = xs 
                | otherwise = x: quitar n xs 
--f)
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n==x = xs
                     | otherwise = x: quitarTodos n xs 

--g)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = [] 
eliminarRepetidos (x:xs) = x: eliminarRepetidos (quitarTodos x xs)

--Voy eliminando a todos los que esten repetidos, agarrando cada elemento, y borrando todas las veces adicionales que aparezca en la lista

--h)
--estaContenida verifica si cada elemento de una lista xs pertenece a otra lista ys, es decir, si xs esta contenida en ys
estaContenida :: (Eq t) => [t] -> [t] -> Bool
estaContenida [] ys = True
estaContenida (x:xs) ys = pertenece x ys && estaContenida xs ys

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = estaContenida xs ys && estaContenida ys xs


--i)
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs) | longitud xs == 0 = True 
               |x == (head (reverso xs)) = True && capicua (quitar x xs)
               | otherwise = False 

--Ejercicio 3 
--a) 
sumatoria :: [Integer] -> Integer
sumatoria [] = 0 
sumatoria (x:xs) = x + sumatoria xs 

--b) 
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

--c)
maximo :: [Integer] -> Integer 
maximo  [x] = x 
maximo (x:y:xs) | x>y = maximo (x:xs)
                | otherwise =  maximo (y:xs) 

--d) 
sumarN :: Integer -> [Integer] -> [Integer] 
sumarN n [x] = [x+n]
sumarN n (x:xs) = [x+n] ++ sumarN n xs 

--e) 
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

--f)
sumarElUltimo :: [Integer] -> [Integer] 
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs) 

--g) 
pares :: [Integer] -> [Integer]
pares [] = [] 
pares (x:xs) | mod x 2==0 = [x] ++ pares xs 
             | otherwise = pares xs  

--h)
multiplosDeN :: Integer -> [Integer] -> [Integer] 
multiplosDeN _ []  = []  
multiplosDeN n (x:xs) | mod x n==0 = [x] ++ multiplosDeN n xs
                      | otherwise = multiplosDeN n xs  
--i) 

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) | longitud xs == 0 = [x]
               | x <= minimo xs = [x] ++ ordenar xs
               | otherwise = ordenar (xs++[x])

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:xs) | x <= y = minimo (x:xs)
                | otherwise = minimo (y:xs) 
  -- Agarro el minimo, lo pongo al principio de la lista, luego ordeno el resto de la lista sin ese minimo

--Ejercicio 4
--a) 
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == ' ' = [' '] ++ sacarBlancosRepetidos xs
                               | otherwise = [x] ++ sacarBlancosRepetidos (y:xs) 

--b)
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) = 1 + contarPalabras xs

--c)

palabras :: [Char] -> [[Char]]
palabras a = palabrasaux a []

palabrasaux :: [Char] -> [Char] -> [[Char]]
palabrasaux [] b = b : []
palabrasaux (x:xs) b | x == ' ' =  b : palabrasaux xs []
                     | otherwise =  palabrasaux xs (b ++ [x])

--d)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga a = palabraMasLargacomparador (palabras a) 

palabraMasLargacomparador :: [[Char]] -> [Char]
palabraMasLargacomparador [] =[]
palabraMasLargacomparador (x:xs) | longitud x == maximo (palabraMasLargaaux (x:xs)) = x
                                 | otherwise = palabraMasLargacomparador xs

palabraMasLargaaux :: [[Char]] -> [Integer]
palabraMasLargaaux [] = []
palabraMasLargaaux (x:xs) = [longitud x] ++ palabraMasLargaaux xs
            
--e)
--f)
--g)

--Ejercicio 5)
--a) 
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada x = sumaAcumuladaAux x 0

sumaAcumuladaAux :: (Num t) => [t] -> t -> [t]
sumaAcumuladaAux (x:xs) c | longitud xs == 0 = [c+x]
                          | otherwise = [c+x] ++ sumaAcumuladaAux xs (c+x)


--b) 

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos (x:[]) = [(descomponerEnPrimosaux x 2)]
descomponerEnPrimos (x:xs) = [(descomponerEnPrimosaux x 2)] ++ descomponerEnPrimos xs 

descomponerEnPrimosaux :: Integer -> Integer -> [Integer]
descomponerEnPrimosaux x a | x<a = []
                              | mod x a == 0 = [a] ++ descomponerEnPrimosaux (div x a) a
                              | otherwise = descomponerEnPrimosaux x (a+1)