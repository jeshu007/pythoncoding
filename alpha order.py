l=[]
n=int(input("enter the no.of  string:"))
for i in range(n):
    r=input("enter the string:")
    l.append(r)
print(l)
a=input("enter the type of order (A/D):")
if a=="A":
    l.sort( )
    print(l)
elif a=="D":
    l.sort(reverse=True )
    print(l)
else:
    print("no order is found")
