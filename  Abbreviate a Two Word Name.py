def abbrev_name(name):
    n = name.split()
    new = ""
    for i in range(len(n)):
        new += n[i][0].upper() + '.'
    return new[:-1] 