#q3
# def (s1,s2):
def check_anagrams(l1,l2):
    if l1==l2:
        return True
        # print("Anagram strings")
    else:
        return False
        print("Not anagram string")
s1=input("Enter 1st string:")
s2=input("Enter 1st string:")
l1=sorted(s1)
l2=sorted(s2)
if check_anagrams(l1,l2):
    print("Anagram strings")
else:
    print("Not anagram string")

#q4
from sys import argv 
def count_digits(l):
    n=len(l)
    print(n)
    p=0
    n=0
    z=0
    for x in l:
        if x>0:
            p=p+1
        elif x<0:
            n=n+1
        else:
            z=z+1
    print(f'Number of positive values:{p}')
    print(f'Number of negative values:{n}')
    print(f'Number of zero values:{z}')

res=[]
for i in range(1,len(argv)):
    res.append(int(argv[i]))
count_digits(res)


#q5
def check_max(mat,r,c):
    l=[mat[0][0],0,0]
    for i in range(r):
        for j in range(c):
            if mat[i][j] >l[0]:
                l[0]=mat[i][j]
                l[1]=i
                l[2]=j
    l[1]=l[1]+1
    l[2]=l[2]+1
    return l
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
print(check_max(mat,r,c))

#q6
n=int(input("Enter n: "))
for i in range(n):
    if i==0:
        for j in range(n-i-1):
            print(chr(65+j),end='')
        print(' '*i,end='')
        for j in range(n-i-1,-1,-1):
            print(chr(65+j),end ='')
        print()
        continue
    for j in range(n-i):
        print(chr(65+j),end='')
    print(' '*i,end='')
    for j in range(n-i-1,-1,-1):
        print(chr(65+j),end ='')
    print()

#q7
def itod(n):
    res=""
    while n>0:
        t=n%2
        n=n//2
        res=str(t)+res
    print(res)
n=int(input("Enter the input: "))
itod(n)

#q1
#q1
def power(a,b):
    res=1
    neg=False
    if b<0:
        neg=True
        b=-1*b
    for i in range(b):
        res*=a
    if neg:
        return 1/res
    return res
a=eval(input("Enter a:")) 
b=eval(input("Enter b:")) 
c=eval(input("Enter c:")) 
if c<0:
    print("Not Possible!")
    exit()
t=power(b,c)
print(power(a,t))

#q2
l=eval(input("Enter list:"))
m1=0
m2=0
n=len(l)
# find the maximum element 'm1' 
m1=l[0]
for i in range(1,n):
    if l[i]>m1:
        m1=l[i]
#find the element less m1 but greater than remaining all 
m2=-1000
idx=1
for i in range(n):
    if l[i]<m1 and l[i]>m2 :
        idx=i
        m2=l[i]
print(m2,idx)
