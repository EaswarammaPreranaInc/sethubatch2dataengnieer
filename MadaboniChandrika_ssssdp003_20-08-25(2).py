#1st prgm
a=[x**3 for x in range(2,11,2)]
print(a)

#2nd prgm
a=eval(input("Enter list of lower case strings: "))
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
b=a.split()
c=[]
for x in b:
    c.append([x.upper(),len(x)])
print(c)

#5th prgm
a=input("Enter any sentence: ")
b=a.split()
c=[[x.upper(),len(x)] for x in b]
print(c)

#6th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
d=min(len(a),len(b))
for x in range(d):
    c.append(a[x]+b[x])
print(c)

#7th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
d=min(len(a),len(b))
c=[a[x]+b[x] for x in range(d)]
print(c)

#8th prgm
a=eval(input("How many lists ? : "))
b=eval(input("How many elements in each list ? : "))
c=[]
for x in range(a):
    c.append([0]*b)
print(c)

#9th prgm
a=eval(input("How many lists ? : "))
b=eval(input("How many elements in each list ? : "))
c=[[0]*b for x in range(a)]
print(c)

#10th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    if x not in b:
        c.append(x)
print(c)

#11th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x for x in a if x not in b]
print(c)

#12th prgm
a=[x for x in range(1,21) if x%2==0]
print(a)

#13th prgm
a=[x for x in range(2,21,2)]
print(a)

#14th prgm
a=[x**2 for x in range(1,21) if (x**2)%2==0]
print(a)

#15th prgm
a=[x**2 for x in range(2,21,2) ]
print(a)

#16th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print(c)

#17th prgm
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x+y for x in a for y in b]
print(c)

#18th prgm
a=eval(input("Enter 1st String: "))
b=eval(input("Enter 2nd String: "))
c=[x+y for x in a for y in b]
print(c)

#19th prgm
a=eval(input("Enter nested list: "))
b=[]
for x in a:
    b.extend(x)
print(b)

#20th prgm
a=eval(input("Enter nested list: "))
b=[y for x in a for y in x]
print(b)

#21st prgm
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y in x]
print(b)#[[10 , 20],[10 , 20],[30 , 40 , 50],[30 , 40 , 50],[30 , 40 , 50],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90]]

#22nd prgm
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

#23rd program
a=eval(input('Enter list of strings: ')) # Reads a list of strings
b = [] # Empty list
for str in a:# str is each string of list 'a'
    firstchar=str[0] # First char of each string in list
    if firstchar not in b:
        b. append(firstchar) # Appends first char to list 'b' if it is not in list 'b'
c = [] # Empty list
for ch in b: #ch is each char of list 'b'
    d = [] # Empty list
    for str in a: # for str is each string of list 'a'
        if str.startswith(ch):
            d.append(str) # Appends the string to list 'd' if it starts with the char ch
    c.append (d) # Appends list 'd' to  list 'c'
print (c)

#24th program
a=eval(input("Enter lst list: ")) 
b=eval(input("Enter 2nd list: ")) 
a.sort() 
b.sort() 
c=[]
i=j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]: 
        c.append(a[i])
        i+=1    
    else:
        c.append(b[j])
        j+=1
c.extend(a[i:]) 
c.extend(b[j:]) 

#25th program
try:
    list=eval(input("Enter list: "))
    n=eval(input("Enter value of n: "))
    s=set(list)
    for i in range(n):
        large=max(s)
        s.remove(large)
    print(f"{n}th largest element is: {large}")
except ValueError:
    print("Invalid Input")

#26th program
list=eval(input("Enter list: "))
new=[]
while list:
    small=min(list)
    new.append(small)   
    list.remove(small)
print(new)