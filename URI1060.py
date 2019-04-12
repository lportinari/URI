pos = 0

for i in range(6):
    num = float(input())
    if num > 0:
        pos += 1
        if num == 0:
            continue
    
print('{} valores positivos'.format(pos))
