n=input("enter the string:")
rv=" "
i=len(n)
while i>0:
    rv+=n[i-1]
    i=i-1
print("reverse of the string :"rv) 
