# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

numbers = eval(input("Enter a list of numbers: "))
cubes = [num ** 3 for num in numbers if num % 2 == 0]
print("Cubes of given numbers are:", cubes)


'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

strings = eval(input("Enter list of lower case strings: "))
result = []
for s in strings:
    result.append(s[0].upper())
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
Output :  ['H' , 'P' , 'C' , 'V']
'''

strings = eval(input("Enter list of lower case strings: "))
result = [s[0].upper() for s in strings]
print(result)


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension
Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

sentence = input("Enter a sentence: ")
words = sentence.split()
result = []
for x in words:
    result.append([x.upper(), len(x)])
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  hyd  is  green  city
Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

sentence = input("Enter a sentence: ")
result = [[x.upper(), len(x)] for x in sentence.split()]
print(result)


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
result = []
min_len = min(len(list1), len(list2))  
for i in range(min_len):
    result.append(list1[i] + list2[i])
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print(result)


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

rows = int(input("How many lists? : "))
cols = int(input("How many elements in each list? : "))
result = []
for i in range(rows):
    result.append([0] * cols)
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Inputs :  3  and  4
Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

rows = int(input("How many lists? : "))
cols = int(input("How many elements in each list? : "))
result = [[0] * cols for _ in range(rows)]
print(result)


'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
result = []
for item in list1:
    if item not in list2:
        result.append(item)
print("Elements of 1st list which are not in 2nd list :", result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
result = [item for item in list1 if item not in list2]
print("Elements of 1st list which are not in 2nd list :", result)


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

result = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers between 1 and 20 :", result)


'''
Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between 1 and 20]
'''

result = [x for x in range(2, 21, 2)]
print("Even numbers between 1 and 20 :", result)


'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... , 400]
'''

result = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]
print("Squares of 1 to 20 which are divisible by 2 :", result)


#  Repeat  previous  program  with  comprehension  and  without  using  if

result = [x**2 for x in range(2, 21, 2)]
print("Squares of 1 to 20 which are divisible by 2 :", result)


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Hint : Nested for loops
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
result = []
for i in list1:
    for j in list2:
        result.append(i + j)
print(result)


'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
result = [i + j for i in list1 for j in list2]
print(result)


'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
Hint: Same  as  previous program
'''

str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
result = [ch1 + ch2 for ch1 in str1 for ch2 in str2]
print(result)


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

nested_list = eval(input("Enter nested list : "))
result = []
for sublist in nested_list:   
    for item in sublist:     
        result.append(item)
print(result)


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

nested_list = eval(input("Enter nested list : "))
result = [item for sublist in nested_list for item in sublist]
print(result)


# Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y in x]
print(b)

'''
Output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
'''


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

'''
Output:
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
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
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''

a = eval(input("Enter list of strings: "))
groups = {}
for name in a:
    first = name[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(name)
result = list(groups.values())
print(result)


'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]
Hint1 :  Unsorted  lists  can  not  be  merged
Hint2 :  Use  single while loop
'''

a = eval(input("Enter 1st sorted list: "))
b = eval(input("Enter 2nd sorted list: "))
i, j = 0, 0
c = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c.extend(a[i:])
c.extend(b[j:])
print("Merged sorted list:", c)


'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''

a = eval(input("Enter list: "))
n = int(input("Enter which largest to be shown: "))
a.sort(reverse=True)
print(f"{n}th largest element : {a[n-1]}")


'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''

a = eval(input("Enter list: "))
for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)