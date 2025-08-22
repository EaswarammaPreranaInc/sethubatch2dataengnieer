1.
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i) #15 is found at index :2<next line>15 is found at index :5<nextline>
                                                        15 is found at index : 8 <next line>
		i = a . index(15 , i + 1)     
except:
		print(F'15  is  found  {a . count(15)}  times')  #15  is  found 3 times

2.
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35   #error: item assignment is not possible in tuple because tuple is immutable
print(a)   #(10,20,30,40,50)
print(id(a)) #address of tuple
#How  to  modify  30  in  tuple  to  35 --> using slicing and concatenate method
a=(a[:2])+(35,)+(a[3:])  #using slicing of tuple and then concatenating a new element 35
print(a)
print(id(a)) #address of new tuple


3.
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) #we get error as tuple doesn't support item deletion as it is immutable
del  a[2]   #we get error as tuple doesn't support item deletion as it is immutable
a . pop(2) #we get error as tuple doesn't support item deletion as it is immutable
print(a)   #(10 , 20 , 30 , 40 , 50)
print(id(a))  #address of tuple
#How  to  remove  30  from  tuple  'a'--> using slice method and concatenation
a=a=(a[:2])+(a[3:5])
print(a)   #(10, 20, 40, 50)
print(id(a))   #133004532434240


4.
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)  #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  #<class 'tuple'>
print(len(a))   #3
print(How  to  print  1st  inner  tuple) #a[0]
print(How  to  print  2nd  inner  tuple)  #a[1]
print(How  to  print  3rd  inner  tuple)  #a[2]
print(How  to  print  20)   #a[0][1]
print(How  to  print  50)   #a[1][2]
print(How  to  print  90)   #a[2][3]


5.
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)  #print(a[0])
print(How  to   print  inner  tuple  in  another  way)  #print(a[-1])
print(How   to  print   10)  #print(a[0][0])
print(How   to  print   20)  #print(a[0][1])
print(How   to  print   30)  #print(a[0][2])
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')  #print(a[0])
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)  #print(a[-1])



6.
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)  #(10,20,30)
print(*a)  #unpacks tuple 10 20 30
b = (())
print(b)  #()
print(*b)  #unpacks b we get empty line as there is nothing inside the tuple(empty tuple)


7.
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')  #giving values {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)  #input function will create any given value to string hence {10 , 20 , 15 , 18 , 20 , 12 , 18} becomes string
print(type(a)) #<class 'str'>
b = eval(a)  #eval({10 , 20 , 15 , 18 , 20 , 12 , 18})--> eval of string {10 , 20 , 15 , 18 , 20 , 12 , 18} eval function turns string {10 , 20 , 15 , 18 , 20 , 12 , 18} to respective obj that is set
print(b)  #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b))  #<class 'set'>


8.
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})  #{(10,20,30)}
print({[10 , 20 , 30]})  #error lists are mutable
print({{10 , 20 , 30}})  # error sets are mutable
print({{}})  #dictionary is mutable


9.
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop


10.
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #{25, True, 'Hyd', 10.8}
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop   #for x in a:
						print(x) 
#25
10.8
Hyd
True  we get set elements in unordered as set is unordered


11.
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}  
print(s)  #{25, True, 'Hyd'}  1 and 'Hyd' are ignored because we already have True and 'Hyd', set ignores duplicates
print(len(s))  #3
print(type(s))  #<class 'set'>

12.
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)   #{'Hyd',  25,  True,  10.8 }not sure if we get elements in same order
a , b , c , d = s
print(a)  #'Hyd'
print(b)  #'25'
print(c)  #True
print(d)  #10.8


13.
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  #unordered elements {'Hyd', 10.8, 25, True}
a, *b = s #{'Hyd', [10.8, 25, True]}
print(a) Hyd
print(type(a)) #<class 'str'>
print(b)   #[10.8, 25, True]
print(type(b))  #<class 'list'>



14.
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 } can be in different format like 25 in first place and True in second
a , *b , c = s  #{'Hyd',[25, True],10.8}
print(a)  #Hyd
print(b)  #[25, True]
print(c)  #10.8


15.
s = {20 , 10 , 20 , 10}
print(s)  #{20,10} removes duplicates and may not be in same order
x , y = s  #20,10 = s
print(x)  #20
print(y)  #10


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)  #100 110 120 130 140 150
b = set(a)  #set(100 110 120 130 140 150)-->{100, 110, 120, 130, 140, 150}
print(b)  #{100, 110, 120, 130, 140, 150} can not expect in same order because set is unordered
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)  #set([10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18])-->removed duplicated and we get ordered {10, 20, 15, 18, 12, 50}
print(d)  #{10, 20, 15, 18, 12, 50} could be different because it is unordered
e = set('Rama  rAo') 
print(e) #{'a', 'R', 'm', ' ', 'A', 'o', 'r'} not in ordered
print(set(25))  #error, set of sequence is not possible
print(set())  #set()

