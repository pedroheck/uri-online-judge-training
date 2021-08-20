vitorias_inter, vitorias_gremio, empates = 0, 0, 0
numero_grenais = 1

while True:
    placar_inter, placar_gremio = input().split()

    placar_inter = int(placar_inter)
    placar_gremio = int(placar_gremio)

    if placar_inter > placar_gremio:
        vitorias_inter += 1
    elif placar_gremio > placar_inter:
        vitorias_gremio += 1
    else:
        empates += 1

    resposta_grenal = int(input('Novo grenal (1-sim 2-nao)\n'))
    if resposta_grenal == 2:
        break
    elif resposta_grenal == 1:
        numero_grenais += 1

print(f'{numero_grenais} grenais')
print(f'Inter:{vitorias_inter}\nGremio:{vitorias_gremio}\nEmpates:{empates}')

if vitorias_gremio > vitorias_inter:
    print('Gremio venceu mais')
elif vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
