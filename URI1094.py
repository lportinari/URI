testes = int(input())

totCobaias = ratos = coelhos = sapos = 0

for c in range(testes):
    caso = input().split(' ')
    
    num = int(caso[0])
    esp = str(caso[1]).upper()
    
    totCobaias += num
    
    if 'R' in esp:
        ratos += num
    elif 'C' in esp:
        coelhos += num
    elif 'S' in esp:
        sapos += num

print('Total: {} cobaias'.format(totCobaias))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(float((100*coelhos)/totCobaias)))
print('Percentual de ratos: {:.2f} %'.format(float((100*ratos)/totCobaias)))
print('Percentual de sapos: {:.2f} %'.format(float((100*sapos)/totCobaias)))
