Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... def calculator():
...     print("Welcome to Python Calculator!")
... 
...     num1 = float(input("Enter first number: "))
...     operator = input("Choose (+, -, *, /): ")
...     num2 = float(input("Enter second number: "))
... 
...     if operator == "+":
...         result = num1 + num2
...     elif operator == "-":
...         result = num1 - num2
...     elif operator == "*":
...         result = num1 * num2
...     elif operator == "/":
...         if num2 == 0:
...             print("Cannot divide by zero!")
...             return
...         result = num1 / num2
...     else:
...         print("Invalid operator!")
...         return
... 
...     print("Result:", result)
... 
... 
... calculator()
SyntaxError: invalid syntax
>>> 
===== RESTART: C:/Users/ASUS/OneDrive/Desktop/New folder/calculatormain.py =====
Welcome to Python Calculator!
Enter first number: 67
Choose (+, -, *, /): *
Enter second number: 56667773342222907877000
Result: 3.7967408139289353e+24
>>> 
