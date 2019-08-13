my_list = []

while True:
    number = int(input('Enter number '))
    if number <= 0:
        print('Error!')
        break
    else:
        my_list.append(number)
        print(my_list)