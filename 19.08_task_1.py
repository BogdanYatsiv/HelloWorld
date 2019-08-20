from random import randint

rand_num = randint(1,101)

while True:
    user_num = int(input("guess the number: "))
    if user_num > rand_num:
        print("Your answer is bigger")
    elif user_num < rand_num:
        print("Your answer is smaller")
    else:
        print("You are winner!!!")
        break