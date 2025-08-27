#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1  2     3    4     5   6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)			
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
	#OUTPUTS
	15 is found at index: 2
	15 is found at index: 5
	15 is found at index: 8
	15 is found 3 times


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35					# tuples cannot modified
print(a)					# (10, 20, 30, 40, 50)
print(id(a))					# address of the object
How  to  modify  30  in  tuple  to  35		# a=a[0:3]+(35,)+[3:5]
print(a)					# (10, 20, 30, 35, 40, 50)
print(id(a))					# address of the object


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)					# tuple does not have any remove method we cannot modified
del  a[2]					# tuple does not have any del method and we cannot modified
a . pop(2)					# tuple does not have any pop() method and we cannot modified
print(a)					# (10, 20, 30, 40, 50)
print(id(a))					# address of the object
How  to  remove  30  from  tuple  'a'	
	#a=a[0:2]+[3:5]
print(a)					# (10, 20, 40, 50)
print(id(a))					# address of the object


#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)					# ((10, 20), (30, 40, 50), (60, 70, 80,90))
print(type(a))					# <class tuple>
print(len(a))					# 3
print(a[0])					# (10, 20) How  to  print  1st  inner  tuple)	
print(a[1])					# (30, 40, 50) How  to  print  2nd  inner  tuple)
print(a[2]) 					# (60, 70, 80, 90) How  to  print  3rd  inner  tuple)
print(a[0][1])					# How  to  print  20)
print(a[1][2])					# How  to  print  50)
print(a[2][3])					# How  to  print  90)


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])					# (10, 20, 30)How  to   print  inner  tuple)
print(*a)					# How  to   print  inner  tuple  in  another  way)
print(a[0][0])					# How   to  print   10)
print(a[0][1])					# How   to  print   20)
print(a[0][2])					# How   to  print   30)
b = ((),)
print(b[0])					# How  to   print  inner  tuple  of  tuple  'b')
print(*b)					# How  to   print  inner  tuple  of  tuple  'b'  in  another  way)


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)					# ((10, 20, 30))
print(*a)					# (10, 20, 30)
b = (())			
print(b)					# (() )
print(*b)					# ()


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)					# {10, 20, 15, 18, 20, 12, 18}
print(type(a))					# <class str>
b = eval(a)					#class string  convert into set and 'a' assign to 'b'
print(b)					# {10, 20, 15, 18, 12}
print(type(b))					# <class set>


 #  Find  outputs  (Home  work)
print({(10 , 20 , 30)})				#{(10, 20, 30)} 
print({[10 , 20 , 30]})				# error becoz list is mutable 
print({{10 , 20 , 30}})				# error becoz set mutable set inside set
print({{}})					# error becoz set mutable set inside set


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(*a)					# 'set  with  print  function')		
print(a)					# {25, True, 'Hyd', 10.8}
#print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
			#output			# 25
		for i in a:			 'Hyd'
			print(i)		  10.8
						  True


 # Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)						# {'Hyd', True, 25}
print(len(s))						# 3
print(type(s))						# <class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)						# {'Hyd', 25, True, 10.8}
a , b , c , d = s					# this references are assigning set values
print(a)						# Hyd
print(b)						# 25
print(c)						# True
print(d)						# 10.8


 # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)						# {'Hyd', 25, True, 10.8}
a , *b = s
print(a)						# Hyd
print(b)						# [25, True, 10.8]
print(type(b))						# <class list>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)						#{'Hyd', 25, True, 10.8}
a , *b , c = s
print(a)						# Hyd
print(b)						# [25, True]
print(c)						# 10.8


 # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)						# {20,10}
x , y = s						# set assing another references
print(x)						# 10
print(y)						# 20

 # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)						# {100,110,120,130,140,150} any order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)						
print(d)						#  {10, 20, 15, 18, 12}
e = set('Rama  rAo')					
print(e)						# {'R','a','m, 'A','r', ','o'}
print(set(25))						# error
print(set())						# set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''