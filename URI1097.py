i = 1
j = 8
cont = 0
for c in range(15):
    cont += 1
    j -= 1
    print('I={} J={}'.format(i, j))
    if cont == 3:
        i += 2
        j += 5
        cont = 0
     
