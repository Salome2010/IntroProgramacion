import Test.HUnit
import Data.List
import TPHaskell
-- No está permitido agregar nuevos imports.


run = runTestTT allTests

allTests = test [
    "ciudadesConectadas" ~: testsEjciudadesConectadas
    ]

-- corregir los tests si es necesario con las funciones extras que se encuentran al final del archivo


testsEjciudadesConectadas = test [
    "ciudad conectada con un elemento" ~: ciudadesConectadas  [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
    "ciudad conectada 1" ~: ciudadesConectadas  [("bs as", "ros", 5.0),("ros","bs as",7.0),("ros","cor",8.0),("cor","ros",9.0),("ros","men",8.0),("men","ros",6.0)] "ros" ~?= ["bs as","cor","men"]
    ]
