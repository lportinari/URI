while True: 
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    soma = 0
    
    if y <= 0 or x <= 0:
        break
    
    if x < y:
        for i in range(x, y+1):
            soma += i
            print('{}'.format(i), end=' ')
            if i == y:
                print('Sum={}'.format(soma))
            
    if y < x:
        for i in range(y, x+1):
            soma += i
            print('{}'.format(i), end=' ')
            if i == x:
                print('Sum={}'.format(soma))
