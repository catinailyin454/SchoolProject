def add_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

def square_root(num):
    if num > 0:
        return math.sqrt(num)
    else:
        return "Square root of negative number is not possible."

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def print_operation():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    operation = input("Enter an arithmetic operation (+, -, *, /): ")

    if operation == "+":
        result = add_numbers(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        print("Invalid operation.")
        return

    print(f"The result of {operation} {a} and {b} is: {result}")

print_operation()
