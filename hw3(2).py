number=int(input("Enter four-digit number: "))
str_number=str(number)
str_number.split()

result=eval("int(str_number[0])*int(str_number[1])*int(str_number[2])*int(str_number[3])")
print ('Result of multiplication:',result)

print ('Reversed number:',''.join(reversed(str(number))))

list_of_numbers=list(str_number)
list_of_numbers.sort()
print('Sorted numbers:',list_of_numbers)
