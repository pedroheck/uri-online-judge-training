N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1)/10

print("Media: %.1f" % media)

if media >= 7:
    print("Aluno aprovado.")
if media < 5:
    print("Aluno reprovado.")
if 5 <= media < 7:
    print("Aluno em exame.")
    score = float(input())
    print("Nota do exame: %.1f" % score)
    media_2 = (media + score)/2
    if media_2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media_2)
