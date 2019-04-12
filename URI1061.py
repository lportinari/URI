dInicial = int(input().split()[1])

h = input().split(':')
hi = int(h[0])
mi = int(h[1])
si = int(h[2])

dFinal = int(input().split()[1])

h = input().split(':')
hf = int(h[0])
mf = int(h[1])
sf = int(h[2])

days = dFinal - dInicial

hour = hf - hi
if hour < 0:
    hour += 24
    days -= 1

min = mf - mi
if min < 0:
    min += 60
    hour -= 1

sec = sf - si
if sec < 0:
    sec += 60
    min -= 1

print('{} dia(s)'.format(days))
print('{} hora(s)'.format(hour))
print('{} minuto(s)'.format(min))
print('{} segundo(s)'.format(sec))
