# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')[10,20,30,40]
print(type(a)) #class list
print(a) #[10,20,30,40]
b = eval(a)
print(b) #[10,20,30,40]
print(type(b)) #class list
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)#false
print(a  ==  b)#true
b[2] = 12 
print(a)#[10, 20, 15, 18]

#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)#[10 , 20 , 15 , 18 , 100 , 200 , 150]
print(a + 5)#error sequence and interger
print(a + '5')#invalid type of operands
print([10 , 20] + (30 , 40))#invalid type of operands

#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a))#1000 [1,2,3]
a += b
print(a , id(a))#new list 2000 [1,2,3,4,5,6]

#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) #[1,2,3] 1000
a  = a + b
print(a , id(a))#new list[1,2,3,4,5,6] 2000

# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e)#[25,10.8,'Hyd',True]
print(type(e))#class list
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b))# class list
x , *y = list 
print('x : ' , x) #25
print('y : ' , y) #[10.8,'Hyd',True]
*p , q = list
print('p : ' , p) #[25,10.8,'Hyd']
print('q : ' , q) #True
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list #gives error because no enough values to unpack
a , b , *c , d , e = list 
print('a : ' , a) #25
print('b : ' , b) #10.8
print('c : ' , c) #[]
print('d : ' , d) #'Hyd'
print('e : ' , e) #True
a , b , *c , d , e , f = list #error

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ :  ' , _)#'Hyd'
print('d : ' , d)#True

# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)#25 
print('b : ' , b)#10.8
print('d : ' , d)#too many values to unpack

#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ : ' , _) #'Hyd'
print('d : ' , d) #True
print('_: ' , _) #error because _ can use only once

# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a) #[25 , 10.8]
print('b :  ' , b) #'Hyd'
print('c :  ' , c) #True

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #[25]
print('b : ' , b) #[10.8]
print('c : ' , c) #'Hyd'
print('d : ' , d) # True
a , b , c , d = list #[[[25],[10.8],'Hyd',True]

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #true
print(a  is   b) # False
print(a < c) # True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #false

# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #false
print(a  is   b) #false
