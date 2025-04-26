def find_duplicate_numbers(nums):
    """
    Find all duplicates in an array of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list containing all duplicate numbers found.
    """
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Example usage
numbers = [1, 5, 3, 6, 4, 7, 2]
print(find_duplicate_numbers(numbers))
