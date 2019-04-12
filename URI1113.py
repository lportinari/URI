while True: 
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    
    if y == x:
        break
    
    if x < y:
        print('Crescente')
            
    if x > y:
        print('Decrescente')
