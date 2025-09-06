
#q4
#Multiply 2 Matrices
def take_matrix():
    r=int(input("Enter no of rows: "))
    c=int(input("Enter no of cols: "))
    l=input("Enter matrix:")
    l=l.split()
    mat=[]
    x=0
    for i in range(r):
        t=[]
        for j in range(c):
            t.append(int(l[x]))
            x=x+1
        mat.append(t)
    return mat

def multiply_rows(mat1,i,mat2,j):
    l1=mat1[i]
    l2=[]
    for k in range(len(mat2)):
        l2.append(mat2[k][j])
    #multiply l1 and l2
    res=0
    for i in range(len(l1)):
        res+=l1[i]*l2[i]
    return res
def multiply_matrices(mat1,mat2):
    n1=len(mat1)
    m1=len(mat1[0])
    n2=len(mat2)
    m2=len(mat2[0])
    res=[]
    if m1!=n2:
        print("Not Possible to multiply")
    else:
        for i in range(n1):
            v=[]
            for j in range(m2):
                v.append(multiply_rows(mat1,i,mat2,j)) #ith row of mat1 and jth col of mat2
            res.append(v)
    return res
mat1=take_matrix()
mat2=take_matrix()
print(multiply_matrices(mat1,mat2))