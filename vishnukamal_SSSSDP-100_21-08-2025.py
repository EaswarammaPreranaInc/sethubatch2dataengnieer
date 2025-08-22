
# Find  outputs   (Home  work)

a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)# output: (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))# output: <class 'tuple'>
a[3] = 'Sec' # Error as tuple is immutable can't be modified
a[3 : 6] = 60 , 70 , 80 # Error as tuple is immutable can't be modified



# 1) Find  outputs

a = (1,2,3)
b = (4,5,6)
print(a , id(a))# output: (1, 2, 3) address of tuple object 'a'
a += b
print(a , id(a))# output: (1, 2, 3, 4, 5, 6) address of new tuple object 'a'



# 2) Find  outputs

a = (1,2,3)
b = (4,5,6)
print(a , id(a))# output: 1, 2, 3) address of tuple object 'a'
a = a + b
print(a , id(a))# output: (1, 2, 3, 4, 5, 6) address of new tuple object 'a'



# 3) What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)

a = input('Enter  Tuple  :  ')
print(a)# output: (10, 20, 30, 40)
print(type(a))# output: <class 'str'>
b = eval(a)
print(b)# output: (10, 20, 30, 40)
print(type(b))# output: <class 'tuple'> 
print(len(b))# output: 4



# 4) Find  outputs  (Home  work)

a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)# output: (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] # Error as tuple is immutable can't be modified
print(a)



# 5) Find  outputs  (Home  work)

a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 # Error as tuple is immutable can't be modified
print(a)
a[1] = [80 , 90]
print(a)# output: [10, [80, 90], 50, 60]



# 6) Find  outputs   (Home  work)

a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d # tuple packing
print(x)# output: (25, 10.8, 'Hyd', True)
print(type(x))# output: <class 'tuple'>



# 7) Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x # tuple unpacking
print(a)# output: 25
print(b)# output: 10.8
print(c)# output: 'Hyd'
print(d)# output: True
p , q , r =  x # error as tuple elements are excess to unpack 
a , b , c , d  , e = x # error as tuple elements are fewer to unpack



# 8) Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x # tuple unpacking
print(a)# output: 25
print(b)# output: [10.8,'Hyd'] 
print(c)# output: True



# 9) Find  outputs   (Home  work)

tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)# output: 25
print(b)# output: 10.8
print(c)# output: []
print(d)# output: 'Hyd'
print(e)# output: True



# 10) Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)# output: 25
print(b)# output: 10.8
print(_)# output: 3 + 4j 
print(d)# output: True
print(_)# output: 3 + 4j
 


# 11) tuple()  function  demo  program   (Home  work)

a = range(100 , 150 , 10)
b = tuple(a)# range object is converted to tuple
print(b)# output: (100,110,120,130,140)
print(type(b))# output: <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)# list is converted to tuple
print(d)# output: (10 , 20 , 15, 18)
e = tuple('Vamsi')# str is converted to tuple
print(e)# output: ('V', 'a', 'm', 's', 'i')
print(tuple(25))# error as tuple() fuction argument should has sequence only
print(tuple())# output: () empty tuple