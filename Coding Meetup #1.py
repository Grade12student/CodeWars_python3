def count_developers(lst):
    # Your code here
    count=0
    for d in lst:
        if d['continent']=='Europe' and d['language']=='JavaScript':
            count+=1
    return count