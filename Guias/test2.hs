tests = test [
        "caso base" ~: (relacionesValidas []) ~?= True,
        "tupla repetida" ~: (relacionesValidas [("ana", "pedro"), ("ana", "pedro")]) ~?= False,
        "tupla repetida invertida" ~: (relacionesValidas [("ana", "pedro"), ("pedro", "ana")]) ~?= False,
        "todas diferentes" ~: (relacionesValidas [("mica", "pedro"), ("ana", "carlos")]) ~?= True
        ] 

tests = test [
     "caso base" ~: (personas []) ~?= []
     "ya pertenecen a y b " ~: (personas [("mica", "salo"), ("mica", "salo",  "dani")]) ~?=[("mica", "salo", "dani")]
     "pertenece solo a" ~: (personas [("mica", "salo"), ("mica", "dani")]) ~?= [("mica", "salo", "dani")]
     "no pertenece ninguno" ~: (personas [("mica", "salo"), ("dani")]) ~?= [("mica", "salo", "dani")]
     ]  