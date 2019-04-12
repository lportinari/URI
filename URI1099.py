n = int(input())

for t in range(n):
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    impar = 0
    
    if x == y:
        print(impar)
    
    if x < y:
        for i in range(x+1, y):
            if i % 2 == 1:
                impar += i
        print(impar)
    
    if y < x:
        for i in range(y+1, x):
            if i % 2 == 1:
                impar += i
        print(impar)
