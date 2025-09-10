
-----------------------------------------  LAMBDA FUNCTIONS QUESTIONS  05/09/2025 part 1


# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100

-------------------------

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) #49
print( lambda   x  :  x * x(7)) # ERROR
print( lambda   x  :   x * x) # ERROR
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x
print(square(5)) # 25

--------------------------------

# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments # add = lambda a,b : a+b
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) #31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # 8+10j
print(add(10 , '20')) # error
print(add()) # error
print(add) # error prints functions object not result

-----------------------------------------

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3
----------------------------------------

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30 
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # error 

----------------------------------------

#  Find  outputs (Home  work)
How  to  define  lambda  to  determine  largest  of  two  arguments # large = lambda a,b: a if a>b else b
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) #10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False)) # True
---------------------------------------

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.06
print(power()) # 12.25
print(power(9)) # 81

------------------------------------------

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # <class 'Tuple'>
print(x) # 17, 3 , 70 , 1.42
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7
print(r) #18
print(s) #1.42
