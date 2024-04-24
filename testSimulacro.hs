import Simulacro
import Test.HUnit  

main = runTestTT tests

tests = test [
        "caso base" ~: (relacionesValidas []) ~?= True,
        "tupla repetida" ~: (relacionesValidas [("ana", "pedro"), ("ana", "pedro")]) ~?= False,
        "tupla repetida invertida" ~: (relacionesValidas [("ana", "pedro"), ("pedro", "ana")]) ~?= False,
        "todas diferentes" ~: (relacionesValidas [("mica", "pedro"), ("ana", "carlos")]) ~?= True
        ] 

