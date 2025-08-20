# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
############
# Program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension

numbers = [2, 4, 6, 8, 10]
cubes = [n**3 for n in numbers]

print("Cubes:", cubes)

#############
Cubes: [8, 64, 216, 512, 1000]

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']


#################
# Program to extract 1st character of each string in capital letters
# without list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
first_chars = []

for city in cities:
    first_chars.append(city[0].upper())

print(first_chars)

###################
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
###############
# Program to extract 1st character of each string in capital letters
# using list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
first_chars = [city[0].upper() for city in cities]

print(first_chars)

: '''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
: Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
############
# Program to append each word of the sentence and its length to a list
# (word should be in capital letters) without comprehension

sentence = input("Enter any sentence: ")

words = sentence.split()   # split into list of words
result = []

for w in words:
    result.append([w.upper(), len(w)])

print(result)
'''

(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]

'''
###################
# Program to append each word and its length to a list
# (word should be in capital letters) using list comprehension

sentence = input("Enter any sentence: ")

result = [[w.upper(), len(w)] for w in sentence.split()]

print(result)

###########
: '''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
: Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]

####################
# Program to add two lists of unequal length without comprehension

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []
min_len = min(len(list1), len(list2))   # take smaller length

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
#############
# Program to add two lists of unequal length using list comprehension

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)

: '''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
: How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

#######################

# Program to initialize a nested list with zeroes without comprehension

rows = int(input("How many lists ? : "))
cols = int(input("How many elements in each list ? : "))

result = []
for _ in range(rows):
    result.append([0] * cols)   # repetition operator *

print(result)
'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''


##############

# Program to initialize a nested list with zeroes using list comprehension

rows = int(input("How many lists ? : "))
cols = int(input("How many elements in each list ? : "))

result = [[0] * cols for _ in range(rows)]

print(result)


: '''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
: Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]
###########
# Program to extract elements of 1st list not in 2nd list (without comprehension)

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []
for x in list1:
    if x not in list2:
        result.append(x)

print("Elements of 1st list which are not in 2nd list : ", result)




: '''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]

'''
############
# Program to extract elements of 1st list not in 2nd list (with comprehension)

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [x for x in list1 if x not in list2]

print("Elements of 1st list which are not in 2nd list : ", result)


: #  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
: Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
############
# Program to print even numbers between 1 and 20 using comprehension

evens = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers between 1 and 20 :", evens)




: '''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]

'''
############
# Program to print even numbers between 1 and 20 using comprehension (without if)

evens = [x for x in range(2, 21, 2)]

print("Even numbers between 1 and 20 :", evens)



: '''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
: Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
##############

# Program to print squares of 1..20 that are divisible by 2 using comprehension

squares = [x*2 for x in range(1, 21) if (x*2) % 2 == 0]

print("Squares of 1 to 20 which are divisible by 2 :", squares)


: #  Repeat  previous  program  with  comprehension  and  without  using  if
################
# Program to print squares of 1..20 that are divisible by 2 
# using comprehension and without if

squares = [x**2 for x in range(2, 21, 2)]

print("Squares of 1 to 20 which are divisible by 2 :", squares)


: '''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
: Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
###############
# Program to add each element of 1st list with all elements of 2nd list
# without comprehension (using nested loops)

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)



: '''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
###########
# Program to add each element of 1st list with all elements of 2nd list
# using list comprehension

list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [x + y for x in list1 for y in list2]

print(result)



: '''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program

'''
##############

# Program to concatenate each character of 1st string with every character of 2nd string
# using comprehension

s1 = input("Enter 1st string : ")
s2 = input("Enter 2nd string : ")

result = [ch1 + ch2 for ch1 in s1 for ch2 in s2]

print(result)



: '''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
: Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
##############
# Program to convert a nested list to a single list without comprehension

nested = eval(input("Enter nested list : "))
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)


: '''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
##############
# Program to convert a nested list to a single list using comprehension

nested = eval(input("Enter nested list : "))

flat = [item for sublist in nested for item in sublist]

print(flat)



: # Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
#############
[[10, 20], [10, 20],
 [30, 40, 50], [30, 40, 50], [30, 40, 50],
 [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

: #  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
: '''
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
: Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
###########
# Program to group strings into nested list by first character

strings = eval(input("Enter list of strings : "))

result = []   # final nested list
seen = []     # to track processed first letters

for s in strings:
    first = s[0]  # first character
    if first not in seen:   # new group
        # collect all strings starting with this character
        group = [word for word in strings if word[0] == first]
        result.append(group)
        seen.append(first)

print(result)



 : '''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
###########
# Program to merge two sorted lists into another sorted list

a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

c = []   # final merged list

i = j = 0   # pointers for list a and b

# merge until one list is finished
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# add remaining elements (if any)
c.extend(a[i:])
c.extend(b[j:])

print("Merged list :", c)



: '''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
: Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
##########
# Program to determine n-th largest element of a list

lst = eval(input("Enter list: "))
n = int(input("Enter which largest element to be shown: "))

# sort in descending order
sorted_lst = sorted(lst, reverse=True)

nth_largest = sorted_lst[n-1]

print(f"{n}th largest element : {nth_largest}")


: '''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
: Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
############
# Program to sort a list without using sorted() or sort()

lst = eval(input("Enter list: "))

# Bubble Sort
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]   # swap

print(lst)
