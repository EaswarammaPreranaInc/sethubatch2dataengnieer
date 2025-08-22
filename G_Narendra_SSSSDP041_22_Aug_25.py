#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
    i = a . index(15)
    while  True:
        print('15 is found at index : ' , i)    # 15 is found at index :  2 , 15 is found at index :  5 , 15 is found at index :  8
        i = a . index(15 , i + 1)
except:
    print(F'15  is  found  {a . count(15)}  times')   # 15  is  found  3  times


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
a[2] = 35      # error: 'tuple' object does not support item assignment
print(a)       # not executed
print(id(a))   # not executed


# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
a . remove(30)    # AttributeError: 'tuple' object has no attribute 'remove'
del  a[2]         # TypeError: 'tuple' object does not support item deletion
a . pop(2)        # AttributeError: 'tuple' object has no attribute 'pop'
print(a)          # not executed
print(id(a))      # not executed


#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)             # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))       # <class 'tuple'>
print(len(a))        # 3
print(a[0])          # (10, 20)
print(a)          # (30, 40, 50)
print(a)          # (60, 70, 80, 90)
print(a)       # 20
print(a)       # 50
print(a)       # 90


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a)     # (10, 20, 30)
print(a[-1])    # (10, 20, 30)
print(a)  # 10
print(a)  # 20
print(a)  # 30
b = ((),)
print(b)     # ()
print(b[-1])    # ()


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)      # (10, 20, 30)
print(*a)     # 10 20 30
b = (())
print(b)      # ()
print(*b)     # (nothing printed)


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')          # Enter  Set  :  {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)                             # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))                       # <class 'str'>
b = eval(a)
print(b)                             # {10, 12, 15, 18, 20}
print(type(b))                       # <class 'set'>


#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})     # {(10, 20, 30)}
print({[10 , 20 , 30]})     # TypeError: unhashable type: 'list'
print({{10 , 20 , 30}})     # TypeError: unhashable type: 'set'
print({{}})                 # set()


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')  # set  with  print  function
print(a)                             # {25, True, 'Hyd', 10.8}
print('Iterate  elements  of  set  with  for  loop')   # Iterate  elements  of  set  with  for  loop
for i in a: print(i)   # Elements printed one by one, order random


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)        # {25, True, 'Hyd'}
print(len(s))   # 3
print(type(s))  # <class 'set'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)            # {'Hyd', 25, True, 10.8}
a , b , c , d = s
print(a)            # one element (order random)
print(b)            # one element (order random)
print(c)            # one element (order random)
print(d)            # one element (order random)


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)        # {'Hyd', 25, True, 10.8}
a , *b = s
print(a)        # one element (random)
print(b)        # remaining 3 elements in list
print(type(b))  # <class 'list'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)        # {'Hyd', 25, True, 10.8}
a , *b , c = s
print(a)        # one element (random)
print(b)        # middle elements in list
print(c)        # one element (random)


# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)        # {10, 20}
x , y = s
print(x)        # 10  (or 20, order not guaranteed)
print(y)        # 20  (or 10, order not guaranteed)


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)       # {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)       # {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e)       # {'m', 'r', ' ', 'R', 'a', 'A', 'o'}
print(set(25)) # TypeError: 'int' object is not iterable
print(set())   # set()
