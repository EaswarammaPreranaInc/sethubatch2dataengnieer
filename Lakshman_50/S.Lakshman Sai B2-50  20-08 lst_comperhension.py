# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
lst=eval(input("Enter list of numbers : "))
b=[x**3 for x in lst]
print(b) 


#**************************************************************************

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

 Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''
lst=eval(input("Enter list of lower case strings : "))
b = []
for x in lst:
   b.append(x[0].upper())
print(b)

#**************************************************************************

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
lst=eval(input("Enter list of lower case strings : "))
b=[x[0].upper() for x in lst]
print(b)



#**************************************************************************

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

 Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]

'''

a=(input("enter the str: "))
c=a.split()
b=[]
for i in c:
   b.append([i.upper(),len(i)])
print(b)
   
#**************************************************************************
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a=(input("enter the str: "))
b=[[i.upper(),len(i)] for i in a.split()]
print(b)

#**************************************************************************
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
 Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]

a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for i in range(min(len(a),len(b))):
   c.append(a[i]+b[i])
print(c)

#**************************************************************************

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[(a[i]+b[i]) for i in range(min(len(a),len(b)))]
print(c)


#**************************************************************************

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *

 How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
 '''
a=eval(input("How many lists: "))
b=eval(input("how many elements in each list: "))
c=[]
for _ in range(a):
   c.append([0]*b)
print(c)
 

#**************************************************************************

'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
a=eval(input("How many lists: "))
b=eval(input("how many elements in each list: "))
c=[([0]*b) for _ in range(a)]
print(c)



#**************************************************************************

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]

a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
for i in a:
  for j in b:
    if i==j:
      a.remove(i)
print(a)


#**************************************************************************
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[a.remove(i) for i in a for j in b if i==j ]
print(a)

#**************************************************************************

'''
 #  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
 Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
 
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a=[i for i in range(2,21,2)]
print("even numbers b/w 1 and 20: ",a)


#**************************************************************************

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
#Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
 #  Repeat  previous  program  with  comprehension  and  without  using  if
a=[i**2 for i in range(2,21,2)]
print("squares of even numbers b/w 1 and 20: ",a)



#**************************************************************************

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]

a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
for x in a:
   for y in b:
      d=x+y
      c.append(d)
print(c)   

#**************************************************************************

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[x+y for x in a for y in b]
print(c)

#**************************************************************************

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a=(input("Enter 1st string: "))
b=(input("Enter 2nd string: "))
c=[x+y for x in a for y in b]
print(c)  

#**************************************************************************

'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]

a=eval(input("Enter 1st list: "))
b=[]
for x in a:
   b.extend(x)
print(b)


#**************************************************************************

'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
''' # Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ y  for  x  in  a  for  y  in  x]
print(b)


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)


#**************************************************************************
'''
Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' ,  , 'Z' , 'K' ]

2) c = []

3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''
a = eval(input("Enter the list: "))
b = []
d = []
for i in a:
    if i[0] not in b:
        b.append(i[0] )
print(b)
for y in b:
    c = []
    for x in a:
        if x[0] == y:
            c.append(x)
            a.remove(x)
    d.append(c)
print(d)

#**************************************************************************
'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
   List  'b'   --->  [5  ,  12  , 20   ,  37]
   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be merged
Hint2 :  Use single while loop
'''
a = eval(input("Enter 1st sorted list: "))
b = eval(input("Enter 2nd sorted list: "))
a.extend(b)
print(sorted(a))

# a.sort()
# b.sort()
# c = []
# i = j = 0
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#       c.append(a[i])
#       i += 1
#     elif a[i] > b[j]:
#       c.append(b[j])
#       j += 1
#     else:
#       c.append(a[i])
#       c.append(b[j])
#       i += 1
#       j += 1
# c.extend(a[i:])
# c.extend(b[j:])
# print(c)
         



#**************************************************************************

'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
 
Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
'''

a=eval(input("enter the list: "))
a.sort()
c=int(input("enter which largest to be shown: "))
print(f'{c}th largest element: {a[-c]}')

#**************************************************************************
'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
 Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]

a=eval(input("enter The list: "))
for i in range(len(a)):
   for j in range(i):
      if a[i]<a[j]:
         a[i],a[j]=a[j],a[i]
print(a)

#**************************************************************************
a=eval(input("enter The list: "))
for i in range(len(a)-1):
   for j in range(i+1):
      if a[j]>a[i+1]:
         a[j],a[i+1]=a[i+1],a[j]
print(a)

