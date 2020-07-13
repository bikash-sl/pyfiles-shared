"""
Exercise 2 - Faulty Calculator
a calculator which will correctly solve all the problems
except the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
"""

operator = input("Enter any of the available operator (/, *, +, -): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
ans = float()
if num1 == 45 and operator == '*' and num2 == 3:
    ans = 555
elif num1 == 56 and operator == '+' and num2 == 9:
    ans = 77
elif num1 == 56 and operator == '/' and num2 == 6:
    ans = 4
elif operator == '/':
    ans = num1 / num2
elif operator == '*':
    ans = num1 * num2
elif operator == '+':
    ans = num1 + num2
elif operator == '-':
    ans = num1 - num2
else:
    print("Error! Please check your input.")
    exit()
print("Result =", str(ans))
