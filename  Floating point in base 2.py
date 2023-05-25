def binary(value):
    if isinstance(value, int):
        return bin(value)
    
    neg = '-' if value < 0 else ''
    value = abs(value)
    whole = ''
    i = abs(int(value))
    while i > 0:
        whole = str(i%2) + whole
        i//=2
    dec = ''
    d = value % 1;
    while d > 0:
        d*=2
        dec += str(int(d))
        d%=1
    return neg + '0b' + (whole or '0') + '.' + (dec or '0')