n = int(input())
medias = []

numeros = [input().split() for a in range(0,  n)]

for i in range(0, n):
    # numeros[i].append(input().split())
    numeros = [list(map(float, item)) for item in numeros]

    media = (2 * numeros[i][0] + 3 * numeros[i][1] + 5 * numeros[i][2]) / 10
    medias.append(media)

for i in range(0, len(medias)):
    print("{:.1f}".format(medias[i]))
