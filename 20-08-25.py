#1st program
a=[x**3 for x in range(2,11,2)]
print(a)

#2nd program
a=eval(input("Enter list of lower case strings: "))
b=[]
for x in a:
    b.append(x[0].upper())
print(b)

#3rd program
a=eval(input("Enter list of lower case strings: "))
b=[x[0].upper() for x in a]
print(b)

#4th program
a=input("Enter any sentence: ")
b=a.split()
c=[]
for x in b:
    c.append([x.upper(),len(x)])
print(c)

#5th program
a=input("Enter any sentence: ")
b=a.split()
c=[[x.upper(),len(x)] for x in b]
print(c)

#6th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
d=min(len(a),len(b))
for x in range(d):
    c.append(a[x]+b[x])
print(c)

#7th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
d=min(len(a),len(b))
c=[a[x]+b[x] for x in range(d)]
print(c)

#8th program
a=eval(input("How many lists ? : "))
b=eval(input("How many elements in each list ? : "))
c=[]
for x in range(a):
    c.append([0]*b)
print(c)

#9th program
a=eval(input("How many lists ? : "))
b=eval(input("How many elements in each list ? : "))
c=[[0]*b for x in range(a)]
print(c)

#10th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    if x not in b:
        c.append(x)
print(c)

#11th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x for x in a if x not in b]
print(c)

#12th program
a=[x for x in range(1,21) if x%2==0]
print(a)

#13th program
a=[x for x in range(2,21,2)]
print(a)

#14th program
a=[x**2 for x in range(1,21) if (x**2)%2==0]
print(a)

#15th program
a=[x**2 for x in range(2,21,2) ]
print(a)

#16th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print(c)

#17th program
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x+y for x in a for y in b]
print(c)

#18th program
a=eval(input("Enter 1st String: "))
b=eval(input("Enter 2nd String: "))
c=[x+y for x in a for y in b]
print(c)

#19th program
a=eval(input("Enter nested list: "))
b=[]
for x in a:
    b.extend(x)
print(b)

#20th program
a=eval(input("Enter nested list: "))
b=[y for x in a for y in x]
print(b)

#21st program
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y in x]
print(b)#[[10 , 20],[10 , 20],[30 , 40 , 50],[30 , 40 , 50],[30 , 40 , 50],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90],[60 , 70 , 80 , 90]]

#22nd program
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


#23th program
a = eval(input("Enter first sorted list: "))
b = eval(input("Enter second sorted list: "))
c = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print("Merged sorted list:", c)

#24th program
a = eval(input("Enter the list: "))
n = int(input("Enter n (for n-th largest element): "))

if n > len(a) or n < 1:
    print("Invalid value of n")
else:
    temp = a.copy()
    count = 1
    while count < n:
        temp.remove(max(temp))
        count += 1
    print(f"{n}-th largest element is:", max(temp))