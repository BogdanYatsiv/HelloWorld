def correct_tail(body, tail):
    temp = ''.join(reversed(body))
    if temp[0] == tail:
        return True
    else:
        return False