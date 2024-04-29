module ParcialHaskell where 

-- PARCIAL SEG. CUATRIMESTRE 2023
--1)
atajaronSuplentes :: [(String,String)] -> [Int] -> Int -> Int
atajaronSuplentes _ goles totalDeGolesTorneo = totalDeGolesTorneo - golesDeTitulares goles

golesDeTitulares :: [Int] -> Int
golesDeTitulares [] = 0 
golesDeTitulares (x:xs) = x + golesDeTitulares xs 


--2)

equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((x, y):xs) = nombreValido && equiposValidos xs
  where nombreValido = not (elem x ( equiposValidosAux xs)) && not (elem y ( equiposValidosAux xs))

equiposValidosAux :: [(String, String)] -> [String]
equiposValidosAux [] = []
equiposValidosAux ((x, y):xs) = x : y : equiposValidosAux xs 

--3) 
porcentajeDeGoles :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeGoles arquero arqueroPorEquipo goles = division ((golesDeArquero arquero arqueroPorEquipo goles)*100) (golesDeTitulares goles)


golesDeArquero :: String -> [(String,String)] -> [Int] -> Int
golesDeArquero arquero ((equipo,nombre):xs) (goles:ys)  | nombre == arquero = goles 
                                              | otherwise = golesDeArquero arquero xs ys 

--4) 
menosGoles :: [Int] -> Int
menosGoles [x] = x
menosGoles (x:y:xs) | x <= y = menosGoles (x:xs)
                    | otherwise = menosGoles (y:xs)

vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida ((equipo,nombre):xs) (goles:ys) | (menosGoles (goles:ys) == goles) = nombre
                              | otherwise = vallaMenosVencida xs ys

--PARCIAL 25/08/2023

--1)
--Funcion auxiliar para el ejercicio 1
votosValidosAux :: [Int] -> Int
votosValidosAux [] =  0
votosValidosAux (x:xs) = x + votosValidosAux xs

--EJERCICIO 1
votosEnBlanco :: [(String,String)] -> [Int] -> Int -> Int
votosEnBlanco _ votos votosTotales = votosTotales - (votosValidosAux votos)

--2) 
formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((x,y):xs) = formulasAceptadas && formulasValidas xs
 where formulasAceptadas = not(elem x (formulasValidasAux xs)) && not(elem y (formulasValidasAux xs))

formulasValidasAux :: [(String,String)] -> [String]
formulasValidasAux [] = []
formulasValidasAux ((x,y):xs) = x: y: formulasValidasAux xs 


--3)
porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos presidente formulas votos = division ((cantidadDeVotos presidente formulas votos)*100) (votosValidosAux votos)

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b) 

cantidadDeVotos :: String -> [(String,String)] -> [Int] -> Int
cantidadDeVotos presidente ((candidato,vice):xs) (votos:ys)  | candidato == presidente = votos 
                                              | otherwise = cantidadDeVotos presidente xs ys 

--4)

-- 25/08

--1) 
{-porcentajeDeVotosAfirmativos :: [(String,String)] -> [Integer] -> Integer -> Float
porcentajeDeVotosAfirmativos formula votos cantTotalVotos = (division (votosAceptados votos) cantTotalVotos) * 100 

division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)  


votosAceptados :: [Integer] -> Integer
votosAceptados [] = 0
votosAceptados (x:xs) = x: votosAceptados xs 
-}

--2)
formulasInvalidas :: [(String,String)] -> Bool
formulasInvalidas [] = False 
formulasInvalidas ((x,y):xs) = formulasNoAcep && formulasInvalidas xs 
 where formulasNoAcep = (elem x(formulasInvalidasAux xs)) && (elem y(formulasInvalidasAux xs))

formulasInvalidasAux :: [(String,String)] -> [String]
formulasInvalidasAux [] = []
formulasInvalidasAux ((x,y):xs) = x: y: formulasInvalidasAux xs  

{- TAMBIEN SE PUEDE RESOLVER ASI 
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

listaFormulas :: [(String, String)] -> [String]
listaFormulas [] = []
listaFormulas ((x,y):xs) = x : y : listaFormulas xs

formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((x,y):xs) | x == y || pertenece x (listaFormulas xs) || pertenece y (listaFormulas xs) = True
                             | otherwise = formulasInvalidas xs
-}

--3) 
{- 
porcentajeDeVotos2 :: [String] -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos2 vice formula votos = division((porcentajeVice vice formula votos)*100) && (votosValidosAux votos)

porcentajeVice :: [String] -> [(String,String)] -> [Int] -> Int
porcentajeVice vice ((candidato1,candidato2):xs) (votos:ys) | vice == candidato2 = votos
                                                            | otherwise = porcentajeVice xs ys 
-}

--4)
menosVotos :: [Int] -> Int
menosVotos [x] = x
menosVotos (x:y:xs) | x <= y = menosVotos (x:xs)
                    | otherwise = menosVotos (y:xs)

menosVotado :: [(String, String)] -> [Int] -> String
menosVotado ((candidato,vice):xs) (votos:ys) | (menosVotos (votos:ys) == votos) = candidato
                              | otherwise = menosVotado xs ys


                              


