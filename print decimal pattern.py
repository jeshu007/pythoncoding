a=float(input("Enter the starting number you want: "))
b=int(input("Enter the number of rows to be printed: "))
for i in range(b):
    for j in range(i+1):
        print("%.1f"%a, end=" ")
        a = a+0.1
    print()
