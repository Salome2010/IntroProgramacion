import ParcialHaskell 
import Test.HUnit 

ejecutar = runTestTT testHaskell

testHaskell = test [
             "caso base" ~: (formulasValidas []) ~?= True,
             "caso que no vale" ~: (formulasValidas [("sa","me"),("sa","lo")]) ~?= False,
             "caso que si vale" ~: (formulasValidas [("sa","me"),("lo","de")]) ~?= True
             ]
