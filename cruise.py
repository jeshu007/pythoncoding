T=int(input("enter the value"))
E=[]
L=[]
for i in range(T):
    e=int(input("Enter the no of guest entering list: "))
    E.append(e)
print(E)
print("\n")
for i in range(T):
    l=int(input("Enter the no of guest leaving list: "))
    L.append(l)
print(L)
print("\n")
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("Maximum no. of guests on the cruise: ", Max)
