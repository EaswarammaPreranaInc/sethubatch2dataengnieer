# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True] 
a = input('Enter  list  :  ')   #   [25,10.8,'Hyd',True]
print(type(a))  #  <class 'str'>
print(a)  #  [25,10.8,'Hyd',True]
b = eval(a) 
print(b)  #  [25, 10.8, 'Hyd', True]
print(type(b))  #  <class 'list'>


#  Find  outputs 
a = [10, 20, 15, 18]
b = a
print(a  is  b)  # True : a and b refer to the same object
print(a  ==  b)  # True
b[2] = 12  #  Value at index 2 is changed from 15 to 12
print(a)  #  [10, 20, 12, 18]

#  Find  outputs  
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)  #  [10, 20, 15, 18, 100, 200, 150]
#print(a + 5) # cannot concatenate list and int
#print(a + '5')  # connot concatenate list and str
#print([10 , 20] + (30 , 40))  #  error : cannot concatenate list and tuple


#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))  #  [1,2,3] and prints address of 'a'
a += b  #  concatenates b to a 
print(a , id(a))  #  [1, 2, 3, 4, 5, 6] and prints address of 'a'


#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))  # [1,2,3] and prints address of 'a'
a = a+b  #  concatenates b to a
print(a , id(a))  #  [1,2,3,4,5,6] and prints address of 'a'


# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e)  #  [25, 10.8, 'Hyd', True]
print(type(e))  #  <class 'list'>

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b))  #  <class 'list'>
x , *y = list  #  x takes first element  25 and *y takes all remaining elements [10.8, 'Hyd', True]
print('x : ' , x)  #  x : 25
print('y : ' , y)  #  y: [10.8, 'Hyd']
*p , q = list  #  q takes last element  True and *p takes everything before last  [25, 10.8, 'Hyd']
print('p : ' , p)  #  p :  [25, 10.8, 'Hyd']
print('q : ' , q)  #  q :  True

# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list  # not enough values to unpack (expected 5,got 4)
a , b , *c , d , e = list 
print('a : ' , a)  # a :  25
print('b : ' , b)  # b :  10.8
print('c : ' , c)  # c :  []
print('d : ' , d)  # d :  Hyd
print('e : ' , e)  # e :  True
#a , b , *c , d , e , f = list # ValueError: not enough values to unpack (expected at least 5, got 4)


# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)  #  a :  25
print('b : ' , b)  # b :  10.8
print('_ :  ' , _)  #  _ :   Hyd
print('d : ' , d)  #  d :  True

# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)  # a :  (3+4j)
print('b : ' , b)  # b :  10.8
print('d : ' , d) # d :  True


# Find  outputs 
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)  #  a :  25
print('b : ' , b)  # b :  10.8
print('_ : ' , _)  # _ :  (3+4j)
print('d : ' , d)  #  d :  True
print('_: ' , _)  #  _:  (3+4j)

# Identify  error 
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
#a , *b , c , *d , e  = list  #  SyntaxError: multiple starred expressions in assignment

# Find  outputs 
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a)  #  a :   [25, 10.8]
print('b :  ' , b)  #  b :   Hyd
print('c :  ' , c)  #  c :   True

# Find  outputs  
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)  # a:25
print('b : ' , b) # b: 10.8
print('c : ' , c) # c: Hyd
print('d : ' , d)  # d: True
#a , b , c , d = list # ValueError:not enough values to unpack(expected 4, got 3)

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)  # True : The lists have the same elements in the same order
print(a  is   b)  #  # False: 'a' and 'b' refer to two different objects in memory
print(a < c)  # True: 15 < 25
print(a > d)  # True: 15 > 7
print(a >= c)  # False: 15 < 25
print(a <= d)  # False : 15 > 7
print(a != c)  # True 
print(a != b)  # False: The lists are equal because they have the same elements
print(a == c)  # False: The lists are not equal because they have different elements

# Comparing  Lists  
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False :a and b contain the same values but their elements are arranged in a different sequence
print(a  is   b)  # False