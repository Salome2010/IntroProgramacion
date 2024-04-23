-- EJERCICIO 1
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Eta reduce" #-}
{-# HLINT ignore "Redundant bracket" #-}
fibonacci:: Integer ->Integer 
fibonacci n | n==0 = 0
            | n==1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--Ejercicio 2
parteEntera :: Float -> Integer 
parteEntera n | n < 1 && n > 0 = 0
              | n > -1 && n <= 0 = -1
              | n >= -1 = 1 + parteEntera(n-1)
              | otherwise = -1 + parteEntera(n+1)
-- o es lo mismo que poner:
--parteEntera :: Float -> Integer 
--parteEntera n = trucante x

--Ejercicio 3
esDivisible :: Integer ->Integer ->Bool
esDivisible x y | x==y = True
                | x<y = False
                | otherwise = esDivisible(x-y) y 

--Ejercicio 4
sumaImpares :: Int -> Int
sumaImpares 1 = 1
sumaImpares x = sumaImpares (x-1) + (2*x-1) 

--Ejercicio 5
medioFact :: Integer ->Integer 
medioFact n | n==0 = 1
            | otherwise = n * medioFact(n-2) 

--Ejercicio 6
sumaDigitos :: Integer ->Integer 
sumaDigitos n | n < 10 = n
              | otherwise = (mod n 10) + sumaDigitos (div n 10) 


--Ejercicio 7
todosDigitosIguales :: Integer ->Bool 
todosDigitosIguales n | n< 10 = True 
                      | n<100 = mod n 10 == div n 10
                      | otherwise = todosDigitosIguales (mod n 100) && todosDigitosIguales (div n 10)

--Ejercicio 8
cantDigitos :: Int -> Int
cantDigitos n   | n<10 = 1
                | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i    | cantDigitos n == i = sacarUltimoDigito
                    | otherwise = iesimoDigito (div n 10) i 
                    where sacarUltimoDigito = mod n 10

--Ejercicio 9
esCapicua::Integer->Bool
esCapicua n = n== inverso n

inverso::Integer->Integer
inverso = read . reverse . show

--Ejercicio 10
--a)
f1::Integer->Integer
f1 0 = 1
f1 n = 2^n + f1 (n-1)

--b) 
f2:: Integer -> Float -> Float
f2 1 q= q 
f2 n q= q^n + f2 (n-1) q

--c) 
f3 :: Integer -> Float -> Float 
f3 0 q = 0
f3 1 q = q + q^2
f3 n q = q^(2*n -1) + q^(2*n) + f3 (n-1) q


--d)

f4 :: Integer -> Integer -> Integer
f4 n q = f4aux (2 * n) q n

f4aux :: Integer -> Integer -> Integer -> Integer
f4aux n q i | i == n = q^n
            | otherwise = q^n + f4aux (n - 1) q i

--Ejercicio 11
--a) 
esAprox :: Integer -> Float
esAprox n | n==0 = 1
          | otherwise = (1 / factorial n) + esAprox(n-1)

factorial :: Integer -> Float
factorial n | n==0 = 1
            | otherwise = fromIntegral n * (factorial (n-1))

-- agrego fromIntegral para que no me aparezca error en el n solo o 2*n 

--b)
e :: Float
e = esAprox 10 

--Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = aprox n - 1

aprox :: Integer -> Float
aprox n | n==1 = 2
        | otherwise = 2 + ( 1 / aprox (n-1) ) 

--Ejercicio 13
sumatoriaDoble :: Integer->Integer->Integer
sumatoriaDoble 1 m = sumatoriaAux 1 m
sumatoriaDoble n m = sumatoriaAux n m + sumatoriaDoble (n-1) m 

sumatoriaAux::Integer->Integer->Integer
sumatoriaAux n 1 = n
sumatoriaAux n m  = n^m + sumatoriaAux n (m-1)


--Ejercicio 14
sumaPotencias :: Integer ->Integer ->Integer ->Integer
sumaPotencias q 1 b = sumaPotenciasaux q 1 b
sumaPotencias q a b = sumaPotenciasaux q a b + sumaPotencias q (a-1) b

sumaPotenciasaux :: Integer -> Integer -> Integer ->Integer
sumaPotenciasaux q a 1 = q^(a+1)  
sumaPotenciasaux q a b = q^(b+a) + sumaPotenciasaux q a (b-1) 

 
--Ejercicio 15
sumaRacionales::Integer->Integer->Float
sumaRacionales 1 m= sumaRacionalesAux 1 m
sumaRacionales n m = sumaRacionalesAux n m + sumaRacionales (n-1) m 

sumaRacionalesAux::Integer->Integer->Float
sumaRacionalesAux n 1=  fromInteger n
sumaRacionalesAux n m = fromIntegral n / fromIntegral m + sumaRacionalesAux n (m-1)




