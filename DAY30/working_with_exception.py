
"""worwing with exception"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error you can not divide by cero, try with numbers greater than 0.")

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
user = input("type 'yes' to continue or 'not' to finish: ")
if user == "not":
    False  
while user:
    choice = input("Enter choice(1/2/3/4): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError: 
        print("It is not allowed to enter any letter to make calculator, try with numbers")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))
    else:
        print("Invalid input, only is allow number from 1 to 4.")
  