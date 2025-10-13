'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = -1
	while (i := a.index(15, i + 1)) >= 0:
		print(i)
except ValueError:
	print(f'15  is  found  {a.count(15)}  times ')

#****************************************************************************
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

5) Hint:  Use  index()  method
'''

lst1 = eval(input('Enter the first list: '))
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



'''
Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True

 Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False'''

#****************************************************************************

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)   #[10,20,15,18]
print(a  is  b)  #FAlse
print(a  ==  b)  #True
c = a[:]
print(c)  #[10,20,15,18]
print(a  is  c)   #False
print(a  ==  c)   #True
d = a
print(d)    #[10,20,15,18]
print(a  is  d)   #True
print(a  ==  d)	#True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Returns  a  new  list  with  same  elements

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''

#****************************************************************************

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
    ctr = 5
'''
ctr=0
mode=0
lst=eval(input("enter list: "))
for x in set(lst):
	if lst.count(x)>ctr:
		mode=x
		ctr=lst.count(x)
emp_lst=[]
for x in set(lst):
	if lst.count(x)==ctr:
		emp_lst.append(x)
print(f"{emp_lst} is repeated {ctr} times in lst. So Mode is {emp_lst}")



'''
Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15

'''

#****************************************************************************

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[0][2])
print(a[1][3])
print(a[2][1])


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''

#****************************************************************************

 #  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])
print(a[1])
print(a[2])
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))

#****************************************************************************

 #  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a)
print()

#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
	print(x)
print()

#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
	for y in x:
		print(y,end= " ")
	print()

# How to print elements of each inner list using indexes in matrix style (use nested loop)
print('Elements in the form of matrix using indexes')
for x in range(len(a)):
   for y in range(len(a[x])):
      print(a[x][y], end=' ')
   print()


'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''

#****************************************************************************

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)      #[10 , 20]<next line>[30 , 40]<next line>[50 , 60]<next line>[70 , 80]
print()
for  x , y  in  a:
	print(x , y , sep = '...')   #10...20<next line>30...40<next line>50...60<next line>70...80

#****************************************************************************

 #  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)  #[10 , 20 , 30]<next line>[40 , 50 , 60]<next line>[70 , 80 , 90]
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')    #10...20...30<next line>40...50...60<next line>70...80...90<next line>
	
#****************************************************************************

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:   #[10 , 20]<next line>[30 , 40 , 50]<nect line>[60 , 70 , 80 , 90]
	print(x)  #[
for  x , y  in  a:
	print(x , y ,	sep = '...')   #10...20 <next iteration is Error becausse of 3 values
	
#****************************************************************************
#  Find  outputs  (Home  work)
a = [[]]
print(a[0])  # prints the empty inner list: []
# Another way to print the inner list
for x in a:
	print(x)

#****************************************************************************

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) #[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) #[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] 