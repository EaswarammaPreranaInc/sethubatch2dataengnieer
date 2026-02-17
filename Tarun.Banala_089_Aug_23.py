#Tarun Banala      23-08-2025                                                                                                                                                                    #index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10 
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
'''output:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times'''

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 # error
print(a) # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # address 1 
b=list(a)
b[2]=35
a=tuple(b)
print(a)
print(id(a))

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) #error
#del  a[2] # error
#a . pop(2) # error
print(a) # (10 , 20 , 30 , 40 , 50)
print(id(a)) # adress of tuple
b=list(a) 
b.remove(30)
a=tuple(b)
print(a) # (10 , 20 , 40 , 50)
print(id(a)) # 140140673926464

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #  ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])
print(*a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(a[0])
print(*a)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) # (10, 20, 30)
print(*a) # (10, 20, 30)
print(a[0][0]) # 10
print(a[0][1]) # 20
print(a[0][2]) # 30
b = ((),)
print(a[0]) # (10,20,30)
print(*a) # (10,20,30)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10,20,30)
print(*a) # 10 20 30
b = (())
print(b) # ()
print(*b) #

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class  'str'>
b = eval(a) 
print(b) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b)) # <class 'set'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})
print({[10 , 20 , 30]}) # error
print({{10 , 20 , 30}}) # error
print({{}}) # error

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(set(a)) # {25 , True , 'Hyd' , 10.8}
print(a) # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
    print(x)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd',True,25} in any order
print(len(s)) # 3
print(type(s)) # <class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , b , c , d = s
print(a) # Hyd
print(b) # 25
print(c) # True
print(d) # 10.8



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # Hyd
print(b) # [25 ,True ,10.8 ]
print(type(b)) # <class 'list'>


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , *b , c = s 
print(a) # Hyd
print(b) # [{25,  True}]
print(c) # 10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {10,20}
x , y = s 
print(x) # 10
print(y) # 20


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e) # {'R', 'A', 'm', ' ', 'a', 'o', 'r'}
print(set(25)) # error non sequence
print(set()) # set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
