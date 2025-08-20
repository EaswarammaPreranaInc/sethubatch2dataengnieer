                           NAME:M.SAICHARAN                   HOMEWORK
                           DATE:20-08-2025


1)# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

#program:
a = [x ** 3 for x in range(2,11,2)]
print(a)


2)'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']

Sample output:
Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''
#program:
a =[]
b = eval(input("Enter a of  lower  case  strings : "))
for i in range(len(b)):
    a.append(b[i][0].upper())
print(a)

    

3)'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
#program:
b = eval(input("Enter list of lower case strings : "))
a = [i[0].upper() for i in b]
print(a)




4)'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'
sample output:
Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
'''
#program:
a = input("Enter any sentence : ")
b = a.split()
c = []
for x in b:
    c.append([x.upper(), len(x)])
print(c)


5)'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
#program:
a = input("Enter any sentence : ")
b = a.split()
c = [[x.upper(), len(x)] for x in b]
print(c)




6)'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]

sample output:
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]
'''
#program:
a = eval(input("Enter first list : "))
b = eval(input("Enter second list : "))
c = []
i = 0
while i < len(a) and i < len(b):
    c.append(a[i] + b[i])
    i += 1
print(c)


7)'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
#program:
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
print(c)


8)'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *

sample output:
How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''
#program:
a = int(input("How many lists ? : "))
b = int(input("How many elements in each list ? : "))
c = []
for i in range(a):
    c.append([0] * b)
print(c)


9)'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
#program:
a = int(input("How many lists ? : "))
b = int(input("How many elements in each list ? : "))
c = [[0] * b for i in range(a)]
print(c)


10)'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]

sample output:
Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]
'''
#program:
a = eval(input("Enter first list : "))
b = eval(input("Enter second list : "))
c = []
for x in a:
    if x not in b:
        c.append(x)
print("Elements of 1st list which are not in 2nd list :", c)



11)'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
#program:
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = [x for x in a if x not in b]
print("Elements of 1st list which are not in 2nd list :", c)



12)#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
'''
sample output:
Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
#program:
a = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers between 1 and 20 :", a)



13)'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
#program:
c = [x for x in range(2, 21, 2)]
print("Even numbers between 1 and 20 :", c)


14)'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]

sample output:
Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''
#program:
a = [x*x for x in range(1, 21) if (x*x) % 2 == 0]
print("Squares of 1 to 20 which are divisible by 2 :", a)


15)#  Repeat  previous  program  with  comprehension  and  without  using  if
#program:
a = [x*x for x in range(2, 21, 2)]
print("Squares of 1 to 20 which are divisible by 2 :", a)


16)'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops

sample output:
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''
#program:
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = []
for x in a:
    for y in b:
        c.append(x + y)
print(c)



17)'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
#program:
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = [x + y for x in a for y in b]
print(c)



18)'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
#program:
a = input("Enter 1st string : ")
b = input("Enter 2nd string : ")
c = [x + y for x in a for y in b]
print(c)



19)'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]

sample output:
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
#program:
a = eval(input("Enter nested list : "))
b = []
for x in a:
    for x in x:
        b.append(x)
print(b)



20)'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
#program:
a = eval(input("Enter nested list : "))
b = [x for x in a for x in x]
print(b)



21)# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)	#[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50],[60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]



22)#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)	#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]



23)'''
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

sample output:
Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''
#program:
a = input("Enter a list of strings : ")s
input_list = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
seen_letters = []
grouped_list = []
for name in input_list:
    first_char = name[0]
    if first_char in seen_letters:
        index = seen_letters.index(first_char)
        grouped_list[index].append(name)
    else:
        seen_letters.append(first_char)
        grouped_list.append([name])
print(grouped_list)




24)'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                        0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
     List  'b'   --->  [5  ,  12  , 20   ,  37]
	               0     1       2       3
     List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
#program:
a = eval(input("Enter first list : "))
b = eval(input("Enter second list : "))
i = j = 0
c = []
while i < len(a) or j < len(b):
    if i < len(a) and (j == len(b) or a[i] <= b[j]):
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print("Merged Sorted List :", c)



25)'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30

sample output:
Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
'''
#program:
a = eval(input("Enter list: "))
n = int(input("Enter which largest which to be shown: "))
b = sorted(a, reverse=True)
if n <= len(b):
    print(f"{n}th largest element : {b[n-1]}")
else:
    print("Not enough elements in list")



26)'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]

sample output:
Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
'''
#program:
a = eval(input("Enter list: "))
b = []
while a:   
    m = min(a)      
    b.append(m)
    a.remove(m)    
print(b)
