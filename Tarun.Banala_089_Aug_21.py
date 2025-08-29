#Tarun Banala  21-08-2025

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#100,110,120,103,140
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10,20,15,18)
e = tuple('vamsi')
print(e)#('V','a','m','s','i')
#print(tuple(25))#no becoz argument sholud be sequence only
print(tuple())
 #  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3),Address of a
a += b#a is added to b and pointing to new object 
print(a , id(a))#(1,2,3,4,5,6),address of new obj
#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3), Address of a
a = a + b#a is pointing to obj that is a+b
print(a , id(a))#(1,2,3,4,5,6),Adderess of a+b
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')#(10,20,30,40)
print(a)#(10,20,30,40)
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10,20,30,40)
print(type(b))#<class 'tuple'>
print(len(b))#4
 # Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70#tuple is cant be modified
print(a)#(10 , [20 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]#tuple is cant be modified
print(a)
 # Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'Hyd',True)
print(type(x))#<class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#'Hyd'
print(d)#True
#p , q , r =  x# excess no of values
#a , b , c , d  , e = x# not enough values
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8,True]
print(c)#'Hyd'
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#10.8
print(d)#True
print(e)#not enough values
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#100,110,120,103,140
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10,20,15,18)
e = tuple('vamsi')
print(e)#('V','a','m','s','i')
#print(tuple(25))#no becoz argument sholud be sequence only
print(tuple())
