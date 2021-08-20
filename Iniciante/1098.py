### NÃO TERMINADO ###
i = 0
j = 1
for x in range(33):
    if x % 3 == 0 and x != 0:
        i += 0.2
        j -= 2.8

    if i % 1 != 0 and j % 1 != 0:  # se nem i nem j forem inteiros
        print(f'I={i:.1f} J={j:.1f}')
    elif i % 1 == 0 and j % 1 != 0:
        print(f'I={int(i)} J={j:.1f}')
    elif i % 1 != 0 and j % 1 == 0:
        print(f'I={i:.1f} J={int(j)}')
    elif i % 1 == 0 and j % 1 == 0:
        print('I=', int(i), 'J=', int(j))
    j += 1
