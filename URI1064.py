pos = media = 0

for i in range(6):
    a = float(input())
    if a > 0:
        pos += 1
        media += a
        
media = media / pos

print('{} valores positivos'.format(pos))
print('{:.1f}'.format(media))
