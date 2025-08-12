# float  object  demo  program (Home  work)
a = 10.8 # reference 'a' is assigned to float class object 10.8
print(a) # 10.8
print(type(a)) # <class 'float'>
print(id(a)) # prints address of object 
b = 25. # reference b is assigned to integer class object 25
print(b)# prints 25
print(type(b))# prints type of the object <class 'int'>
c = .689 # ref c is pointed to float class object
print(c)# 0.689
d = 3.4E2 # reference d is assigned to float class object
print(d) # prints mantissa-exponent number 3.4E2
print(type(d)) # print type of the object <class 'float'>
e = 9.62e-2# reference 'e' is assigned to float class object 
print(e)# prints 9.62e-2
print(9.8.2)# error ,invalid syntax

# complex object demo program
a = 3 + 4j # reference 'a' is pointed to complex class object
print(a)# prints 3 + 4j
print(type(a)) # <class  'complex'>
print(id(a))# prints address of object
print(a . real)# 3.0 is real number
print(a . imag)# 4.0 is imaginary number
print(type(a . real))# <class 'float'>
print(type(a . imag))#<class 'float'>


# Find outputs (Home work)
a = 6j # reference 'a' is assigned to complex class object
print(a)# prints 6j
print(type(a))# <class 'complex'>
print(a.real)# 0.0
print(a.imag)# 6.0
print(5 + j6) # error because j should be after the number
print(3 + 4i)# error because python only supports j as imaginary not i  
print(4+j)# prints 4 + j
print(4 + 1j) # prints 4 + 1j
print(4 + 0j)# prints 4+0j


# bool object demo program  (Home  work)
a = True # reference 'a' is pointed to bool class object
print(a) # True
print(type(a)) # <class 'bool'>
print(id(a)) # prints address of bool object
b = False # reference 'b' is pointed to bool class object
print(b) # False
print(type(b)) # <class 'bool'>
print(True + True) # 1 + 1 =2
print(True + False) # 1
print(False + True)# 1
print(False + False)# 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False)# True
print(True)# True
print(False) # False
print(true) # error
print(false) # error


# Find  outputs (Home  work)
a = 0O6247 # ref 'a' is assigned to int class object, object is decimal equivalent
print(a) # prints decimal number
print(type(a)) #<class 'int'>
print(id(a)) # prints address of the 'a' 
b = 0o6247 # octal integer 
print(id(b)) # prints address of 'b'
print(b)# prints decimal number
c = 3239 # ref 'c' is pointed to int class object
print(c) # 3239
print(id(c)) # prints address of 'c'
print(0o9248) # prints decimal number


# Find  outputs  (Home  work)
a = 0XA7B9 # ref 'a' is pointed to int class object
print(a) # prints decimal number
print(type(a)) # <class 'int'>
b = 0xBEEF# object is hexa decimal integer
print(b) # prints decimal number
print(A7B9) # error
print('A7B9')# A7B9
print(0XBEER)# invalid syntax
print(0XHYD)# invalid syntax
print(0xA7G9B)# invalid syntax

# Find outputs (Home  work)
a = 9248 # reference 'a' is assigned to int class object 
print(a) # 9248
print(type(a)) # <class 'int'>