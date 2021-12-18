# LA-ESCALERA
Mi dirección de Github es:https://github.com/claudiaalozano/LA-ESCALERA.git

A continuación muestro un esquema de como se generaría el programa:

![Figma escalera](https://user-images.githubusercontent.com/91722847/146638855-a3e72a23-45bf-4d0e-9db9-8c555e456311.png)

El código finalmente es:
```from random import randint

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
   
   ```
