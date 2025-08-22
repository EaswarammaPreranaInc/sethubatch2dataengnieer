#index()  and  count()  methods 
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times'''

#  How  to  modify  an  element  of  tuple 
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 # tuple is immutable. so, we cannot add,remove or change elements
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # Address of 'a'
a=a[:2]+(35,)+a[3:]# modify  30  in  tuple  to  35
print(a) #  (10, 20, 35, 40, 50)
print(id(a)) # Address of 'a' which is diff from previous 'a'


# How  to  delete  an  element  of  tuple
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) # error
#del  a[2] # tuple object doesn't support item deletion
#a . pop(2) # tuple has no pop method
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # Address of tuple object (10, 20, 30, 40, 50)
#How  to  remove  30  from  tuple
b=list(a)
b.remove(30)
a=tuple(b)
print(a) # (10, 20, 40, 50)
print(id(a)) # Address of tuple object (10,20,40,50)

#  Nested   tuple
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) # (10,20 ) print  1st  inner  tuple
print(a[1]) # (30,40,50)  print  2nd  inner  tuple
print(a[2]) # (60,70,80,90)  print  3rd  inner  tuple
print(a[0][1]) # 20
print(a[1][2]) # 50
print(a[2][3]) # 90


# Find  outputs
a = ((10 , 20 , 30),)
print(a[0]) # (10, 20, 30)
print(*a) # (10, 20, 30)
print(a[0][0]) #   10
print(a[0][1]) #   20
print(a[0][2]) #  30
b = ((),)
print(b[0]) #   () :print  inner  tuple  of  tuple  'b'
print(*b) #  () :print  inner  tuple  of  tuple  'b'  


#  Find  outputs 
a = ((10 , 20 , 30))
print(a) # (10, 20, 30)
print(*a) # 10 20 30
b = (())
print(b) # ()
print(*b) # empty
'''
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #   {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # (18,20,10,12,15)
print(type(b)) # <class 'set'>
'''

#  Find  outputs
#print({(10 , 20 , 30)}) # Typeerror 
#print({[10 , 20 , 30]}) # TypeError
#print({{10 , 20 , 30}}) # Typeerror
#print({{}}) # Typeerror


# How  to  print  set  in  differnet ways 
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # {'Hyd', 10.8, 25, True}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
	print(x) 
'''
Hyd
10.8
25
True
'''


# Find  outputs
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {True, 'Hyd', 25}
print(len(s)) # 3
print(type(s)) # <class 'set'>


# Find  outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 'Hyd', 10.8, True}
a , b , c , d = s
print(a) # 25
print(b) # Hyd
print(c) # 10.8
print(d) # True


# Find  outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , *b = s
print(a) # 25
print(b) # [10.8, 'Hyd', True]
print(type(b)) # <class 'list'>


# Find  outputs  
s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True}
a , *b , c = s
print(a) # 25
print(b) # [10.8,'Hyd']
print(c) # True


# Find  outputs  
s = {20 , 10 , 20 , 10}
print(s) # {10,20}
x , y = s
print(x) # 10
print(y) # 20


# set()  function  
a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e) # {'A', 'o', 'r', 'a', ' ', 'm', 'R'}
#print(set(25)) # 25 is non sequence
print(set()) # set()


