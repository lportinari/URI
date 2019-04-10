dias = int(input()) 
ano = mês = 0

while dias >= 365:
    dias -= 365
    ano += 1

while dias >= 30:
    dias -= 30
    mês += 1
    
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mês))
print('{} dia(s)'.format(dias))
