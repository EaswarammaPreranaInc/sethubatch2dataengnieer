'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')

    # output
	a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
	try:
		i=0
		while a:=index(15,i):
			print(i)				# 2 5  8 
			i=i+1
	except:
		print(F'15 is found {a.count(15)} time')		# 15 is found 3 times

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
	# outputs
 Enter  the  first  list :  [10 , 20 , 30]
 Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
 True


 Enter  the  first  list : [10 , 20 , 20]
 Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
 False

	# output
		list1 = eval(input('enter list1 of nums'))
		list2 = eval(input('enter a list2 of numbers'))
		i=0;
		result=True
		for item in list1:
			try:
				i=list2.index(item,i)
				i=i+1
			except:
				result=False
			


 # copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)			# [10, 20, 15, 18]
print(a  is  b)			# false
print(a  ==  b)			# True
c = a[:]
print(c)			# [10, 20, 15, 18]
print(a  is  c)			# False
print(a  ==  c)			# True
d = a
print(d)			# [10, 20, 15, 18]
print(a  is  d)			# True
print(a  ==  d)			# True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Returns  a  new  list  with  same  elements

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''


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

 Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15

		# output
		nums=eval(input('enter a list nums: '))
		unique=set(nums)

		mode=None
		ctr=0

		for i in unique:
			count=nums.count(i)
			print(f"{i} is repeated {count} time")
		
			if count>ctr:
				ctr=count
				mode=i
		print(f"\n mode  {mode}")
		print(f"ctr {ctr}")

 #  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)  					# [[10,20,30,40],[50,60,70,80],[90,100,110,120]]
print(len(a))					# 3
print(How  to  print  1st  inner  list)		# print(a[0])		# [10,20,30,40]
print(How  to  print  2nd  inner  list)		# print(a[1])		# [50,60,70,80]
print(How  to  print  3rd  inner  list)		# print(a[2])		# [90,100,110,120]
print(How  to  print  30)			# print(a[0][2])	# 30
print(How  to  print  80)			# print(a[1][3])	# 80
print(How  to  print  100)			# print(a[2][1])    	# 100


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''


 #  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)				# print(a[0]) # [10,20]
print(How  to  print  2nd   inner  list)				# print(a[1])	#[30,40,50]
print(How  to  print  3rd   inner  list)				# print(a[2])	#[60,70,80,90]
print(How  to  print  number  of  elements  in  1st  inner  list)	# print(len(a[0]))	# 2
print(How  to  print  number  of  elements  in  2nd  inner  list)	# print(len(a[1]))	# 3
print(How  to  print  number  of  elements  in  3rd  inner  list)	# print(len(a[2]))	# 4


 #  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')					
	#output
	for i in a:
		print(i) #[[10,20],[30,40,50],[60,70,80,90]]
print(???)
	#output
	for i in a:
		for j in i:
			print(j)
print('Each  inner  list   of   outer  list  without  indexes')
		#output
		for i in a:
			for j in a:
				print(j)	
		
	
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
		#output
		for i in range(len(a)):
			print(i)
		# output
		

How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
	# output
	for i in range(len(a)):
		for j in ramge(len(a)):
			print(a[i][j],end=' ')
		print()
	# output
	10 20
	30 40 50
	60 70 80 90

How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)



'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''


 #  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
       # output
		[10,20]
		[30,40]
		[50,60]
		[70,80]
for  x , y  in  a:
	print(x , y , sep = '...')
	 # output
	10...20	
	30...40
	50...60
	70...80


#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
	# output
	[10,20,30]
	[40,50,60]
	[70,80,90]

for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

	#output
	10..20..30
	40..50..60
	70..80..90

 #  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
	#output
	[10,20],[30,40,50],[60,70,80,90]

for  x , y  in  a:
	print(x , y ,	sep = '...')

	#output
	error

 #  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)
	#output
	for i in a:
		print(i)
print(How  to  print  inner  list  in  another  way)
	#output
	for i in a:
		print(a[i])


 #  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))			# [[5,'Amar',5000.0],[10,'Rama',1000.0],[18,'Kiran',2800.0],[20,'Sita',2000],[15,Rajesh,3500.0]]
print(sorted(a , reverse = True))	# [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)				# [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]