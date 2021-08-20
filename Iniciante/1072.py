n = int(input())
numeros = []
dentro, fora = 0, 0

for i in range(0, n):
    numeros.append(int(input()))
    if numeros[i] in range(10, 21):
        dentro += 1
    else:
        fora += 1

print(dentro, " in\n", fora, " out", sep='')
