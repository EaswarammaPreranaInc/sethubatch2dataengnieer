'''''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
#Program
a=eval(input("Enter a sentence: "))
b=[[x.upper(),len(x)] for x in a.split()]
print(b)


'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]
'''
#Program
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''
#Program
a = eval(input("Enter 1st list : "))    
b = eval(input("Enter 2nd list : "))
c= [a[i]+b[i] for i in range(min(len(a), len(b)))]
print(c) 


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''
#Program
n = int(input())
m = int(input())
a=[]
for i in range(n):
    a.append([0]*m)
print(a)    


'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
#Program
n = int(input())
m = int(input())
a=[[0]*m for i in range(n)]
print(a)


'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]

Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]
'''
#Program
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = []
for i in a:
    if i not in b:
        c.append(i) 
print("Elements of 1st list which are not in 2nd list : ", c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''
#Program
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = [x for x in a if x not in b]
print("Elements of 1st list which are not in 2nd list : ", c)


'''
#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
Even numbers  between  1  and  20 :   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between  1  and  20]
'''
#Program
a = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers between 1 and 20 : ", a)

a=[i for i in range(2, 21, 2)]
print("Even numbers between 1 and 20 : ", a)


'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]

Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
#  Repeat  previous  program  with  comprehension  and  without  using  
'''
#Program
a = [x**2 for x in range(1, 21) if x**2 % 2 == 0]
print("Squares of 1 to 20 which are divisible by 2 : ", a)
a = [x**2 for x in range(2, 21, 2)]
print("Squares of 1 to 20 which are divisible by 2 : ", a)


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''
#Program
a=eval(input("Enter 1st list : "))
b=eval(input("Enter 2nd list : "))
c=[]
for i in a:
    for j in b:
        c.append(i + j)
print(c)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
#Program
a = eval(input("Enter 1st list : "))
b = eval(input("Enter 2nd list : "))
c = [i + j for i in a for j in b]
print(c)


'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a = input("Enter 1st string : ")
b = input("Enter 2nd string : ")
c = [i + j for i in a for j in b]
print(c)


'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
#Program
a = eval(input("Enter nested list : "))
b = []
for i in a:
    for j in i:
        b.append(j)

print(b)


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
#Program
a = eval(input("Enter nested list : "))
b = [j for i in a for j in i]
print(b)


# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) #[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)  #[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


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

Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''
#Program
a=eval(input())
b=[]
c=[]
for i in a:
    if i[0] not in b:
        b.append(i[0])
    else:
        a.remove(i)
        c.append(i)

res=[[i,j] for i in a for j in c if i[0]==j[0]]
print(res)


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
a = eval(input("Enter 1st sorted list : "))
b = eval(input("Enter 2nd sorted list : "))
c = []
i = j = 0
while i < len(a) and j < len(b):   
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
if i < len(a):
    c.extend(a[i:])
if j < len(b):
    c.extend(b[j:])
print(c)



'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30

Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
'''
#Program
a = eval(input("Enter list: "))
n = int(input("Enter which largest which to be shown: "))
a=set(a)
a=list(a)
a.sort(reverse=True)
if n <= len(a):
    print(f"{n}th largest element : {a[n-1]}")
else:
    print(f"{n}th largest element does not exist in the list")

'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
'''
#Program
a = eval(input("Enter list: "))
for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)    