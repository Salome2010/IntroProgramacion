import Test.HUnit
import Simulacro 

main = runTestTT tests

tests = test [
       "caso base" ~: (amigosDe  []) ~?= []
       "persona en a" ~: (amigosDe "persona" [("persona", "salo")]) ~?= [("persona", "salo")]
       "persona no esta" ~: (amigosDe "persona" [("salo")]) ~?= [("persona", "salo")]
       ]
