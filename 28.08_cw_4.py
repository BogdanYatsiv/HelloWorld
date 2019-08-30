class Number_error(Exception):
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return repr(self.data)

WEEK = {1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"}

while True:
    try:
        day = int(input("Enter number of the day: "))

    except ValueError:
        print("Enter number!")

    else:
        print(WEEK.get(day,"There is no such day"))