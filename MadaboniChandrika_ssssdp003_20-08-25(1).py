#1st prgm
a=[x**3 for x in range(2,11,2)]
print(a)

#2nd prgm
a=eval(input("Enter list of lower case strings: "))
print(a)
b=[]
for x in a:
    b.append(x[0].upper())
print(b)

#3rd prgm
a=eval(input("Enter list of lower case strings: "))
b=[x[0].upper() for x in a]
print(b)

#4th prgm
a=input("Enter any sentence: ")
l=a.split()
b=[]
for x in l:
    b.append([x.upper(),len(x)])    
print(b)

#5th prgm
a=input("Enter any sentence: ").split()
b=[[x.upper(),len(x)] for x in a]
print(b)

#6th prgm
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
sum=[]
try:
    for x in range(len(min(l1,l2))):
        c=l1[x]+l2[x]
        sum.append(c)
    print(sum)
except:
    print(sum)

##7th prgm
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
sum=[]
try:
    c=[(l1[x]+l2[x]) for x in range(len(min(l1,l2)))]
    print(sum)
except:
    print(sum)
