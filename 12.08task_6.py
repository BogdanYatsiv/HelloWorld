my_list = []
repits = int(input('Enter amount of numbers '))

i = 0
while i < repits:
    number = int(input('Enter number '))
    if number <= 0:
        print('Error!')
        break
    else:
        my_list.append(number)
        print(my_list)
        i+=1