p_numbers = [x for x in range(10) if x % 2 == 0]

np_numbers = [x for x in range(10) if x%2 == 1 and x%3 == 0]

numbers = [x for x in range(10) if x%2 == 1 and x%3 == 1]

print(p_numbers,'\n',np_numbers,'\n',numbers)