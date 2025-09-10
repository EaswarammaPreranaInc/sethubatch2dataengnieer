
# 1) index()  and  count()  methods  demo  program   (Home  work)

a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0   1    2    3    4    5    6    7   8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
'''
# Output: 
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8 
15 is found at 3 times 
'''



# 2) How  to  modify  an  element  of  tuple ?    (Home  work)

a  =  10 ,  20 ,  30 ,   40 ,  50
#     0     1     2     3      4
a[2] = 35 # Error as we cannot the modify the tuple because tuple is immutable
print(a) # Output: (10, 20, 30, 40, 50)
print(id(a)) # Output: Address of tuple object (10, 20, 30, 40, 50)
a=a[:2]+(35,)+a[3:]# How  to  modify  30  in  tuple  to  35
print(a) # Output: (10, 20, 35, 40, 50)
print(id(a)) # Output: Address of new tuple object (10, 20, 35, 40, 50)




# 3) How  to  delete  an  element  of  tuple ?   (Home  work)

a  = 10 , 20 , 30 , 40 , 50
#    0    1    2    3    4
a . remove(30) # Error as tuple is immutable it does not has remove method
del  a[2] # Error as we cannot the delete the tuple elements because tuple is immutable
a . pop(2) # Error as tuple is immutable it does not has pop method
print(a) # Output: (10, 20, 30, 40, 50
print(id(a)) # Output: Address of tuple object (10, 20, 30, 40, 50)
a=a[:2]+a[3:] # How  to  remove  30  from  tuple  'a' # Output:
print(a) # Output:(10, 20, 40, 50)
print(id(a)) # Output: Address of new tuple object (10, 20, 40, 50)




# 4) Nested   tuple  (Home  work)

a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # Output: ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # Output: <class 'tuple'>
print(len(a)) # Output: 3
print(a[0]) # How  to  print  1st  inner  tuple # Output: (10, 20)
print(a[1]) # How  to  print  2nd  inner  tuple # Output: (30, 40, 50)
print(a[2]) # How  to  print  3rd  inner  tuple # Output: (60, 70, 80, 90)
print(a[0][1]) # How  to  print  20 # Output: 20
print(a[1][2]) # How  to  print  50 # Output: 50
print(a[2][3]) # How  to  print  90 # Output: 90




# 5) Find  outputs  (Home  work)

a = ((10 , 20 , 30),)
print(a[0]) # How  to   print  inner  tuple # Output: (10 , 20 , 30) 
print(*a) # How  to   print  inner  tuple  in  another  way # Output: (10 , 20 , 30)
print(a[0][0]) # How   to  print   10 # Output: 10 
print(a[0][1]) # How   to  print   20 # Output: 20
print(a[0][2]) # How   to  print   30 # Output: 30
b = ((),)
print(b[0]) # How  to   print  inner  tuple  of  tuple  'b' # Output: ()
print(*b) # How  to   print  inner  tuple  of  tuple  'b'  in  another  way # Output: ()



# 6) Find  outputs (Home  work)

a = ((10 , 20 , 30))
print(a) # Output: (10 , 20 , 30)
print(*a) # Output: 10 , 20 , 30
b = (()) 
print(b) # Output: ()
print(*b) # Output: empty



# 7) What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}

a = input('Enter  Set  :  ')
print(a) # Output: {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # Output: <class 'str'>
b = eval(a) # string is converted to set
print(b) # Output: {18, 20, 10, 12, 15}
print(type(b)) # Output: <class 'set'> 



# 8) Find  outputs  (Home  work)

print({(10 , 20 , 30)}) # Output: {(10, 20, 30)}
print({[10 , 20 , 30]}) # Error as set elements should be only immutable object not mutable object[list]
print({{10 , 20 , 30}}) # Error as set elements should be only immutable object not mutable object{set}
print({{}}) # Error as set elements should be only immutable object not mutable object {}




# 9) How  to  print  set  in  differnet ways  (Home  work)

a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # Output: 
print(a) # Output: {25, 'Hyd', 10.8, True}
print('Iterate  elements  of  set  with  for  loop')
for i in a:
	print(i)# How  to  iterate  set  with  for  loop
''' 
# Output: 
25
Hyd
10.8
True
'''


# 10) Find  outputs  (Home  work)

a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # Output: {True, 'Hyd', 25}
print(len(s)) # Output: 3
print(type(s)) # Output: <class 'set'>



# 11) Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # Output: {25, 'Hyd', 10.8, True}
a , b , c , d = s
print(a) # Output: 25
print(b) # Output: 'Hyd'
print(c) # Output: 10.8 
print(d) # Output: True




# 12) Find  outputs  (Home  work)

s = {'Hyd', 25, True, 10.8 }
print(s) # Output: {'Hyd', 25, True, 10.8 }
a , *b = s
print(a) # Output: 'Hyd'
print(b) # Output: [25, True, 10.8 ]
print(type(b)) # Output: <class 'list'>



# 13) Find  outputs  (Home  work)

s = {'Hyd', 25, True, 10.8 }
print(s) # Output: {'Hyd', 25, True, 10.8 }
a , *b , c = s
print(a) # Output: 'Hyd'
print(b) # Output: [25, True]
print(c) # Output: 10.8




# 14) Find  outputs  (Home  work)

s = {20 , 10 , 20 , 10}
print(s) # Output: {10, 20}
x , y = s
print(x) # Output: 10
print(y) # Output: 20




# 15) set()  function  demo  program  (Home  work)

a = range(100 , 151 , 10)
b = set(a) # range object is converted to set
print(b) # Output: {100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) # list object is converted to set 
print(d) # Output: {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo') # string object is converted to set
print(e) # Output: {'R','a','m','a',' ','r','A','o'}
print(set(25)) # Error as set() fuction argument should be sequence only
print(set()) # Error as set() fuction argument should be sequence only


