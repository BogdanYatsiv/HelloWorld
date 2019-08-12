while True:    
    num = int(input('Enter your number '))
    temp = 2
    while num % temp != 0:
        temp += 1
    if temp == num:
        print('It is prime number\n')
    else:
        print('It is not prime number\n')
