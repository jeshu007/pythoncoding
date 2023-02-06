a=input("enter the string")
b=input("enter the string")
def matches(a,b):
    matches=0
    for i in range (min(len(a),len(b))):
        if a[i] == b[i]:
            matches+=1
    return matches
print("no of matches",matches(a,b))
