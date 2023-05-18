#Should return whether or not n is a perfect number

def is_perfect(n):
    sum = 1
    i=2
    while i*i<=n:
        if n%i ==0:
            sum=sum+i+n/i
        i+=1
    return True if sum==n and n!=1 else False
    pass