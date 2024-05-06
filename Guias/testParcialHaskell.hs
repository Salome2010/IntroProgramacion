import Test.HUnit
import ParcialHaskell

main = runTestTT tests


tests = test [
       "caso base" ~: porcentajeDeGoles "nico" [("boca","nico"),("river","salo")] [10,10] ~?= 50.0,
       "porcentaje total" ~: porcentajeDeGoles  "salo" [("boca","salo"),("boca","mica")] [20,0] ~?= 100.0,
       "otro arquero" ~: porcentajeDeGoles "mica" [("boca","salo"),("river","mica")] [20,30] ~?= 60.0
       ]

ejecutar = runTestTT prueba

prueba = test [
       
       ]
