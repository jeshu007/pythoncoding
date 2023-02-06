def fact(n):
   if n==0:
      return 1
   else:
      return n*fact(n-1)
def countfactors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        return count
def main():
    n=int(input("enter the positive integer:"))
    result=fact(n)
    print("fact of",n,"is",result)
    count=countfactors(n)
    print("no of factors for",n,"is",count)
if __name__=="__main__":
    main()
