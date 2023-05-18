def duplicate_encode(word):
    #your code here
    return "".join(["(" if word.lower().count(i) == 1 else ")" for i in word.lower()])