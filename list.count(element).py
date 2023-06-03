def find_it(seq):
    count=[]
    for i in seq:
        ii = seq.count(i)
        if ii%2!=0:
            return i
    return None
