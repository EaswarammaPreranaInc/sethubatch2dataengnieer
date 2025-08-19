1) Modify  the  following  program  with  walrus  operator
Hint:  Call  index()  method  only  once
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')	
ans)a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
    i = -1
    while (i := a . index(15 , i + 1)) >= 0 :
	    print(i)
except:
	print(F'15  is  found  {a . count(15)} times ')

2) Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
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
5) Hint:  Use  index()  method 
Ans) lst1 = eval(input('Enter the first list: '))
lst2 = eval(input('Enter the second list: '))
pos = 0
found = True
for x in lst1:
   try:
      pos = lst2.index(x, pos) + 1
   except ValueError:
      found = False
      break
print(found)    

3)a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10, 20, 15, 18]
print(a  is  b) # False
print(a  ==  b) # True
c = a[:] 
print(c) # [10, 20, 15, 18]
print(a  is  c) # False
print(a  ==  c) # True
d = a
print(d) # [10, 20, 15, 18]
print(a  is  d) # True
print(a  ==  d) # True

4)  Write  a  program  to  determine  mode
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
    ctr = 5
Ans)a = eval(input('enter the list : '))
ctr = 0
mode = 0
for i in set(a):
    if a.count(i)>ctr:
        mode = i
        ctr = a.count(i)
print(f'{mode} is repeated {ctr} times in the list.')
print(f'Mode is {mode}')


5)a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
(How  to  print  1st  inner  list) # print(a[0])
(How  to  print  2nd  inner  list) # print(a[1])
(How  to  print  3rd  inner  list) # print(a[2])
(How  to  print  30) # print(a[0][2])
(How  to  print  80) # print(a[1][3])
(How  to  print  100) # print(a[2][1])

6)a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list) # print(a[0])
print(How  to  print  2nd   inner  list) # print(a[1])
print(How  to  print  3rd   inner  list) # print(a[2])
print(How  to  print  number  of  elements  in  1st  inner  list) # print(a[0][0],a[0][1])
print(How  to  print  number  of  elements  in  2nd  inner  list) # print(a[1][0],a[1][1],a[1][2])
print(How  to  print  number  of  elements  in  3rd  inner  list) # print(a[2][0],a[2][1]),a[2][2],a[2][3])

7)a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function') # Nested list  with  print function'
print(???) # print(a)
print('Each  inner  list   of   outer  list  without  indexes') # Each  inner  list   of   outer  list  without  indexes'
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop) 
# for i in a:
    print(i)
print('Elements  in  the  form   of  matrix   without  using  indexes') # Elements  in  the  form   of  matrix   without  using  indexes'
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
# for i in a:
    for x in i:
        print(x,end = ' ')
    print()
print('Elements  in  the  form   of  matrix  using  indexes') # Elements  in  the  form   of  matrix  using  indexes'
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
# for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()

8)a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x) # [10 , 20]     # [30 , 40]     # [50 , 60]     # [70 , 80]
print()
for  x , y  in  a:
	print(x , y , sep = '...')  # 10...20  # 30...40  # 50...60  # 70...80

9)a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x) # [10, 20, 30]     # [40, 50, 60]      # [70, 80, 90]
print() # 'cursor moves to new line  '
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...') # 10...20...30     #  40...50...60      #  70...80...90

10)a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x) #[10 , 20]  #[30 , 40 , 50]  # [60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,sep = '...') # 10...20    # more or few values to unpack

11)a = [[]]
print(a[0]) # (How  to  print  inner  list)
print(*a) # (How  to  print  inner  list  in another way)

12)a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) # [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
