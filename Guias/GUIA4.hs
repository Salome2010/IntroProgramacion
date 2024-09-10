-- EJERCICIO 1
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
import Data.Fixed (div')
{-# HLINT ignore "Eta reduce" #-}
{-# HLINT ignore "Redundant bracket" #-}
fibonacci:: Integer ->Integer 
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)



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

-- o tambien sin recu
--sumaImpares :: Int -> Int
--sumaImpares 1 = 1
--sumaImpares x = x*x

--Ejercicio 5
medioFact :: Integer ->Integer 
medioFact 0 = 1
medioFact n = n * medioFact(n-2) 

--Ejercicio 6
sumaDigitos :: Integer ->Integer 
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito n  + sumaDigitos (div n 10) 


--Ejercicio 7
{-todosDigitosIguales :: Integer ->Bool 
todosDigitosIguales n | n< 10 = True 
                      | n<100 = mod n 10 == div n 10
                      | otherwise = todosDigitosIguales (mod n 100) && todosDigitosIguales (div n 10)-}

todosDigitosIguales2 ::  Integer -> Bool
todosDigitosIguales2 n | n<10 = True
                       | otherwise = ultimoDigito n == ultimoDigito(div n 10 ) && todosDigitosIguales2(div n 10)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10 


--Ejercicio 8
cantDigitos :: Int -> Int
cantDigitos n   | n<10 = 1
                | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i    | i == cantDigitos n = mod n 10 
                    | otherwise = iesimoDigito (div n 10) i 
                    

--Ejercicio 9

iEsimoDigito :: Int -> Int -> Int
iEsimoDigito n 1 = div n (10^((cantidadDigitos n)-1))
iEsimoDigito n i = iEsimoDigito sacarPrimerDigito (i-1)
    where primerDigito = div n (10^((cantidadDigitos n)-1))
          sacarPrimerDigito = mod n (10^((cantidadDigitos n)-1))

cantidadDigitos :: Int -> Int
cantidadDigitos n | n < 10 = 1
                  | otherwise = cantidadDigitos (div n 10) + 1

esCapicua :: Int -> Bool
esCapicua x | x < 10 = True
            | x < 100 = iEsimoDigito x 1 ==  iEsimoDigito x 2
            | otherwise = iEsimoDigito x 1 == ultimoDigito && esCapicua sacarPrimeroYultimo
    where ultimoDigito = mod x 10
          sacarPrimeroYultimo = div (mod x (10^((cantidadDigitos x)-1))) 10

--Ejercicio 10
--a)
f1::Integer->Integer
f1 0 = 1
f1 n = 2^n + f1 (n-1)

--b) 
f2:: Integer -> Integer -> Integer
f2 _ 0= 1 
f2 q n = q^n + f2 q (n-1) 

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
esAprox 0 = 1
esAprox n = (1 / factorial n) + esAprox(n-1)

factorial :: Integer -> Float
factorial 0 = 1
factorial n = fromIntegral n * (factorial (n-1))

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
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaSimple n m + sumatoriaDoble (n-1) m 

sumatoriaSimple::Integer->Integer->Integer
sumatoriaSimple n 1 = n
sumatoriaSimple n m  = n^m + sumatoriaSimple n (m-1)


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
sumaRacionales p m = sumaRacionalesAux p m + sumaRacionales (p-1) m 

sumaRacionalesAux::Integer->Integer->Float
sumaRacionalesAux p 1=  fromInteger p
sumaRacionalesAux p m = fromIntegral p / fromIntegral m + sumaRacionalesAux p (m-1)

---Ejercicio 16

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer
menorDivisorAux n i | mod n i == 0 = i
                    | otherwise = menorDivisorAux n (i+1) 

esPrimo :: Integer -> Bool
esPrimo n =  n == menorDivisor n 

{-sonPrimos :: Integer -> Integer -> Bool
sonPrimos n m = not(fromIntegral (menorDivisor n / menorDivisor m ) ) -- ver -}

{-sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = mod n m == 1 && mod m n == 1-}

nEsimoPrimo::Integer->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimo (nEsimoPrimo (n-1))
-- Devuelve el primo nº n, 
-- Ej: nEsimoPrimo 4 = 7, nEsimoPrimo5=11 , nEsimoPrimo 19=67

siguientePrimo::Integer->Integer
siguientePrimo n | esPrimo (n+1) = n+1
                 | otherwise = siguientePrimo (n+1)
-- Si el siguiente numero es primo, devuelve ese numero, si no, vuelve a chequear hasta tener uno primo
-- Ej: siguientePrimo 3 = 5, siguientePrimo 5=7, siguientePrimo 6=7


--Ejercicio 17 
esFibonacciAux::Integer->Integer->Integer->Bool
esFibonacciAux n fibAnterior fib
    | fib == n = True
    | fib > n = False
    | otherwise = esFibonacciAux n fib (fib+fibAnterior) -- Esto pues en la siguiente iteracion fibAnterior es fib, y fib es (fib+fibAnterior) por def de Fibonacci

esFibonacci :: Integer->Bool
esFibonacci n = esFibonacciAux n 0 1 --Con 0 y 1 arranco la secuencia de Fibonacci. Prendo la chispa de la recursion

--eJERCICIO 18
mayorDigitoPar::Integer->Integer
mayorDigitoPar n | n<10 && even n = n
                 | n<10 && odd n = -1
                 | even (mod n 10 )= max (mod n 10) (mayorDigitoPar (div n 10))
                 | otherwise = mayorDigitoPar (div n 10) 
                 

