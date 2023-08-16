# Header
print("=" * 40)
print("Welcome to the simple calculator app.")
print("=" * 40)

# Input First Number
print("Please enter a number:")
number1 = int(input())

# Input Operator
print("Input your Aritmetich Operators: (+, -, *, /):")
operator = input()

# Input Second Number
print("Please enter a number:")
number2 = int(input())

# Aritmetich Operator Functions
if operator == "+":
    result = number1 + number2 
    print("=" * 40)
    print("The result of the addition of:", f"\n{number1} {operator} {number2} = {result}")
elif operator == "-":
    result = number1 - number2
    print("=" * 40)
    print("Subtraction result of:", f"\n{number1} {operator} {number2} = {result}")
elif operator == "*":
    result = number1 * number2
    print("=" * 40)
    print("The multiplication result of:", f"\n{number1} {operator} {number2} = {result}")
elif operator == "/":
    result = number1 / number2
    print("=" * 40)
    print("The results of the Division of:", f"\n{number1} {operator} {number2} = {result}")
else:
    print("=" * 40)
    print("Error: No Aritmetich Operators")