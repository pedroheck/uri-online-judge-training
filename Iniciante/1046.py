begin, end = input().split()

begin = int(begin)
end = int(end)

if end > begin:
    duracao = end - begin
    print("O JOGO DUROU", duracao, "HORA(S)")
if begin > end:
    duracao = (24 - begin) + end
    print("O JOGO DUROU", duracao, "HORA(S)")
if begin == end:
    print("O JOGO DUROU 24 HORA(S)")
