
from random import randint

n = int(input("Elija el tamaño de la escalera:"))


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