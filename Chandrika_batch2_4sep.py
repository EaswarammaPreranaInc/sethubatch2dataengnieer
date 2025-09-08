#4th september
#1st program
def gcd(a,b):
    if a==0 :
        return abs(b)
    elif b==0:
        return abs(a)
    else:
        c=b%a
        while c!=0:
            b=a
            a=c
            c=b%a
        return abs(a)
res=gcd(-4,6)
print(res)


#2nd program
def largest(a):
    c=a[0]
    d=[]
    for i  in range(len(a)):
        if a[i]>c :
            c=a[i]
    for j in range(len(a)):
        if a[j]==c:
             d.append(j)
    return d
a=eval(input("Enter the list: "))
print(largest(a))


#3rd program
def num(a):
    ch,v,c,s,t = 0,0,0,0,0
    for i  in a:
        if i in 'AEIOUaeiou':
            v+=1
        elif not i.isspace():
            c+=1
        if i.isspace():
            if i==' ':
                s+=1
            elif i=='\t':
                t+=1
        elif i.isalpha():
            ch+=1
           
    return [ch,c,v,s,t]
    
a=input("Enter any input: ")
num(a)
print("Number of characters: ",len(a))
print("Number of Vowels: ",num(a)[2])
print("Number of consonants: ",num(a)[1])
print("Number of spaces: ",num(a)[3])
print("Number of tabs: ",num(a)[4])
print("Number of words: ",len(a.split()))


#4th program
from sys import argv
for i in argv[1:]:
    x=eval(i)
    max=0
    min=int(argv[1])
    if x>max:
        max=x
for j in argv[1:]:
    y=eval(j)
    if y<min:
        min=y
print("Largest element: ",max)
print("Smallest element: ",min)


#5th program
def symmetric(a):
    n=len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j]!=a[j][i]:
                return False
    return True
a=eval(input("Enter the matrix: "))
if symmetric(a):
    print("symmetric matrix")
else:
    print("not symmetric")


#6th program
#print pascal triangle
def pascal(n):
    for i in range(n):
        # Print leading spaces for formatting
        print(" " * (n - i), end="")
        c = 1  # First value in each row is always 1
        for k in range(i + 1):
            print(c, end=" ")  # Print current value
            # Calculate next value using binomial coefficient formula
            c = c * (i - k) // (k + 1)
        print()  # Move to next line after each row
        # Call the function to print Pascal's triangle with 5 rows
pascal(5)


#7th program
#convert binary to decimal 
def binaryToDecimal(n):
    n = str(n)
    dec_value = 0
    i=0
    for digit in n[::-1]:
        dec_value += int(digit) * (2**i)
        i+=1
    return dec_value
n = input("Enter a binary number: ")
print(binaryToDecimal(n))









