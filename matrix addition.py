def add_matrices(mat1,mat2):
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    return result
m=int(input("enter the number of rows in matrix"))
n=int(input("enter the number of columns in matrix"))

mat1=[]
for i in range(m):
    row=list(map(int,input("enter the row{i+1}of mat1").strip().split()))
    mat1.append(row)

mat2=[]
for i in range(m):
    row=list(map(int,input("enter the row{i+1}of mat2").strip().split()))
    mat2.append(row)

result=add_matrices(mat1,mat2)
for row in result:
    print(row)
