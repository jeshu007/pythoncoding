l=[]
n=int(input("enter the no of elements"))
for i in range(n):
    r=int(input("enter the value"))
    l.append(r)
    
def sumsquare(l):
    odd=0
    even=0
    for num in l:
        if num%2==0:
            even+=(num**2)
        else:
            odd+=(num**2)
    return[odd,even]
print(sumsquare(l))
