#q1
n=21
c=0
while True:
    u=int(input("Take 1 or 2 or 3 or 4 matchsticks: "))
    n-=u
    if n==0:
        print("user picks Last so computer wins")
        break
    c=5-u
    print(f'computer picked {c}')
    n-=c

#q2) roman to value
s=input("Enter Roman Number: ")
n=len(s)
res=0
d={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,
   'CD':400,'D':500,'CM':900,'M':1000}
for i in range(n-1):
    if d[s[i]]<d[s[i+1]]:
        res-=d[s[i]]
    else:
        res+=d[s[i]]
res+=d[s[n-1]]
print(res)

#q3

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


#q5
#check if string is palindrone or not
s=input("Enter the string: ")
n=len(s)
for i in range(len(s)/2):
    if s[i]!=s[n-1-i]:
        print("False")
        break
print(f'{s} is palindrone')

#q6
#check if n is armstrong
s=int(input("Enter the string: "))
x=int(s)
n=len(s)
res=0
for i in s:
    res+=(int(i),n)
if x==res:
    print("yes")
print("no")

#q7
#print pyramid of numbers
n=int(input(("Enter the no of rows: ")))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i):
        print(j+1,end='')
    for j in range(i-1):
        print(j+1+i,end='')
    print()


        
