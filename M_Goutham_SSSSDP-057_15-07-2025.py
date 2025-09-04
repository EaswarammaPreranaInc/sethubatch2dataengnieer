# float  object  demo  program (Home  work)
a = 10.8 #10.8 is a float object and a = reference of float object
print(a) # prints the 10.8
print(type(a)) #prints the type of float object i,e <class 'float'>
print(id(a)) # Prints the address of reference a 
b = 25. #25. is treated as 25.0 and yes it is valid float object
print(b) #Prints as 25.0
print(type(b)) #Prints the type of float object i,e <class 'float'>
c = .689 #.689 is a treated as 0.689 and yes it is a valid float object
print(c) #Prints as 0.689
d = 3.4E2#It is treated as 3.4*10 to the power of 2 whereever we specify E/e in between the numbers it multiplies before E/e with 10 to the power of the number after E/e
print(d) #Prints the result of 3.4*10 to the power of 2 i,e 370.0 so basically E/e is an exponent
print(type(d))#Prints the type of float object i,e <class 'float'>
e = 9.62e-2#It is also treated as 9.62*10 to the power of -2 same but it will take the exponent as negative i,e -2
print(e)#Prints the calculated result i,e 0.0962
#print(9.8.2) #It is invalid as there should have only 1 decimal point in one number that you are printing

# complex object demo program
a = 3 + 4j #3+4j is a complex object and a is reference to this complex object
print(a) #Prints the 3+4j where 3 is the real part and 4j is the imaginary part i,e is imag
print(type(a)) #Prints the type of object i,e <class 'complex'>
print(id(a)) #Prints the Address of complex object a 
print(a . real) #Prints the real part of the complex number i,e 3 
print(a . imag) #Prints the imaginary part of the complex number i,e 4j
print(type(a . real)) #Prints the type of real part of the complex object i,e <class 'float'> 
                      #Complex objects are always float class only (3.0) and (4.0)
print(type(a . imag)) #Prints the type of imag(imaginary part) of the the complex object i,e <class 'float'>

# Find outputs
a = 6j #It is a complex imag part and it assumes the real part as 0 so 0+6j
print(a) #Prints the output as 6j
print(type(a)) #Prints the type of object class i,e <class 'complex'>
print(a.real) #Prints the 0 as real part of the above complex object
print(a.imag) #Prints the 6j as imag part as already mentioned
print(5 + j6) #We will get the error i,e j should be kept always after the number
#print(3 + 4i) #Error #Because we cannot use i instead of j always for imag part we must use j
print(4+j) #Error #Not a valid complex object there should a number with j
print(4 + 1j) #Valid one #Prints the 4+1j
print(4 + 0j) #Valid one #Prints the 4+0j

# bool object demo program
a = True #True is a bool object and a is reference to bool object
print(a) #Prints True
print(type(a)) #Prints the type of object i,e <class 'bool'>
print(id(a)) #Prints the address of a
b = False #False is also a bool object and b is reference to bool object
print(b) #Prints False
print(type(b)) #Prints the type of object i,e <class 'bool'>
print(True + True) #Here when we perform any operation True is treated as 1 and False is treated as 0 so it prints 1+1 is 2
print(True + False) #Same we are performing operation 1 + 0 is 1
print(False + True) #Same we are performing operation 0 + 1 is 1
print(False + False) #Same 0 + 0 is 0
print(True + True + True) #Here also we are performing the operation 1 + 1 + 1 is 3
print(25 + 10.8 + True) #Here we are performing operation with integer + float + bool and yes it works 25 + 10.8 + 1 = 36.8
print(True > False) #Here it returns the bool as result True > False i,e 1 > 0 and yes it returns the True
print(True) #Returns the True as output
print(False) #Returns the False as output
print(true) #It gives an error that when ever we are using bool objects then the 1st letter must be capital i,e True as it is a keyword in python 
print(false) #Here also same the 1st letter must be Capital i,e False as False is a keyword in python

# Find  outputs (Home  work)
a = 0O6247 #It is an octal Integer so it is specified as 0o6247
print(a) #Prints the decimal value of the octal number i,e 3239 (6*8 power 3 + 2*8 power 2 + 4*8 power 1 + 7*8 power 0)
print(type(a)) #prints the type of object a i,e <class 'int'>
print(id(a)) #Prints the address of object a 
b = 0o6247 #It is also octal integer we can use lowercase o or uppercase O 
print(id(b)) #Prints the address of object b
print(b) #prints the decimal value of octal number i,e 3239
c = 3239 #3239 is an int object and c is reference of int object 
print(c) #Prints the value of c i,e 3239
print(id(c)) #Prints the address of int object 
#print(0o9248) #We will get an error i,e for octal we have base 8 (0-7) but here we have 9 so it gives us an error

# Find  outputs
a = 0XA7B9 #It is Hexa-decimal object (0-9 and A-F(a-f)) and a is reference
print(a) #Prints the value of Hexa-decimal value i,e 42937 decimal value
print(type(a)) #Prints the type of object that is <class 'int'>
b = 0xBEEF #It is also a Hexa-decimal object and b is reference
print(b) #Prints the decimal value of Hexa-decimal i,e 48879
print(A7B9) #Throws an error that if we want to use hexa-decimal integer we need to add a prefix as 0x/0X
print('A7B9') #Prints A7B9 as we are specifying the value in '' so the PVM thinks it is a string
#print(0XBEER) #As we have hexa-decimal from 0-9 and A-F but we are using R here so invalid syntax
#print(0XHYD) #Same here also we are using H and Y which are not part of hexa-decimal
#print(0xA7G9B) #Here also same we are using G so invalid syntax

# Find outputs
a = 9248 #9248 is int object and a is reference of this int object
print(a) #prints the value 9248
print(type(a)) #prints the type of object i,e <class 'int'>