# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

a=[pow(x,3) for x in range(2,11,2)]
print(a)

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

a=eval(input('enter a list: '))
b=[]
for x in a:
    c=x[:1].upper()
    b.append(c)
print(b)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''

a=eval(input('enter a list: '))
b=[x[:1].upper() for x in a]
print(b)

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

a=input('enter a string: ').upper().split()
b=[]
for x in a:
    b.append([x,len(x)])
print(b)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

a=input('enter a string: ').upper().split()
b=[[x,len(x)] for x in a]
print(b)


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

a=eval(input('enter a list: '))
b=eval(input('enter another list: '))

c=[]
for i in range(min(len(a),len(b))):
    c.append(a[i]+b[i])
print(c)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a=eval(input('enter a list: '))
b=eval(input('enter another list: '))
c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
print(c)


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

a=int(input('How many lists ? '))
b=int(input('How  many  elements  in  each  list ? '))
c=[]
for i in range(a):
    c.append([0]*b)
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

a=int(input('How many lists ? '))
b=int(input('How  many  elements  in  each  list ? '))
c=[[0]*b for i in range(a) ]
print(c)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

a=eval(input('enter a list: '))
b=eval(input('enter another list: '))
c=[]
for x in a:
    if x not in b:
        c.append(x)
print('Elements  of  1st  list  which  are  not  in  2nd  list  : ',c)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

a=eval(input('enter a list: '))
b=eval(input('enter another list: '))
c=[x for x in a if x not in b ]
print('Elements  of  1st  list  which  are  not  in  2nd  list  : ',c)

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

c=[x for x in range(2,21) if x%2==0]
print('Even numbers  between  1  and  20 : ',c)



'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
c=[x for x in range(2,21,2)]
print('Even numbers  between  1  and  20 : ',c)


'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''

c=[x**2 for x in range(1,21) if x%2==0]
print('Squares  of  1  to  20  which  are  divisible  by   2  : ',c)

#  Repeat  previous  program  with  comprehension  and  without  using  if

c=[x**2 for x in range(2,21,2) ]
print('Squares  of  1  to  20  which  are  divisible  by   2  : ',c)


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

a=eval(input('enter a list: '))
b=eval(input('enter another list: '))
c=[]
for x in a:
    for y in b:
        c.append(x+y)
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

a=eval(input('enter a list: '))
b=eval(input('enter another list: '))
c=[x+y for x in a for y in b]
print(c)

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a=input('enter a string: ')
b=input('enter another string: ')
c=[x+y for x in a for y in b]
print(c)


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

a=eval(input('enter a nested list: '))
c=[]
for x in a:
    for y in x:
        c.append(y)
print(c)




'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''


a=eval(input('enter a nested list: '))
c=[y for x in a for y in x]
print(c)


# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y in x]
print(b) #each inner list is repeated as many as as elemnets inside that list [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # I varies from 0 to 4 so for each I element take range of I and such j is printed
'''
I varies from 0 to 4
for I=0 j in range(0)= empty range=[]
for i=1 j in range(1)=0=[0]
for i=2 j in range(2)=0,1=[0,1]
for i=3 j in range(3)=0,1,2=[0,1,2]
for i=4 j in range(4)=0,1,2,3=[0,1,2,3]
so output is [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''
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

a = eval(input('Enter a list of strings: '))
b=[]
for x in a:
    if x[:1] not in b:
        b.append(x[:1])
c=[]
for y in b:
    d=[x for x in a if x.startswith(y) ]
    c.append(d)
print(c)


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
a = eval(input('Enter a sorted list : '))
b=eval(input('enter 2nd sorted list : '))
c=[]
i=j=0
while(i<len(a) and j<len(b) ):
    if(a[i]<b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
c.extend(a[i:])
c.extend(b[j:])
print(c)

'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''

a = eval(input('Enter a list : '))
b=int(input('Enter which largest which to be shown: '))
for x in range(b):
    b=max(a)
    a.remove(b)
print(b)

'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''

a = eval(input('Enter a list : '))
c=[]
for x in range(len(a)-1):
    b=min(a)
    c.append(b)
    a.remove(b)
print(c)


