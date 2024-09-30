--2) 
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas ((pres, vice):xs) | pres==vice = False
                                  | pertenece pres xs || pertenece vice xs = False
                                  | otherwise = formulasValidas xs 

pertenece :: String ->  [(String, String)] -> Bool
pertenece _ [] = False
pertenece candidato ((p, v):xs) | candidato==p || candidato==v = True
                                | otherwise = pertenece candidato xs 

--1)
votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int 
votosEnBlanco _ votos cantTotalVotos = cantTotalVotos - votosNoBlancos votos 

votosNoBlancos :: [Int] -> Int
votosNoBlancos [] = 0
votosNoBlancos (x:xs) = x + votosNoBlancos xs 

--3) 
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos p formula votos = (division (votosDeP p formula votos) (votosNoBlancos votos)) * 100

votosDeP :: String -> [(String, String)] -> [Int] -> Int
votosDeP _ _ [] = 0
votosDeP p ((pres, vice):xs) (voto:ys) | p==pres = voto
                                       | otherwise = votosDeP p xs ys

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)


--4) 
proximoPresidente ::  [(String, String)] -> [Int] -> String
proximoPresidente [(a,_)] _ = a 
proximoPresidente ((p1, vice1):(p2, vice2):xs) (v1:v2:ys) | v1 > v2 = proximoPresidente ((p1,vice1):xs) (v1:ys)
                                                          | otherwise =  proximoPresidente ((p2,vice2):xs) (v2:ys)


--------------------
--5)
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos _ votos cantTotalVotos = (division (votosNoBlancos votos) cantTotalVotos) * 100

--6) 
menosVotado ::  [(String, String)] -> [Int] -> String 
menosVotado [(_,b)] _ = b
menosVotado ((p1, v1):(p2, v2):xs) (voto1:voto2:ys) | voto1 < voto2 = menosVotado ((p1, v1):xs) (voto1:ys) 
                                                    | otherwise = menosVotado ((p2, v2):xs) (voto2:ys)

-------------------------
--7) 

aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias registro alumno n =  notasMayoresIguales4 (notasAlumno registro alumno) > n

notasAlumno :: [(String, [Int])] -> String -> [Int]
notasAlumno [] _ = []
notasAlumno ((alumno, notas):xs) nombre | nombre==alumno = notas
                                        | otherwise = notasAlumno xs nombre 

notasMayoresIguales4 :: [Int] -> Int
notasMayoresIguales4 [] = 0
notasMayoresIguales4 (x:xs) | x>=4 = 1 + notasMayoresIguales4 xs 
                            | otherwise = notasMayoresIguales4 xs 

-- aproboMasDeNMaterias [("m",[1,4,6]),("s",[4,5,6])] "s" 2

--8)
buenosAlumnos :: [(String, [Int])] -> [String] 
buenosAlumnos registro = listaBuenosAlumnos registro


listaBuenosAlumnos :: [(String, [Int])] -> [String]
listaBuenosAlumnos [] = []
listaBuenosAlumnos ((alumno, notas):xs) | (promedio notas)>=8 && noTieneAplazos notas = alumno: listaBuenosAlumnos xs 
                                        | otherwise = listaBuenosAlumnos xs


cantidadDeNotasTotal :: [Int] -> Int
cantidadDeNotasTotal [] = 0
cantidadDeNotasTotal (x:xs) = 1 + cantidadDeNotasTotal xs 

sumaDeNotas :: [Int] -> Int
sumaDeNotas [x] = x
sumaDeNotas (x:xs) = x + sumaDeNotas xs 

promedio :: [Int] -> Float
promedio notas = (fromIntegral (sumaDeNotas notas)) / (fromIntegral (cantidadDeNotasTotal notas))

noTieneAplazos :: [Int] -> Bool
noTieneAplazos [] = True
noTieneAplazos (x:xs) | x<4 = False
                      | otherwise = noTieneAplazos xs 


--9)
mejorPromedio :: [(String, [Int])] -> String
mejorPromedio [(a,_)] = a
mejorPromedio ((alumno1, notas1):(alumno2, notas2):xs) | (promedio notas1) >= (promedio notas2) = mejorPromedio ((alumno1, notas1):xs) 
                                                       | otherwise = mejorPromedio ((alumno2, notas2):xs)

--10) 
seGraduoConHonores :: [(String, [Int])] -> String -> Int -> Bool
seGraduoConHonores registro nombre cantidadDeMateriasDeLaCarrera = (aproboMasDeNMaterias registro nombre (cantidadDeMateriasDeLaCarrera -1)) && (pertenece2 nombre (buenosAlumnos registro)) && ((promedio(notasAlumno registro nombre) ) >= ((notaMejorPromedio registro) -1))

pertenece2 :: String -> [String] -> Bool
pertenece2 _ [] = False
pertenece2 nombre (x:xs) | nombre==x = True
                        | otherwise = pertenece2 nombre xs 

notaMejorPromedio :: [(String, [Int])] -> Float
notaMejorPromedio [(_,notas)] = promedio notas
notaMejorPromedio ((alumno1, notas1):(alumno2, notas2):xs) | (promedio notas1) >= (promedio notas2) = notaMejorPromedio ((alumno1, notas1):xs) 
                                                           | otherwise = notaMejorPromedio ((alumno2, notas2):xs)


--------- ej 4 y 5 guia5

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x==' ' && x==y =  sacarBlancosRepetidos (y:xs)
                               | otherwise = x: sacarBlancosRepetidos (y:xs) 
--
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras palabras = contarEspacios(sacarEspFinal(sacarEspIn (sacarBlancosRepetidos palabras))) + 1

sacarEspIn :: [Char] -> [Char]
sacarEspIn [] = []
sacarEspIn (x:xs) | x==' ' = xs
                  | otherwise = (x:xs)

sacarEspFinal :: [Char] -> [Char]
sacarEspFinal [] = []
sacarEspFinal [' '] = []
sacarEspFinal (x:xs) = x: sacarEspFinal xs

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x==' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs 

--
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras p = primeraPalabra(sacarEspFinal(sacarEspIn (sacarBlancosRepetidos p))) : palabras(sacarPrimeraPalabra(sacarEspFinal(sacarEspIn (sacarBlancosRepetidos p))))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x==' ' = []
                      | otherwise = x: primeraPalabra xs 

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x/=' ' = sacarPrimeraPalabra xs 
                           | otherwise = xs 

--
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga p = mayorCaracteres(palabras p)

mayorCaracteres :: [[Char]] -> [Char]
mayorCaracteres [x] = x
mayorCaracteres (x:y:xs) | cantidadCaracteres x >= cantidadCaracteres y = mayorCaracteres(x:xs)
                         | otherwise = mayorCaracteres(y:xs)

cantidadCaracteres :: [Char] -> Integer
cantidadCaracteres [] = 0 
cantidadCaracteres (x:xs) = 1 + cantidadCaracteres xs 

--
aplanarConNBlancos ::  [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (x:xs) n = x ++ nBlancos n ++ aplanarConNBlancos xs n

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = ' ' : nBlancos(n-1)

--5
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [x] = [x]
sumaAcumulada (x:xs) = sumaAcumuladaAux (x:xs) 0 

sumaAcumuladaAux :: (Num t) => [t] -> t -> [t]
sumaAcumuladaAux [] _ = []
sumaAcumuladaAux (x:xs) n = (x+n) : sumaAcumuladaAux xs (x+n)

descomponerEnPrimos :: [Integer] -> [[Integer]] 
descomponerEnPrimos [x] = [(descomponerEnPrimosAux x 2)]
descomponerEnPrimos (x:xs) = [(descomponerEnPrimosAux x 2)] ++ descomponerEnPrimos xs 

descomponerEnPrimosAux :: Integer -> Integer -> [Integer]
descomponerEnPrimosAux x n | x<n = []
                           | mod x n == 0 = n : descomponerEnPrimosAux (div x n) n 
                           | otherwise = descomponerEnPrimosAux x (n+1)

---- 

