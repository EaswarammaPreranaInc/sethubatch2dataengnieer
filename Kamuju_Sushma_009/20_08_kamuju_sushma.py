#Home Work-1
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a=[pow(x,3) for x in range(2,11,2)]
print(a)

#Home Work-2
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  with  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
l=eval(input("Enter the list: "))
res=[x[0].upper() for x in l ]
print(res)

#Home Work-3
'''
(Home  work)
Repeat   previous  program  without  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
l=eval(input("Enter the list: "))
res=[]
for i in range(len(l)):
    res.append(l[i][0].upper())
print(res)

#Home Work-4
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   "hyd  is  green  city"
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
s=input("Enter the string: ")
l=s.split()
# print(l)
res=[]
for x in l:
    res.append([x.upper(),len(x)])
print(res)

#Home Work-5
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
s=input("Enter the sentence: ")
l=s.split()
res=[[x.upper(),len(x)] for x in l]
print(res)

#Home Work-6
'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[]
n=min(len(l1),len(l2))
for i in range(n):
    res.append(l1[i]+l2[i])
print(res)

#Home Work-7
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[l1[i]+l2[i] for i in range(min(len(l1),len(l2)))]
print(res)

#HOme Work-8
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
n=int(input("How  many  lists  ?  :"))
m=int(input("How  many  elements  in  each  list ?  :"))
res=[]
for i in range(n):
    res.append([0]*m)
print(res)

#HOme work-9
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
n=int(input("How  many  lists  ?  :"))
m=int(input("How  many  elements  in  each  list ?  :"))
res=[[0]*m for i in range(n)]
print(res)

#HOme Work-10
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[]
for x in l1:
    if x not in l2:
        res.append(x)
print(res)

#Home Work-11
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[x for x in l1 if x not in l2 ]
print(res)

#Home Work-12
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
res=[x for x in range(1,20) if x%2==0]
print(res)

#Home Work-13
'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
res=[x for x in range(2,20,2)]
print(res)

#Home Work-14
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
res=[x**2 for x in range(2,21) if x%2==0]
print(res)

#Home Work-15
#  Repeat  previous  program  with  comprehension  and  without  using  if
res=[x**2 for x in range(2,21,2)]
print(res)

#Home Work-16
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        res.append(l1[i]+l2[j])
print(res)

#Home Work-17
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
l1=eval(input("Enter 1st list: "))
l2=eval(input("Enter 2nd list: "))
res=[l1[i]+l2[j] for i in range(len(l1)) for j in range(len(l2))]
print(res)

#Home Work-18
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
s1=input("Enter the 1st string: ")
s2=input("Enter the 2nd string: ")
res=[]
for i in range(len(s1)):
    for j in range(len(s2)):
        res.append(s1[i]+s2[j])
print(res)

#Home Work 19
''' 
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
l=eval(input("Enter the nested list: "))
res=[]
for x in l:
    res.extend(x)
print(res)

#Home Work-20
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
l=eval(input("Enter the nested list: "))
res=[y for x in l for y in x]
print(res)

#HOme Work-21
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) #[[10 , 20], [10 , 20],[30 , 40 , 50], [30 , 40 , 50], [30 , 40 , 50],[60 , 70 , 80 , 90], [60 , 70 , 80 , 90], [60 , 70 , 80 , 90], [60 , 70 , 80 , 90] ]

#Home Work-22
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) #[[],[0],[0,1],[0,1,2],[0,1,2,3]]

#Home Work-23
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
'''
l1=eval(input("Enter the list: "))
chars=[]
res=[]
for x in l1:
    if x[0] not in chars:
        chars.append(x[0])
for c in chars:
    temp=[]
    for x in l1:
        if x.startswith(c):
            temp.append(x)
    res.append(temp)
print(res)
    
#Home Work-24
'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
l1=eval(input("Enter the 1st list: "))
l2=eval(input("Enter the 2nd list: "))
n1=len(l1)
n2=len(l2)
i=0 
j=0 
res=[]
while i<n1 and j<n2 :
    if l1[i]<=l2[j]:
        res.append(l1[i])
        i=i+1
    else:
        res.append(l2[j])
        j=j+1
res.extend(l1[i:])
res.extend(l2[j:])
print(res)

#Home Work-25
'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
l1=eval(input("Enter the list: "))
n=int(input("Enter which largest which to be shown: "))
while n-1>0:
    l1.remove(max(l1))
    n=n-1
print(max(l1))

#Home Work-26
'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
l1=eval(input("Enter the list: "))
l2=[]
while l1 :
    t=min(l1)
    l2.append(t)
    l1.remove(t)
print(l2)





