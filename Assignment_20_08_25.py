'''# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
print([x**3 for x in range(2,11,2)])#[8, 64, 216, 512, 1000]

(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

a=eval(input("Enter the list elemnts: "))
t=[]
for x in a:
    t.append(x[0].upper())
print(t,end=' ')    
output:
Enter the list elemnts:  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V'] 

#(Home  work)
#Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  with  comprehension
a=eval(input("Enter the list elements:"))
print(([(x[0].upper()) for x in a]))
output:
Enter the list elements:['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']

#(homework)
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

a=(input("Enter the sentence: "))
t=a.split(' ')
x=[]
for i in t:
    x.append([i.upper(),len(i)])
print(x)

output:
Enter the sentence: hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]

#Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
#(word  should  be  in  capital  letters)  with  comprehension


a=input("Enter the sentence: ")
t=a.split(' ')
print([(i.upper(),len(i)) for i in t])
#output:
Enter the sentence: hyd is green city
[('HYD', 3), ('IS', 2), ('GREEN', 5), ('CITY', 4)]


#Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

list1 = eval(input("Enter the 1st list: "))
list2 = eval(input("Enter the 2nd list: "))
result = []   # empty list to store sums
length = min(len(list1), len(list2))   # smallest length
i = 0
while i < length:
    result.append(list1[i] + list2[i])
    i += 1

print(result)
output:
Enter the 1st list: [10,20,30,40,50,60,70]
Enter the 2nd list: [1,2,3,4]
[11, 22, 33, 44]
    
#Write  a  program  to  add  two  lists  of  unequal  length  with comprehension
list1 = eval(input("Enter the 1st list: "))
list2 = eval(input("Enter the 2nd list: "))
result=[list1[i]+list2[i] for i in range(min(len(list1), len(list2)))]
print(result)
output:
Enter the 1st list: [10,20,30,40,50,60,70,80]
Enter the 2nd list: [1,2,3,4,5]
[11, 22, 33, 44, 55]'''

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

a=int(input("Enter the row value: "))
b=int(input("Enter the colm value: "))
result = []
for i in range(a):
    result.append([0] * b)  

print(result)

output:
Enter the row value: 3
Enter the colm value: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
#Write   a  program  to  initialize  a  nested  list  with  zeroes  with  comprehension

a=int(input("Enter the row value: "))
b=int(input("Enter the colm value: "))
result = [[0]*b for i in range(a)]
print(result)
output:
Enter the row value: 3
Enter the colm value: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

f=eval(input("enter list1 elements: "))
s=eval(input("enter list2 elements: "))
r=[]
for i in f:
    if i not in s:
        r.append(i)
print(r)
output:
enter list1 elements: [10,20,30,15,16,17,18,40]
enter list2 elements: [10,20,15,40]
[30, 16, 17, 18]
#Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   with  comprehension

f=eval(input("enter list1 elements: "))
s=eval(input("enter list2 elements: "))
r=[i for i in f if i not in s]
print(r)
ouput:
enter list1 elements: [10,20,30,15,16,17,18,40]
enter list2 elements: [10,20,15,40]
[30, 16, 17, 18]
    
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension   
print([i for i in range(1,21) if i%2==0])
output:
[2, 4, 6, 8, 10, 12, 14, 16, 18,20]

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension without using if 
print([i for i in range(2,21,2) ])
#output:
#[2, 4, 6, 8, 10, 12, 14, 16, 18,20]

#Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
print([i**2 for i in range(1,21) if i%2==0])
output:
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


#Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension without using if
print([i**2 for i in range(2,21,2) ])
#output:
#[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
 

Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
 
f=eval(input("Enter the list1 : "))    
s=eval(input("Enter the list2 : "))      
r=[]
for i in f:
    for j in s:
        r.append(i+j)
print(r)        
output:
Enter the list1 : [10,20,15,25]
Enter the list2 : [40,15,10,30,60]
[50, 25, 20, 40, 70, 60, 35, 30, 50, 80, 55, 30, 25, 45, 75, 65, 40, 35, 55, 85]
    
#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with  comprehension
f=eval(input("Enter the list1 : "))    
s=eval(input("Enter the list2 : "))
print([i+j for i in f for j in s])
output:
Enter the list1 : [10,20,15,25]
Enter the list2 :  [40,15,10,30,60]
[50, 25, 20, 40, 70, 60, 35, 30, 50, 80, 55, 30, 25, 45, 75, 65, 40, 35, 55, 85]
    


#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehensio

s1=input("Enter the string1: ")   
s2=input("Enter the string2 : ")
s11=s1.split()
s22=s2.split()
print([i+j for i in s1 for j in s2])
output:
Enter the string1: HYD
Enter the string2 : PUNE
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']

Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

list1=eval(input("Enter the nested list : "))
l=list(list1)
r=[]
for i in l:
    for j in i:
       (r.append(j))
print(r)

output:
Enter the nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]

#Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
list1=eval(input("Enter the nested list : "))
l=list(list1)
print([j for i in l for j in i])
output:
Enter the nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
    
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

names = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

c = []

for name in names:
    placed = False
    for sub in c:
        if sub[0][0] == name[0]:   # check first letter
            sub.append(name)
            placed = True
            break
    if not placed:
        c.append([name])   # create new sublist

print(c)#[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]'''

'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
a=eval(input("Enter the list1 elements"))
b=eval(input("Enter the list1 elements"))
c = []
i = j = 0   # pointers for a and b

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Append remaining elements (only one of these will run)
while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)
output:
Enter the list1 elements[10  ,  20  , 30   ,  40   ,  50]
Enter the list1 elements[5  ,  12  , 20   ,  37]

[5, 10, 12, 20, 20, 30, 37, 40, 50]

#Write  a  program  to  determine  n-th  largest  element   of   a   list
a=eval(input("Enter the list1 elements"))
n=int(input("Enter the n value"))
a_sorted = sorted(a, reverse=True)  # sort in descending order
result = a_sorted[n-1]
print(result)
output:
Enter the list1 elements[10,20,30,25,40,35,12,5]
Enter the n value4
25'''

#Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

a = [10, 20, 30, 25, 40, 35, 12, 5]

n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
output:
[5,10,12,20,25,30,35,40]    








    
