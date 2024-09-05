dondeEsta :: String -> [(String,Int)]-> Int
dondeEsta _ [] = 0
dondeEsta nombre ((persona,numero):xs) | nombre==persona = numero
                                       | otherwise= dondeEsta nombre xs  