#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

##1
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15  is  found  3  times
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))
# Output:
a = (10, 20, 30, 40, 50)
a = a[:2] + (35,) + a[3:]
print(a)

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
# Output:
a = (10, 20, 30, 40, 50)
print("Original:", a, "id =", id(a))

temp = list(a)   # convert tuple → list
temp.remove(30)  # remove element
a = tuple(temp)  # convert back

print("Modified:", a, "id =", id(a))
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))#<class 'tuple'>
print(len(a))#3
print(a[0])#(10, 20)
print(a[1])#(30, 40, 50)
print(a[2])#(60, 70, 80, 90)
print(a[0][1])#20
print([1][2])#50
print(a[2][3])#90
# Find  outputs  (Home  work)
a = ((10, 20, 30),)
print("Inner tuple:", a[0])# (10, 20, 30) 
print("Inner tuple (another way):", a[-1])# (10, 20, 30)
print("10:", a[0][0])# 10
print("20:", a[0][1])# 20
print("30:", a[0][2])# 30

b = ((),)# (10, 20, 30), (40, 50, 60)
print("Inner tuple of b:", b[0])# (10, 20, 30)
print("Inner tuple of b (another way):", b[-1])# (10, 20, 30)

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)# (10, 20, 30)
print(*a)# (10, 20, 30)
b = (())
print(b)# ()
print(*b)# ()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)# {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))# <class 'str'>
b = eval(a)# {10, 20, 15, 18, 12}
print(b)# {10, 20, 15, 18, 12}
print(type(b))# <class 'set'>

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})# {(10, 20, 30)}
print({[10 , 20 , 30]})# TypeError
print({{10 , 20 , 30}})# TypeError
print({{}})# TypeError
##
a = {25, True, 'Hyd', 10.8}

print("Set with print function:")
print(a)

print("Iterate elements of set with for loop:")
for x in a:
    print(x)
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)# {True, 1, 25, 'Hyd'}
print(len(s))# 4
print(type(s))# <class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd', 25, 10.8, True}
a , b , c , d = s
print(a)# Hyd
print(b)# True
print(c)# 25
print(d)# 10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd', 25, 10.8, True}
a , *b = s
print(a)# Hyd
print(b)# {True, 25, 10.8}
print(type(b))# <class 'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd', 25, 10.8, True}
a , *b , c = s
print(a)# Hyd
print(b)# [True, 25]
print(c)# 10.8

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)# {10, 20}
x , y = s
print(x)# 10
print(y)# 20

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)# {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)# {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e)# {'a', ' ', 'm', 'o', 'R', 'r'}
print(set(25))# TypeError
print(set())# set()

