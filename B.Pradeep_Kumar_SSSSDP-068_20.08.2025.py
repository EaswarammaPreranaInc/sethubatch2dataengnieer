# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

cube = [ x**3 for x in range(0,11,2)]
print(cube)


'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a=eval(input("Enter the list of lower case string :"))
b=[]
for i in a:
    b.append(i[0].upper())
print(b)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a=eval(input("Enter the list of lower case string :"))
capital = [ i[0].upper() for i in a]
print(capital)

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
a=input("Enter the input:")
b=a.split(" ")
c=[]
for i in b:
    c.append([i,len(i)])
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

a=input("Enter the input:")
b=a.split(" ")
c = [([i,len(i)]) for i in b]
print(c)


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
a=eval(input("Enter the 1st list:"))
b=eval(input("Enter the 2nd list:"))
c=len(a)
d=len(b)
e=min(c,d)
list=[]
for i in range(e):
        list.append(a[i]+b[i])
print(list)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a=eval(input("Enter the 1st list:"))
b=eval(input("Enter the 2nd list:"))
list=[(a[i]+b[i]) for i in range(min(len(a),len(b)))]
print(list)

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
a=int(input("How many lists? :"))
b=int(input("How manay elemnts in each list ? :"))
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
a=int(input("How many lists? :"))
b=int(input("How manay elemnts in each list ? :"))
c=[[0]*b for i in range(a)]
print(c)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
a=eval(input("input 1 :"))
b=eval(input("input 2 :"))
c=[]
for i in a:
    if i not in b:
        c.append(i)
print("Elements  of  1st  list  which  are  not  in  2nd  list  :",c)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a=eval(input("input 1 :"))
b=eval(input("input 2 :"))
c=[(i) for i in a if i not in b]
print("Elements  of  1st  list  which  are  not  in  2nd  list  :",c)


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a=[i for i in range(1,21) if i%2==0]
print(a)


'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a=[i for i in range(2,21,2)]
print(a)


'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
a=[ i*i for i in range(1,21) if i*i%2==0]
print(a)

#  Repeat  previous  program  with  comprehension  and  without  using  if
a=[ i*i for i in range(2,21,2)]
print(a)


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
a=eval(input("Enter the 1st list:"))
b=eval(input("Enter the 2nd list:"))
list=[]
for i in a:
    for j in b:
        list.append(i+j)
print(list)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a=eval(input("Enter the 1st list:"))
b=eval(input("Enter the 2nd list:"))
list=[(i+j) for i in a for j in b]
print(list)


'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a=input("Enter the 1st input:")
b=input("Enter the 2nd input:")
list=[(i+j) for i in a for j in b]
print(list)


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a=eval(input("Enter the 1st list:"))
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a=eval(input("Enter the 1st list:"))
b=[j for i in a for j in i]
print(b)


# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


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

a = eval(input("Enter input"))
b = []
for word in a:
    if word[0] not in b:
        b.append(word[0])
c = []
for letter in b:
    d = []
    for word in a:
        if word[0] == letter:
            d.append(word)
    c.append(d)
print(c)
