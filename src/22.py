def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

result = sum_of_squares(5)
print("The sum of squares up to", 5, "is:", result)
