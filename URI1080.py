maior = cont = pos = 0

for i in range(100):
    num = int(input())
    cont += 1
    
    if cont == 1:
        maior = num
        
    elif num > maior:
        maior = num
        pos = i+1

print(maior)
print(pos)
