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


--SIMULACRO 

--1)
relacionesValidas :: [(String, String)] -> Bool 
relacionesValidas [] = True
relacionesValidas (unaAmistad:masLista) = not (mismaPersona unaAmistad) && not (amistadRepetida unaAmistad masLista) && pasoRecursivo
                                        where pasoRecursivo = relacionesValidas masLista

mismaPersona:: (String, String) -> Bool
mismaPersona (a,b) = a == b

amistadRepetida :: (String, String) -> [(String, String)] -> Bool
amistadRepetida _ [] = False
amistadRepetida a (b:elResto) = mismaAmistad a b || amistadRepetida a elResto
                                where mismaAmistad (a,b) (c,d) = (a==c && b == d) || (a==d && b == c) 

{- COMO LO HICE YO:
  relacionesValidas :: [(String,String)] -> Bool
  relacionesValidas [] = True
  relacionesValidas ((a,b):xs) | pertenece (a,b) xs = False
                               | pertenece (b,a) xs = false
                               | a==b = False
                               | otherwise = relacionesValidas xs

  pertenece :: Int -> [Int] -> Bool
  pertenece _ [] = False
  pertenece n ((a,b):xs) | n==a = True
                         | otherwise = pertenece n xs 


-}


--2)
personas :: [(String,String)] -> [String]
personas rs = eliminarRepetidos (personasConRepes rs)

personasConRepes :: [(String,String)] -> [String]
personasConRepes [] = []
personasConRepes ((p1,p2):rs) = p1 : p2 : personasConRepes rs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitarTodos x xs)

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                    | otherwise = x:(quitarTodos e xs)

{-
personas :: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) | pertenece a xs || pertenece b xs = personas xs
                    | pertenece a xs = b: personas xs
                    | pertenece b xs = a: personas xs 
                    | otherwise = a:b: personas xs 



-}

--3)
amigosDe :: String -> [(String, String)] -> [String] 
amigosDe a [] = []
amigosDe a ((p1,p2):elResto) 
    | a == p1 = p2 : pasoRecursivo
    | a == p2 = p1 : pasoRecursivo
    | otherwise = pasoRecursivo 
    where pasoRecursivo = amigosDe a elResto

{-
amigosDe :: String -> [(String, String)] -> [String] 
amigosDe _ [] = []
amigosDe persona ((a,b):xs) | persona==a = b: amigosDe persona xs 
                            | persona== b = a: amigosDe persona xs 
                            | otherwise = amigosDe persona xs 

-}


--4)
personaConMasAmigos :: [(String, String)] -> String 
personaConMasAmigos relaciones =  personaConMasAmigosAux personasDeRelacion (cantidadDeAmigosDePersonas personasDeRelacion relaciones) 
                                    where personasDeRelacion = personas relaciones

cantidadDeAmigosDePersonas :: [String] -> [(String, String)] -> [Int]
cantidadDeAmigosDePersonas [] _ = []
cantidadDeAmigosDePersonas (p1:ps) relaciones = longitud (amigosDe p1 relaciones) : pasoRecursivo
                                                where pasoRecursivo = cantidadDeAmigosDePersonas ps relaciones

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

personaConMasAmigosAux :: [String] -> [Int] -> String
personaConMasAmigosAux [p1] _ = p1
personaConMasAmigosAux (p1:p2:ps) (c1:c2:cs) | c1 > c2 = personaConMasAmigosAux (p1:ps) (c1:cs)
                                             | otherwise = personaConMasAmigosAux (p2:ps) (c2:cs)

                              


