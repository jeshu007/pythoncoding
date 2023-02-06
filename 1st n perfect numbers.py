def is_perfect(num):
    
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

def first_n_perfect_numbers(n, m):
    
    count = 0
    num = 2
    while count < n:
        if is_perfect(num):
            count += 1
            print("Perfect number:", num)
            print("First", m, "factors:", end=" ")
            for i in range(1, m + 1):
                if num % i == 0:
                    print(i, end=", ")
            print("\n")
        num += 1


n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
print("the perfect numbers are ",first_n_perfect_numbers(n, m))

