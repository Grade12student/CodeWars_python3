def accum(s):
    # your code
    res='-'.join([s[i].upper()+(s[i].lower()*i)for i in range(len(s))])
    return res