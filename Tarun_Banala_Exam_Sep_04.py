#TARUN BANALA      04-09-2025

#1st question answer:

def power(a,b):
    if b<0:
        total=1
        for i in range(-b):
            total*=a
        return 1/total
    else:   
        total=1
        for i in range(b):
            total*=a
        return total
    
a=int(input())
b=a.split()

if len(b)==3:
    print(power(float(b[0]),power(int(b[1]),int(b[2]))))

else :
    print(power(int(b[0]),int(b[1])))

 #2nd question answer:

def Second_Largest(n):
    for i in range(len(n)):
        count=0

        for j in range(len(n)):
            if n[i]>n[j]:
                count+=1
        if count==len(n)-2:
            return  "second largest value in list",n[i],"and its index is",i
n=eval(input("enter a list of elements:"))
print(Second_Largest(n))


 # 3rd question answer:

def Anagram(n,o):
    b=True
    if len(n)==len(o):
        for i in n:
            if i not in o:
                b=False
                break
    return b

n=input("enter the string1").upper()
o=input("enter the string2").upper()
a=Anagram(n,o)

if a==True:
    print("Anagram strings")
else:
    print("Not Anagram strings")



# 7th question answer:

def Convert_Decimal_Binary(n):
    a=''
    while n>=1:
       a+=str(n%2)
       n=n//2

    return a[::-1]
n=int(input("enter a decimal number:"))
print(Convert_Decimal_Binary(n))

#6th question answer:

n=int(input("enter a number of rows"))

for i in range(n):
    for j in range(n-i):
        print(chr(65+j), end="")
    print(" "*i,end="")
    for k in range(n-i-1,-1,-1):
        print(chr(65+k), end="")
    print()



#4th question answer:

from sys import argv
neg_val=0
zero_val=0
pos_val=0
for i in argv[1:]:
    if i<0:
        neg_val+=1
    elif i==0:
        zero_val+=1
    else:
        pos_val+=1

print("NUmber of +ve values:",pos_val)
print("Number of -ve values:",neg_val)
print("Number of Zeroes:",zero_val)

