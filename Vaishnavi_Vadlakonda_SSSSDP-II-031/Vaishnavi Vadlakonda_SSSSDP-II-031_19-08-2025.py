'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25] # Ref 'a' points to list
try:
	i = 0
	while (i := a.index(15 , i + 1)):
		print(i)
except:
	print(F'15  is  found  {a . count(15)} times')
	












'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index() method
Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
True
Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
False
'''
a = eval(input("Enter the first list:"))
b = eval(input("Enter the second list:"))
index = -1
try:
    for i in a:
        index = b.index(i, index + 1)
    print(True)
except ValueError:
    print(False)
'''
Outputs:

Enter the first list:[10 , 20 , 30]
Enter the second list:[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
True

Enter the first list:[10 , 20 , 20]
Enter the second list:[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
False
'''











# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18] # Ref 'a' points to list of 4 elements
b = a . copy() # elements of 'a' copied to reference 'b' i.e., shallow copy
print(b) # prints list 'b' i.e., [10, 20, 15, 18]
print(a  is  b) # prints False
print(a  ==  b) # prints True
c = a[:] # elements of 'a' copied to reference 'c' 
print(c) # prints list 'c' i.e., [10, 20, 15, 18]
print(a  is  c) # prints False
print(a  ==  c) # prints True
d = a # Address of list 'a' copied to reference 'd'
print(d) # prints list 'd' i.e., [10, 20, 15, 18]
print(a  is  d) # prints True
print(a  ==  d) # prints True












'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
ctr=5
Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode:15
'''

a = eval(input("Enter list:"))
mode = None
ctr = 1
for i in a:
    if a.count(i) > ctr:
        ctr += 1
        mode = i
print("Mode:",mode)

'''
Outputs:

Enter list:[12 , 20 , 18 , 10 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode: 10
Enter list:[12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode: 15
'''








#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ] # Ref 'a' points to list of lists or nested list
print(a) # prints list 'a' i.e., [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120]]
print(len(a)) # prints number of elements in the list i.e., 3
print(a[0]) # How to print  1st  inner  list, prints inner list at index 0 i.e., [10 , 20 , 30 ,  40]
print(a[1]) # How to print  2nd  inner  list, prints inner list at index 1 i.e., [50 , 60 ,  70 , 80]
print(a[2]) # How to print  3rd  inner  list, prints inner list at index 2 i.e., [90 , 100 , 110 , 120]
print(a[0][2]) # How to print 30, prints 30 at index 2 of inner list at index 0 of list 'a'
print(a[1][3]) # How to print 80, prints 80 at index 3 of inner list at index 1 of list 'a'
print(a[2][1]) # How to print 100, prints 100 at index 1 of inner list at index 2 of list 'a'









#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]] # # Ref 'a' points to list of lists or nested list
print(a[0]) # How to print 1st inner list
print(a[1]) # How to print 2nd inner list
print(a[2]) # How to print 3rd inner list
print(len(a[0])) # How to print number of elements in 1st inner list
print(len(a[1])) # How to print number of elements in 2nd inner list
print(len(a[2])) # How to print number of elements in 3rd inner list
	  







#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    print(i)
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
    for j in i:
        print(j, end = ' ')
    print()
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ') 
    print()
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''








#  Find  outputs (Home  work)
a = [[10, 20] , [30, 40] , [50, 60] , [70, 80]] # Ref 'a' points to nested list
for x in a:
    print(x) 
print()
for x, y in a:
	print(x, y,sep = '...')

'''
Outputs:

[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
'''
	   










#  Find  outputs (Home  work)
a = [[10, 20, 30] , [40, 50, 60] , [70, 80, 90]] # Ref 'a' points to nested list
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x, y, z, sep = '...')

'''
Outputs:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''












#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]] # # Ref 'a' points to nested list
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x, y,	sep = '...')

'''
Outputs:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]

10...20
30...40...50
60...70...80...90
'''











#  Find  outputs  (Home  work)
a = [[]]
print(a[0]) # How to print inner list
for i in a:
    print(i) # How to print inner list in another way










#  Find  outputs  (Home  work)
a = [[10, 'Rama', 1000.0] , [20, 'Sita', 2000.0] , [15, 'Rajesh', 3500.0] , [18, 'Kiran', 2800.0] , [5, 'Amar',5000.0]] # Ref 'a' points to nested list
print(sorted(a)) # list is sorted and prints list i.e., [[5, 'Amar',5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) # list is sorted in descending order and prints sorted list i.e., [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar',5000.0]]
print(a) # prints list 'a' i.e., [[10, 'Rama', 1000.0] , [20, 'Sita', 2000.0] , [15, 'Rajesh', 3500.0] , [18, 'Kiran', 2800.0] , [5, 'Amar',5000.0]]