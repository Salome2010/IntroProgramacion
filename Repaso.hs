--1)
generarStock :: [String] -> [(String, Integer)]
generarStock [] = []
generarStock (prod:xs) | pertenece prod xs = (prod, cantidadProd (prod:xs)) : generarStock (eliminar prod xs)
                       | otherwise = (prod, 1) : generarStock(eliminar prod xs)

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece p (x:xs) | p==x = True
                   | otherwise = pertenece p xs 

cantidadProd ::  [String] -> Integer
cantidadProd  [] = 0 
cantidadProd [x] = 1
cantidadProd (x:y:xs) | x==y = 1 + cantidadProd (x:xs) 
                      | otherwise = cantidadProd (x:xs) 

eliminar :: String -> [String] -> [String]
eliminar _ [] = []
eliminar p (x:xs) | p==x = eliminar p xs
                  | otherwise = x: eliminar p xs 

--2)

stockDeProducto2 :: [(String, Int)] -> String -> Int
stockDeProducto2 [] _ = 0 
stockDeProducto2 ((prod, cantidad):xs) nombre | nombre==prod = cantidad
                                              | otherwise = stockDeProducto2 xs nombre 

--3) verr
dineroEnStock :: [(String, Int)] ->[(String, Float)] ->Float
dineroEnStock [] _ = 0.0
dineroEnStock ((prod, cant):xs) ((nombre, precio):ys) = ((fromIntegral cant) * (buscarPrecio prod ((nombre, precio):ys))) + dineroEnStock xs ((nombre, precio):ys)

buscarPrecio :: String ->[(String, Float)] -> Float
buscarPrecio _ [] = 0
buscarPrecio prod ((nombre, precio):ys) | prod==nombre = precio
                                        | otherwise = buscarPrecio prod ys 


--4) 
aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
aplicarOferta _ [] = []
aplicarOferta productos ((nombre, precio):ys) | ((stockDeProducto2 productos nombre ) > 10) = (nombre, (0.8 * precio)) : aplicarOferta productos ys
                                              | otherwise = (nombre, precio) : aplicarOferta productos ys

--9) 
divisoresPropios :: Int -> [Int]
divisoresPropios 2 = [1]
divisoresPropios n = divisoresN n (n-1)

divisoresN :: Int -> Int -> [Int]
divisoresN _ 1 = [1]
divisoresN n m | m<n && mod n m == 0 =  divisoresN n (m-1) ++ [m]
               | otherwise = divisoresN n (m-1)

sonAmigos :: Int ->Int ->Bool
sonAmigos n m = (sumaDivisores(divisoresN m (m-1)) == n && sumaDivisores(divisoresN n (n-1)) == m )

sumaDivisores :: [Int] -> Int
sumaDivisores [] = 0
sumaDivisores (x:xs) = x + sumaDivisores xs 



{-losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 1 = [6]
losPrimerosNPerfectos n  = NPerfecto n 3 : losPrimerosNPerfectos (n-1)
-}

listaAmigos :: [Int] -> [(Int,Int)]
listaAmigos [] = []
listaAmigos [x] = []
listaAmigos (x:xs) | tieneAmigo x xs = (x,buscarAmigo x xs) : listaAmigos xs 
                   | otherwise = listaAmigos xs 

tieneAmigo :: Int -> [Int] -> Bool
tieneAmigo _ [] = False
tieneAmigo n (x:xs) | sonAmigos n x = True
                    | otherwise = tieneAmigo n xs 

buscarAmigo :: Int -> [Int] -> Int
buscarAmigo n (x:xs) | sonAmigos n x = x
                     | otherwise = buscarAmigo n xs 


maximo :: [[Integer]] ->Integer
maximo [x] = mayor x
maximo (x:y:xs) | mayor x < mayor y = maximo (y:xs)
                | otherwise = maximo (x:xs)

mayor :: [Integer] -> Integer
mayor [a] = a
mayor (a:b:cs) | a<b = mayor (b:cs)
               | otherwise = mayor (a:cs) 
--
masRepetido ::  [[Int]] ->Int 
masRepetido tablero = mayorApariciones(aplanar tablero) 

aplanar :: [[Int]] -> [Int]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs 

contarApariciones :: Int -> [Int] -> Int
contarApariciones _ [] = 0
contarApariciones n (x:xs) | n==x = 1 + contarApariciones n xs
                           | otherwise = contarApariciones n xs 

mayorApariciones :: [Int] -> Int
mayorApariciones [x] = x
mayorApariciones (x:y:xs) | contarApariciones x (y:xs) >= contarApariciones y (x:xs) = mayorApariciones (x:xs)
                          | otherwise = mayorApariciones (y:xs)


valoresDeCamino :: [[Integer]]-> [(Integer,Integer)] ->[Integer]
valoresDeCamino _ [] = []
valoresDeCamino (x:xs) ((fila, columna):ys) = (buscarColumna(buscarFila(x:xs) fila) columna) : valoresDeCamino (x:xs) ys



buscarFila :: [[Integer]] -> Integer -> [Integer]
buscarFila [] _ = []
buscarFila (x:xs) 1 = x
buscarFila (x:xs) n | n == longitud(x:xs) = last(x:xs) 
                    | otherwise = buscarFila(sacarUltimo(x:xs)) n 

sacarUltimo :: [[Integer]] -> [[Integer]] 
sacarUltimo [x] = []
sacarUltimo (x:xs) = x: sacarUltimo xs 

sacarUltimo2 :: [Integer] -> [Integer] 
sacarUltimo2 [x] = []
sacarUltimo2 (x:xs) = x: sacarUltimo2 xs 


longitud :: [[Integer]] -> Integer

longitud [] = 0
longitud (x:xs) = 1 + longitud xs

longitud2 :: [Integer] -> Integer
longitud2 [] = 0
longitud2 (x:xs) = 1 + longitud2 xs


buscarColumna :: [Integer] -> Integer -> Integer
buscarColumna [x] 1 = x
buscarColumna (x:xs) n | n== longitud2(x:xs) = last(x:xs) 
                       | otherwise = buscarColumna(sacarUltimo2(x:xs)) n 

--------------------------- ver

fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo n = fibo(n-1) + fibo(n-2)

listaFibo :: Int -> [Int]
listaFibo 0 = [1]
listaFibo 1 = [1]
listaFibo n =  listaFibo (n - 1) ++ [fibo n]


listaSoloFibo :: [Int] -> [Int]
listaSoloFibo [] = []
listaSoloFibo (x:xs) | esFibo x = x: listaSoloFibo xs 
                     | otherwise = listaSoloFibo xs 


esFibo x = pertenece2 x (listaFibo (x+1))

pertenece2 :: Int -> [Int] -> Bool
pertenece2 _ [] = False
pertenece2 p (x:xs) | p==x = True
                    | otherwise = pertenece2 p xs 

dejarDesde :: [Int] -> Int -> [Int]
dejarDesde [] _ = []
dejarDesde (x:xs) n | n==x = xs
                    | otherwise = dejarDesde xs n 


--esCaminoFibo :: [Int] -> Int -> Bool
--esCaminoFibo (x:xs) n = (dejarDesde (listaSoloFibo (x:xs)) n)                       

---------------------

minimo :: [[Int]] -> Int
minimo tablero = buscarMinimo(aplanar2 tablero)

aplanar2 :: [[Int]] -> [Int]
aplanar2 [x] = x
aplanar2 (x:xs) = x ++ aplanar2 xs

buscarMinimo :: [Int] -> Int
buscarMinimo [x] = x
buscarMinimo (x:y:xs) | x<= y = buscarMinimo(x:xs)
                      | otherwise = buscarMinimo (y:xs)

--
repetidos :: [[Int]] -> [Int]
repetidos tablero =  listaTerminada(aplanar2 tablero) 

listaTerminada :: [Int] -> [Int]
listaTerminada [] = []
listaTerminada (x:xs) | (cantidadDeRepeticiones (x:xs)) +1 >=2 = x : listaTerminada (eliminarApariciones x xs)
                      | otherwise = listaTerminada xs


cantidadDeRepeticiones ::  [Int] -> Int
cantidadDeRepeticiones [x] = 0
cantidadDeRepeticiones  (x:y:xs) | x==y = 1 + cantidadDeRepeticiones (y:xs)
                                 | otherwise = cantidadDeRepeticiones (x:xs)

eliminarApariciones :: Int -> [Int] -> [Int]
eliminarApariciones _ [] = []
eliminarApariciones n (x:xs) | n==x = eliminarApariciones n xs
                             | otherwise = x: eliminarApariciones n xs  


-- igual al anterior
{-valoresDeCamino2 :: [[Int]] -> [(Int,Int)] -> [Int]
valoresDeCamino2 _ [] = []
valoresDeCamino2 (x:xs) ((fila, columna):ys) = (buscoColumna (buscoFila (x:xs) fila) columna) : valoresDeCamino (x:xs) ys


buscoFila :: [[Int]] -> Int -> [Int]
buscoFila [] _ = []
buscoFila (x:xs) n | n== longitud (x:xs) = ultimo xs 
                   | otherwise = buscoFila(sacarUlt (x:xs)) n 

ultimo :: [[Int]] -> [Int]
ultimo [x] = x
ultimo (x:xs) = ultimo xs

sacarUlt :: [[Int]] -> [[Int]]
sacarUlt [x] = []
sacarUlt (x:xs) = x: sacarUlt xs 

buscoColumna :: [Int] -> Int -> Int
buscoColumna [x] 1 = x
buscoColumna (x:xs) n | n==length(x:xs) = last xs 
                      | otherwise = buscoColumna(sacarUlti(x:xs)) n

sacarUlti :: [Int] -> [Int]
sacarUlti [x] = []
sacarUlti (x:xs) = x: sacarUlti xs -}