ganadores = [['messi','cristano','mba'],[7,5,1]]

#con for
for i in range(len(ganadores)):
    for j in range(len(ganadores[i])):
        print("ganadores ["+str(i)+"]["+str(j)+"] ="+str(ganadores[i][j])) 

# con while
fila = 0
while fila < len(ganadores):
    columna = 0
    while columna < len(ganadores[fila]):
         print("ganadores ["+str(fila)+"]["+str(columna)+"] ="+str(ganadores[fila][columna]))
         columna +=1
    fila+=1 

""" ambos imprimen:
ganadores [0][0] =messi
ganadores [0][1] =cristano
ganadores [0][2] =mba
ganadores [1][0] =7
ganadores [1][1] =5
ganadores [1][2] =1
"""
