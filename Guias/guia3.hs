
-- GUIA 3

-- Ejercico 1
--a) 
f :: Integer -> Integer
f x | x==1 = 8
    | x==4 = 131
    | x==16 = 16

--b)
g :: Integer -> Integer
g x | x==8 = 16
    | x==16 = 4
    | x==131 = 1

--c) 
h :: Integer -> Integer
h x = f (g x)

k :: Integer -> Integer
k x = g (f x)

-- Ejercicio 2
--a)
absoluto :: Integer -> Integer
absoluto x | x >=0 = x
           | otherwise = -x

--b) 
maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto n s | absoluto n >= absoluto s = absoluto n
                   | otherwise = absoluto s 

--c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z |  x>=y && x>=z = x
              | y>=x && y>=z = y
              | z>=x && z>=y = z

--d) 
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y = x == 0 || y==0 

ambosSon0 :: Float -> Float -> Bool
ambosSon0 n s = n==0 && s==0 
              

--f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo n s = perteneceIntervalo n   == perteneceIntervalo  s 
                   

perteneceIntervalo :: Float -> Integer
perteneceIntervalo x | x<=3 = 1
                     | x>3 && x<=7 = 2
                     | x>7 = 3


--g) 
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x==y && y==z = 0
                    | x==y = z
                    | x==z = y
                    | y==z = x
                    | otherwise = x+y+z

--h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y =  x `mod` y == 0 
                 
--i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

--J) en espicificacion aclarar x>9
digitoDecenas :: Integer -> Integer
digitoDecenas x = digitoUnidades (div x 10)

--Ejercicio 3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b =  mod a b == 0 
                      

--Ejercicio 4
--a) lo mismo que producto escalar entre dos vectores 
prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (x,y) (z,w) =  x*z + y*w

--b)
todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (x,y) (z,w) = x<z && y<w 
                      

--c) calcula la distancia entre dos puntos de R2. Se deduce de pitágoras => vectorDistancia ((x1-x2),(y1-y2)) y distancia = |vectorDistancia|
distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (x,y) (z,w) = sqrt ((z-x)^2+(w-y)^2)

--d) 
sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (x,y,z) = x+y+z

--e) 
sumarSoloMultiplos :: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (x,y,z) w | mod x w == 0 && mod y w == 0 && mod z w == 0 = x+y+z
                             | mod x w /= 0 && mod y w == 0 && mod z w == 0 = y+z
                             | mod x w == 0 && mod y w == 0 && mod z w /= 0 = x+y
                             | mod x w == 0 && mod y w /= 0 && mod z w == 0 = x+z
                             | mod x w == 0 && mod y w /= 0 && mod z w /= 0 = x
                             | mod x w /= 0 && mod y w == 0 && mod z w /= 0 = y
                             | mod x w /= 0 && mod y w /= 0 && mod z w == 0 = z
                             | otherwise = 0

--f)
posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (x,y,z) | esPar x && x/=0 = 0
                     | esPar y && y/=0 = 1
                     | esPar z && z/=0 = 2
                     | otherwise = 4
                     where esPar x = mod x 2 == 0

--g) 
crearPar :: a -> b -> (a, b)
crearPar a b = (a,b)

--h) 
invertir :: (a, b) -> (b, a)
invertir (a,b) = (b,a)

--Ejercicio 5
{-todosMenores :: (Integer, Integer, Integer) -> Bool 
todosMenores x y z = (f x > g x) && (f y > g y) && (f z > g z) 

f :: Integer -> Integer
f n | n<= 7 = n**2
    | otherwise = 2*x - 1

g :: Integer -> Integer 
g n | esPar n = n/2
    | otherwise = 3*x + 1
    where esPar x = mod x 2 == 0
-}
--Ejercicio 6
bisiesto :: Integer ->Bool
bisiesto n = mod n 4 == 0 || (mod n 100 /= 0 && mod n 400 ==0) 
           

--Ejercicio 7
distanciaManhattan:: (Float, Float, Float) ->(Float, Float, Float) ->Float
distanciaManhattan (x,y,z) (a,b,c) = -((x-a) + (y-b) + (z-c))

-- tamnien podia hacerlo de la sig manera: 
--distanciaManhattan::(Float, Float, Float) -> (Float, Float, Float) -> Float
--distanciaManhattan (x,y,z) (a,b,c) | calculo (x,y,z) (a,b,c) > 0 = calculo (x,y,z) (a,b,c)
--                                  | otherwise = - calculo (x,y,z) (a,b,c)

--calculo :: (Float, Float, Float) -> (Float, Float, Float) -> Float
--calculo (x,y,z) (a,b,c) = (x-a) + (y-b) + (z-c)


--Ejercico 8
comparar :: Integer ->Integer ->Integer
comparar x y | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | otherwise =0

sumaUltimosDosDigitos :: Integer -> Integer 
sumaUltimosDosDigitos x = mod x 10 + (mod (div x 10) 10)

 



