try:
    data = input("Enter *num* , *num*: ").split()
    print(int(data[0])/int(data[2]))

except ZeroDivisionError:
    print("Division by zero!")

except ValueError:
    print("Enter corect data!")

finally:
    print("Finally block")