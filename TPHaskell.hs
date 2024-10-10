module TPHaskell where

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)
type AgenciaDeViajes = [Vuelo]


--1)
vueloValido :: [(String, String,Float)] -> Bool
vueloValido [(v1,v2,t)] = v1/=v2 && t>0

pertenece ::  (String,String,Float) -> [(String,String,Float)] -> Bool
pertenece  _ [] = False
pertenece (x1,x2,t1) ((x11,x22,t2):xs) | (x1 == x11 && x2 == x22) = True
                                       | otherwise = pertenece (x1,x2,t1) xs

vuelosValidos :: [(String,String,Float)] -> Bool
vuelosValidos [] = True 
vuelosValidos [(v1,v2,t)] = vueloValido([(v1,v2,t)])
vuelosValidos ((v1,v2,t):xs) | not(vueloValido [(v1,v2,t)]) || pertenece (v1,v2,t) xs  = False
                             | otherwise = vuelosValidos xs 

--2)
ciudadesConectadas ::  [(String,String,Float)] -> String -> [String]
ciudadesConectadas [] _ = []
ciudadesConectadas ((x1,x2,t1):xs) n | n==x2  = x1: ciudadesConectadas (ciudadesConectadasAux xs x1) n 
                                     | n==x1  = x2: ciudadesConectadas (ciudadesConectadasAux xs x2) n 
                                     | otherwise = ciudadesConectadas xs n

-- ciudadesConectadasAux toma la ciudad agregada en res y deja los vuelos sin esa ciudad para no tener repetidos en res
ciudadesConectadasAux :: [(String,String,Float)] -> String -> [(String,String,Float)] 
ciudadesConectadasAux [] _ = []
ciudadesConectadasAux ((x1,x2,t1):xs) n | (n/=x1 && n/=x2) = (x1,x2,t1) : ciudadesConectadasAux xs n
                                        | otherwise = ciudadesConectadasAux xs n 


--4)
ciudadMasConectada :: AgenciaDeViajes -> Ciudad
ciudadMasConectada agencia = mayorCantidadApariciones(aplanar agencia) 

-- Defino aplanar para juntar todas las ciudades en una sola lista, sin considerar la duracion del vuelo
aplanar :: AgenciaDeViajes -> [Ciudad]
aplanar [] = []
aplanar ((x1,x2,_):xs) = x1 : x2:  aplanar xs

-- Devuelvo la ciudad que mayores apariciones tiene en la lista de ciudades resultante de aplanar 
mayorCantidadApariciones :: [Ciudad] -> Ciudad
mayorCantidadApariciones [x] = x
mayorCantidadApariciones (x:y:xs) | cantidadApariciones x xs >= cantidadApariciones y xs = mayorCantidadApariciones(x:xs)
                                  | otherwise = mayorCantidadApariciones (y:xs) 

-- cantidadApariciones cuenta la cantidad de veces que aparece una ciudad en la lista de ciudades resiltante de aplanar 
cantidadApariciones :: Ciudad -> [Ciudad] -> Integer
cantidadApariciones _ []  = 0
cantidadApariciones n (x:xs)  | n==x = 1 + cantidadApariciones n xs
                              | otherwise = cantidadApariciones n xs  

{-eliminarRepeticiones :: [String] -> [String]
eliminarRepeticiones [] = []
eliminarRepeticiones (x:xs) = x : eliminarRepeticionesAux x xs

eliminarRepeticionesAux :: String -> [String] -> [String]
eliminarRepeticionesAux _ []  = []
eliminarRepeticionesAux x (y:xs) | x==y = eliminarRepeticionesAux x xs
                                 | otherwise = y: eliminarRepeticionesAux x xs-}

