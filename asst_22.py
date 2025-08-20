# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

nums = [2, 4, 6, 8, 10]
cubes = [x ** 3 for x in nums]

print("Original list :", nums)
print("Cubes list    :", cubes)
-------------------------------------------
# Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

n = int(input("How many strings? : "))
words = []

for i in range(n):
    s = input("Enter lower case string : ")
    words.append(s)

result = []
for w in words:
    if len(w) > 0:
        result.append(w[0].upper())

print("Original list :", words)
print("First letters :", result)
----------------------------------------------
# Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
words = ['hyd', 'pune', 'chennai', 'vijayawada']

result = [w[0].upper() for w in words]

print("Input  :", words)
print("Output :", result)
-------------------------------------
# Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

sentence = input("Enter a sentence : ")

words = sentence.split()
result = []

for w in words:
    result.append([w.upper(), len(w)])

print("Output :", result)
----------------------------------
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
sentence = input("Enter a sentence : ")

words = sentence.split()
result = [[w.upper(), len(w)] for w in words]

print("Output :", result)
-----------------------------------------
# Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = []
length = min(len(list1), len(list2))

for i in range(length):
    result.append(list1[i] + list2[i])

print("Result :", result)
--------------------------------------------
# (Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print("Output :", result)
-------------------------------------
# Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

rows = 3
cols = 4

nested_list = []
for i in range(rows):
    nested_list.append([0] * cols)

print("Output :", nested_list)
---------------------------------------------
# Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []
for x in list1:
    if x not in list2:
        result.append(x)

print("Output :", result)
-------------------------------------------
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [x for x in list1 if x not in list2]

print("Output :", result)
-----------------------------------------
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

E_Numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers :", E_Numbers )
----------------------------------------
# Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
evens = [x for x in range(2, 21, 2)]

print("Even numbers :", evens)
------------------------------------------
# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
squares = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]

print("Output :", squares)
-----------------------------------------------
#  Repeat  previous  program  with  comprehension  and  without  using  if

squares = [x**2 for x in range(2, 21, 2)]

print("Output :", squares)
------------------------------------------
'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print("Output :", result)
------------------------------------------------
# Repeat   previous  program  with  comprehension

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [x + y for x in list1 for y in list2]

print("Output :", result)
-----------------------------------------
# Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")

result = [a + b for a in str1 for b in str2]

print("Output :", result)
------------------------------------------
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

nested = eval(input("Enter a nested list : "))

result = []
for sub in nested:
    for x in sub:
        result.append(x)

print("Output :", result)
-----------------------------------------
# Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

nested = eval(input("Enter a nested list : "))

result = [x for sub in nested for x in sub]

print("Output :", result)
----------------------------------------------
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50],
               [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
------------------------------------------------
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
--------------------------------------
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

-----------------------------------------------------------
'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''

nums = eval(input("Enter the list : "))
n = int(input("Enter n (which largest element?) : "))

nums.sort(reverse=True)   
result = nums[n-1]        
print("Output :", result)
------------------------------------------
'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
 a= eval(input("Enter list : "))
n = len(a)

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

print("Sorted list :", a)
----------------------------------------
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






























