# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiply/divide any two numbers you provide.")
first_input = float(input("Enter in first number>> "))
second_input = float(input("Enter in second number>> "))
operation = input("Would you like to add/subtract/multiply/divide? (please be exact with the wording and spelling)>> ")


#define all functions and their operations
def add():
    result = first_input + second_input
    print(result)
def subtract():
    result = first_input - second_input
    print(result)
def multiply():
    result = first_input * second_input
    print(result)
def divide():
    result = first_input / second_input
    print(result)


if operation == "add":
    add()
elif operation == "subtract":
    subtract()
elif operation == "multiply":
    multiply()
elif operation == "divide":
    divide()
else:
    print("Sorry, I do not understand your request :(. Please try again.")

