 # Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

n = [i**3 for i in range(2,11,2)]
print(n)

'''output:
[8, 64, 216, 512, 1000]
'''



'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

list = eval(input("Enter list of lower case strings: "))
b = []
for i in list:
    b.append(i[0].upper())
print(b)

'''output:
Enter list of lower case strings: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''


list = eval(input("Enter list of lower case strings: "))
b = [i[0].upper() for i in list]
print(b)

'''output:
Enter list of lower case strings: ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
'''output:
Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
'''
n = input("Enter any sentence: ")
b = n.split()
c =[]
for i in b:
    c.append([i.upper(),len(i)])
print(c)

'''output:
Enter any sentence: Hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''



'''(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a = input("Enter any sentence: ")
b = a.split()
c = [[i.upper(),len(i)] for i in b]
print(c)

'''output:
Enter any sentence: hyd is green city
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
'''




'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
b =[]
for i in range(len(list2)):
    s = list1[i] + list2[i]
    b.append(s)
print(b)

'''output:
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
b =[list1[i]+list2[i] for i in range(len(list2))]
print(b)



'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''


'''How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''

a = eval(input("Enter how many lists : "))
b = eval(input("How many elements in each list: "))
c = []
for i in range(a):
    c.append([0]*b)
print(c)

'''output:
Enter how many lists : 3
How many elements in each list: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''


'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
a = eval(input("Enter how many lists: "))
b = eval(input("Enter how many elements you want: "))
c =[[0]*b for i in range(a)]
print(c)

'''output:
Enter how many lists: 3
Enter how many elements you want: 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''


'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
b = []
for i in range(len(list1)):
    if list1[i] not in list2:
        b.append(list1[i])
print(b)

'''output:
Enter 1st list: [10,20,15,18,25,32]
Enter 2nd list: [30,40,10,25,15]
[20, 18, 32]
'''


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))
b = [list1[i] for i in range(len(list1)) if list1[i] not in list2]
print(b)

'''output:
Enter 1st list: [10,20,15,18,25,32]
Enter 2nd list: [30,40,10,25,15]
[20, 18, 32]
'''



'''
 #  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
b = [i for i in range(1,21) if i % 2 == 0]
print(b)


'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''
b = [i for i in range(2,21,2)]
print(b)



'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''

n =[i**2 for i in range(1,21) if i**2 % 2 == 0]
print(f"Squares of 1 to 20 which are divisible by 2 : {n}")

'''output 
Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''



#Repeat  previous  program  with  comprehension  and  without  using  if
n = []
for i in range(1,21):
    if i % 2 == 0:
        c = i**2
        n.append(c)
print(f"Squares of 1 to 20 which are divisible by 2 : {n}")

'''output 
Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''




'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
a = eval(input("Enter 1st list: "))
b = eval(input("Enter 2nd list: "))
c = []
for i in a:
    for j in b:
        sum = i+j
        c.append(sum)
print(c)

'''output
Enter 1st list: [10 , 20 , 15]
Enter 2nd list:  [30 , 40 , 35 , 32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
'''




'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
a = eval(input("Enter 1st list: "))
b = eval(input("Enter 2nd list: "))
c = [i+j for i in a for j in b]
print(c)

'''
output:
Enter 1st list: [10 , 20 , 15]
Enter 2nd list: [30 , 40 , 35 , 32]
[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
'''



'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a = input("Enter 1st list: ")
b = input("Enter 2nd list: ")
c = [i+j for i in a for j in b]
print(c)

'''output:
Enter 1st list: HYD
Enter 2nd list: PUNE
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
'''




'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
'''Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''

n = eval(input("Enter nested list: "))
c =[]
for i in n:
    for j in i:
        c.append(j)
print(c)

'''output:
Enter nested list: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''



'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
n = eval(input("Enter nested list: "))
c =[j for i in n for j in i]
print(c)

'''output:
Enter nested list: [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''


# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x] #Here each list inside the list is appended to list be with respect to number elements in the inner list 
#Example 1st inner list is having 2 elementss so into b that list is appended 2 times and so on..
print(b) 

'''output
[[10,20],[10,20],[30,40,50],[30,40,50],[30,40,50],[60,70,80,90],[60,70,80,90],[60,70,80,90],[60,70,80,90]]
'''


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)

'''output:
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
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

'''
'''
Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''

n = eval(input("Enter list: "))
c = []
for i in n:
    b = i[0]
    c.append(b)
m = set(c)
res = []
for i in m:
    p = []
    for j in n:
        if j[0] == i:
            p.append([j])
    res.append(p)
print(res)

'''output:
Enter list: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Anand', 'Amar'], ['Swathi', 'Srinivas'], ['Zebra'], ['King']]
'''


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

list1 = [10, 20, 30, 40, 50]
list2 = [5, 12, 20, 37]
a = sorted(list1)
b = sorted(list2)
c = []
i = j = 0   
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

'''output:
Merged sorted list: [5, 10, 12, 20, 20, 30, 37, 40, 50]
'''


'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''

n = eval(input("Enter list: "))
a = eval(input("Enter which largest number should be shown: "))
b = sorted(n)
print(f"{a}th largest element: ",b[-a])

'''output:
Enter list: [10,20,30,25,40,35,12,5]
Enter which largest number should be shown: 4
4 largest element:  25
'''
                #OR

'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
a = eval(input("Enter list : "))
n = eval(input("Enter nth largest element you want: "))
c = set(a)
for i in range(n):
    e = max(c)
    c.remove(e)
print(e)

'''output:
Enter list : [10,20,30,25,40,35,12,5]
Enter the element: 3
30
'''


'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
a = eval(input("Enter list: "))
c = []
while a:
    small = min(a)
    c.append(small)     
    a.remove(small)     
print("Sorted list:", c)

'''output:
Enter list:  [10,20,30,25,40,35,12,5]
Sorted list: [5, 10, 12, 20, 25, 30, 35, 40]
'''