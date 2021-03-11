import calculator

a = int(input("First number: "))
cmd = str(input("Command: "))
b = int(input("Second number: "))

if cmd == '+':
    print(calculator.sum(a, b))

if cmd == '-':
    print(calculator.minus(a, b))

if cmd == '/':
    print(calculator.div(a, b))
