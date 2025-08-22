# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #Returns the tuple of elements i.e (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) #Returns the type of object i.e <class 'tuple')
a[3] = 'Sec' #Error #we cannot modify tuple because tuple is immutable
a[3 : 6] = 60 , 70 , 80 #Error #slicing is also not possible



#  Find  outputs
a = (1,2,3) #Reference a points to tuple of elements
b = (4,5,6) #Reference b points to tuple of elements
print(a , id(a)) #Returns the tuple a and its address
a += b #Here we are concatinating the two tuples 
print(a , id(a)) #Returns the concatinated tuple and its id and id will not be same beacause now b points to concatinated tuple


#  Find  outputs
a = (1,2,3) #Reference a points to tuple of elements
b = (4,5,6) #Reference b points to tuple of elements
print(a , id(a)) #Returns the tuple a and address of a
a = a + b #Here we are assigning concatinated tuple where two tuples are concatinated and assigned to a 
print(a , id(a)) #Returns the concatinated tuple and address of that tuple



#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') #takes the str as input (10 , 20 , 30 , 40)
print(a) #Returns the str tuple of elements i.e (10 , 20 , 30 , 40)
print(type(a)) #Retunns the type of object a i.e <class 'str'>
b = eval(a) #str a is converted to tuple and reference b points to converted tuple
print(b) #Returns the tuple of elements
print(type(b)) #Returns the type of object b i.e <class 'tuple'>
print(len(b)) #Returns the length of tuple b i.e 4



# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60) #Reference a points to tuple of elements and a list inside the tuple
a[1][0] = 70 #As we know list is mutable so we can modify the list which is inside the tuple i.e 20 is replaced with 70
print(a) #Returns the updated tuple i.e (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] #Error we cannot modify tuple
print(a) #Returns the tuple i.e (10 , [70 , 30 , 40] , 50 , 60)



# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60] #Reference a points to list of elements a tuple is present inside a list
a[1][0] = 70 #Error #We cannot modify tuple because tuple is immutable
print(a) #Returns the list i.e [10 , (20 , 30 , 40) , 50 , 60] 
a[1] = [80 , 90] #Here index a[1] tuple is replaced with [80 , 90]
print(a) #Returns the updated list i.e [10, [80, 90], 50, 60]



 # Find  outputs   (Home  work)
a = 25 #Reference a points to int object 25
b = 10.8 #Reference b points to float object 10.8
c = 'Hyd' #Reference c points to str object 'Hyd'
d = True #Reference d points to bool object True
x = a , b , c , d #All the abcd is converted to tuple of elements 
print(x) #Returns the tuple of elements i.e (25, 10.8, 'Hyd', True)
print(type(x)) #Returns the type of object x i.e <class 'tuple'>



 # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True #Reference x points to tuple of elements as , is mandatory to create a tuple 
a , b , c , d = x #Here each element in the tuple assigned to a b c d i.e a = 25 b = 10.8 c = 'Hyd' d = True #Tuple unpacking 
print(a) #Returns the value of a i.e a = 25
print(b) #Returns the value of a i.e b = 10.8
print(c) #Returns the value of a i.e c = 'Hyd'
print(d) #Returns the value of a i.e d = True
p , q , r =  x #Error there are not enough references to pack
a , b , c , d  , e = x #Error there are not enough values to pack




# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True #Reference x points to list of elements
a , *b , c = x #Tuple unpacking is done i.e a = 25 and *b = 10.8 , 'Hyd' and c = True
print(a) #Reference a points to value 25
print(b) #Reference *b points to value 10.8 and 'Hyd'
print(c) #Reference c points to value True



# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True #Reference tpl points to tuple of elements
print(tpl)
a , b , *c , d , e = tpl #Error #References a = 25 b = 10.8 c = [] d = 'Hyd' e = True
print(a) #a = 25
print(b) #b = 10.8
print(c) #c = []
print(d) #d = 'Hyd'
print(e) #e = True



# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j #Reference x points to tuple of elements
a , b , _ , d , _= x #Tuple is unpacked i.e a = 25 b = 10.8 _ = 'Hyd'  d = True _ = 3+4j
print(a) #a = 25
print(b) #b = 10.8
print(_) #_ = 'Hyd'
print(d) #d = True 
print(_) #_ = 3+4j



 # tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10) #Reference a points to range from 100 to 150 in steps of 10
b = tuple(a) #Here range object is converted to tuple object
print(b) #Returns the tuple object i.e (100, 110, 120, 130, 140)
print(type(b)) #Returns the type of b i.e <class 'tuple'>
c = [10 , 20 , 15, 18] #Reference c points to list of elements 
d = tuple(c) #Here list is converted to tuple
print(d) #Returns the (10, 20, 15, 18) of elements
e = tuple('Vamsi') #here str 'vamsi' is converted tuple 
print(e) #Returns tuple i.e ('V', 'a', 'm', 's', 'i')
print(tuple(25)) #Error #int object cannot be converted 
print(tuple()) #Returns the empty tuple


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  ---> Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''