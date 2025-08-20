# program to create a list with cubes of 2,4,6,8,10 with list comprehension
a=[2,4,6,8,10]
b=[x**3 for x in a]
print(b)


# program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
a=eval(input("Enter a list of lower case strings: "))
b=[]
for x in a:
    y=x[0].upper().capitalize()
    b.append(y)
print(b)
'''
o/p:
Enter a list of lower case strings: ['hyd','pune','chennai']
['H', 'P', 'C']'''

# with list comprehension
a=eval(input("Enter a list of lower case strings: "))
b=[x[0].upper().capitalize() for x in a]
print(b)
'''
Enter a list of lower case strings: ['hyd','pune','chennai']
['H', 'P', 'C']
'''


#program  to  append  each  word  of  the  sentence  and  its  length  to  a  list (word  should  be  in  capital  letters)  without  comprehension
a=input("Enter any sentence :")
b=a.split()
d=[]
for x in b:
    y=x.upper()
    d.append([y,len(x)])
print(d)
'''
Enter any sentence :hyd is clean city
[['HYD', 3], ['IS', 2], ['CLEAN', 5], ['CITY', 4]]
'''

# with list comprehension
a=input("Enter any sentence :").upper()
b=a.split()
d=[[x,len(x)] for x in b]
print(d)

'''
output:
Enter any sentence :hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]'''


#program  to  add  two  lists  of  unequal  length  without  comprehension
x=eval(input("Enter 1st list: "))
y=eval(input("Enter 2nd list: "))
result=[]
a=min(len(x),len(y))
for i in range(a):
    result.append(x[i]+y[i])
print(result)

'''
o/p
Enter 1st list:  [10 , 20 , 30 , 40 , 50 , 60 , 70]
Enter 2nd list:   [100 , 200 , 300 , 400]
[110, 220, 330, 440]
'''

# with list comprehension
x=eval(input("Enter 1st list: "))
y=eval(input("Enter 2nd list: "))
result=[x[i]+y[i] for i in range(min(len(x),len(y)))]
print(result)
'''
o/p:
Enter 1st list: [10 , 20 , 30 , 40 , 50 , 60 , 70]
Enter 2nd list: [100 , 200 , 300 , 400]
[110, 220, 330, 440]
'''

# program  to  initialize  a  nested  list  with  zeroes  without  comprehension
a=eval(input("How many list?: "))
b=eval(input("How many elemets in the list? : "))
c=[]
for x in range(a):
    c.append([0]*b)
print(c)
'''
o/p:
How many list?: 3
How many elemets in the list? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''


# with list comprehension
a=eval(input("How many list?: "))
b=eval(input("How many elemets in the list? : "))
c=[[0]*b for x in range(a)]
print(c)
'''
o/p:
How many list?: 3
How many elemets in the list? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''

# program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    if x not in b:
        c.append(x)
print(c)
'''
output:
Enter 1st list: [10 , 20 , 15 , 18 , 25 , 32]
Enter 2nd list:  [30 , 40 , 10 , 25 , 15]
[20, 18, 32]
'''

# with list comprehension
a = eval(input("Enter 1st list: "))
b = eval(input("Enter 2nd list: "))
c = [x for x in a if x not in b]
print(c)

'''
output:
Enter 1st list: [10 , 20 , 15 , 18 , 25 , 32]
Enter 2nd list: [30 , 40 , 10 , 25 , 15]
[20, 18, 32]'''

# program  to  print  even  numbers  between  1  and  20  with  comprehension
x=[x for x in range(1,21) if x%2==0]
print('Even numbers between 1 and 20:',x)

'''
output:
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]'''


# with  comprehension  and  without  using  if
x=[x for x in range(2,21,2)]
print('Even numbers between 1 and 20:',x)
'''
output:
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]'''


#program  to  print the  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
x=[x**2 for x in range(1,21) if x%2==0]
print('squares of 1 and 20 which are divisible by 2:',x)
'''
o/p:
Even numbers between 1 and 20: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''

#with  comprehension  and  without  using  if
x=[x**2 for x in range(2,21,2)]
print('squares of 1 and 20 which are divisible by 2:',x)
'''
squares of 1 and 20 which are divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''


# program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print(c)
'''
Enter 1st list: [10,20,15]
Enter 2nd list: [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''

# with list comprehension
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x+y for x in a for y in b]
print(c)
'''
output:
Enter 1st list: [10,20,15]
Enter 2nd list: [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''


 # program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
a=input("Enter 1st string: ").upper()
b=input("Enter 2nd string: ").upper()
c=[x+y for x in a for y in b]
print(c)
'''
output:
Enter 1st string: hyd
Enter 2nd string: pune
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
'''


# program  to  convert  a  nested  list  to  list  without  comprehension
a=eval(input("enter nested list: "))
b = []
for x in a:        
    for y in x:  
        b.append(y)
print(b)
'''
o/p:
enter nested list: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''

# program to convert a nested list to list with comprehension
a=eval(input("enter nested list: "))
b = [y for x in a for y in x]
print(b)
'''
enter nested list: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''

# Find  outputs 
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]


#  Nested  comprehension 
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)  # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


a = eval(input("Enter list of strings: "))
c = []   
b = []   
for x in a:
    y = x[0]  
    if y not in b:
        b.append(y)
        d = []
        for z in a:        
            if z[0] == y:
                d.append(z) 
        c.append(d)
print(c)

'''
output:
Enter list of strings: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''

# program to merge two sorted list to produce another sorted list
a = eval(input("Enter 1st list: "))
b = eval(input("Enter 2nd list"))
c = []
i=0
j=0
while i<len(a) or j<len(b):
    if i<len(a) and (j==len(b) or a[i]<=b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
print(c)
'''
output:
Enter 1st list: [10,20,30,40,50]
Enter 2nd list [5,12,20,37]
[5, 10, 12, 20, 20, 30, 37, 40, 50]
'''


# program to determine n-th largest element of a list
a = eval(input("Enter list: "))
b = int(input("Enter which largest element to be shown: "))
for i in range(b-1):
    a.remove(max(a)) 
print(max(a)) 

'''
output:
Enter list: [10,20,30,25,40,35,12,5]
Enter which largest which to be shown: 3
3rd largest element is: 30
'''


#Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
a=eval(input("Enter a list: "))
b = len(a)
for x in range(b):
    for y in range(0,b-x-1):
        if a[y] > a[y+1]:   
            a[y],a[y+1] =a[y+1],a[y]
print(a)
'''
output:
Enter a list: [10,20,30,25,40,35,12,5]
[5, 10, 12, 20, 25, 30, 35, 40]
'''
