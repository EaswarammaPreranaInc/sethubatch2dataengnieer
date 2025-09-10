#Q1
def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)

def gcd3(a, b, c):
    temp_gcd = gcd2(a, b)
    return gcd2(temp_gcd, c)

try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = int(input('Enter the third number: '))
    
    result = gcd3(a, b, c)
    print(f'The GCD of {a}, {b}, and {c} is: {result}')

except ValueError:
    print('Invalid input. Please enter valid integer numbers.')

#Q3
s=input()
v='AEIOUaeiou'
char=len(s)
vowel=cons=sp=tab=word=0
for i in s:
    if i.isalpha(): 
        if i in v:
            vowel += 1
        else:
            cons += 1
    elif i.isspace():  
        sp += 1
    elif i == '\t':  
        tab += 1

n=s.split()
word=len(n)
print('no of character:',char)
print('no of vowel:',vowel)
print('no of consonant:',cons)
print('no of space:',sp)
print('no of tab:',tab)
print('no of word:',word)
    
#Q4
from sys import argv
a=[]
for x in argv[1:]:
    a.append(int(x))
large=a[0]
small=a[0]
for i in a:
    if i>large:
        large=i
for i in a:
    if i<small:
        small=i
print('largest element is :',large)
print('smallest element is :',small)

#Q5
try:

    print('Enter matrix until ctrl+z')
    a = []
    while True:
        line=input().split() 
        row = [] # Empty list
        for x in line: 
            row.append (int(x))
        a. append (row) 
except:
        b=[]
        m=len(a)
        n=len(a[0])
        for j in range(n):
            row=[]
            for i in range(m):
                row.append(a[i][j])
            b.append(row)
if(a==b):
    print('Symmetric')
else:
    print('Not Symmetric')

#Q7
n=int(input('enter any binary number'))
k=str(n)[::-1]
m=0
for i in range(len(k)):
    m+=(2**i*int(k[i]))
print(m)

