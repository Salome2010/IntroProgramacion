

import Test.HUnit
import Solucion
import Data.List


-- No está permitido agregar nuevos imports.

runCatedraTests = runTestTT allTests

allTests = test [
    "esMinuscula" ~: testsEjesMinuscula,
    "letraANatural" ~: testsEjletraANatural,
    "desplazar" ~: testsEjdesplazar,
    "cifrar" ~: testsEjcifrar,
    "descifrar" ~: testsEjdescifrar,
    "cifrarLista" ~: testsEjcifrarLista,
    "frecuencia" ~: testsEjfrecuencia,
    "cifradoMasFrecuente" ~: testsEjcifradoMasFrecuente,
    "esDescifrado" ~: testsEjesDescifrado,
    "todosLosDescifrados" ~: testsEjtodosLosDescifrados,
    "expandirClave" ~: testsEjexpandirClave,
    "cifrarVigenere" ~: testsEjcifrarVigenere,
    "descifrarVigenere" ~: testsEjdescifrarVigenere,
    "peorCifrado" ~: testsEjpeorCifrado,
    "combinacionesVigenere" ~: testsEjcombinacionesVigenere
    ]


testsEjesMinuscula = test [
    esMinuscula 'd' ~?= True,
    esMinuscula '9' ~?= False,
    esMinuscula 'A' ~?= False,
    esMinuscula ' ' ~?= False,
    esMinuscula 'z' ~?= True
    ]

testsEjletraANatural = test [
    letraANatural 'b' ~?= 1,
    letraANatural 'z' ~?= 25,
    letraANatural 'a' ~?= 0,
    letraANatural 'm' ~?= 12
    ]

testsEjdesplazar = test [
    desplazar 'a' 3 ~?= 'd',
    desplazar 'z' 1 ~?= 'a',
    desplazar 'a' (-1) ~?= 'z',
    desplazar 'z' (-26) ~?= 'z',
    desplazar 'c' 52 ~?= 'c',
    desplazar '9' 18 ~?= '9',
    desplazar 'Z' 20 ~?= 'Z',
    desplazar ' ' 89 ~?= ' '

    ]

testsEjcifrar = test [
    cifrar " " 3 ~?= " ",
    cifrar "computacion" 3 ~?= "frpsxwdflrq",
    cifrar "computacion" 78 ~?= "computacion",
    cifrar "computacion" 0 ~?= "computacion",
    cifrar "computacioN" 3 ~?= "frpsxwdflrN",
    cifrar "ComputacioN" 26 ~?= "ComputacioN",
    cifrar "COMPUTACION" 15 ~?= "COMPUTACION" 
    ]

testsEjdescifrar = test [
    descifrar " " 9 ~?= " ",    
    descifrar "frpsxwdflrq" 3 ~?= "computacion",
    descifrar "frpsxwdflrq" 0 ~?= "frpsxwdflrq",
    descifrar "FrpsxwdflrQ" 3 ~?= "FomputacioQ",
    descifrar "COMIDA" 55 ~?= "COMIDA",
    descifrar "comida" 26 ~?= "comida"
    ]

testsEjcifrarLista = test [
    cifrarLista ["compu", "labo", "intro"] ~?= ["compu", "mbcp", "kpvtq"],
    cifrarLista ["COMPU", "labo", "intro"] ~?= ["COMPU", "mbcp", "kpvtq"],
    cifrarLista ["COMPU", "labo", "INTRO"] ~?= ["COMPU", "mbcp", "INTRO"],
    cifrarLista ["COMPU", "LABO", "INTRO"] ~?= ["COMPU", "LABO", "INTRO"],
    cifrarLista ["comPU", "LAbo", "iNTRo"] ~?= ["comPU", "LAcp", "kNTRq"],
    cifrarLista [] ~?= []

    ]

testsEjfrecuencia = test [
    expectlistProximity (frecuencia " ") ([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]),
    expectlistProximity (frecuencia "taller") [16.666668,0.0,0.0,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0,33.333336,0.0,0.0,0.0,0.0,0.0,16.666668,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0],
    expectlistProximity (frecuencia "TalleR") [25.0,0.0,0.0,0.0,25.0,0.0,0.0,0.0,0.0,0.0,0.0,50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    expectlistProximity (frecuencia "TaLLEz") [50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,50.0],
    expectlistProximity (frecuencia "abcdefghijklmnopqrstuvwxyz") [3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846,3.846],
    expectlistProximity (frecuencia "aBcDeFgHiJkLmNoPqRsTuVwXyZ") [7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0,7.68,0.0],
    expectlistProximity (frecuencia "PaaaPaaa") [100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    expectlistProximity (frecuencia "zzzz9470") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,100.0]

    ]

testsEjcifradoMasFrecuente = test [
    
    cifradoMasFrecuente "taller" 3 ~?= ('o', 33.333336)
    {-cifradoMasFrecuente "a" 3 ~?= ('d', 100.0),
    cifradoMasFrecuente "zzzz" 1 ~?= ('a', 100.0),
    cifradoMasFrecuente "aaabbcc" 10 ~?= ('k', 42.85),
    cifradoMasFrecuente "aabbbzzzz" 10 ~?= ('j', 44.44),
    cifradoMasFrecuente "ab" 7 ~?= ('h', 50.0),
    cifradoMasFrecuente "ABCDEaFGHI" 25 ~?= ('z', 100.0),
    cifradoMasFrecuente "ABCDEFGHIa" 5 ~?= ('f', 100.0),
    cifradoMasFrecuente "hZOPAIE" 10 ~?= ('r', 100.0),
    cifradoMasFrecuente "aABCDEFGbb" 25 ~?= ('a', 66.66),
    cifradoMasFrecuente "aABCDaEFGbb" 25 ~?= ('z', 50.0)     -}       
    ]

testsEjesDescifrado = test [
    esDescifrado "taller" "compu" ~?= False,
    esDescifrado " " " " ~?= True,
    esDescifrado " " "compu" ~?= False,
    esDescifrado "compu" " " ~?= False,
    esDescifrado "compu" "compu" ~?= True,
    esDescifrado "a" "b" ~?= True,
    esDescifrado "b" "a" ~?= True,    
    esDescifrado "A" "A" ~?= True,
    esDescifrado "B" "A" ~?= False,
    esDescifrado "AAAb" "AAAa" ~?= True, 
    esDescifrado "AAAa" "AAAb" ~?= True,
    esDescifrado "zPPP" "aPPP" ~?= True,
    esDescifrado "frpsx" "compu" ~?= True               
    ]

testsEjtodosLosDescifrados = test [
    todosLosDescifrados ["compu", "frpsx", "mywza"] ~?= [("compu", "frpsx"), ("frpsx", "compu")]
    ]

testsEjexpandirClave = test [
    expandirClave "compu" 8 ~?= "compucom"
    ]

testsEjcifrarVigenere = test [
    cifrarVigenere "computacion" "ip" ~?= "kdueciirqdv"
    ]

testsEjdescifrarVigenere = test [
    descifrarVigenere "kdueciirqdv" "ip" ~?= "computacion"
    ]

testsEjpeorCifrado = test [
    peorCifrado "computacion" ["ip", "asdef", "ksy"] ~?= "asdef"
    ]

testsEjcombinacionesVigenere = test [
    combinacionesVigenere ["hola", "mundo"] ["a", "b"] "ipmb" ~?= [("hola", "b")]
    ]

-- Funciones útiles

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)