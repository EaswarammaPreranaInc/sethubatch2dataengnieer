#Home work-1
# float  object  demo  program (Home  work)
a = 10.8 
print(a) #value of the object 'a', which is 10.8
print(type(a)) #type of the object 'a', which is <class 'float'>
print(id(a)) #address of the object 'a', say 1000
b = 25.
print(b) #value of the object 'b', which is 25.0
print(type(b)) #type of the object 'b', which is <class 'float'>
c = .689 
print(c) #value of the object 'c', which is 0.689
d = 3.4E2
print(d) #value of the object 'd', which is 340.0
print(type(d)) #type of the object 'd', which is float
e = 9.62e-2 
print(e) #value of the object e, which is 0.0962
print(9.8.2) #error, reason for the error: keeping 2 decimal points isn't the correct way to form a float object

#Home work-2
# complex object demo program
a = 3 + 4j
print(a) #value of the object 'a', which is 3+4j
print(type(a)) #type of the object 'a', which is <class 'complex'>
print(id(a)) #address of the object 'a', say 2000
print(a . real) #value of the real component of the object 'a', which is 3
print(a . imag) #value of the imaginary component of the object 'a', which is 4
print(type(a . real)) #type of the real component of object 'a', which is <class 'float'>
print(type(a . imag)) #type of the imaginary component of object 'a', which is <class 'float'>

#Home work-3
# Find outputs (Home work)
a = 6j
print(a) #value of the object 'a', which is 6j
print(type(a)) #type of the object 'a', which is <class 'complex'>
print(a.real) #the value of the real component of object 'a', which is 0
print(a.imag)  #the value of the imaginary component of object 'a', which is 6
print(5 + j6) #error, reason for error: 'j' should be placed after '6' in the imaginary component 
print(3 + 4i)  #error, reason for error: have to use 'j' instead 'i'
print(4+j) #error, reason for error: in the imaginary component it should be '1j' not j
print(4 + 1j) #value of the object, which is 4+1j
print(4 + 0j) #value of the object, which is 4+0j

#Home work-4
# bool object demo program  (Home  work)
a = True
print(a)#value of the object 'a', which is True
print(type(a)) #type of the object 'a', which is <class 'bool'>
print(id(a)) #address of the object 'a', say 3000
b = False
print(b) #value of the object 'b', which is False
print(type(b)) #type of the object 'b', which is <class 'bool'>
print(True + True) # prints 2, True will be considered as '1' here since this involves operation
print(True + False) # prints 1, True will be considered as '1' and False as '0' here since this involves operation
print(False + True) # prints 1, True will be considered as '1' and False as '0' here since this involves operation
print(False + False) # prints 0,False will be considered as '0' here since this involves operation
print(True + True + True) # prints 3, True will be considered as '1' here since this involves operation
print(25 + 10.8 + True) #prints 36.8, True will be considered as '1' here since this involves operation
print(True > False) #prints True, True will be considered as 1 and false as 0. as (1 > 0) is true it prints True
print(True) #prints True
print(False) #prints False
print(true) #error: True is keyword, it should not be written with 't' as lower case
print(false) #error: False is keyword, it should not be written with 'f' as lower case

#Home Work-5
# Find  outputs (Home  work)
a = 0O6247
print(a) #the decimal equivalent of the octal number will be printed, which is 3239
print(type(a)) #the type of the object 'a', which is <class 'int'>
print(id(a)) # the address of the object 'a', say 5000
b = 0o6247 
print(id(b)) # 5000 , new object will not be created will refer to the already existing object because there is object storing same content 
print(b) #the decimal equivalent of the octal number will be printed, which is 3239
c = 3239 
print(c) #the value of the object 'c', which is 3239
print(id(c)) #5000, new object will not be created will refer to the already existing object because there is object storing same content
print(0o9248) #Error, reason for error: '9' is not allowed in octal representation

#Home Work-6
# Find  outputs  (Home  work)
a = 0XA7B9
print(a) #the decimal equivalent will be printed which is 42937
print(type(a)) #the type of the object 'a' is <class 'int'>
b = 0xBEEF
print(b) #the decimal equivalent will be printed which is 48879
print(A7B9) #error, reason for error: this is not the way to represent a hexadecimal number, '0' is missing at the front
print('A7B9') #prints A7B9 as a string
print(0XBEER) #'R' isn't allowed in hexadecimal representation
print(0XHYD) #'H', 'Y', 'D' are not allowed in hexadecimal representation.
print(0xA7G9B) #'G' is not allowed in hexadecimal representation

#Home work-7
# Find outputs (Home  work)
a = 9248
print(a) #the value of the object 'a', which is 9248
print(type(a)) # the type of the object 'a', which is <class 'int'>
