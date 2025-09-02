# home work 16/08/2025
# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')
print(type(a))
print(a)
b = eval(a)
print(b)
print(type(b))
###
a = input('Enter list : ')
print(type(a)) # <class 'str'>
print(a) # [25, 10.8, 'Hyd', True]
b = eval(a)
print(b) # [25, 10.8, 'Hyd', True]
print(type(b)) # <class 'list'>

---------------------------------------------
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)
print(a  ==  b)
b[2] = 12
print(a)

##
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)  # True
print(a  ==  b)  # True
b[2] = 12
print(a)  # [10, 20, 12, 18]

---------------------------------------------
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) # [10 , 20 , 15 , 18, 100 , 200 , 150]
print(a + 5) # error
print(a + '5')# error we can't concatenate str
print([10 , 20] + (30 , 40)) # error can't add tuple and list 

-------------------------------------------------------

#  Tricky  program
#  Find  outputs
a = [1,2,3]
b = [4,5,6]
print(a , id(a)) #  [1, 2, 3] 
a += b
print(a , id(a)) # [1, 2, 3, 4, 5, 6]

-------------------------------------------------------

a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e) # [25, 10.8, 'Hyd', True]
print(type(e)) # <class 'list'>

-----------------------------------------------------
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)  # a :  25
print('b : ' , b) # b : [10.8 , 'Hyd']
print('c : ' , c) # c :  True
print(type(b)) # <class 'list'>
x , *y = list
print('x : ' , x) # x :  25
print('y : ' , y) # y : [10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) # p : [25, 10.8, 'Hyd']
print('q : ' , q) # q :  True

-----------------------------------------------------
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # ValueError: not enough values to unpack (expected 5, got 4)
a , b , *c , d , e = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('c : ' , c) # c : []
print('d : ' , d) # d : Hyd
print('e : ' , e) # e : True
a , b , *c , d , e , f = list # ValueError:

-----------------------------------------------------
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) # a : 25
print('b : ' , b) # b : 10.8
print('_ :  ' , _) # _ :  Hyd
print('d : ' , d) # d : True

-----------------------------------------------------
