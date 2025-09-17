#q2
str=input("Enter the string: ")
d={}
for x in str:
    d[x]=d.get(x,0)+1
freq=0
res=''
for x in str:
    if d[x]>freq:
        freq=d[x]
        res=x
print(res)

#q3
def sort_mat(mat):
    for i in range(len(mat)):
        mat[i]=sorted(mat[i])
    return mat
n=int(input("Number of rows: "))
m=int(input("Number of columns: "))
mat=input("Enter comma seperated values: ")
mat=mat.split(',')
res=[]
k=0
for i in range(n):
    t=[]
    for j in range(m):
        t.append(int(mat[k]))
        k+=1
    res.append(t)
mat=res
print(sort_mat(mat))
#q4
def sum_digits(l):
    if(len(l)==0):
        return 0
    return l[0]+sum_digits(l[1:])
l=eval(input("Enter the list: "))
print(sum_digits(l))

#q5
list_strings=eval(input("Enter list of strings: "))
def count_strings(list_strings):
    count=0
    for str in list_strings:
        if len(str)>2:
            if str[0]==str[-1]:
                count+=1
    return count
print(count_strings(list_strings))

#q6
n=int(input("Enter n: "))
x=1
for i in range(n):
    for j in range(i+1):
        print(x,end=' ')
        x+=2
    print()

#q7
s=input("Enter the string: ")
s=s.upper()
s=sorted(s)
d={}
for x in s:
    d[x]=d.get(x,0)+1
v=('A','E','I','O','U')
for x in set(s):
    if x in v:
        print(x,d[x],sep='...',end=',')

