n = int(input())


def time(n):
    m = h = 0
    while n >= 60:
        n -= 60
        m += 1
    while m >= 60:
        m -= 60
        h += 1
    return print('{}:{}:{}'.format(h, m, n))
    

time(n) 
