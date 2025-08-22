#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25) # tuple obj
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i) # 2 5 8
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times') # 15 is found 3 times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50 # tuple obj
#     0      1       2       3      4
a[2] = 35 # error 
print(a) # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # address of obj 'a'
a = a[:2] + (35,) + a[3:] # How  to  modify  30  in  tuple  to  35
print(a) (10 ,  20 ,  35 ,   40 ,  50)
print(id(a)) # new address of tuple


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50 # tuple obj
#    0     1      2     3      4
a . remove(30) # error no remove method in tuple
del  a[2] # error
a . pop(2) # error
print(a) # (10 , 20 , 30 , 40 , 50)
print(id(a)) # address of tuple
a = a[:2] + (45,) + a[3:] # How  to  remove  30  from  tuple  'a'
print(a) # (10 , 20 , 45 , 40 , 50)
print(id(a)) # new address


#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) ) # nested tuple
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) # How  to  print  1st  inner  tuple
print(a[1]) # How  to  print  2nd  inner  tuple
print(a[2]) # How  to  print  3rd  inner  tuple
print(a[0][1]) # How  to  print  20
print(a[1][2]) # How  to  print  50
print(a[2][3]) # How  to  print  90


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) # How  to   print  inner  tuple
print(*a) # How  to   print  inner  tuple  in  another  way
print(a[0][0]) # How   to  print   10
print(a[0][1]) # How   to  print   20
print(a[0][2]) # How   to  print   30
b = ((),)
c,=b # unpacking tuple
print(b[0]) # How  to   print  inner  tuple  of  tuple  'b')
print(c) # How  to   print  inner  tuple  of  tuple  'b'  in  another  way


#  Find  outputs (Home  work)
a = ((10 , 20 , 30)) # tuple obj
print(a) # (10 , 20 , 30)
print(*a) # 10  20  30
b = (()) # tuple obj
print(b) # ()
print(*b) # ()


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ') # it reads string input
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a) # # ref a is assigned to b
print(b) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b)) # <class 'set'>


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10 , 20 , 30)}--set of tuple
print({[10 , 20 , 30]}) # error
print({{10 , 20 , 30}}) # error
print({{}}) # error


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8} # set obj
print('set  with  print  function')
print(a) # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
-- for i in a:
	print(i)



# Find  outputs  (Home  work)
a = 'Hyd' # str obj
b = True # bool obj
c = 25 # int obj
d = 1 # int obj
e = 'Hyd' # str obj
s = {a , b , c , d , e} # set packing
print(s) # {'Hyd', True, 25, 1}
print(len(s)) # 4
print(type(s)) # <class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } # set obj
print(s) # {'Hyd',  25,  10.8, True }
a , b , c , d = s # packing of set elements 
print(a) # Hyd
print(b) # 25
print(c) # 10.8
print(d) # True


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 } # set obj
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s # unpacks elements
print(a) # Hyd
print(b) # [25, True, 10.8]
print(type(b)) # <class 'list'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , *b , c = s # unpacks elements
print(a) # 25
print(b) # [10.8, 'Hyd']
print(c) # True


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10} # set obj
print(s) # {20 , 10}
x , y = s # unpacks elements
print(x) # 20
print(y) # 10


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10) # range obj
b = set(a) # 'a' is converted to set 
print(b) # (100,110,120,130,140)--unordered way
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18] # list obj
d = set(c) # list converted to set
print(d) # (10 , 20 , 15 , 18 , 50 , 12)
e = set('Rama  rAo') # str converted to set
print(e) # {'A', 'o', 'm', 'r', 'R', 'a', ' '}
print(set(25)) # error
print(set()) # set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''