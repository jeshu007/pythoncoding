l=[]
n=int(input("enter the number of elements"))
for i in range(n):
     r=int(input("enter the value"))
     l.append(r)
def sumsquare(l):
     odd=0
     even=0
     for i in l:
         if i%2==0:
             even+=i**2
         else:
             odd+=i**2

     return [odd,even]
print(sumsquare(l))
