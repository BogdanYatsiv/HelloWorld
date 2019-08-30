class Age_negative_error(Exception):
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return repr(self.data)

def check_paire_age(age):

    if age <= 0:
        raise Age_negative_error("Age can`t be negative!")

    if age % 2 == 0:
        print(f"{age} % 2 == 0")
    else:
        print(f"{age} % 2 != 0")


try:
    age = int(input("Enter your age: "))

    check_paire_age(age)

except Age_negative_error as e:
    print("We obtained error: ",e.data)

except ValueError:
    print("Enter corect data!")