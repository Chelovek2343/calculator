a = round(int(input('Write the first number: ')))
b = round(int(input('Write the second number: ')))
operators = input('Write the operations u want(+ - * /:) ')
if(operators == '+'):
    print(a + b)
elif(operators == '-'):
    print(a - b)
elif(operators == '*'):
    print(a * b)
else:
    print(a / b)