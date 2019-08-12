from random import random

number = list(str(int(random()*100)))
print(number)
if int(number[0])>int(number[1]):
    print(number[0])
else:
    print(number[1])