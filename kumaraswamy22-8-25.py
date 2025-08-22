#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i) # 2, 5, 8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times') # 3
  
output:
15 is found at index :2
15 is found at index :5
15 is found at index :8
15  is  found 3 times


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35 # Error Tuble Element cannot be modified bcoz it is immutable
print(a) # ( 10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # Address of Tuple 'a'
# How  to  modify  30  in  tuple  to  35
a=a[:2] + (35,) + a[3:]
print(a) # ( 10 ,  20 ,  35 ,   40 ,  50 )
print(id(a)) # Different Address of Tuple 'a'

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # Error Tuble Element cannot be Deleted bcoz it is immutable
del  a[2]  # Error Tuble Element cannot be Deleted bcoz it is immutable
a . pop(2) # Error Tuble Element cannot be Deleted bcoz it is immutable
print(a) # (10 , 20 , 30 , 40 , 50)
print(id(a)) # Address of Tuple 'a'
How  to  remove  30  from  tuple  'a'
a=a[:2] + a[3:]
print(a) # (10 , 20 , 40 , 50)
print(id(a))

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # < class 'tuple'>
print(len(a)) # 3
print(How  to  print  1st  inner  tuple)
print(a[0])
print(How  to  print  2nd  inner  tuple)
print(a[1])
print(How  to  print  3rd  inner  tuple)
print(a[2])
print(How  to  print  20)
print(a[0][1])
print(How  to  print  50)
print(a[1][2])
print(How  to  print  90)
print(a[2][3])

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)
print(a[0])
print(How  to   print  inner  tuple  in  another  way)
print(*a)
print(How   to  print   10)
print(a[0][0])
print(How   to  print   20)
print(a[0][1])
print(How   to  print   30)
print(a[0][2])
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(b[0])
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
print(*b)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # ((10 , 20 , 30))
print(*a) # (10 , 20 , 30)
b = (())
print(b) # ()
print(*b) # <Empty blank printed>

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # < class 'str'>
b = eval(a) # convers 'str set' into 'set' 
print(b) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b)) # < class 'set'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}
print({[10 , 20 , 30]}) # Error set cannot hold mutalble elements
print({{10 , 20 , 30}}) # Error set cannot hold mutalble elements
print({{}}) # Error set cannot hold mutalble elements

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
for x in a:
  print(x)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # { 'Hyd',True,25}
print(len(s)) # 3
print(type(s)) # < class 'str'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } not nessessary in same it can be changed every time when runs the program
a , b , c , d = s
print(a) # Hyd
print(b) # 25
print(c) # True
print(d) # 10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  # {'Hyd',  25,  True,  10.8 } not nessessary in same it can be changed every time when runs the program
a , *b = s 
print(a) # 'Hyd'
print(b) # [25,  True,  10.8]
print(type(b)) < class 'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) # 'Hyd'
print(b) # [25,True
print(c) # 10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20 , 10 , 20 , 10}
x , y = s # Error due Too many values in the s
print(x) # Error
print(y) # Error

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) # {100,110,120,130,140,150}
print(b)  # {100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) { 10,20,15,18,50,12}
e = set('Rama  rAo')
print(e) # {'R','A','a','m',' ','r','o'}
print(set(25)) # Error becoz  argument  should  be  sequence
print(set()) # Returns  an  empty  set



'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
