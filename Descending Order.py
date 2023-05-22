def descending_order(num):
    # Bust a move right here
    sort = sorted(str(num),reverse=True)
    return int(''.join(sort))
