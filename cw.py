i = 0
while i<100:
    if i%2!=0:
        print(i,end=' ')
    i=i+1

print("for")
a=range(100)
for x in list(a):
    if a[x]%2!=0:
        print(a[x],end=' ')