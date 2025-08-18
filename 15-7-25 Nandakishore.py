# float  object  demo  program (Home  work)
a = 10.8 # reference 'a' points to object 10.8
print(a) #prints the value of 'a' i.e.10.8
print(type(a))#Type of object 'a' is <class 'float'> 
print(id(a)) # Address of 'a'
b = 25. # reference 'b' points to object 25.0
print(b) #prints the value of 'b' i.e. 25.0
print(type(b)) #Type of object 'b' is <class 'float'> 
c = .689  # reference 'c' points to object 0.689
print(c) #prints the value of 'c' i.e.0.689
d = 3.4E2 # reference 'd' points to object 3.4E2
print(d)  #prints the value of 'd' i.e. 3.4x10^2
print(type(d)) #Type of object 'd' is <class 'float'> 
e = 9.62e-2 # reference 'd' points to object 9.62e-2
print(e)  #prints the value of 'e' i.e. 3.4x10^-2
print(9.8.2) #Error because float can have only one decimal point

------------------------------------------------------------------------

# complex object demo program
a = 3 + 4j  # reference 'a' points to object 3+4j
print(a) #prints the value of 'a' i.e. (3+4j)
print(type(a)) #Type of object 'a' is <class 'complex'>
print(id(a))  # Address of 'a'
print(a . real) #prints the value of real part of 'a' i.e. 3.0
print(a . imag) #prints the value of imag part of 'a' i.e. 4.0
print(type(a . real)) #Type of object a.real is <class 'float'>
print(type(a . imag)) #Type of object a.imag is <class 'float'>

------------------------------------------------------------------------

# Find outputs (Home work)
a = 6j  # reference 'a' points to object 6j
print(a) #prints the value of 'a' i.e.6j
print(type(a)) #Type of object 'a' is <class 'complex'>
print(a.real) #prints the value of real part of 'a' i.e.0
print(a.imag)  #prints the value of imag part of 'a' i.e. 6.0
print(5 + j6) #Error due to j should be after imag
print(3 + 4i) #Error due to i  
print(4+j) #Error due to imag part is missing
print(4 + 1j) #prints (4 + 1j)
print(4 + 0j) #prints (4+0j)

------------------------------------------------------------------------

# bool object demo program  (Home  work)
a = True # reference 'a' points to object True
print(a) #prints the value of 'a' i.e. True
print(type(a)) #Type of object 'a' is <class 'bool'>
print(id(a)) # Address of 'a'
b = False # reference 'b' points to object False
print(b) #prints the value of 'b' i.e. False
print(type(b)) #Type of object 'b' is <class 'bool'>
print(True + True) #prints 2 i.e.1+1=2
print(True + False) #prints 1 i.e.1+0=1
print(False + True) #prints 1 i.e.1+0=1
print(False + False) #prints 0 i.e.0+0=0
print(True + True + True) #prints 3 i.e.1+1+1=3
print(25 + 10.8 + True) #prints 36.8 i.e.25+10.8+1=36.8
print(True > False) #prints True as 1>0
print(True) #prints True
print(False)  #prints False
print(true) #Error due to 't'
print(false) #Error due to 'f'

-------------------------------------------------------------------------

# Find  outputs (Home  work)
a = 0O6247 # reference 'a' points to object which contains decimal equivalent i.e.3239
print(a) # prints the decimal equivalent i.e. 3239
print(type(a)) #Type of object 'a' is <class 'int'> 
print(id(a)) # Address of 'a'
b = 0o6247 #reference 'b' points to same object
print(id(b)) #same address
print(b) # 3239
c = 3239 #reference 'c' points to same object
print(c) #3239
print(id(c)) #same address
print(0o9248) #Error due to 9. octal contains 0 t0 7

--------------------------------------------------------------------------

# Find  outputs  (Home  work)
a = 0XA7B9 # reference 'a' points to object which contains decimal equivalent i.e.42937
print(a)  # prints the decimal equivalent i.e. 42937
print(type(a)) #Type of object 'a' is <class 'int'>
b = 0xBEEF # reference 'a' points to object which contains decimal equivalent i.e.48879
print(b)  # prints the decimal equivalent i.e. 48879
print(A7B9) #Error due to there is no representation of hexa-decimal
print('A7B9') #prints A7B9
print(0XBEER) #Error due to R 
print(0XHYD) #Error due to H 
print(0xA7G9B)# Error due to G

----------------------------------------------------------------------------

# Find outputs (Home  work)
a = 9248
print(a) #Prints 9248
print(type(a))#Prints the type of 'a' <class int>