a=int(input("Enter the row limit: "))
b=int(input("enter the row number"))
for i in range(1,a+1):
    for j in range(0, a-i+1):
        print(' ', end='')
    c=1
    for j in range(1,i+1):
        print(' ', c, sep='', end='')
        c=c*(i-j)//j
    print()
from math import pow
def sumoftermsinnthrow(n):
    sum=n*(2*pow(n,2)+1)
    return sum
if __name__=="__main__":
    n=4
    print("sum of all the terms in nth row",int(sumoftermsinnthrow(n)))

