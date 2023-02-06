def simple_interest(principal,time,age):
    if age>=60:
        roi=12
    else:
        roi=10
    interest=(principal*time*roi)/100
    return interest
principal=float(input("enter the principal amount"))
time=float(input("enter the time in years"))
age=int(input("enter the age of customer"))
result=simple_interest(principal,time,age)
print("the simple interest is:",result)
