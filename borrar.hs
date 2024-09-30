
--4) 

sacarBlancosRepetidos2 :: [Char] -> [Char]
sacarBlancosRepetidos2 [x] = [x]
sacarBlancosRepetidos2 (x:y:xs) | x==' ' && x==y =  sacarBlancosRepetidos2 (y:xs)
                               | otherwise = x: sacarBlancosRepetidos2 (y:xs)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) = contar(limpiar(x:xs)) + 1 

limpiar :: [Char] -> [Char]
limpiar (x:xs) = sacarEspIn(sacarEspFin(sacarBlancosRepetidos2 (x:xs))) 

sacarEspFin :: [Char] -> [Char]
sacarEspFin [] = []
sacarEspFin [' '] = []
sacarEspFin (x:xs) = x: sacarEspFin xs 

sacarEspIn :: [Char] -> [Char]
sacarEspIn [] = []
sacarEspIn (x:xs) | x==' ' = xs
                  | otherwise = (x:xs)

                
contar :: [Char] -> Integer
contar [] = 0
contar (x:xs) | x==' ' = 1 + contar xs 
              | otherwise = contar xs  

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras xs = primeraPalabra(limpiar xs) : palabras(sacarPrimeraPalabra(limpiar xs))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x==' ' = []
                      | otherwise = x: primeraPalabra xs  

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x== ' ' =  xs
                           | otherwise = sacarPrimeraPalabra xs 


palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga xs = laMasLarga(limpiar xs)

laMasLarga :: [Char] -> [Char]
laMasLarga xs | sacarPrimeraPalabra xs == [] = primeraPalabra xs 
              | length(primeraPalabra xs) > length(laMasLarga xs) = primeraPalabra xs
              | otherwise = laMasLarga(sacarPrimeraPalabra xs )

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs 

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



