from itertools import cycle

def find_pattern(sequence):
    diffs = [y - x for x, y in zip(sequence, sequence[1:])]    
    for i in range(1, len(diffs) + 1):
        if len(diffs) % i == 0 and all(a == b for a, b in zip(diffs, cycle(diffs[:i]))): 
            return diffs[:i]
#