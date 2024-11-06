#TODO: Write a calculator that asks for 2 float numbers and ask for a operator the user want to
#TODO: apply for the numbers. Implement summation, substraction, multiplication and division
#TODO: Implement everything as a function

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
    else:
        print("Invalid operator")

    print("Result:", result)

calculator()