par = impar = pos = neg = 0

for i in range(5):
    num = int(input())
    
    if num % 2 == 0:
        par += 1
        
    elif num % 2 == 1:
        impar += 1
        
    if num > 0:
        pos += 1
        
    if num < 0:
        neg += 1
            
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
        
