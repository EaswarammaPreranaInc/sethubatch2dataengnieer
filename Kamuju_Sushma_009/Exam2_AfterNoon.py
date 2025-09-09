#q1
def gcd(a,b):
    a=abs(a)
    b=abs(b)
    if b%a==0:
        return a
    while b>0:
        t=b%a
        if t==0:
            return a
        b=a
        a=t
    return a 
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print(gcd(gcd(a,b),c))

#q2
def max_element_indices(l):
    n=len(l)
    res=[]
    #find the max element 
    m=l[0]
    n=len(l)
    for i in range(n):
        if l[i]>m:
            m=l[i]
    print(m)
    # finding the indices of 'm'
    for i in range(n):
        if m==l[i]:
            res.append(i)
    return res
l=eval(input("Enter the list: "))
print(max_element_indices(l))

#q3
#charecters, vowels, consonants, spaces, tabs, words in string 
vowels=('A','E','I','O','U')
def count_consonants_vowels_space_tabs(s):
    v=0
    cons=0
    t=0
    sp=0
    for x in s:
        if x>= 'A' and x<='Z':
            if x in vowels:
                v=v+1
            else:
                cons=cons+1
        elif x=='\t':
            t=t+1
        elif x==' ':
            sp=sp+1
    return (v,cons,t,sp)
s=input("Enter the string: ")
s=s.upper()
l=s.split()
print(f'No of words: {len(l)}')
res=count_consonants_vowels_space_tabs(s)
n=len(s)
print(f'Number of charecters: {n}')
print(f'Number of consonants: {res[0]}')
print(f'Number of vowels: {res[1]}')
print(f'Number of spaces: {res[2]}')
print(f'Number of tabs: {res[3]}')

#q4
from sys import argv
l=[]
for i in range(1,len(argv)):
    l.append(int(argv[i]))
lar=l[0]
sml=l[0]
for x in l:
    if x>lar:
        lar=x
    if x<sml:
        sml=x
print(f'Larget: {lar}')
print(f'Smallest :{sml}')

#q5
def is_symmetric_matrix(mat):
    n=len(mat)
    m=len(mat[0])
    if n==m:
        return True
    return False
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
if is_symmetric_matrix(mat):
    print("Symmetric Matrix")
else:
    print("Not Symmetric Matrix")

#q7
def bin_to_dec(s):
    res=0
    n=len(s)
    res=0
    for i in range(n):
        if int(s[i]):
            res+=pow(2,n-1-i)
    return res
s=input("Enter Binary Number: ")
print(bin_to_dec(s))