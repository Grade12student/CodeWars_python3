def count_bits(n):
    res = 0
    for i in bin(n):
        if i=='1':
            res+=1
    return res