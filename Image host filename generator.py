import random, string
def generateName():
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(6))
    pass