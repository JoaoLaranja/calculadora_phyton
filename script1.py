import operator

operator = input("insira um operador (+, -, *, /): ")


num1 = float(input("insira um numero: "))
num2 = float(input("insira um segundo numero: "))

if operator == "+":
     result = num1 + num2
     print(f"0 resultado e {result}")
elif operator == "-":
     result = num1 - num2
     print(f"0 resultado e {result}")
elif operator == "*":
    result = num1 * num2
    print(f"0 resultado e {result}")
elif operator == "/":
     result = num1 / num2
     print(f"0 resultado e {result}")
else:
    print("Operador invalido")
