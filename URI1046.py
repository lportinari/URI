i, f = input().split(' ')
i = int(i)
f = int(f)

cont = 0

while True:
    i += 1
    cont += 1
    if i == 24:
        i = 0
    if i == f:
        break

print('O JOGO DUROU {} HORA(S)'.format(cont))
