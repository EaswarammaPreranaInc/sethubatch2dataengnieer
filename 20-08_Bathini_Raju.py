#BATHINI RAJU

# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
cubes=[x**3 for x in range(2,11,2)]
print(cubes) # [8, 64, 216, 512, 1000]

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
input =eval(input("Enter list of cities: ")) #input: ['hyd', 'pune', 'chennai', 'vijayawada']
output = []
for x in input:
    output.append(x[0].upper())
print(output) # ['H', 'P', 'C', 'V']

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
l = [x[0].upper() for x in eval(input())]
print(l) # ['H', 'P', 'C', 'V']


'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

l=input("Enter the String Input: ").split()
res=[]
for x in l:
  res.append([x.upper(),len(x)])
    
print(res)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''

res=[ [x.upper(),len(x)] for x in input().split()]
print(res)






'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''


l1=eval(input("Enter 1st list: ")) # [10, 20, 30, 40, 50, 60, 70]
l2=eval(input("Enter 2nd list: ")) # [100, 200, 300, 400]
res=[]
for i in range(min(len(l2),len(l1))):
    res.append(l1[i]+l2[i])
print(res)


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

l1=eval(input("Enter 1st list: ")) # [10, 20, 30, 40, 50, 60, 70]
l2=eval(input("Enter 2nd list: ")) # [100, 200, 300, 400]

res=[l1[i]+l2[i] for i in range(min(len(l2),len(l1)))]
print(res)


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

rows = int(input("Enter number of rows: "))  # 3
cols = int(input("Enter number of columns: "))  # 4
res=[]
for i in range(rows):
    res.append([0] * cols)
print(res)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''


rows = int(input("Enter number of rows: "))  # 3
cols = int(input("Enter number of columns: "))  # 4
res=[[0] * cols for i in range(rows)]

print(res)


'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

l=eval(input("Enter 1st list: "))  # [10, 20, 15, 18, 25, 32]
m=eval(input("Enter 2nd list: "))  # [30, 40, 10, 25, 15]
res=[]
for x in l:
    if x not in m:
        res.append(x)
print(res)  # [20, 18, 32]


'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''


l=eval(input("Enter 1st list: "))  # [10, 20, 15, 18, 25, 32]
m=eval(input("Enter 2nd list: "))  # [30, 40, 10, 25, 15]
res=[ x for x in l if x not in m ]

print(res)  # [20, 18, 32]


#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

x=[i for i in range(1,21) if i%2==0]
print(x) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
Repeat  previous  program  with  comprehension  and  without  using  if

Output: [Even  numbers  between  1  and  20]
'''

x=int(input("Enter the range: "))  # 20

for i in range(2,x+1,2):
    print(i)
    
    
'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''

res=[i**2 for i in range(1,21) if (i**2)%2==0]
print(res)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


#Repeat  previous  program  with  comprehension  and  without  using  if

x=int(input("Enter the range: "))  # 20
res=[]
for i in range(2,x+1,2):
    res.append(i**2)
print(res) # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''

l1=eval(input("Enter 1st list: "))  # [10, 20, 15]
l2=eval(input("Enter 2nd list: "))  # [30, 40, 35, 32]
res=[]
for i in l1:
    for j in l2:
        res.append(i+j)
print(res)



'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

l1=eval(input("Enter 1st list: "))  # [10, 20, 15]
l2=eval(input("Enter 2nd list: "))  # [30, 40, 35, 32]
res=[i+j for i in l1 for j in l2]
print(res)

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

l1=eval(input("Enter 1st string: "))  # 'HYD'
l2=eval(input("Enter 2nd string: "))  # 'PUNE'
res=[i+j for i in l1 for j in l2]
print(res)



'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

l=eval(input("Enter nested list: "))  # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
res=[]
for i in l:
    res.extend(i)
print(res)


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

res=[j for i in eval(input("Enter nested list: ")) for j in i]  # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(res)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]



# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [10, 20, 30, 40, 50, 60, 70, 80, 90]


#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]


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

l=eval(input())
c = {}
res= []
for i in l:
    ch = i[0]
    if ch not in c:
        c[ch] = []
        res.append(c[ch])  
    c[ch].append(i)

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

a = eval(input("Enter first sorted list: "))  # [10, 20, 30, 40, 50]
b = eval(input("Enter second sorted list: "))  #    [5, 12, 20, 37]
c = []
i, j = 0, 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c.extend(a[i:])
c.extend(b[j:])
print(c)


'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
n = eval(input("Enter list: "))  # [10, 20, 30, 25, 40, 35, 12, 5]
k = eval(input("Enter n: "))  # 3
n.sort(reverse=True)
print(n[k-1])

#if there is no duplicates it works



'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''


l=eval(input())
res=[]
low=0
high=len(l)-1

while(low<=high):
  l[low],l[high]=l[high],l[low]
  low+=1
  high-=1
print(l) # [5, 10, 12, 20, 25, 30, 35, 40]