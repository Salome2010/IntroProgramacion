module Simulacro where 

--1)
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas relaciones = componentesDistintas relaciones  && sinRepetidos relaciones

componentesDistintas :: [(String, String)] -> Bool
componentesDistintas [] = True
componentesDistintas ((a,b):xs) | a/=b = componentesDistintas xs
                                | otherwise = False

sinRepetidos :: [(String, String)] -> Bool
sinRepetidos [x] = True
sinRepetidos ((a,b):xs) | pertenece (a,b) xs || pertenece (b,a) xs = False
                        | otherwise = sinRepetidos xs 


pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece tupla (x:xs) | tupla==x = True
                       | otherwise = pertenece tupla xs 


{--Funcion para utilizar 
pertenece :: (Eq t)=> t -> [t] -> Bool
pertenece _ [] = False
pertenece t (x:xs) | t==x = True
                   | otherwise = pertenece t xs 

--1)
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) | pertenece (a,b) xs = False
                             | pertenece (b,a) xs = False
                             | a==b = False 
                             | otherwise = relacionesValidas xs
-}

--2)
personas :: [(String, String)] -> [String]
personas [] =[]
personas ((a,b):xs) | pertenece2 a xs && pertenece2 b xs = personas xs
                    | pertenece2 a xs = b: personas xs
                    | pertenece2 b xs = a: personas xs
                    | otherwise = a:b: personas xs 

pertenece2 :: String -> [(String, String)] -> Bool
pertenece2 _ [] = False
pertenece2 x ((a,b):xs) | x==a || x==b = True
                        | otherwise = pertenece2 x xs 


{-

personas :: [(String, String)] -> [String]
personas [] = []
personas ((a,b):xs) | pertenece a (personas xs) && pertenece b (personas xs) = personas xs 
                    | pertenece a (personas xs) = b: personas xs 
                    | pertenece b (personas xs) = a: personas xs 
                    | otherwise = a:b: personas xs 
-}

--3) 
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a,b):xs) | persona==a = b: amigosDe persona xs
                            | persona==b = a: amigosDe persona xs
                            | otherwise = amigosDe persona xs 

--4)
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos relaciones = mayorCantidadApariciones(armarLista relaciones)

armarLista :: [(String, String)] -> [String]
armarLista [] = []
armarLista ((a,b):xs) = a:b: armarLista xs 

mayorCantidadApariciones :: [String] -> String
mayorCantidadApariciones [a] = a
mayorCantidadApariciones (a:b:xs) | cantApariciones a xs >= cantApariciones b xs = mayorCantidadApariciones(a:xs)
                                  | otherwise = mayorCantidadApariciones(b:xs)

cantApariciones :: String -> [String] -> Int
cantApariciones _ [] = 0
cantApariciones a (x:xs) | a==x  = 1+ cantApariciones a xs
                         | otherwise = cantApariciones a xs 