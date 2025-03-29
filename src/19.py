import numpy as np

def sample_data(n):
    """
    Generate n samples from a normal distribution.
    
    Parameters:
    - n (int): Number of samples to generate.
    
    Returns:
    - list: A list of random samples drawn from a normal distribution with mean 0 and standard deviation 1.
    """
    return np.random.randn(n)

sampled_data = sample_data(5)
print(sampled_data)
