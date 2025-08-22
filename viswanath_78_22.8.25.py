a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
try:
    i = a.index(15)
    while True:
        print('15 is found at index : ' , i)   # 15 is found at index :  2
                                               # 15 is found at index :  5
                                               # 15 is found at index :  8
        i = a.index(15 , i + 1)
except:
    print(f'15 is found {a.count(15)} times')  # 15 is found 3 times

a  =  10 ,  20 ,  30 ,  40 ,  50
#     0      1       2       3      4
a[2] = 35   # Error: tuple does not support item assignment
print(a)      # (10, 20, 30, 40, 50)
print(id(a))  # some id 
a = a[:2] + (35,) + a[3:]  # How to modify 30 in tuple to 35
print(a)      # (10, 20, 35, 40, 50)
print(id(a))  # new id 

a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
# a.remove(30)  # Error: tuple object has no attribute 'remove'
# del a[2]      # Error: tuple does not support item deletion
# a.pop(2)      # Error: tuple object has no attribute 'pop'
print(a)        # (10, 20, 30, 40, 50)
print(id(a))    # some id (original tuple)
a = a[:2] + a[3:]  # How to remove 30 from tuple 'a'
print(a)        # (10, 20, 40, 50)
print(id(a))    # new id (different from original tuple)

a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90)
print(type(a)) # <class tuple>
print(len(a)) #3
print(a[0])#print(How  to  print  1st  inner  tuple)
print(a[1])#print(How  to  print  2nd  inner  tuple)
print(a[2])#print(How  to  print  3rd  inner  tuple)
print(a[0][1])#print(How  to  print  20)
print(a[1][2])#print(How  to  print  50)
print(a[2][3])#print(How to print 90)

a = ((10 , 20 , 30),)
print(a[0])#print(How  to   print  inner  tuple)
print(*a)#print(How  to   print  inner  tuple  in  another  way)
print(a[0][0])#print(How   to  print   10)
print(a[0][1])#print(How   to  print   20)
print(a[0][2])#print(How   to  print   30)
b = ((),)
print(b[0])#print(How  to   print  inner  tuple  of  tuple  'b')
print(*b)#print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

a = ((10 , 20 , 30))
print(a)    # (10, 20, 30)
print(*a)   # 10 20 30
b = (())
print(b)    # ()
print(*b)   # ‘’

What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter Set : ')   # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)                    # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))              # <class 'str'>
b = eval(a)
print(b)                    # {10, 12, 15, 18, 20}
print(type(b))              # <class 'set'>

print({(10 , 20 , 30)})   # {(10, 20, 30)}
print({[10 , 20 , 30]})   # Error: list is unhashable, cannot be inside set
print({{10 , 20 , 30}})   # Error: set is unhashable, cannot be inside set
print({{}})               # Error: dict is unhashable, cannot be inside set

a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # set  with  print  function
print(a) #25 , True , 'Hyd' , 10.8, order may change
print('Iterate  elements  of  set  with  for  loop')#Iterate  elements  of  set  with  for  loop
for i in a:
    print(i) #How  to  iterate  set  with  for  loop

a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)        # {'Hyd', True, 25}   (duplicates removed, order may change)
print(len(s))   # 3
print(type(s))  # <class 'set'>
s = {'Hyd', 25, True, 10.8}
print(s)        # {'Hyd', 25, True, 10.8}  (order may change)
a, b, c, d = s
print(a)        # Hyd
print(b)        # 25
print(c)        # True
print(d)        # 10.8

s = {'Hyd', 25, True, 10.8}
print(s)        # {'Hyd', 25, True, 10.8}  (order may change)
a, *b = s
print(a)        # Hyd
print(b)        # [25, True, 10.8]
print(type(b))  # <class 'list'>

s = {'Hyd', 25, True, 10.8}
print(s)        # {'Hyd', 25, True, 10.8}  (order may change)
a, *b = s
print(a)        # Hyd
print(b)        # [25, True, 10.8]
print(type(b))  # <class 'list'>

s = {'Hyd', 25, True, 10.8}
print(s)          # {'Hyd', 25, True, 10.8}  (order may change)
a, *b, c = s
print(a)          # Hyd
print(b)          # [25, True]
print(c)          # 10.8

s = {20, 10, 20, 10}
print(s)      # {10, 20}   (duplicates removed, order may change)
x, y = s
print(x)      # 10
print(y)      # 20

a = range(100 , 151 , 10)
b = set(a)
print(b)        # {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)        # {10, 12, 15, 18, 20, 50}  (duplicates removed, order may change)
e = set('Rama  rAo')
print(e)        # {'m', 'o', ' ', 'R', 'r', 'a', 'A'}  (characters as set, order may change)
print(set(25))  # Error: 'int' object is not iterable
print(set())    # set()
print(set())    # set()
