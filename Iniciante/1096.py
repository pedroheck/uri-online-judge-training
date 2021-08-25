i = 1
j = 7
for x in range(15):
    if x % 3 == 0 and x != 0:
        i += 2
        j = 7
    print(f'I={i} J={j}')
    j -= 1
