
def is_valid_set(quantities, shapes, colours, patterns):
    return all(len(set(i)) in (1,3) for i in (quantities, shapes, colours, patterns))
    pass
