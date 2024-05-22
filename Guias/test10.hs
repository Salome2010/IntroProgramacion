testsEjtodosLosDescifrados = test [
    "Lista vacia" ~: todosLosDescifrados [] ~?= [],
    "Un elemento" ~: todosLosDescifrados ["Esquina"] ~?= [],
    "Dos elementos cifrados" ~: todosLosDescifrados ["compu", "frpsx"] ~?= [("compu","frpsx"),("frpsx","compu")],
    "Dos elementos no cifrados" ~: todosLosDescifrados ["arbol","pelota"] ~?= [],
    "Varios elementos pero 1 par" ~: todosLosDescifrados ["botella","mouse","suayv","uhmxeet"] ~?= [("botella","uhmxeet"),("uhmxeet","botella")],
    "Varios elementos con mas pares" ~: todosLosDescifrados ["xqdtrqbb","armario","izuizqw","handball","dupdulr"] ~?= [("handball","xqdtrqbb"),("xqdtrqbb","handball"),("armario","dupdulr"),("armario","izuizqw"),("izuizqw","armario"),("dupdulr","armario"),("izuizqw","dupdulr"),("dupdulr","izuizqw")],
    "Dos elementos cifrados con algunas minusculas" ~: todosLosDescifrados ["Ej nuMero 2","Em qxMhur 2","ej numero 2"] ~?= [("Ej nuMero 2","Em qxMhur 2"),("Em qxMhur 2","Ej nuMero 2")]
    ] 