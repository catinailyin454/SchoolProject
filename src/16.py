import random

def create_random_string(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    for _ in range(length):
        result += characters[random.randint(0, len(characters) - 1)]
    return result

print(create_random_string(10))
