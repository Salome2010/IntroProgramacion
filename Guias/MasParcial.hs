import Data.Char

esMin :: Char -> Bool
esMin a = ord a >= ord 'a' && ord a <= ord 'z'
charANat :: Char -> Int
charANat a | esMin a = (ord a) - (ord 'a')
natAChar :: Int -> Char
natAChar n | 0 <= n && n <= 25 = chr ((ord 'a' )+n)
natAChar1 :: Int -> Char
natAChar1 n | (-25) <= n && n < 0 = chr ((ord 'z' )+n)

--ejercicio 1
cantMinusculas :: String -> Int
cantMinusculas ("") = 0
cantMinusculas a | esMin (last a) = 1 + cantMinusculas (init a)
                 | otherwise = cantMinusculas (init a) 
{-
--ejercicio 2
maximoCambios :: [String] -> String
maximoCambios [x] = (x)
maximoCambios (x:xs) | (cantMinusculas(x)) >= (cantMinusculas(head(xs)))   = maximoCambios (x:(tail(xs)))
                     | otherwise = maximoCambios xs

--ejercicio 3
desplazar :: (Char) -> (Int) -> (Char)
desplazar 'z' 1 = 'a' 
desplazar a 0 = a
desplazar 'a' (-1) = 'z'
desplazar a n | (0<=(charANat(a)+n) && (charANat(a)+n)<=25)= natAChar(charANat(a) + n)
              | ((charANat(a)+n)>25) = natAChar(charANat(a)+n-26)
              | ((-25)<=(charANat(a)+n) && (charANat(a)+n)<=0)= natAChar1(charANat(a) + n+1)
              | ((charANat(a)+n)<(-25)) = natAChar(charANat(a)+n-26)
              | otherwise = a              

--ejercicio 4
codificar :: String -> Int -> String
codificar ("") _ =("")
codificar x n | esMin(head(x)) = (desplazar (head x) n) : (codificar (tail x) n)
              | otherwise = (head(x) : codificar (tail x) n)

--ejercicio 5
decodificar :: String -> Int -> String
decodificar ("") _ = ("")
decodificar x n | esMin(head(x)) = (desplazar (head x) (-n)) : (decodificar (tail x) n)
                | otherwise = (head (x) : decodificar (tail x) n)

-}