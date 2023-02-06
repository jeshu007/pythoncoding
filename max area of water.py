def maxarea(a,len):
    b=0
    for i in range(len):
        for j in range(i+1,len):
            b=max(b,min(a[j],a[i])*j-i)
    return b
a=[1,5,4,3]
len1=len(a)
print(maxarea(a,len1)
