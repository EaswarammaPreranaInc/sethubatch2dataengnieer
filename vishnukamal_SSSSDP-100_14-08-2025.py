'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
i = -1   
try:
    while (i:= a.index(15, i + 1)):
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')

'''
# Output: 
2
5
8
15 is found 3 times
'''



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
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in   [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
a=eval(input('Enter  the  first  list :'))
b=eval(input('Enter  the  second  list :'))
try:
	i=-1
	for x in a:
		i = b.index(x,i + 1)
	print('True')
except:
	print('False')	
	
'''
# Output:

Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True

Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False
'''




# copy()  method  demo program  (Home  work)

a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)# Output: [10 , 20 , 15 , 18]
print(a  is  b)# Output: False
print(a  ==  b)# Output: True
c = a[:]
print(c)# Output: [10 , 20 , 15 , 18]
print(a  is  c)# Output: False
print(a  ==  c)# Output: True
d = a
print(d)# Output: [10 , 20 , 15 , 18]
print(a  is  d)# Output: True
print(a  ==  d)# Output: True




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
   ctr  = 5
'''
a=eval(input('Enter any list :'))
mode=0
ctr=0
for i in a:
	count=a.count(i)
	if count > ctr:
		ctr=count
		mode=i
print('Mode:',mode)

'''
# Output:
Enter any List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15
'''



#  Nested  List  demo  program  (Home  work)

a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)# Output: [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))# Output: 3
print(a[0])# How  to  print  1st  inner  list # Output: [10, 20, 30, 40]
print(a[1])# How  to  print  2nd  inner  list # Output: [50, 60, 70, 80]
print(a[2])# How  to  print  3rd  inner  list # Output: [90, 100, 110, 120]
print(a[0][2])# How  to  print  30 # Output: 30
print(a[1][3])# How  to  print  80 # Output: 80
print(a[2][1])# How  to  print  100 # Output: 100



#  Find  outputs  (Home  work)

a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) # How  to  print  1st   inner  list # Output: [10, 20]
print(a[1]) # How  to  print  2nd   inner  list # Output: [30, 40, 50]
print(a[2]) # How  to  print  3rd   inner  list # Output: [60, 70, 80, 90]
print(len(a[0])) # How  to  print  number  of  elements  in  1st  inner  list # Output: 2
print(len(a[1])) # How  to  print  number  of  elements  in  2nd  inner  list # Output: 3
print(len(a[2])) # How  to  print  number  of  elements  in  3rd  inner  list # Output: 4




#  How  to  print  nested  list  in  differnent  ways

a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function') 
print(a) # Output:[[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Each  inner  list   of   outer  list  without  indexes') 
for x in a:#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
	print(x)
'''
# Output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
'''
print('Elements  in  the  form   of  matrix   without  using  indexes') 
for i in a:#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
	for j in i:
		print(j,end='   ')
	print()
'''
# Output:
10   20
30   40   50
60   70   80   90
'''
print('Elements  in  the  form   of  matrix  using  indexes') 
for i in range(len(a)):#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
	for j in range(len(a[i])):
		print(a[i][j],end='   ')
	print()
'''
# Output:
10   20
30   40   50
60   70   80   90
'''



#  Find  outputs (Home  work)

a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
'''
# Output: 
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

error as too many values are there to unpack
'''



#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
'''
# Output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''



#  Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
	
'''
# Output: 
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20
error as too many values are there to unpack
'''



#  Find  outputs  (Home  work)

a = [[]]
print(a[0])# How  to  print  inner  list # Output: []
print(*a) # How  to  print  inner  list  in  another  way # Output: []



#  Find  outputs  (Home  work)

a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))# Output: [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))# Output: [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)# Output: [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]