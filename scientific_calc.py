import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Invalid input"

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

# You can add more functions as needed

# Example usage
result = add(5, 3)
print(result)