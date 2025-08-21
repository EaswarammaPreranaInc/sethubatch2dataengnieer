#1st prgm
# Find  outputs   (Home  work)

a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#<class'tuple'>
#a[3] = 'Sec' #Error,becoz tuple is immutable
#a[3 : 6] = 60 , 70 , 80 #Error,becoz tuple is immutable

#2nd prgm
#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3) some random address(say 1000)
#a += b #Error ,tuple is immutable
print(a , id(a)) #(1,2,3) same address(say 1000)

#3rd prgm
#  Find  outputs
a = (1,2,3)
b = (4,5,6)
print(a , id(a))#(1,2,3) some random address(say 1000)
a = a + b #reference is changed to (a+b)
print(a , id(a))#(1,2,3,4,5,6)

#4th prgm
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') #(10,20,30,40)
print(a)#(10,20,30,40)
print(type(a))#<class'str'>
b = eval(a)
print(b)#(10,20,30,40)
print(type(b))#<class'tuple'>
print(len(b))#4

#5th prgm
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 #valid ,becoz  inner list can be modified
print(a)#(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]
print(a)#10 , [80 , 90 , 100] , 50 , 60)

#6th prgm
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70#error,becoz tuple is immutable
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
#a[1] = [80 , 90]#error
print(a)#[10 , (20 , 30 , 40) , 50 , 60]

#7th prgm
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,"Hyd",True)
print(type(x))#<class'tuple'>

#8th prgm
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#Hyd
print(d)#True
#p , q , r =  x # error,few elements to unpack
#a , b , c , d  , e = x # error,excess elements to unpack

#9th prgm
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8,'Hyd']
print(c)#True

#10th prgm
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#Hyd
print(e)#True

#11th prgm
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#(3+4j)
print(d)#True
print(_)#(3+4j)

#12th prgm
# tuple()  function  demo  prgm
#   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#<class'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10,20,15,18)
e = tuple('Vamsi')
print(e)#('v','a','m','s','i')
#print(tuple(25))#error,argument cannot be a non-sequence
print(tuple())#()
