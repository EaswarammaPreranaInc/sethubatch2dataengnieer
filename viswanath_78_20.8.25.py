q) Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list comprehension 
Ans) i = [ x**3 for x in range(2,11,2)]
print(i)

q) Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Ans)a = eval(input('Enter the string : '))
c = []
for i in range(len(a)):
    c.append(a[i][0].upper())
print(c)

q)Repeat   previous  program  with  comprehension
ans)a = eval(input('Enter the string : '))
c = [a[i][0].upper()  for i in range(len(a))]
print(c)

q) Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension
Ans) a = input('Enter the string : ')
c = []
for i in a.split():
    c.append([i.upper(),len(i)])
print(c)

q) Repeat   previous  program  with  comprehension
Ans) a = input('Enter the string : ')
c = [[i.upper(), len(i)] for i in a.split()]
print(c)

q) Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
ans)a = eval(input('Enter the first list : '))
b = eval(input('Enter the second list : '))
c = []
for i in range(min(len(a), len(b))):   
    c.append(a[i] + b[i])
print(c)

q) Repeat   previous  program  with  comprehension
ans) a = eval(input('Enter the first list : '))
b = eval(input('Enter the second list : '))
c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
print(c)

q)Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Hint:  Use  repetition  operator  *
Ans) x = int(input("Enter number of rows: "))   
y = int(input("Enter number of columns: ")) 
a = []
for i in range(x):
    a.append([0] * y)
print(a)

q) Repeat   previous  program  with  comprehension
ans) x = int(input("Enter number of rows: "))  
y = int(input("Enter number of columns: "))  
a = [[0 for j in range(y)] for i in range(x)]  
print("a is:", a)

q) Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
ans) a = eval(input("Enter 1st list: "))  
b = eval(input("Enter 2nd list: "))  
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)

q) Repeat   previous  program  with  comprehension
ans) a = eval(input("Enter 1st list: "))  
b = eval(input("Enter 2nd list: "))  
c = [i for i in a if i not in b]
print(c)  

q) Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
ans) c = [i for i in range(1,21) if i%2==0 ]
print(c)


q) Repeat  previous  program  with  comprehension  and  without  using  if
ans) c = [i for i in range(2,21,2)]
print(c)

q) Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
ans) c = [i**2 for i in range(1,21) if i%2==0]
print(c)

q) Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between  1  and  20]
Ans) c = [i**2 for i in range(2,21,2) ]
print(c)

q) Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Hint : Nested  for  loops
ans)a = eval(input("Enter the list1 : ")) 
b = eval(input("Enter the list2 : "))
c = []
for i in range(len(a)):
    for j in range(len(b)):
        c.append(a[i]+b[j])
print(c)

q) Repeat   previous  program  with  comprehension
ans) a = eval(input("Enter the list1 : ")) 
b = eval(input("Enter the list2 : "))
c = [(a[i]+b[j]) for i in range(len(a)) for j in range(len(b))]
print(c)

q) Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
ans) a = input("Enter the str1 : ") 
b = input("Enter the str2 : ")
c = [(a[i]+b[j]) for i in range(len(a)) for j in range(len(b))]
print(c)
q) Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
Ans) a = eval(input("Enter the list1 : ")) 
c = []
for i in range(len(a)):
    for j in range(len(a[i])):
        c.append(a[i][j])
print(c)

q) Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
Ans) a = eval(input("Enter the list : ")) 
c = [(a[i][j]) for i in range(len(a)) for j in range(len(a[i]))]
print(c)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

q) Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
Hint: Do  not  sort  the  lists
Ans) A = eval(input("Enter the list of strings: "))
B = []
C = {}
for i in A:
    K = i[0].lower()  
    if K in C:
        C[K].append(i)
    else:
        C[K] = [i]
        B.append(C[K])   
print(B)

q) Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]
Hint1 :  Unsorted  lists  can  not  be  merged
Hint2 :  Use  single  while  loop
Ans) a = eval(input("Enter the 1st sorted list : "))  
b = eval(input("Enter the 2nd sorted list : "))  
c = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c += a[i:]
c += b[j:]
print(c)

q) Write  a  program  to  determine  n-th  largest  element   of   a   list
Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
Ans) try:
    a = eval(input("Enter the list : ")) 
    b = int(input("Enter the nth value to find that max value : "))
    a.sort(reverse = True)
    print(a)
    print(f'{b} largest number is {a[b-1]}')
except:
    print('index out of range.')


q) Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
Ans) a = eval(input("Enter the list : ")) 
b = []
while a :
    c = min(a)
    a.remove(c)
    b.append(c)
print(b)
