from os import system

a = round(int(input('Write the first number: ')))
b = round(int(input('Write the second number: ')))
operators = input('Write the operations u want(+ - * /:) ')
if(operators == '+'):
    _ = system('cls')
    print(a + b)
elif(operators == '-'):
    _ = system('cls')
    print(a - b)
elif(operators == '*'):
    _ = system('cls')
    print(a * b)
else:
    _ = system('cls')
    print(a / b)
