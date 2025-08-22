#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
OUTPUT:-
------------
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15 is found 3 times
----------------------------------
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4

a[2] = 35
print(a) # 10,20,30,40,50
print(id(a)) # address of (10,20,30,40,50)

Q ) How  to  modify  30  in  tuple  to  35
a = (10, 20, 30, 40, 50)
# Convert tuple to list
temp = list(a)
temp[2] = 35  # Change 30 to 35

# Convert back to tuple
a = tuple(temp)
print(a) # (10,20,35,40,50)
print(id(a)) # address of (10,20,35,40,50)
-------------------------------
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4

a . remove(30)
del  a[2]
a . pop(2)
print(a) # 10,20,30,40,50
print(id(a)) # address of (10,20,30,40,50)

Q)How  to  remove  30  from  tuple  'a'

a = (10, 20, 30, 40, 50)

# Convert tuple to list
temp_list = list(a)

# Remove 30
temp_list.remove(30)

# Convert back to tuple
a = tuple(temp_list)
print(a)

print(a) # (10,20,40,50)
print(id(a)) # address of (10,20,40,50)
-------------------------------------------
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #  ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(How  to  print  1st  inner  tuple) # a[0]
print(How  to  print  2nd  inner  tuple) # a[1]
print(How  to  print  3rd  inner  tuple) # a[2]
print(How  to  print  20) # a[0][1]
print(How  to  print  50) # a[1][2]
print(How  to  print  90) # a[2][3]
-------------------------------------------
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple) # a[0]
print(How  to   print  inner  tuple  in  another  way) 
print(How   to  print   10) # a[0][0]
print(How   to  print   20) # a[0][1]
print(How   to  print   30) # a[0][2]
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b') # print(b[0])
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way) # b = ((),)
												(inner,) = b
												print(inner)
---------------------------------------------
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10,20,30)
print(*a) # 10 20 30 
b = (())
print(b) # ()
print(*b)
--------------------------
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #  {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {18, 20, 10, 12, 15}
print(type(b)) # <class 'set'>
------------------------------
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10, 20, 30)}
print({[10 , 20 , 30]}) # error
print({{10 , 20 , 30}}) # error
print({{}}) # error
---------------------------------
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #  {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop # for element in a:
    							   print(element)
-----------------------------------
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd', True, 25}
print(len(s)) # 3
print(type(s)) # <class 'set'>
------------------------------------
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a) # Hyd
print(b) # 25
print(c) # True
print(d) # 10.8
---------------------------
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd', 25, True, 10.8}
a , *b = s
print(a) # 'Hyd'
print(b) # [25 , True , 10.8]
print(type(b)) # <class 'list'>
--------------------------------
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #  {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) # Hyd
print(b) # [25,True]
print(c) # 10.8
--------------------------------
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20, 10}
x , y = s
print(x) # 20
print(y) # 10
---------------------------
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {100, 130, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e) # {'r', 'R', 'm', 'a', ' ', 'A', 'o'}
print(set(25)) # error
print(set()) # ()


