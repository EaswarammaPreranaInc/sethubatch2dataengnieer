#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4    5    6    7    8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)   
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
		
''' output is as follows
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15  is  found  3  times  '''





#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1    2       3     4
#a[2] = 35                       #This throws error as tuple is immutable
print(a)                        #(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))                    #Address of tuple a
a = a[:2] + (35, ) + a[3:]#How  to  modify  30  in  tuple  to  35
print(a)                        #(10 ,  20 ,  35 ,   40 ,  50)
print(id(a))                    #Address of new tuple





# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1    2    3    4
a . remove(30)              #This throws error as tuple is immutable
del  a[2]                   #This throws error as tuple is immutable
a . pop(2)                  #This throws error as tuple is immutable
print(a)                    #(10 , 20 , 30 , 40 , 50)
print(id(a))                #Address of tuple a
a =  a[:2] + a[3:]          #How  to  remove  30  from  tuple  'a'
print(a)                    #(10 , 20 , 40 , 50)
print(id(a))                #Address of this new tuple





#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)                #( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(type(a))          #<class 'tuple'>
print(len(a))           #3
print(a[0])             #How  to  print  1st  inner  tuple)
print(a[1])             #How  to  print  2nd  inner  tuple)
print(a[2])             #How  to  print  3rd  inner  tuple)
print(a[0][1])          #How  to  print  20)
print(a[1][2])          #How  to  print  50)
print(a[2][3])          #How  to  print  90)





# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])             #How  to   print  inner  tuple)
print(*a)               #How  to   print  inner  tuple  in  another  way)
print(a[0][0])          #How   to  print   10)
print(a[0][1])          #How   to  print   20)
print(a[0][2])          #How   to  print   30)
b = ((),)
print(b[0])             #How  to   print  inner  tuple  of  tuple  'b')
print(*b)               #How  to   print  inner  tuple  of  tuple  'b'  in  another  way)





# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])             #How  to   print  inner  tuple)
print(*a)               #How  to   print  inner  tuple  in  another  way)
print(a[0][0])          #How   to  print   10)
print(a[0][1])          #How   to  print   20)
print(a[0][2])          #How   to  print   30)
b = ((),)
print(b[0])             #How  to   print  inner  tuple  of  tuple  'b')
print(*b)               #How  to   print  inner  tuple  of  tuple  'b'  in  another  way)





#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)                #(10, 20, 30)
print(*a)               #10, 20, 30
b = (())
print(b)                #()
print(*b)               #





# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)                    #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))              #<class 'str'>
b = eval(a)
print(b)                    #{10 , 20 , 15 , 12 , 18}
print(type(b))              #<class 'set'>





#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})         #{(10 , 20 , 30)}
print({[10 , 20 , 30]})         #Throws error as set can't have mutable elements
print({{10 , 20 , 30}})         #Throws error as set can't have mutable elements
print({{}})                     #Throws error as set can't have mutable elements





# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') #set  with  print  function
print(a)                            # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')#Iterate  elements  of  set  with  for  loop
for i in a:                         #How  to  iterate  set  with  for  loop
    print(i)





# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)                    #{'Hyd', True, 25}
print(len(s))               #3
print(type(s))              #<class 'set'>





# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                            #{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)                            #Hyd
print(b)                            #25
print(c)                            #True
print(d)                            #10.8





# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                        #{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)                        #Hyd(or any other set element)
print(b)                        #[list of 3 remaining elements]
print(type(b))                  #<class 'list'>





# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                #{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)                #one of the set element example 'Hyd'
print(b)                #list of two elements example [25, True]
print(c)                #remaining element of the set example 10.8





# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)                #{20 , 10} or {10, 20}
x , y = s
print(x)                #20 or 10
print(y)                #10, or 20





# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)            #{100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)            #{10, 20, 15, 18, 50, 12}
e = set('Rama  rAo')
print(e)            #{'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(set(25))      #Throws error as set(non sequence) is not valid
print(set())        #set()