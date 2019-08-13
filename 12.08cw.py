list_of_numbers = []
emount = input('Enter emount of numbers ')

i = 0
while i < int(emount):
    list_of_numbers.append(int(input('enter number ')))
    i += 1

print(list_of_numbers)

max_number = max(list_of_numbers)
min_number = min(list_of_numbers)

print('Max = '+str(max_number)+' \nMin = '+str(min_number))