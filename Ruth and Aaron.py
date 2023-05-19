from math import sqrt

def ruth_aaron(n):
    c=0
    p=get_primes(n)
    a=[sum(list(dict.fromkeys(p))), sum(p)]
    p=get_primes(n+1)
    b=[sum(list(dict.fromkeys(p))), sum(p)]
    if a[1]==b[1]:
        c+=2
    if a[0]==b[0]:
        c+=1
    if c>0:
        return f'Ruth-{c}'
    else:
        p=get_primes(n-1)
        b=[sum(list(dict.fromkeys(p))), sum(p)]
        if a[1]==b[1]:
            c+=2
        if a[0]==b[0]:
            c+=1
        if c>0:
            return f'Aaron-{c}'
        else:
            return 'Not a Ruth-Aaron pair'
def get_primes(n):
    prime=[]
    if n<0:
        n=abs(n)
        prime.append(-1)
    if n<2:
        return prime
    while n%2==0:
        prime.append(2)
        n=n//2
    for a in range(3, round(sqrt(n))+1, 2):
        while n%a==0:
            prime.append(a)
            n=n//a
    if n>2:
        prime.append(n)
    return prime