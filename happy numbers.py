def happy(n):
    a=set()
    while n not in a:
        a.add(n)
        n=sum([int(i)**2 for i in str(n)])
    return n==1
n=int(input("enter the number:"))
print(happy(n))
