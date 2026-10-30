# bhavya-prasad
A simple arithmatic calculater to solve basic mathematical problems 

def calculator():
    print("Welcome to Python Calculator!")

    num1 = float(input("Enter first number: "))
    operator = input("Choose (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print("Result:", result)


calculator()

