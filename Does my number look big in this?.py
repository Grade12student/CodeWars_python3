def narcissistic(value):
    digits = [int(i) for i in str(value)]
    result = sum(d ** len(digits) for d in digits)
    if result == value:
        return True
    return False # Code away