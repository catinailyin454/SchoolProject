import math

def find_prime_numbers(n):
    """
    This function returns a list of prime numbers less than or equal to n.
    
    Args:
    - n: An integer representing the upper limit for finding prime numbers.
    
    Example usage:
    >>> find_prime_numbers(10)
    [2, 3, 5, 7]
    """
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        # Check if the number is divisible by any number from 2 to its square root.
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example usage
print(find_prime_numbers(10))
