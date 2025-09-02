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
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35                                                               Error
print(a)                                                                (10,20,30,40,50)
print(id(a))                                                            140534410434112
How  to  modify  30  in  tuple  to  35                                  a = a[:2] + (35,) + a[3:]
print(a)                                                                (10, 20, 35, 40, 50)
print(id(a))                                                            140534410435264

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)                                   Error
del  a[2]                                        Error
a . pop(2)                                       Error
print(a)                                         (10,20,30,40,50)                                        
print(id(a))                                     140728918233600
How  to  remove  30  from  tuple  'a'            a = a[:2] + a[3:]
print(a)                                         (10,20,40,50)
print(id(a))                                     140728918233920

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)                                                            ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))                                                      <class 'tuple'>
print(len(a))                                                       3
print(How  to  print  1st  inner  tuple)                            print(a[0])
print(How  to  print  2nd  inner  tuple)                            print(a[1])
print(How  to  print  3rd  inner  tuple)                            print(a[2])
print(How  to  print  20)                                           print(a[0][1])
print(How  to  print  50)                                           print(a[1][2])
print(How  to  print  90)                                           print(a[2][3])

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)                                                print(a[0])
print(How  to   print  inner  tuple  in  another  way)                              print(a[-1])
print(How   to  print   10)                                                         print(a[0][0])
print(How   to  print   20)                                                         print(a[0][1])
print(How   to  print   30)                                                         print(a[0][2])
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')                                print(b[0])
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)              print(b[-1])

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)                                 (10, 20, 30)
print(*a)                                10 20 30
b = (())
print(b)                                 ()
print(*b)

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)                                                                                  {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))                                                                            <class 'str'>
b = eval(a)
print(b)                                                                                  {10, 12, 15, 18, 20}
print(type(b))                                                                            <class 'set'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})                                 {(10, 20, 30)}
print({[10 , 20 , 30]})                                 Error
print({{10 , 20 , 30}})                                 Error
print({{}})                                             Error

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
for item in a:
        print(item)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)                           {'Hyd', True, 25}
print(len(s))                       3
print(type(s))                     <class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                               {'Hyd', 25, 10.8, True}
a , b , c , d = s
print(a)                               Hyd
print(b)                               25
print(c)                               10.8                           
print(d)                               True

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                                 {'Hyd', 25, 10.8, True}
a , *b = s
print(a)                                 Hyd
print(b)                                 [25, 10.8, True]
print(type(b))                           <class 'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                                   {'Hyd', 25, 10.8, True}
a , *b , c = s
print(a)                                   Hyd
print(b)                                   [25, 10.8]
print(c)                                   True

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)                           {10, 20}
x , y = s
print(x)                           10
print(y)                           20

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)                                                              {100, 130, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)         
print(d)                                                              {50, 18, 20, 10, 12, 15}
e = set('Rama  rAo')
print(e)                                                              {'m', 'R', 'o', ' ', 'A', 'a', 'r'}
print(set(25))                                                        Error
print(set())                                                          set()
