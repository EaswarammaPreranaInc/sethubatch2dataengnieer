# 1.
#Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
num= [2 , 4 , 6 , 8 , 10 ]
print([i*i*i for i in num])


#2
'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
newlist=[]
a=eval(input("enter the list string values:")
for i in a:
    newlist.append(i[0])
print(newlist)

#3
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a=eval(input("enter the list string values:"))
print([i[0].upper() for i a])

#4
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

a=eval(input("enter the list string :"))
for i in a.split():
    print(i)
	
a=input("enter the list string :")
c=[]
for i in a.split():
   b=i.upper(),len(i)
   c.append(list(b))
print(c)

#5
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a=input("enter the list string :")
print([[i.upper(),len(i)] for i in a.split()])

#6 '''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
a=eval(input("enter 1st the list with number:"))
b=eval(input("enter 2nd the list with number:"))
c=[]
for i in range(min(len(a),len(b))):
    c.append(int(a[i])+int(b[i]))
print(c)

#7
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]

a=eval(input("enter 1st the list with number:"))
b=eval(input("enter 2nd the list with number:"))
print([ (int(a[i])+int(b[i])) for i in range(min(len(a),len(b)))])

#8
'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
a = int(input("How many lists ? : "))
b = int(input("How many elements in each list ? : "))

# initialize matrix
m = []
for i in range(a):
    m.append([0] * )b

print(m)

#9
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

a = int(input("How many lists ? : "))
b = int(input("How many elements in each list ? : "))
print([[0 for j in range(b)] for i in range(a)])

#10
'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

a=eval(input("enter 1st the list with number:"))
b=eval(input("enter 2nd the list with number:"))
lst=[]
for i in a:
    if i not in b:
	     lst.append(i)
print(lst)

#11
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a=eval(input("enter 1st the list with number:"))
b=eval(input("enter 2nd the list with number:"))

print([i for i in a:if i not in b])


#12
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
print(f'even no between 1 to 20:',[i for i in range(1,21) if i%2==0])

#13
'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
print(f'Even numbers between 1 to 20:', [i for i in range(2, 21, 2)])

#14
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
print([ i**2 for i in range(1,21) if i%2==0])

#15
#  Repeat  previous  program  with  comprehension  and  without  using  if
print(f'Even numbers between 1 to 20:', [i**2 for i in range(2, 21, 2)])

#16

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))

c = []

for x in a:         
    for y in b:   
        c.append(x + y)

print(c)

#17
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))

print([x + y for x in a for y in b])

#18
'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a=input("enter the string:")
b=input("enter the string:")
lst=[]
for i in a:
    for j in b:
        lst.append(i+j)
print(lst)
#19
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

flat_list = []

for i in a:        
    for j in i:  
        flat_list.append(j)

print(flat_list)

#20
'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

a=[[10,20,30],[40,50,60]]
print([j for i in a for j in i])


#21
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
  #[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#22
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

#23
[12:41 PM, 8/20/2025] Srinivas Sir @Task: '''
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
Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]


# Input
a = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

c = []     
b = []    

for name in a:
    first_char = name[0] 
    
    if first_char not in b:   
        d = []             
        for x in a:
            if x[0] == first_char:   
                d.append(x)
        c.append(d)    
        b.append(first_char) 

print(c)


#24
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
a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

c = []

i = j = 0   


while i < len(a) and j < len(b):
    if a[i] <= b[j]:
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

print(c)

#25
'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
a = [10, 20, 30, 25, 40, 35, 12, 5]
n = int(input("Enter n (which largest element): "))

a.sort(reverse=True)

print(f"{n}rd largest element is:", a[n-1])

#26
'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
a = [10, 20, 30, 25, 40, 35, 12, 5]

n = len(a)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)
