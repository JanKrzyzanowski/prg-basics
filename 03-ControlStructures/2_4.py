number1= int(input("Enter your first number: "))
number2= int(input("Enter your second number: "))
operator= input("Enter your operation: ")

if operator == "+":
    result = int(number1+number2)
elif operator == "-":
    result = int(number1-number2)
elif operator == "*":
    result = int(number1*number2)
elif operator == "/":
    result = int(number1/number2)
else:
    result = ("You have entered an invalid operator")

print(f'{number1} {operator} {number2} = {result}')