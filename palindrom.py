a=input("enter the number")
def palindrom(a):
    b=a[::-1]
    if a ==b:
        return True
    else:
        a!=b
        return False
print(palindrom(a))
