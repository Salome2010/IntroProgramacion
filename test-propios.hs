import Test.HUnit
import Data.List
import TPHaskell

--tests ejercicio 1

runTestsPersonales = runTestTT allTests

allTests = testsEjciudadMasConectada


-- tests ejercicio 4
testsEjciudadMasConectada = test [
    "caso para un solo vuelo devuelve cualquiera de las dos ciudades" ~: expectAny (ciudadMasConectada [("BsAs","Cordoba",5.0)])  ["BsAs", "Cordoba"],
    "caso que aparece dos veces" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "caso empate" ~: expectAny (ciudadMasConectada  [("BsAs", "Rosario", 10.0), ("Rosario", "Cordoba", 7.0),("BsAs", "Salta", 7.0)]) ["BsAs","Rosario"],
    "caso aparece mas de dos veces" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Cordoba", 7.0),("BsAs", "Salta", 7.0),("BsAs", "Jujuy", 4.0),("Rosario", "Salta", 7.0),("Formosa", "Rosario", 9.0)]  ~?= "Rosario",
    "caso varios empates" ~: expectAny ( ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Cordoba", 7.0),("BsAs", "Salta", 7.0),("BsAs", "Jujuy", 4.0),("Rosario", "Salta", 7.0),("Formosa", "Rosario", 9.0),("BsAs","Cordoba",5.4),("Cordoba","Salta",5.4),("Cordoba","Jujuy",6.3)]) ["BsAs","Rosario","Cordoba"],
    "caso se repite varias veces en la primer mitad" ~: ciudadMasConectada [("c1","c2",5.0),("c1","c3",3.0),("c1","c4",2.0),("c1","c6",2.0),("c1","c7",2.0),("c5","c2",1.0),("c5","c3",0.5),("c5","c4",0.6)]  ~?= "c1",
    "caso se repite varias veces en la segunda mitad" ~: ciudadMasConectada [("c1","c2",5.0),("c2","c3",3.0),("c3","c4",2.0),("c4","c6",2.0),("c5","c7",2.0),("c5","c2",1.0),("c5","c3",0.5),("c5","c4",0.6)]  ~?= "c5",
    "caso primera ciudad tiene mas apariciones, pero sacando la primera aparición de las ciudades gana otra" ~: ciudadMasConectada[("c1","c5",5.0),("c5","c3",3.0),("c1","c4",2.0),("c1","c6",2.0),("c1","c7",2.0),("c5","c2",1.0),("c1","c3",0.5),("c5","c4",0.6)] ~?= "c1",
    "caso varias ciudades" ~: ciudadMasConectada  [("c1","c2",5.0),("c2","c3",3.0),("c3","c4",2.0),("c4","c6",2.0),("c5","c7",2.0),("c3","c1",2.0),("c5","c2",1.0),("c5","c3",0.5),("c5","c4",0.6),("c6","c3",4.0)]  ~?= "c3"
    ]


-- Funciones extras

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [StringxStringxFloat], expected: [StringxStringxFloat]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para algun elemento t de actual existe un elemento x de expected tal que t1 = x1 && t2 = x2 && |t3-x3| < margenFloat
expectlistProximity:: [(String,String,Float)] -> [(String,String,Float)] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [(String,String,Float)] -> [(String,String,Float)] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoDeAUno actual expected)

esParecidoDeAUno :: [(String,String,Float)] -> [(String,String,Float)] -> Bool
esParecidoDeAUno [] _ = True
esParecidoDeAUno (x:xs) list2 = hayAproxEnLista x list2 && esParecidoDeAUno xs list2

hayAproxEnLista :: (String,String,Float) -> [(String,String,Float)] -> Bool

hayAproxEnLista _ [] = False

hayAproxEnLista (ac1,ac2,af) ((bc1,bc2,bf):xs) 
    | ac1 == bc1 && ac2 == bc2 = aproximado af bf
    |otherwise = hayAproxEnLista (ac1,ac2,af) xs

-- expectAproximado (actual: Float, expected: Float):Test
--asegura : res es un test verdadero si y sólo si:
--                  | actual - expected | < margenFloat
expectAproximado :: Float -> Float -> Test

expectAproximado actual expected = aproximado actual expected ~? ("expected approximation: " ++ show expected ++ "\nbut got: " ++ show actual)

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