def duplicate_count(text):
    text = text.lower()
    count = 0
    c_count = {}
    
    for c in text:
        if c.isalnum():
            if c in c_count:
                c_count[c] += 1
                if c_count[c] == 2:
                    count += 1
            else:
                c_count[c] = 1
    
    return count