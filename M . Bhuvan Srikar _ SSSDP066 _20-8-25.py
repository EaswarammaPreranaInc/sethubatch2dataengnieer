# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [x**3 for x in range(2 , 11 , 2)]
print(a)

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''
a = eval(input('Enter a list of strings : '))
b = []
for i in range(len(a)):
	b . append(a[i][0] . upper())
print(b)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a = eval(input('Enter a list of strings : '))
b = [a[i][0].upper() for i in range(len(a))]
print(b)

'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city

Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]

'''
a = input('Enter a string : ')
b = a . split(' ')
c = []
for i in range(len(b)):
	c . append([b[i] . upper() , len(b[i])])
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a = input('Enter a string : ')
b = a . split(' ')
c = [([b[i] . upper() , len(b[i])]) for i in range(len(b))]
print(c)


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = min(len(a) , len(b))
d = []
for i in range(c):
	d . append(a[i] + b[i])
print(f'Result : {d}')


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = min(len(a) , len(b))
d = [a[i] + b[i] for i in range(c)]
print(d)


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *

How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''
a  = int(input('How many lists : '))
b = int(input('How many elements in the list : '))
c = []
for i in range(a):
	c . append([0] * b)
print(c)




'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
a  = int(input('How many lists : '))
b = int(input('How many elements in the list : '))
c = [([0] * b) for i in range(a)]
print(c)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = []
for i in range(len(a)):
	if a[i] not in b:
		c . append(a[i])
print(f'Elements  of  1st  list  which  are  not  in  2nd  list : {c}')

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = [a[i] for i in range(len(a)) if a[i] not in b]
print(f'Elements  of  1st  list  which  are  not  in  2nd  list : {c}')


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a = [x for x in range(21) if x % 2 == 0]
print(a)


'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a = [x for x in range(0 , 21 , 2)]
print(a)

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
a = [x**2 for x in range(21) if x % 2 == 0]
print(a)

#  Repeat  previous  program  with  comprehension  and  without  using  if
a = [x**2 for x in range(0 , 21 , 2)]
print(a)


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
		[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = []
for i in range(len(a)):
	for j in range(len(b)):
		c . append(a[i] + b[j])
print(f'Result : {c}')


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
c = [a[i] + b[j] for i in range(len(a)) for j in range(len(b))]
print(f'Result : {c}')



'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a = input('Enter 1st List : ')
b = input('Enter 2nd List : ')
c = []
for i in range(len(a)):
	for j in range(len(b)):
		c . append(a[i] + b[j])
print(f'Result : {c}')


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = input('Enter 1st List : ')
b = input('Enter 2nd List : ')
c = [a[i] + b[j] for i in range(len(a)) for j in range(len(b))]
print(f'Result : {c}')


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = eval(input('Enter nested list : '))
b = []
for i in range(len(a)):
	for j in range(len(a[i])):
		b . append(a[i][j])
print(f'Result : {b}')


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[0] , [0 , 1] , [0 , 1 , 2] , [0 , 1 , 2 , 3]]


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
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''
a = eval(input('Enter a List : '))
b = []
for i in range(len(a)):
	if a[i][0] not in b:
		b . append(a[i][0])
c = []
for x in b:
	d = []
	for j in range(len(a)):
		if a[j] . startswith(x):
			d . append(a[j])
	c . append(d)
print(c)


'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
a = eval(input('Enter 1st List : '))
b = eval(input('Enter 2nd List : '))
a . sort()
b . sort()
i = 0
j = 0
c = []
while i < len(a) and j < len(b):
	if a[i] < b[j]:
		c . append(a[i])
		i += 1
	else:
		c . append(b[j]])
		j += 1
c . extend(a[i:])
c . extend(b[j:])
print(f'Sorted List : {c}')


'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
a = eval(input('Enter a List : '))
b = int(input('Enter a number : '))
i = 0
while i < b:
	c = max(a)
	a . remove(c)
	i += 1
print(f'Output : {c}')


'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
a = eval(input('Enter a List : ')) 
for i in range(len(a)):
	for j in range(i + 1 , len(a)):
		if a[i] > a[j]:
			a[i] , a[j] = a[j] , a[i]
print(f'Sorted list : {a}')
