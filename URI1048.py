salario = float(input())

if salario <= 400:
    percentual = 15
    reajuste = salario * percentual / 100
    total = reajuste + salario
    
elif salario <= 800:
    percentual = 12
    reajuste = salario * percentual / 100
    total = reajuste + salario
    
elif salario <= 1200:
    percentual = 10
    reajuste = salario * percentual / 100
    total = reajuste + salario
    
elif salario <= 2000:
    percentual = 7
    reajuste = salario * percentual / 100
    total = reajuste + salario

else:
    percentual = 4
    reajuste = salario * percentual / 100
    total = reajuste + salario    

print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: {} %'''.format(total, reajuste, percentual))
