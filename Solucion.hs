module Solucion where
import Data.Char
-- No se permite agrear nuevos imports
-- Sólo está permitido usar estas funciones:
-- https://campus.exactas.uba.ar/pluginfile.php/557895/mod_resource/content/1/validas_tp.pdf


-- Completar!
-- Nombre de grupo: {Haskell (Taylor´s Version)}
-- Integrante1: { 45.753.027, Camila Nohara Arakaki}
-- Integrante2: { DNI2,apellidoYNombre2}
-- Integrante3: { DNI3,apellidoYNombre3}
-- Integrante4: { DNI4,apellidoYNombre4}
-- Integrantes que abandonaron la materia: {En caso que haya abandonado la materia algún
                        -- integrante, completar con los dni y apellidos, sino dejar vacío}


-- ejercicio 1
esMinuscula :: Char -> Bool 
esMinuscula c = ord c >= 97 && ord c <= 122



-- ejercicio 2
letraANatural :: Char -> Int
letraANatural c = (ord c) - 97 



-- ejercicio 3 
desplazar :: Char -> Int -> Char
desplazar caracter n | esMinuscula caracter == False = caracter 
                     | n >= 0 = natAChar(mod(charANat(caracter) + n) 26)
                     | otherwise = natAChar(mod(charANat(caracter) + n) 26)

charANat :: Char -> Int 
charANat c = ord c - 97

natAChar :: Int -> Char 
natAChar x = (chr (x+97)) 



-- ejercicio 4
cifrar :: String -> Int -> String
cifrar [] _ = [] 
cifrar (x:xs) n | esMinuscula x == True = desplazar x n : cifrar xs n
                | otherwise = x : cifrar xs n



-- ejercicio 5
descifrar :: String -> Int -> String
descifrar [] _ = []
descifrar (x:xs) n | esMinuscula x == True = desplazar x (-n) : descifrar xs n 
                   | otherwise = x : descifrar xs n



-- ejercicio 6
cifrarLista :: [String] -> [String]
cifrarLista [] = [] 
cifrarLista (x:xs) = invertirLista (cifrarListaHasta (invertirLista (x:xs)) 0)
 
longitudLista :: [String] -> Int
longitudLista [] = 0
longitudLista (x:xs) = 1 + longitudLista xs 

cifrarListaHasta :: [String] -> Int -> [String]
cifrarListaHasta [] 0 = []
cifrarListaHasta (x:xs) n = cifrar x (longitudLista (x:xs)-1) : cifrarListaHasta xs n


invertirLista :: [String] -> [String]
invertirLista [x] = [x]
invertirLista (x:xs) = invertirLista xs  ++ [x] 



-- ejercicio 7
frecuencia :: String -> [Float]
frecuencia (x:xs) = frecuenciaAux (x:xs) 97 

porcentaje :: Int -> Int -> Float
porcentaje x y = fromIntegral(x * 100) / fromIntegral (y)

longitudMinusculas :: String -> Int
longitudMinusculas [] = 0
longitudMinusculas (x:xs) | esMinuscula x == True = 1 + longitudMinusculas xs
                          | otherwise = longitudMinusculas xs 

cantidadApariciones :: Char -> String -> Int
cantidadApariciones _ [] = 0
cantidadApariciones a (x:xs) | a == x = 1 + cantidadApariciones a xs 
                             | otherwise = cantidadApariciones a xs 
 
frecuenciaAux :: String -> Int -> [Float]
frecuenciaAux _ 123 = []
frecuenciaAux (x:xs) n | pertenece (chr n) (x:xs)  = porcentaje (cantidadApariciones (chr n) (x:xs)) (longitudMinusculas(x:xs))  : (frecuenciaAux (x:xs) (n+1))  
                       | otherwise = 0 : (frecuenciaAux (x:xs) (n+1))

pertenece :: Char -> String -> Bool
pertenece c [] = False
pertenece c (x:xs) | c == x = True 
                   | otherwise = pertenece c xs  



--ejercicio 8
cifradoMasFrecuente :: String -> Int -> (Char, Float)
cifradoMasFrecuente (x:xs) n = ((cifradoMasFrecuenteAux1 (x:xs) n), (cifradoMasFrecuenteAux2 (x:xs) n))

cifradoMasFrecuenteAux1 :: String -> Int -> Char
cifradoMasFrecuenteAux1 [x] n = desplazar x n 
cifradoMasFrecuenteAux1 (x:xs) n | cantidadApariciones (head(cifrar (x:xs) n)) (cifrar (x:xs) n) == maximo (listaCantApariciones (cifrar (x:xs) n)) && esMinuscula x = head(cifrar (x:xs) n)
                                 | otherwise = cifradoMasFrecuenteAux1 xs n 

cifradoMasFrecuenteAux2 :: String -> Int -> Float 
cifradoMasFrecuenteAux2 (x:xs) n = maximo (frecuencia (cifrar (x:xs) n ))

maximo :: (Ord t) => [t] -> t
maximo [x] = x 
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos t [] = []
quitarTodos t (x:xs) | t == x = quitarTodos t xs 
                     | otherwise = x : quitarTodos t xs 

listaCantApariciones :: String -> [Int] 
listaCantApariciones [] = [] 
listaCantApariciones (x:xs) = cantidadApariciones x (x:xs) : listaCantApariciones (quitarTodos x (x:xs))



-- ejercicio 9
esDescifrado :: String -> String -> Bool
esDescifrado (x:xs) (y:ys) = esDescifradoAux (x:xs) (y:ys) 0 

esDescifradoAux :: String -> String -> Int -> Bool
esDescifradoAux (x:xs) (y:ys) 26 = False 
esDescifradoAux (x:xs) (y:ys) n | (y:ys) == cifrar (x:xs) n = True 
                                | otherwise = esDescifradoAux (x:xs) (y:ys) (n+1)



-- ejercicio 10 
todosLosDescifrados :: [String] -> [(String, String)]
todosLosDescifrados [] = []
todosLosDescifrados [x] = []
todosLosDescifrados (x:xs) | hayCifrado x (x:xs) == True = todosLosDescifradosAux x (x:xs) ++ (todosLosDescifrados xs)
                           | otherwise = todosLosDescifrados xs

descifradoNEnLista :: String -> [String] -> Int -> Bool 
descifradoNEnLista _ _ 26 = False 
descifradoNEnLista _ [] _ = False
descifradoNEnLista x (y:ys) n | cifrar x n == y = True  
                              | otherwise = descifradoNEnLista x ys n 

cualquierDescifradoEnLista :: String -> [String] -> Int -> Bool 
cualquierDescifradoEnLista _ _ 26 = False
cualquierDescifradoEnLista x (y:ys) n | descifradoNEnLista x (y:ys) n == True = True 
                                      | otherwise = descifradoNEnLista x (y:ys) (n+1)

todosLosDescifradosAux :: String -> [String] -> [(String,String)]
todosLosDescifradosAux x (y:ys) | hayMasDeUnCifrado x (y:ys) = (x,(buscarCifrado x (y:ys))) : [((buscarCifrado x (y:ys)),x)] ++ (todosLosDescifradosAux x (quitarCifrado x (y:ys)))
                                | cualquierDescifradoEnLista x (y:ys) 0 == True = (x, (buscarCifrado x (y:ys))) : [((buscarCifrado x (y:ys)),x)]
                                | otherwise = []

hayCifrado :: String -> [String] -> Bool 
hayCifrado _ [] = False
hayCifrado x (y:ys) | esDescifradoAux x y 1 == True = True 
                    | otherwise = hayCifrado x ys

hayMasDeUnCifrado :: String -> [String] -> Bool
hayMasDeUnCifrado _ [] = False
hayMasDeUnCifrado x (y:ys) | hayCifrado x (y:ys) == False = False 
                           | hayCifrado x (y:ys) == True && hayCifrado x (quitarCifrado x (y:ys)) == False = False
                           | otherwise = True

quitarCifrado :: String -> [String] -> [String]
quitarCifrado _ [] = []
quitarCifrado x (y:ys) | hayCifrado x (y:ys) == False = (y:ys)
                       | esDescifrado x y = ys 
                       | otherwise = y : (quitarCifrado x ys)

buscarCifrado :: String -> [String] -> String 
buscarCifrado x (y:ys) | esDescifradoAux x y 1 == True = y
                       | otherwise = buscarCifrado x ys




-- ejercicio 11 
expandirClave :: String -> Int -> String
expandirClave clave n = expandirAux clave n 

expandirAux :: String -> Int -> String 
expandirAux clave n = expandirAux2 clave n 0 []

expandirAux2 :: String -> Int -> Int -> String -> String
expandirAux2 clave n posicion res | length res == n = res
                                  | otherwise = expandirAux2 clave n (posicion + 1) (res ++ [obtenerCaracter clave posicion])

obtenerCaracter :: String -> Int -> Char 
obtenerCaracter clave posicion = clave !! (posicion `mod` length clave)





--- ejercicio 12

cifrarVigenere :: String -> String -> String
cifrarVigenere [] _ = []
cifrarVigenere _ [] = []
cifrarVigenere (x:xs) (y:ys) = (codificar x y) : cifrarVigenere xs (ys ++ [y])

codificar :: Char -> Char -> Char
codificar a b = chr (97 + mod (ord a + ord b - 2 * ord 'a') 26) --por ASCII


-- ejercicio 13

descifrarVigenere :: String -> String -> String
descifrarVigenere [] _ = []
descifrarVigenere _ [] = []
descifrarVigenere (x:xs) (y:ys) = (decodificar x y) : descifrarVigenere xs (ys ++ [y])

decodificar :: Char -> Char -> Char
decodificar a b = chr (97 + mod (ord a - ord b) 26)

-- ejercicio 14
  
peorCifrado :: String -> [String] -> String
peorCifrado s [claves] = claves
peorCifrado s (claves:claves2:cs) 
  | distanciaCifrado1 <= distanciaCifrado2 = peorCifrado s (claves:cs)
  | otherwise = peorCifrado s (claves2:cs)
  where
    distanciaCifrado1 = distancia s (cifrarVigenere s claves)
    distanciaCifrado2 = distancia s (cifrarVigenere s claves2)

distancia :: String -> String -> Int
distancia [] [] = 0
distancia (x:xs) (y:ys) = abs (ord x - ord y) + distancia xs ys



-- EJ 15

combinacionesVigenere :: [String] -> [String] -> String -> [(String, String)]
combinacionesVigenere [] _ _ = []
combinacionesVigenere (m:ms) claves cifrado = combinar m claves cifrado ++ combinacionesVigenere ms claves cifrado

combinar :: String -> [String] -> String -> [(String, String)]
combinar _ [] _ = []
combinar mensaje (c:cs) cifradoCorrecto = agregarSiCoincide mensaje c cifradoCorrecto (combinar mensaje cs cifradoCorrecto)

agregarSiCoincide :: String -> String -> String -> [(String, String)] -> [(String, String)]
agregarSiCoincide mensaje clave cifradoCorrecto tupla
  | cifrarVigenere mensaje clave == cifradoCorrecto = (mensaje, clave) : tupla
  | otherwise = tupla
