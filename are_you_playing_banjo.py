def areYouPlayingBanjo(name):
    temp = list(name)
    if temp[0] == 'r' or temp[0] == 'R':
        return name+' plays banjo'
    else:
        return name+' does not play banjo'