def move_zeros(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] !=0:
            lst[count] = lst[i]
            count+=1
    while count < len(lst):
        lst[count]=0
        count+=1
    return lst