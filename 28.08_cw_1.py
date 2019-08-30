try:
    num = int(input("Enter int number: "))
    if num % 2 == 0:
        print(f"{num} % 2 == 0")
    else:
        print(f"{num} % 2 != 0")
except Exception:
    print("You entered wrong data!")