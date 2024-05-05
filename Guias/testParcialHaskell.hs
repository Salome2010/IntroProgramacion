import Test.HUnit
import ParcialHaskell

main = runTestTT tests


tests = test [
       "caso base" ~: amigosDe "p" [] ~?= [],
       "caso aparece en a" ~: amigosDe "p" [("p","nico"),("mica","salo")] ~?= ["nico"],
       "caso aparece en xs" ~: amigosDe "p" [("salo","nico"),("mica","p")] ~?= ["mica"]
       ]