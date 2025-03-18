import random

def get_random_code():
    """Returns a random code of length 5"""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5))
