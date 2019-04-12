i = 1
j = 8

for c in range(15):
    j -= 1
    print('I={} J={}'.format(i, j))
    if j == 5:
        i += 2
        j = 8
        
