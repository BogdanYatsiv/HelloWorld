def make_move(sticks):
    if sticks == 21 or sticks == 17 or sticks == 13 or sticks == 9 or sticks == 5 or sticks == 1:
        return 1
    elif sticks == 18 or sticks == 14 or sticks == 10 or sticks == 6 or sticks == 2:
        return 2
    elif sticks == 19 or sticks == 15 or sticks == 11 or sticks == 7 or sticks == 3:
        return 3