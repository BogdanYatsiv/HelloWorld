n = range(int(input("enter number ")))

first = 0
second = 1

for i in list(n):
    first,second = second,first+second
    if second>len(n):
        continue
    print(second,end=' ')
    