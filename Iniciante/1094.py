n = int(input())
coelhos, ratos, sapos = 0, 0, 0

for _ in range(n):
    quantia, tipo = input().split()
    quantia = int(quantia)
    tipo = tipo.upper()
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

total_cobaias = coelhos + ratos + sapos

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}')
print(f'Percentual de coelhos: {((coelhos / total_cobaias) * 100):.2f} %')
print(f'Percentual de ratos: {((ratos / total_cobaias) * 100):.2f} %')
print(f'Percentual de sapos: {((sapos / total_cobaias) * 100):.2f} %')
