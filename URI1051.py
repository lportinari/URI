renda = float(input())

if renda <= 2000:
    print('Isento')

else:
    
    if 2000 < renda <= 3000:
        percentual = 8
        calcImposto = renda - 2000
        imposto = calcImposto * percentual / 100
    
    elif 3000 < renda <= 4500:
        partImposto = 80
        percentual = 18
        calcImposto = renda - 3000
        imposto = calcImposto * percentual / 100 + partImposto
        
    else:
        partImposto = 350
        percentual = 28
        calcImposto = renda - 4500
        imposto = calcImposto * percentual / 100 + partImposto

    
    print('R$ {:.2f}'.format(imposto))
    
