lista = []
contador = 0

for i in range(0, 6):
    lista.append(float(input()))

for i in lista:
    if i > 0:
        contador += 1

print("{} valores positivos".format(contador))
