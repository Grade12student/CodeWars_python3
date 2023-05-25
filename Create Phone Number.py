def create_phone_number(n):
    #your code here
    s = [str(i) for i in n]
    res = "".join(s)

    return ('('+str(res[0:3]) +')'+' '+res[3:6]+'-'+res[6:])