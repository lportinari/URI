a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

unsorted = [a, b, c]
sort = []

sort = sorted(unsorted)

for i in sort:
    print(i)

print()

for i in unsorted:
    print(i)
