def get_random_string(length):
    import random
    import string
    
    characters = string.ascii_letters + string.digits
    
    return ''.join(random.choice(characters) for i in range(length))
