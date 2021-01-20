num1 = float(input("enetr first number: "))
opp = input("enter operation: ")
num2 = float(input("enetr second number: "))

if opp == "+":
    total = str(num1 + num2)
elif opp == "-":
    total = str(num1 - num2)
elif opp == "*":
    total = str(num1 * num2)
elif opp == "/":
    total = str(num1 / num2)
else:
    print("wrong operation!")

print(total)