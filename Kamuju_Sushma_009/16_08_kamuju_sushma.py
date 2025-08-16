#Home Work-1
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a)) # <class 'string'>
print(a) #[25 , 10.8 , 'Hyd' , True] (as a string)
b = eval(a) 
print(b) #[25 , 10.8 , 'Hyd' , True] (as a list)
print(type(b)) #<class 'list'>

#Home Work-2
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12 
print(a) #[10,20,15,18]

#Home Work-3
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
print(a + 5)#error, '+' between sequence and non sequence is not possible
print(a + '5') #error, list sequence and string sequence cannot be concatinated like this
print([10 , 20] + (30 , 40)) #error, list and tuple cannot be concatinated

#Home Work-4
#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) #[1,2,3], 1000 (say address of obj [1,2,3] is 1000)
a += b 
print(a , id(a)) #[1,2,3,4,5,6], 1000 (list is mutable so existing object will be modified instead creating a new one)

#Home Work-5
#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) #[1,2,3], 1000 (say the address of object [1,2,3] is 1000)
a  = a + b #new list object is created and reference 'a' is updated
print(a , id(a)) #[1,2,3,4,5,6], 2000 

#Home Work-6
# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e) #[25, 10.8, 'Hyd', True]
print(type(e)) #<class 'list'>

#Home Work-7
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  #  a :  25
print('b : ' , b) #  b : [10.8 , 'Hyd']
print('c : ' , c) #  c :  True
print(type(b)) #<class 'list'>
x , *y = list 
print('x : ' , x) #x : 25
print('y : ' , y) #y: [10.8, 'Hyd', True]
*p , q = list 
print('p : ' , p)#p: [25,10.8,'Hyd']
print('q : ' , q)#q: True

#Home Work-8
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list #error, lhs 5 ref are present but list have only 4 elements
a , b , *c , d , e = list ##error, lhs 5 ref are present but list have only 4 elements
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list

#Home Work-9
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a: 25
print('b : ' , b)#b: 10.8
print('_ :  ' , _)#_: 'Hyd'
print('d : ' , d)#d: True

#Home Work-10
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #a: 3+4j
print('b : ' , b)#b: 10.8
print('d : ' , d) #d: True

#Home Work-11
#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)#a: 25
print('b : ' , b)#b: 10.8
print('_ : ' , _)#_: 3+4j
print('d : ' , d)#d: True
print('_: ' , _)#_: 3+4j

#Home Work-12
# Identify  error (Home  work)
# list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
# a , *b , c , *d , e  = list #cannot use more than 1 '*' in a single unpacking assignment

#Home Work-13
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]   #  Nested  list
a , b , c = list
print('a :  ' , a)#a: [25,10.8]
print('b :  ' , b)#b: 'Hyd'
print('c :  ' , c)#c: True

#Home Work-14
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)#a: 25
print('b : ' , b)#b: 10.8
print('c : ' , c)#c: 'Hyd'
print('d : ' , d)#d: True
a , b , c , d = list #error

#Home Work-15
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b)#False
print(a < c)#True
print(a > d)#True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#False

#Home Work-16
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False