def alphabet_position(text):
    res = []
    for char in text.lower():
        if char.isalpha():
            position = ord(char) - ord('a') + 1
            res.append(str(position))
    return ' '.join(res)
