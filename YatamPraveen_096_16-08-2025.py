# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))				#<class 'str'>
print(a)				#[25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b)				#[25, 10.8, 'Hyd', True]
print(type(b))				#<class 'list'>




#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)			#True
print(a  ==  b)			#True
b[2] = 12
print(a)			#[10, 20, 12, 18]





#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)                    #[10, 20, 15, 18, 100, 200, 150]
print(a + 5)                    #Returns error as a list and an integer can't be concatenated.
print(a + '5')                  #Returns error as a list and an string can't be concatenated.
print([10 , 20] + (30 , 40))    #Returns error as a list and a tuple can't be concatenated.





#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))        #[1, 2, 3] <address where [1, 2, 3] is stored>
a += b
print(a , id(a))        #[1, 2, 3, 4, 5, 6] <same address as in previous output as list objects are mutable.





#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))        #[1, 2, 3] <address where [1, 2, 3] is stored>
a  = a + b
print(a , id(a))        #[1, 2, 3, 4, 5, 6] <address where [1, 2, 3, 4, 5, 6] is stored(This is because in case of a=a+b, a is reassigned not modified as in previous code)>





# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e)            #[25, 10.8, 'Hyd', True]
print(type(e))      #<class 'list'>





# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b))          #<class 'list'>
x , *y = list
print('x : ' , x)       #x : 25
print('y : ' , y)       #y : [10.8, 'Hyd', True]
*p , q = list
print('p : ' , p)       #p : [25, 10.8, 'Hyd']a
print('q : ' , q)       #q : True





# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list        #This causes an error as the number of list elements are less than the variables on the left.
a , b , *c , d , e = list
print('a : ' , a)               #a : 25
print('b : ' , b)               #b : 10.8
print('c : ' , c)               #c : []
print('d : ' , d)               #d : Hyd
print('e : ' , e)               #e : True
a , b , *c , d , e , f = list   #This causes error as the number of elements in list are less than the variables on the left. 





# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)       #a : 25
print('b : ' , b)       #b : 10.8
print('_ : ' , _)       #_ : Hyd
print('d : ' , d)       #d : True





# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)       #a : 3+4j
print('b : ' , b)       #b : 10.8
print('d : ' , d)       #d : True





#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)       #a : 25
print('b : ' , b)       #b : 10.8
print('_ : ' , _)       #_ : 3+4j
print('d : ' , d)       #d : True
print('_: ' , _)        #_ : 3+4j





# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , d , e  = list     #There can only be one variable with *





# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a)      #a : [25, 10.8]
print('b :  ' , b)      #b : Hyd
print('c :  ' , c)      #c : True





# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)           #a :25 
print('b : ' , b)           #b : 10.8
print('c : ' , c)           #c : Hyd
print('d : ' , d)           #d : True
a , b , c , d = list        #This causes error as the list here contains 3 elements but we're trying to unpack them into 4 variables.





# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)       #True
print(a  is   b)    #False
print(a < c)        #True
print(a > d)        #True
print(a >= c)       #False
print(a <= d)       #False
print(a != c)       #True
print(a != b)       #False
print(a == c)       #False





# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)           #False
print(a  is   b)        #False