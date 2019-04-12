n = int(input())
i = o = 0

for c in range(n):
    num = int(input())
    if 10 <= num <= 20:
        i += 1
    else:
        o += 1
        
print('{} in'.format(i))
print('{} out'.format(o))
