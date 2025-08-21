1.
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , (3 + 4j) , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))  #<class 'tuple'>
a[3] = 'Sec'   #error, tuple is immutable
a[3 : 6] = 60 , 70 , 80   #error, tuple is immutable

2.
a = (1,2,3)
b = (4,5,6)
print(a , id(a))  #(1,2,3)  address of (1,2,3)
a += b  #a=a+b = a=(1,2,3)+(4,5,6) = (1,2,3,4,5,6)
print(a , id(a)) #(1,2,3,4,5,6) address of (1,2,3,4,5,6)

3.
a = (1,2,3)
b = (4,5,6)
print(a , id(a))  #(1,2,3)  address of (1,2,3)
a = a + b    #a=a+b = a=(1,2,3)+(4,5,6) = (1,2,3,4,5,6)
print(a , id(a))  #(1,2,3,4,5,6) address of (1,2,3,4,5,6)


4.
a = input('Enter  Tuple  :  ')  #input function converts tuple into string
print(a)  #(10 , 20 , 30 , 40) now is a string
print(type(a))  #<class 'str'>  
b = eval(a)   #converts string to tuple 
print(b)   #(10 , 20 , 30 , 40)  is now a tuple
print(type(b))   #<class 'tuple'>
print(len(b))  #4  which is (10 , 20 , 30 , 40)


5.
a = (10 , [20 , 30 , 40] , 50 , 60)  #tuple with a list inside it
a[1][0] = 70
print(a)  #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] #element in tuple is immutable we get error
print(a)  #error


6.
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)  #error, tuple is immutable
a[1] = [80 , 90]
print(a)  #[10 ,[80 , 90] , 50 , 60]


7.
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25, 10.8, 'Hyd', True) #In Python, writing values separated by commas automatically creates a tuple.
print(type(x))  #<class 'tuple'>


8.
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True  #In Python, writing values separated by commas automatically creates a tuple.
a , b , c , d = x
print(a) #25
print(b)  #10.8
print(c)  #'Hyd'
print(d)  #True
p , q , r =  x #error x has 4 values but we gave only 3
a , b , c , d  , e = x #error x has 4 values but we gave 5


9. 
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True  #In Python, writing values separated by commas automatically creates a tuple.
a , *b , c = x
print(a) #25
print(b)  #[10.8, 'Hyd']  *b collects items as list
print(c)  #True


10.
tpl = 25 , 10.8 , 'Hyd' , True  #it is a tuple as it is with commas and is a group of elements
a , b , *c , d , e = tpl #there are only 4 elements in tpl, but we have got 5 to assign
print(a)  #25
print(b)  #10.8
print(c)  #[] empty list as we don't have any other element to assign to *c
print(d)  #'Hyd'
print(e)  #True


11.
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j #is a tuple
a , b , _ , d , _= x 
print(a)  #25
print(b)  #10.8
print(_)  #(3+4j)  #Hyd will be overwritten as _ is present twice 
print(d)  #True
print(_)  #(3+4j)  #if _ is appeared again, the latest value will overwrite


12.
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)  # 100 110  120  130  140
b = tuple(a)  #tuple(100 110  120  130  140)
print(b) #(100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18] 
d = tuple(c)  
print(d) #(10, 20, 15, 18)
e = tuple('Vamsi')  
print(e) #('V', 'a', 'm', 's', 'i')
print(tuple(25)) #error
print(tuple()) #()




