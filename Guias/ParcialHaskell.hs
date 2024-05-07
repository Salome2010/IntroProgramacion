module ParcialHaskell where 

-------------------------PARCIAL SEG. CUATRIMESTRE 2023----------------
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
porcentajeDeGoles arquero arqueroPorEquipo goles = (division (golesDeArquero arquero arqueroPorEquipo goles) (golesDeTitulares goles))*100



golesDeArquero :: String -> [(String,String)] -> [Int] -> Int
golesDeArquero arquero ((equipo,nombre):xs) (goles:ys)  | nombre == arquero = goles 
                                              | otherwise = golesDeArquero arquero xs ys 

--4) 
{-menosGoles :: [Int] -> Int
menosGoles [x] = x
menosGoles (x:y:xs) | x <= y = menosGoles (x:xs)
                    | otherwise = menosGoles (y:xs)

vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida ((equipo,nombre):xs) (goles:ys) | (menosGoles (goles:ys) == goles) = nombre
                              | otherwise = vallaMenosVencida xs ys
-}
vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida [(_,j)] [_] = j
vallaMenosVencida (x:x2:xs) (y:y2:ys) | y>y2 = vallaMenosVencida (x2:xs) (y2:ys)
                                      | otherwise = vallaMenosVencida (x:xs) (y:ys)


---------------------PARCIAL 25/08/2023--------------------

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
proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente [(j,_)] [_] = j 
proximoPresidente (x:x1:xs) (y:y1:ys) | y>y1 = proximoPresidente (x:xs) (y:ys)
                                      | otherwise = proximoPresidente (x1:xs) (y1:ys) 

-------------------------------- 25/08--------------------

--1) 
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos _ votos cantTotalVotos = (division (sumaVotosAfirmativos votos) cantTotalVotos) * 100

sumaVotosAfirmativos :: [Int] -> Int
sumaVotosAfirmativos [] = 0
sumaVotosAfirmativos (x:xs) = x + sumaVotosAfirmativos xs

--2)
{-formulasInvalidas :: [(String,String)] -> Bool
formulasInvalidas [] = False 
formulasInvalidas ((x,y):xs) = formulasNoAcep && formulasInvalidas xs 
 where formulasNoAcep = (elem x(formulasInvalidasAux xs)) && (elem y(formulasInvalidasAux xs))

formulasInvalidasAux :: [(String,String)] -> [String]
formulasInvalidasAux [] = []
formulasInvalidasAux ((x,y):xs) = x: y: formulasInvalidasAux xs  
-}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((x,y):xs) | pertenece (x,y) xs = True
                             | pertenece (y,x) xs = True
                             | pertenece x (listaDeFormulas xs) = True
                             | pertenece y (listaDeFormulas xs) = True
                             | x==y = True
                             | otherwise = formulasInvalidas xs

listaDeFormulas :: [(String,String)] -> [String]
listaDeFormulas [] = []
listaDeFormulas ((x,y):xs) = x:y: listaDeFormulas xs 


--3) 

porcentajeDeVotos2 :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos2 vice formula votos = (division( votosVice vice formula votos) (sumaVotosAfirmativos votos))*100

votosVice :: String -> [(String,String)] -> [Int] -> Int
votosVice vice ((candidato,candVice):xs) (votos:ys) | candVice==vice  = votos
                                                    | otherwise = votosVice vice xs ys 


--4)
menosVotado :: [(String, String)] -> [Int] -> String
menosVotado [(j,_)] [_] = j
menosVotado (x:x1:xs) (y:y1:ys) | y>y1 = menosVotado (x1:xs) (y1:ys)
                                | otherwise = menosVotado (x:xs) (y:ys)

-------------------------------SIMULACRO-------------------- 

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
{-

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

-}



personas :: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) | pertenece a (listasPersonas xs) && pertenece b (listasPersonas xs) = personas xs
                    | pertenece a  (listasPersonas xs)= b: personas xs
                    | pertenece b (listasPersonas xs) = a: personas xs 
                    | otherwise = a:b: personas xs 

listasPersonas :: [(String,String)] -> [String]
listasPersonas [] = []
listasPersonas ((a,b):xs) = a:b: listasPersonas xs 



--3)

{-

amigosDe :: String -> [(String, String)] -> [String] 
amigosDe a [] = []
amigosDe a ((p1,p2):elResto) 
    | a == p1 = p2 : pasoRecursivo
    | a == p2 = p1 : pasoRecursivo
    | otherwise = pasoRecursivo 
    where pasoRecursivo = amigosDe a elResto

-}


amigosDe :: String -> [(String, String)] -> [String] 
amigosDe _ [] = []
amigosDe p ((a,b):xs) | a==p = b: amigosDe p xs 
                      | b==p = a: amigosDe p xs 
                      | otherwise = amigosDe p xs 




--4)
{-personaConMasAmigos :: [(String, String)] -> String 
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

-}
-------------------------PARCISL HECHO EN CLASE 02/05-----------------

--1)
golesDeNoGoleadores :: [(String,String)] -> [Int] -> Int -> Int 
golesDeNoGoleadores _ goles totslGolesTorneo = totslGolesTorneo - sumaGolesDeGoleadores goles 

sumaGolesDeGoleadores :: [Int] -> Int
sumaGolesDeGoleadores [] = 0
sumaGolesDeGoleadores (x:xs) = x + sumaGolesDeGoleadores xs 

--2) ya lo hice en otro ej
{-equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos ((a,b):xs) = equiposAcep && equiposValidos xs
  where equiposAcep = not(elen a(equiposValidosAux xs)) && not(elem b(equiposValidosAux xs))

equiposValidosAux :: [(String,String)] -> [String]
equiposValidosAux [] = []
equiposValidosAux ((a,b):xs) = a:b: equiposValidosAux xs 

-------------haciendo con pertenece:----------

pertenece :: Int -> [Int] -> Bool
petenece a [] = False
pertenece a (x:xs) | a==x = True
                   | otherwise = pertenece a xs

equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos ((a,b):xs) | pertenece (a,b) xs = False
                          | pertenece (b,a) xs = False
                          | a==b = False
                          | otherwise = equiposValidos xs 





-}

--3) tambien es otro ej 
porcentajeDeGoless :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeGoless goleador goleadoresPorEquipo goles = (division(golesGoleador goleador goleadoresPorEquipo goles) (sumaGolesDeGoleadores goles))*100

golesGoleador :: String -> [(String,String)] -> [Int] -> Int
golesGoleador goleador ((equipo,nombre):xs) (goles:ys) | nombre==goleador = goles 
                                                            | otherwise = golesGoleador goleador xs ys 


--4) 
botinDeOro :: [(String,String)] -> [Int] -> String
botinDeOro [(_,j)] [_]= j
botinDeOro (x:x1:xs) (y:y1:ys) | y>y1 = botinDeOro (x:xs) (y:ys)
                               | otherwise = botinDeOro (x1:xs) (y1:ys)  


------------ parcial 06/05 ------------

--1) 
hayQueCodificar :: Char -> [(Char,Char)] -> Bool 
hayQueCodificar c [] = False
hayQueCodificar c ((a,_):xs) | c==a = True
                             | otherwise = hayQueCodificar c xs 

--2) 

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int 
cuantasVecesHayQueCodificar _ [] _ = 0 
cuantasVecesHayQueCodificar c (x:xs) mapeo  | not (hayQueCodificar c mapeo) = 0 
                                            | c == x = 1 + cuantasVecesHayQueCodificar c xs mapeo
                                            | otherwise = cuantasVecesHayQueCodificar c xs mapeo 

--3)
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar (x:xs) mapeo = laQueMasHayQueCodificarAux x xs mapeo

laQueMasHayQueCodificarAux :: Char -> [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificarAux c [] _ = c
laQueMasHayQueCodificarAux c (x:xs) mapeo
    | cuantasVecesHayQueCodificar c (x:xs) mapeo >= cuantasVecesHayQueCodificar x (x:xs) mapeo = laQueMasHayQueCodificarAux c xs mapeo
    | otherwise = laQueMasHayQueCodificarAux x xs mapeo

--4) 
codificarFrase :: [Char] -> [(Char,Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (x:xs) mapeo | hayQueCodificar x mapeo = buscoRemplazo x mapeo : codificarFrase xs mapeo 
                            | otherwise = x: codificarFrase xs mapeo 

buscoRemplazo :: Char -> [(Char,Char)] -> Char
buscoRemplazo caracter ((a,remplazo):ys) | caracter==a = remplazo 
                                         | otherwise = buscoRemplazo caracter ys 


---------------- otro parcial 06/05-------------

--1)
aprobaronMasDeNMaterias :: [([Char],[Int])] -> [Char] -> Int -> Bool 
aprobaronMasDeNMaterias [] _ _ = False
aprobaronMasDeNMaterias ((nombre,notas):xs) alumno n | nombre==alumno = notasMayoresIguales4 notas>n 
                                                     | otherwise = aprobaronMasDeNMaterias xs alumno n 


notasMayoresIguales4 :: [Int] -> Int 
notasMayoresIguales4 [] = 0 
notasMayoresIguales4 (x:xs) | x>=4 = 1 + notasMayoresIguales4 xs
                            | otherwise = notasMayoresIguales4 xs 

--2) 
buenosAlumnos :: [([Char],[Int])] -> [[Char]] 
buenosAlumnos [] = []
buenosAlumnos ((nombre,notas):xs) | promedioDeNotas notas >= 8 && notasMayoresIguales4 notas /=0 = nombre: buenosAlumnos xs 
                                  | otherwise = buenosAlumnos xs 

promedioDeNotas :: [Int] -> Float 
promedioDeNotas [] = 0.0 
promedioDeNotas notas = fromIntegral (sumaDeNotas notas) / fromIntegral (cantidadDeNotas notas)

sumaDeNotas :: [Int] -> Int
sumaDeNotas [x] = x
sumaDeNotas (x:xs) = x + sumaDeNotas xs 

cantidadDeNotas :: [Int] -> Int
cantidadDeNotas [] = 0
cantidadDeNotas (x:xs) = 1 + cantidadDeNotas xs 

--3)
mejorPromedio :: [([Char],[Int])] -> [Char]
mejorPromedio [(j,_)] = j
mejorPromedio ((nombre1,notas1):(nombre2,notas2):xs) | promedioDeNotas notas1 >= promedioDeNotas notas2 = mejorPromedio((nombre1,notas1):xs)
                                                     | otherwise = mejorPromedio((nombre2,notas2):xs)

--4) 
seGraduoConHonores :: [([Char],[Int])] -> Int -> [Char] -> Bool
seGraduoConHonores reguistro cantidadDeMateriasDeLaCarrera alumno = aprobaronMasDeNMaterias reguistro alumno (cantidadDeMateriasDeLaCarrera -1) 
                                                                    && pertenece alumno (buenosAlumnos reguistro) 
                                                                 -- && promedioDeNotas () 

      