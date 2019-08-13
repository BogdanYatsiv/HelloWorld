number = int(input('enter number '))

result = 1
my_list = list(range(number+1))
my_list.pop(0)

for i in my_list:
    result*=i

print(result)
