# Chandra

# 1. Input
num1 = input("Input your first number: ")
num2 = input("Input your second number: ")
operator = input("What do you want to do? (\"+ - * /\"): ")
# 2. Process
if operator == "+":
    result = int(num1) + int(num2)
elif operator == "-":
    result = int(num1) - int(num2)
elif operator == "*":
    result = int(num1) * int(num2)
elif operator == "/":
    result = int(num1) / int(num2)
# 3. Output
print(f"The result of {num1} {operator} {num2} is",result,".")
