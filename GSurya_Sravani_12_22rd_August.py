# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#tuple class
a[3] = 'Sec'#error
a[3 : 6] = 60 , 70 , 80#error


#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3),address of tuple object 
a += b
print(a , id(a))#(1,2,3,4,5,6), address of new tuple


#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3),address of tuple object
a = a + b
print(a , id(a))#(1,2,3,4,5,6), another address of tuple a

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)#(10 , 20 , 30 , 40)
print(type(a))#tuple class
b = eval(a)
print(b)#tuple class
print(type(b))#tuple class
print(len(b))#4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a)#error

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)# [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)# [10 , [80 , 90],(20 , 30 , 40) , 50 , 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'hyd',true)
print(type(x))#tuple class

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#hyd
print(d)#true
p , q , r =  x#error
a , b , c , d  , e = x#error

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[25,10.8'hyd']
print(c)#true

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)25
print(b)10.8
print(c)#[hyd,' ',' ']
print(d)#true
print(e)#error


# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#hyd
print(d)#true
print(_)#3+4j


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#tuple class
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e)#('v','a','m','s','i')
print(tuple(25))#error
print(tuple())#()