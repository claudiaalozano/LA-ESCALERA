TAMAÑO_ESCALERA = int(input("ELIGE EL TAMAÑO DE LA ESCALERA >>>  "))

ESCALERA = []
for i in range(TAMAÑO_ESCALERA):
    ESCALERA.append([])
    for j in range(TAMAÑO_ESCALERA):
        ESCALERA[i].append("#")
        #ESCALERA[i:TAMAÑO_ESCALERA] = ' '

print(ESCALERA)