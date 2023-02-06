l1=[]
l2=[]
n=int(input("enter the no of element"))
m=int(input("enter the no of element"))
for i in range (n):
    a=int(input("enter the value"))
    l1.append (a)
print (l1)
for j in range(m):
    b=int(input("enter the value"))
    l2.append (b)
print(l2)
lst=l1+l2
lst.sort()
print(lst)
