# Function to add two numbers
def add(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

# Function to subtract two numbers
def subtract(num1, num2):
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

# Function to multiply two numbers
def multiply(num1, num2):
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

# Function to divide two numbers
def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

# Main function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    add(num1, num2)
    subtract(num1, num2)
    multiply(num1, num2)
    divide(num1, num2)

# Execute the main function
if __name__ == "__main__":
    main()