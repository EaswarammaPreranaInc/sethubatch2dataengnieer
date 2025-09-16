# write a function for power without using predefinded methods
def power(n,p):
    pow=1
    for i in range(p):
        pow*=n
    return pow
a=eval(input())
b=eval(input())
c=eval(input())
if(b>0):
    k=power(b,c)
    p=power(a,k)
    print(p)
elif(b<0 ):
    b=(-1)*(b)
    k=power(b,c)
    p=1/power(a,k)
    print(p)
elif(c<0 ):
    c=(-1)*(c)
    k=1/power(b,c)
    p=power(a,k)
    print(p)
else:
    print(1)

#write a program for find the seecond largest number in given list

n=eval(input())
m= int(input())
k=n.copy()
b=[]
while n:
    large=n[0]
    for i in n:
            if i>large:
                large=i
    b.append(large)
    n.remove(large)
print(b[m-1])
for i in range(len(k)):
     if k[i]==b[m-1]:
          print(i)
     

    

    
#wite a function to check strings are anargam or not

def ana(a,b):
    if a==b:
                return True
    return False
            
n=input().upper()
m=input().upper()
a=sorted(n)
b=sorted(m)
if(ana(a,b)):
    print('Anagrams')
else:
    print('Not Anagrams')


#write a program for the no.of postives, negative and zeros in cmd

from sys import argv
c=0
c1=0
c2=0
a=argv[1:]
for i in a:
    if int(i)>0:
        c+=1
    elif int(i)<0:
        c1+=1
    else:
        c2+=1
print('Number of +ve values :',c)
print('Number of -ve values :',c1)
print('Number of zeroes :',c2)

#write a program for the find the largest number in matrix and get the row number and column number
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
    max=a[0][0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]>max:
                max=a[i][j]
    print('Largest element: ',max)
    print('Row number :',i)
    print('Column number:',j)


#write a program for print the given patterrn

"""
ABCDEFGFEDCBA
ABCDEF FEDCBA
ABCDE   EDCBA
ABCD     DCBA
ABC       CBA
AB         BA
A           A"""
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
            

# WRITE A function for convert the number from decimal to binary

def dec(n):
    c=''
    while(n>0):
        a=n%2
        c+=str(a) 
        n=n//2
    c=c[::-1]
    return c
n=int(input())

print(dec(n))