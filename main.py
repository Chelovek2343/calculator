from os import system

a = round(int(input('Write the first number: ')))
b = round(int(input('Write the second number: ')))
operators = input('Write the operations u want(+ - * /:) ')
if(operators == '+'):
    _ = system('cls')
    sum = a + b
    print(f'{a} + {b} = {sum}')
elif(operators == '-'):
    _ = system('cls')
    sum = a - b
    print(f'{a} - {b} = {sum}')
elif(operators == '*'):
    _ = system('cls')
    sum = a * b
    print(f'{a} * {b} = {sum}')
else:
    _ = system('cls')
    sum = a / b
    print(f'{a} / {b} = {sum}')
