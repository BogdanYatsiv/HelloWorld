def choose_action():
    action = input('Choose +, -, /, * or q to quit\n')
    return action

def get_sum():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(a,' + ',b,' = ',a+b)

def get_dif():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(a,' - ',b,' = ',a-b)

def get_mult():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(a,' X ',b,' = ',a*b)

def get_div():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(a,' / ',b,' = ',a/b)

status = True
while status:
    status = choose_action()
    if status == '+':
        get_sum()
    elif status == '-':
        get_dif()
    elif status == '*':
        get_mult()
    elif status == '/':
        get_div()
    elif status == 'q':
        print('Thank you for using our product :)\n')
        status = False
    else:
        print('error, choose again')
        status = choose_action()