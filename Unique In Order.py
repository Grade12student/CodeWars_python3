def unique_in_order(s):
    ans = []
    prev = 0
    for cur in s:
        if cur != prev:
            ans.append(cur)
            prev = cur
    return ans