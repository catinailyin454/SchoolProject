import random
def get_random_python_code():
    """Generates a random Python code snippet."""
    # Initialize a list of possible statements
    statements = ["print('Hello, World!')", "my_list = [1, 2, 3, 4, 5]", "for i in range(5):", "if x > 0:", "pass"]
    
    # Get a random statement from the list
    statement = random.choice(statements)
    
    # Return the random statement
    return statement