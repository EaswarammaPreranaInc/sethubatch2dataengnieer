
1)Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
Code:
lst=[x**3 for x in range(2,11,2)]
print(lst)


2) Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
Code:
lst=eval(input("Enter the list: "))
res=[]
for x in lst:
    c=x.upper() 
    res.append(c[0])
print(res)


3) Repeat   previous  program  with  comprehension
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
Output :  ['H' , 'P' , 'C' , 'V']
Code:
lst=eval(input("Enter the list: "))
res=[ x[0].upper() for x in lst]
print(res)


4)Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension
Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
Code:
sentence=input("Enter a sentence: ")
temp=sentence.upper()
temp=temp.split()
res=[]
for x in temp:
    a=[x,len(x)]
    res.append(a)
print(res)


5)Repeat   previous  program  with  comprehension
Input :  hyd  is  green  city
Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
Code:
sentence=input("Enter a sentence: ")
temp=sentence.upper()
temp=temp.split()
res=[[x,len(x)] for x in temp]
print(res)


6)Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]
Code:
lst1=eval(input("Enter the list 1:"))
lst2=eval(input("Enter the list 2:"))
res=[]
for i in range(min(len(lst1),len(lst2))):
    a=lst1[i]+lst2[i]
    res.append(a)
print(res)




7)Repeat   previous  program  with  comprehension
Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
Code:
lst1=eval(input("Enter the list 1:"))
lst2=eval(input("Enter the list 2:"))
res=[(lst1[i]+lst2[i]) for i in range(min(len(lst1),len(lst2)))]
print(res)


8) Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Hint:  Use  repetition  operator  *
How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Code:
a=eval(input("a:"))
b=eval(input("b: "))
res=[]
for i in range(a):
    mini=[]
    for j in range(b):
        mini.append(0)
    res.append(mini)
print(res)


9) Repeat   previous  program  with  comprehension
Inputs :  3  and  4
Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Code:
a=eval(input("a="))
b=eval(input("b= "))
res=[[0 for i in range(b)] for j in range(a) ]
print(res)



10)Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  :   [20, 18, 32]
Code:
lst1=eval(input("list 1:"))
lst2=eval(input("list 2: "))
res=[]
for x in lst1:
    if x not in lst2:
        res.append(x)
print(res)


11)Repeat   previous  program  with  comprehension
Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
Code:
lst1=eval(input("list 1:"))
lst2=eval(input("list 2: "))
res=[x for x in lst1 if x not in lst2]
print(res)


12) Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
Code:
res=[x for x in range(1,21) if x%2==0]
print('even numbers between 1 to 20: ',res)


13) Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between  1  and  20]
Code:
Res=[x for x in range(2,21,2)]
print('even numbers between 1 to 20: ',Res)

14)Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
Squares  of  1  to  20  which  are  divisible  by   2 :   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
Code:
res=[x*x for x in range(1,21) if (x*x)%2==0]
print('even numbers between 1 to 20: ',res)

15)Repeat  previous  program  with  comprehension  and  without  using  if
Code:
res=[x*x for x in range(2,21,2)]
print('even numbers between 1 to 20: ',res)


16)Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Hint : Nested  for  loops
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
Code:
lst1=eval(input("list 1:"))
lst2=eval(input("list 2:"))
res=[]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        c=lst1[i]+lst2[j]
        res.append(c)
print(res)



17) Repeat   previous  program  with  comprehension
Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Code:
lst1=eval(input("list 1:"))
lst2=eval(input("list 2:"))
res=[lst1[i]+lst2[j] for i in range(len(lst1)) for j in range(len(lst2))]
print(res)

18)Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
Hint: Same  as  previous  program
Code:
lst1=input("list 1:")
lst2=input("list 2:")
res=[lst1[i]+lst2[j] for i in range(len(lst1)) for j in range(len(lst2))]
print(res)

19)Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
Code:
lst1=eval(input("list 1:"))
res=[]
for x in lst1:
    for y in x:
        res.append(y)
print(res)

20)Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
Code:
lst1=eval(input("list 1:"))
res=[y for x in lst1 for y in x]
print(res)

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) #[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) #[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


21)Most  tricky  program
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
Code:
lst = eval(input("Enter list of strings: "))

groups = []   
seen = []     

for word in lst:
    first = word[0]
    if first not in seen:
        temp = [w for w in lst if w[0] == first]
        groups.append(temp)
        seen.append(first)

print(groups)







22)Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                   0     1       2       3
       List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]
Hint1 :  Unsorted  lists  can  not  be  merged
Hint2 :  Use  single  while  loop
Code:
a = eval(input("Enter first sorted list: "))
b = eval(input("Enter second sorted list: "))
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
print("Merged sorted list:", c)

23) Write  a  program  to  determine  n-th  largest  element   of   a   list
Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
Code:
lst = eval(input("Enter list: "))
n = int(input("Enter which largest which to be shown: "))
size = len(lst)
for i in range(size):
    for j in range(0, size-i-1):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(f"{n}th largest element : {lst[n-1]}")

24)Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
Code:
lst = eval(input("Enter list: "))
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j] 
print(lst)

