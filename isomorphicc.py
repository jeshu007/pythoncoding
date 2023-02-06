max_char=256
a=str(input("Enter string 1: "))
b=str(input("Enter string 2: "))
def isomorphic(str1, str2):
    m=len(str1)
    n=len(str2)
    if m!=n:
        return False
    mark=[False]*max_char
    map=[-1]*max_char
    for i in range(n):
        if map[ord(str1[i])]==-1:
            if mark[ord(str2[i])]==True:
                return False
            mark[ord(str2[i])]=True
            map[ord(str1[i])]=str2[i]
        elif map[ord(str1[i])]!= str2[i]:
            return False
    return True



print(isomorphic(a,b))
