# 22/08/2025 HOME WORK QUESTION

######################################

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

#######################

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35 # ERROR 
print(a) # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # class < tuple >
How  to  modify  30  in  tuple  to  35
print(a) # a[:2]
print(id(a))

##########################

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))

################

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(How  to  print  1st  inner  tuple)
print(How  to  print  2nd  inner  tuple)
print(How  to  print  3rd  inner  tuple)
print(How  to  print  20)
print(How  to  print  50)
print(How  to  print  90)

######################
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)
print(How  to   print  inner  tuple  in  another  way)
print(How   to  print   10)
print(How   to  print   20)
print(How   to  print   30)
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

####################

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)

################

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))

########################

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})
print({[10 , 20 , 30]})
print({{10 , 20 , 30}})
print({{}})

########################
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop

############################

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))

####################

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)

##################
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))

#############################

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)

###############

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
print(set(25))
print(set())


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''

