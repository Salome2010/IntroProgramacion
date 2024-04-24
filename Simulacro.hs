module Simulacro where 

--Funcion para utilizar 
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

--2) 
personas :: [(String, String)] -> [String]
personas [] = []
personas ((a,b):xs) | pertenece a (personas xs) && pertenece b (personas xs) = personas xs 
                    | pertenece a (personas xs) = b: personas xs 
                    | pertenece b (personas xs) = a: personas xs 
                    | otherwise = a:b: personas xs 

--3)
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a,b):xs) | persona == a = b: amigosDe persona xs 
                            | persona == b = a: amigosDe persona xs
                            | otherwise = amigosDe persona xs 