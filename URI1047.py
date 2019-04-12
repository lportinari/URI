hi, mi, hf, mf = input().split(' ')
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

totHoras = 0
totMin = 0

if hi == hf == mi == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

else:
    while True:
        if mi == 60:
            mi = 0
            hi += 1
            
        if totMin == 60:
            totMin = 0
            totHoras += 1
            
        if mi == mf:
            break
        
        mi += 1
        totMin += 1
          
    while True:
        if hi == 24:
            hi = 0
            
        if hi == hf:
            break
        
        hi += 1
        totHoras += 1
        
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(totHoras, totMin))
    
