def mthmaxnthmin(lst,m,n):
    lst.sort(reverse=True)
    mthmax = lst[m-1]
    lst.sort()
    nthmin = lst[n-1]
    return(mthmax,nthmin)
def main():
    n=int(input("enter the no of elements in the list:"))
    lst=[]
    print("enter the values:")
    for i in range(n):
        lst.append(int(input()))
    m=int(input("enter the Mth largest value"))
    n=int(input("enter the Nth smallest value"))
    mthmax,nthmin = mthmaxnthmin(lst,m,n)
    print("Mth max number:",mthmax)
    print("Nth min number:",nthmin)
    sum=mthmax+nthmin
    print("sum of mth max and nthmin",sum)
    diff=mthmax-nthmin
    print("diff of mthmax and nthmin",diff)
if __name__=="__main__":
    main()   
