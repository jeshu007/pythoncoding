n=input("enter the statment:")
v="aeiou"
vc=0
for i in n:
    if (i in v):
        vc+=1
print("number of vc=",vc)
