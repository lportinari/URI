def bhaskara(A, B, C):
    if A == 0:
       return print('Impossivel calcular')
    
    delta = B**2 - 4*A*C
        
    if delta < 0:
       return print('Impossivel calcular')
    
    
    X1 = (-B + (delta**(1/2))) / (2 * A)
    X2 = (-B - (delta**(1/2))) / (2 * A)
    
    return print('R1 = {:.5f}\nR2 = {:.5f}'.format(X1, X2))
    

A, B, C = input().split(" ")  
A = float(A) 
B = float(B) 
C = float(C)

bhaskara(A, B, C)
