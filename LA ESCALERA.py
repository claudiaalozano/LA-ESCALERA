#TAMAÑO_ESCALERA = int(input("ELIGE EL TAMAÑO DE LA ESCALERA >>>  "))

#ESCALERA = []
#for i in range(TAMAÑO_ESCALERA):
    #ESCALERA.append([])
    #for j in range(TAMAÑO_ESCALERA):
        #ESCALERA[i].append("#")
        #ESCALERA[i:TAMAÑO_ESCALERA] = ' '

#print(ESCALERA)
from random import randint

n = randint(5,10)

matriz = [
    ["a"],
    ["a"],
    ["a"],
]

matrix = []
matrix.append("a")

for k in range(n):
    matrix = matrix.append("a")

print(matrix)


print(matrix)

b = ""

for k in range(3):
    for j in range(1):
        b += str(matriz[k][j])+"\t"
    print(b)