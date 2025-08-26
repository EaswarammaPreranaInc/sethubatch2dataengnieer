# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [x**3 for x in range(2 , 11,2)]
print(a)


'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a = eval(input("Enter a input :"))
b = []
for i in a:
    b += i[0].upper()
print(b)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a = eval(input("Enter a input : "))
b = [i[0].upper() for i in a]
print(b)


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
a = input("Enter a sentence: ") 
b = []
for i in a.split():
    a = [i.upper(), len(i)]
    b.append(a)
print(b)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a = input("Enter a sentence: ") 
b = [[i.upper(), len(i)] for i in a.split()]
print(b)



'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
a = eval(input("Enter a 1st list : "))
b = eval(input("Enter a 2nd list : "))
c = []
min_len = min(len(a) , len(b))
for i in range(min-len):
    c.append(a[i] + b[i])
print(c)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
a = eval(input("Enter a 1st list : "))
b = eval(input("Enter a 2nd list : "))
c = [(a[i] + b[i]) for i in range(min(len(a) , len(b)))]
print(c)



'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
a = int(input("How many lists : "))
b = int(input("How many elements in each list :"))
c = []
for i in range(a):
    c.append([0] * b)
print(c)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
a = int(input("How many lists : "))
b = int(input("How many elements in each list :"))
c = [([0] * b) for i in range(a)]
print(c)



'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
a = eval(input("Enter a 1st list : "))
b = eval(input("Enter a 2nd list : "))
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
a = eval(input("Enter a 1st list : "))
b = eval(input("Enter a 2nd list : "))
c = [i for i in a if i not in b]
print(c)



#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a = [i for i in range(1,21) if i%2==0]
print("Even numbers  between  1  and  20 : ", a)



'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
a = [i for i in range(2,21,2)]
print("Even numbers  between  1  and  20 : ", a)



'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''

a = [i**2 for i in range(1,21) if i**2 % 2 == 0]
print(f'Squares  of  1  to  20  which  are  divisible  by   2 :  {a}') 





# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension and without using if condition
a = [i**2 for i in range(2,21,2) ]
print(f'Squares  of  1  to  20  which  are  divisible  by   2 :  {a}') # Squares  of  1  to  20  which  are  divisible  by   2 :  [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]






#Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15]
b = eval(input("Enter 2nd list : ")) # [30,40,35,12]
c = []
for i in a:
    for j in b:
        c.append(i+j)
print(c) # [40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]






# Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15]
b = eval(input("Enter 2nd list : ")) # [30,40,35,12]
c = [(i+j) for i in a for j in b]
print(c) # [40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]






#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
a = (input("Enter 1st string : ")) # HYD
b = (input("Enter 2nd string : ")) # PUNE
c = [(i+j) for i in a for j in b]
print(c) # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']





#Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
a = eval(input("Enter nested list : ")) # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = []
for i in a:
    for j in i:
        b.append(j)
print(b) # [10, 20, 30, 40, 50, 60, 70, 80, 90]






#Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
a = eval(input("Enter nested list : ")) # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ j for i in a for j in i ]
print(b) # [10, 20, 30, 40, 50, 60, 70, 80, 90]







# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]





#Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]




#Write  a  program  to  merge  two  sorted  lists  to  pvroduce  another  sorted  list
a = eval(input("Enter  1st list : ")) # [10,20,30,40,50]
b = eval(input("Enter  2nd list : ")) # [5,12,20,37]
max = 0
c = []
i = 0
j = 0
while i<len(a) or j < len(b):
    if j == len(b) or (i < len(a) and a[i] <= b[j]):
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print(c) # [5, 10, 12, 20, 20, 30, 37, 40, 50]






#Write  a  program  to  determine  n-th  largest  element   of   a   list
a = eval(input("Enter list : ")) # [10,20,30,25,40,35,12,5]
b = int(input("Enter which largest which to be shown : "))
a.sort()
print(f'{b}th  largest element is {a[-b]}') # 3th  largest element is 30




#Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
a = eval(input("Enter a List : ")) # [10,20,30,25,40,35,12,5]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a) # [5, 10, 12, 20, 25, 30, 35, 40]




#Input :   List  of  strings
#              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
#Output :  Nested  list
#		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
a = eval(input("Enter a list : ")) # ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
b = []
for i in a:
    start = i[0]
    if i[0] not in b:
        b.append(i[0])
c = []
for i in b:
    d = []
    for ch in a:
        if ch.startswith(i):
            d.append(ch)
    c.append(d)
print(c) # [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]