
num1 = 0
num2 = 0
result = 0
operation = ""


num1 = input("Enter the first number: ")


num1 = float(num1)

num2 = input("Enter the second number: ")


num2 = float(num2)


operation = input("Enter the operation (+, -, *, /): ")


if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
else:
  print("Invalid operator")


print("Result:", result)
