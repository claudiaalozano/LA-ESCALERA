#TAMAÑO_ESCALERA = int(input("ELIGE EL TAMAÑO DE LA ESCALERA >>>  "))

#ESCALERA = []
#for i in range(TAMAÑO_ESCALERA):
    #ESCALERA.append([])
    #for j in range(TAMAÑO_ESCALERA):
        #ESCALERA[i].append("#")
        #ESCALERA[i:TAMAÑO_ESCALERA] = ' '

#print(ESCALERA)
from random import randint

n = int(input("Elija el tamaño de la escalera:"))

#matriz = [ ["a"], ["a"], ["a"]]

matrix = []
matrix.append("a" * n)
for k in range(n):
    matrix.append("a")

print(matrix)

b = " "

for k in range(n):
    for j in range(1):
        b += str(matrix[k][j])+ "\t"
    print(b)