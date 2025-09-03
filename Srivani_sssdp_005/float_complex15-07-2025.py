# float  object  demo  program (Home  work)
a = 10.8 # Ref 'a' points to object 10.8
print(a) # Value of object 'a' i.e., 10.8
print(type(a)) # Type of object 'a' i.e., <class float>
print(id(a)) # Address of object 10.8
b = 25. # Ref 'b' points to object 25.
print(b) # Value of object 'b' i.e., 25.0
print(type(b)) # Type of object 'a' i.e., <class float>
c = .689 # Ref 'c' points to object .689
print(c) # Value of object 'c' i.e., 0.689
d = 3.4E2 # Ref 'd' points to object 3.4E2
print(d) # Value of object 'd' i.e., 340.0
print(type(d)) # Type of object 'a' i.e., <class float>
e = 9.62e-2 # Ref 'e' points to object 9.62e-2
print(e) # Value of object 'e' i.e., 0.0962
print(9.8.2) # Error because double decimal is not allowed or float can't have more than one decimal point



# complex object demo program
a = 3 + 4j # Ref 'a' points to object 3 + 4j
print(a) # prints the value of object 'a' i.e., (3 + 4j)
print(type(a)) # Type of object 'a' i.e., <class 'complex'>
print(id(a)) # prints address of the object 'a'
print(a . real) # prints real part of the object 3 + 4j i.e., 3.0
print(a . imag) # prints imaginary part of the object 3 + 4j i.e., 4.0
print(type(a . real)) # prints type of real part of the object 'a' i.e., <class 'float'>
print(type(a . imag)) # prints type of imaginary part of the object 'a' i.e., <class 'float'>



# Find outputs (Home work)
a = 6j # ref 'a' points to object 6j
print(a) # Value of object 'a' i.e., 6j
print(type(a)) # Type of object 'a' i.e., <class 'complex'>
print(a.real) # prints real value of the object 6j i.e., 0.0
print(a.imag) # prints imaginary value of the object 6j i.e., 6.0
print(5 + j6) # Error because j should be right side of the digit
print(3 + 4i)  # Error because python does not support 'i' as imaginary value.it only supports 'j'
print(4+j) # Error because 'j' should be followed by a digit
print(4 + 1j) # prints (4 + 1j)
print(4 + 0j) # prints (4 + 0j)



# bool object demo program  (Home  work)
a = True # Ref 'a' points to object True
print(a) # Value of object 'a' i.e., True
print(type(a)) # Type of object a' i.e., <class 'bool'>
print(id(a)) # Address of object True
b = False # Ref 'b' points to object False
print(b) # Value of object 'b' i.e., False
print(type(b)) # Type of object 'b' i.e., <class 'bool'>
print(True + True) # prints 2 because True is treated as 1 
print(True + False) # prints 1 because True is treated as 1 and False is treated as 0
print(False + True) # prints 1
print(False + False) # prints 0
print(True + True + True) # prints 3
print(25 + 10.8 + True) # prints 36.8
print(True > False) # prints True because 1 > 0
print(True) # prints true
print(False) # prints False
print(true) # Error because True is a keyword and T must be in uppercase
print(false) # Error because False is a keyword and F must be in uppercase



# Find  outputs (Home  work)
a = 0O6247 # Ref 'a' points to object decimal equivalent 3239
print(a) # Value of object 'a' i.e., 3239
print(type(a)) # Type of object 'a' i..e, <class 'int>
print(id(a)) # prints address of object 3239
b = 0o6247 # Ref 'b' points to same object 0o6247
print(id(b))  # prints same address of object 3239
print(b) # Value of object 'b' i.e., 3238
c = 3239 # Ref 'c' points to same object 3239
print(c) # Value of object 'c' i.e., 3239
print(id(c))  # prints same address of object 3239
print(0o9248) # Error because it is octal so it should not contain 9 and 8,it must contain from 0 to 7



# Find  outputs  (Home  work)
a = 0XA7B9 # Ref 'a' points to object decimal equivalent 42937
print(a) # prints the value of object 'a' i.e.,42937
print(type(a)) # prints type of object i.e., <class 'int'>
b = 0xBEEF # Ref 'b' points to object decimal equivalent 48879
print(b) # prints the value of object 'a' i.e., 48879
print(A7B9) # Error because number should be followed by 0X, because it is hexadecimal
print('A7B9') # prints 'A7B9'
print(0XBEER) # Error because it is hexadecimal,it cannot contain 'R'
print(0XHYD) # Error because it is hexadecimal, it cannot conatain 'H' and 'Y'
print(0xA7G9B) # Error because it is hexadecimal, it cannot conatain 'G'



# Find outputs (Home  work)
a = 9248 # Ref 'a' points to object 9248
print(a) # prints the value of object 'a' i.e., 9248
print(type(a)) # Type of object 'a' i.e., <class 'int'>