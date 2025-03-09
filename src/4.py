from random import randint
def get_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += letters[randint(0, len(letters) - 1)]
    return result