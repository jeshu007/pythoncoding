def print_pattern(n):
    for i in range(1,n+1):
        print(" "*(2*(n-i)),end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
n=int(input("enter the number of rows:"))
print_pattern(n)
