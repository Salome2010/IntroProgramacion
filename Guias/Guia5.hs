

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
