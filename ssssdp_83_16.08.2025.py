Input:
[25 , 10.8 , 'Hyd' , True]

Code:
a = input('Enter  list  :  ')
print(type(a))     # <class 'str'>
print(a)           # [25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b)           # [25, 10.8, 'Hyd', True]
print(type(b))     # <class 'list'>

Output:
<class 'str'>
[25 , 10.8 , 'Hyd' , True]
[25, 10.8, 'Hyd', True]
<class 'list'>

#############

Input:
[25 , 10.8 , 'Hyd' , True]

Code:
a = input('Enter  list  :  ')
print(type(a))     
print(a)           
b = eval(a)
print(b)           
print(type(b))     

Output:
<class 'str'>
[25 , 10.8 , 'Hyd' , True]
[25, 10.8, 'Hyd', True]
<class 'list'>

#############
Code:
a = [10, 20, 15, 18]
b = a
print(a is b)
print(a == b)
b[2] = 12
print(a)

Output:
True
True
[10, 20, 12, 18]

##########
Code:
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)
print(a + 5)
print(a + '5')
print([10 , 20] + (30 , 40))

Output:
[10, 20, 15, 18, 100, 200, 150]
TypeError: can only concatenate list (not "int") to list
TypeError: can only concatenate list (not "str") to list
TypeError: can only concatenate list (not "tuple") to list

##########
Code:
a = [1,2,3]
b = [4,5,6]
print(a , id(a))
a += b
print(a , id(a))

Output:
[1, 2, 3] <some_id>
[1, 2, 3, 4, 5, 6] <same_id>

########
Code:
a = [1,2,3]
b = [4,5,6]
print(a , id(a))
a  = a + b
print(a , id(a))

Output:
[1, 2, 3] <some_id>
[1, 2, 3, 4, 5, 6] <different_id>

##########
Code:
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e)
print(type(e))

Output:
[25, 10.8, 'Hyd', True]
<class 'list'>

#########
Code:
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  
print('b : ' , b) 
print('c : ' , c) 
print(type(b))
x , *y = list
print('x : ' , x)
print('y : ' , y)
*p , q = list
print('p : ' , p)
print('q : ' , q)

Output:
a :  25
b :  [10.8, 'Hyd']
c :  True
<class 'list'>
x :  25
y :  [10.8, 'Hyd', True]
p :  [25, 10.8, 'Hyd']
q :  True

#######

Code:
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list

Output:
ValueError: not enough values to unpack (expected 5, got 4)

############
Code:
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)
print('b : ' , b)
print('_ :  ' , _)
print('d : ' , d)

Output:
a :  25
b :  10.8
_ :   Hyd
d :  True


#########

Code:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)
print('b : ' , b)
print('d : ' , d)

Output:
a :  (3+4j)
b :  10.8
d :  True

########

Code:
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)
print('b : ' , b)
print('_ : ' , _)
print('d : ' , d)
print('_: ' , _)

Output:
a :  25
b :  10.8
_ :  (3+4j)
d :  True
_:  (3+4j)

########

Code:
list = [[25 , 10.8] , 'Hyd' , True]   # Nested list
a , b , c = list
print('a :  ' , a)
print('b :  ' , b)
print('c :  ' , c)

Output:
a :   [25, 10.8]
b :   Hyd
c :   True

##########
Code:
list = [[25 , 10.8] , 'Hyd' , True]
[a

##########

Code:
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)
print(a is b)
print(a < c)
print(a > d)
print(a >= c)
print(a <= d)
print(a != c)
print(a != b)
print(a == c)

Output:
True        # a and b have same values
False       # a and b are different objects
True        # comparison goes element by element: 15 < 25
True        # comparison goes element by element: 15 > 7
False       # because at 3rd element: 15 < 25, so not >=
False       # because at 3rd element: 15 > 7, so not <=
True        # values differ at index 2 (15 vs 25)
False       # a and b are equal, so not !=
False       # a and c differ, so not equal

#########

Code:
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)
print(a is b)

Output:
False    # values are not equal (different order)
False    # a and b are two different objects
