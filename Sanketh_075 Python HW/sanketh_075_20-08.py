
a = [x**3 for x in range(2,2,20)]
print(a)

#program to extract first char of strings

a = eval(input("enter the lower case of list of strings:")) #enter a list
b=[]
for x in a:
    b.append(x[0].upper())
print(b)

b = [x[0].upper() for x in a] #with list comprehension 

#program to append each word of sentence and its length

a=input("enter any sentence: ")
b = a.split()                            #without comprehension 
c =[]
for x in b:
    c.append([x.upper(),len(x)])  #print[[x.upper(),len(x)]for x in b]

print(c)

#progam to ADD TWO LIST 
a = eval(input("enter 1st list: ")) #[10,20,30,40,50,60]
b = eval(input("enter 2nd list: ")) #[100,200,300,400]
small = min(lens(a),len(b))
c =[]
for i  in range(small): #with comprehension
    c.append(a[i]+b[i])  #print[c =a[i]]
print(c)


#use initialize list without zeros and commprehension

m = int(input("how many list:"))
n = int(input("how  many elements:"))
a=[]
for i in range(m):
    a.append([0]*n)
print(a)

#with comprehension
a=[[0]*n for i in range(m)]
print(a)

#write a program to extract elements of 1st list which are not in 2nd list
#without comprehension
m = eval(input("1st list:"))
n = eval(input("2nd list:"))
c=[]
for x in m:
    if x not in n:
        c.append(x)
print("elements of  1st list not  present in 2nd list:",c)

#with comprehension

c=[x for x in m if x not  in n]
print(c)


#program to print even numbers betw 1 to 20 with comprehension

a=[x for x in range(1,21)if x%2 == 0]
print("print even numbers:",a)

a = [x for x in range(2,21,2)] #without if condition 
print(a)


#prigram to print those squares of 1,2,3, divisible by 2 till 20

a=[x**2 for x in range(1,21) if x**2%2 == 0]
print(a)


#program to add each elements of 1st list to 2nd elements
#without comprehension
a=eval(input("enter 1st list:"))
b=eval(input("enter 2nd list:"))
c=[]
for x in a:
    for y in b:
        c.append(x + y)
print(c)

with comprehension
c =[x+y for x in a for y in b]
print(c)


#PROGRAM TO  CONCATINATE EACH CHARACTER OF 1ST STRING WITH 2ND STRING
a=input("enter 1st string:")
b=input("enter 2nd string:")
c=[x+y for x in a for y in b] #WITH COMPREHENSION
print(c)


#Convert a nested list to list

a=eval(input("enter nested list:")) #[[10,20,30],[40,50,60],[70,80,90]]
b=[]
for x in a:
    b.extend(x)  #without comprehension
print(b)


b=[y for x in a for y in x]
print(b)

b=eval(input("Enter a nested list:"))
a=[[j for j in range(i)]for i in range(5)]
print(a)


#Most tricky program
a=eval(input("Enter list of strings: ")) #['Sanketh','Deepak','Sumanth','Fanindra','Lakshman,'Dinosaur','Falcon']
b=[]
for str in a:
    firstchar = str[0]
    if firstchar not  in b:
        b.append(firstchar)
c=[]
for ch in b:      #got  errror check once 
    d=[]
    for str in a:
        if str.startswith(ch):
            d.append(str)
    c.append(d)
print(c)



a=eval(input("Enter 1st list:")) #[10,20,30,40]
b=eval(input("Enter 2nd list:")) #[20,30,40,50]
a.sort()
b.sort()    
c=[]
i=j=0
while i<len(a) and len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
c.extend(a[i:])
c.extend(b[j:])
print(c)

#n-th largest elements of list
try:
    list=eval(input("Enter list:"))
    n=eval(input("enter value of n:"))
    for i in range(n):
        large=max(list)
        list.remove(large)
    print(f"(n)th largest element:{large}")
except:
    print("invalid input")


#program to sort a list without using sorted()
list=eval(input("Enter list:"))
new=[]
while list:
    small=min(list)
    new.append(small)
    list.remove(small)

print(new)
