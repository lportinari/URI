n1, n2, n3, n4 = input().split(' ')

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = ((n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)) / (p1 + p2 + p3 + p4)

print('Media: {:.1f}'.format(media))

if media >= 7:
    print('Aluno aprovado.')

elif media < 5: 
    print('Aluno reprovado.')
    
else:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: {}'.format(n5))
    media2 = (media + n5) / 2
    
    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print('Media final: {:.1f}'.format(media2))
