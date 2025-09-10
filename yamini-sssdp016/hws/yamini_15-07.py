a = 10.8  # assigns the object value 10.8 to reference value a
print(a)  # a prints the float object value 10.8
print(type(a)) #<prints the type of object a <class 'Float'>
print(id(a))   # prints the address of float object a
b = 25.  # assigns the object value 25.0 to reference value b
print(b) # b prints the float object value 25.0
print(type(b)) #<prints the type of object a class 'Float'
c = .689  # assigns the object value 0.689 to reference value c
print(c)  # c prints the float object value 0.689
d = 3.4E2  # assigns the object value(mantissa exponent number) 3.4E2 to reference value d
print(d) # d prints the float object value 3.4*10^2 i.e 340
print(type(d))  #<prints the type of object a class 'Float'
e = 9.62e-2  # assigns the object value(mantissa exponent number) 9.62e-2 to reference value e
print(e)  # e prints the float object value 9.62*10^-2 i.e 0.0962
print(9.8.2) #error because float value contains only one decimal point


a = 3 + 4j  #assigns complex object 3+4j to reference value a
print(a)  #prints the complex object value assigned to a
print(type(a))  #prints type of object a i.e <class complex> 
print(id(a))   # prints the address of complex object a
print(a . real) # prints the real part of complex object
print(a . imag) # prints the imag part of complex object
print(type(a.real))# prints the type of real part i.e float of complex object
print(type(a.imag)) # prints the type of imag part i.e float of complex object

a = 6j # assigning the complex object 6j to reference value a
print(a)  #prints the complex object value stored in a i.e 6j
print(type(a)) #prints the type of a i.e typr of object 6j <class complex>
print(a.real) # prints the real part of complex object there is no real part so prints 0.0
print(a.imag) # prints the imag part of complex object 6.0
print(5 + j6) # error because j should be placed after the integer value of imag part
print(3 + 4i)  #error because j should be only used for imag part in python
print(4+j) #error because the imag value is not there
print(4 + 1j) #prints the complex object 4+ij
print(4+0j) #prints the complex object 4+ij

a = True #assign the bool object True to reference value a
print(a) #prints the object value assigned to a
print(type(a)) #prints the type of a i.e type of object True <class bool>
print(id(a)) # prints the address of bool object a
b = False #assign the bool object False to reference value b
print(b) #prints the object value assigned to b
print(type(b)) #prints the type of b i.e type of object False <class bool>
print(True + True) #as the operation is executing the type of the object will change to int so 1+1=2
print(True + False) # operation is there so 1+0=1
print(False + True) # operation is there so 0+1=1
print(False + False) # operation is there so 0+0=0
print(True + True + True) # operation is there so 1+1+0=2
print(25 + 10.8 + True) # operation is there so 25+10.8+1=36.8
print(True > False) # operation is there so checks for 1>0=true
print(True) #prints the Tture value
print(False) #prints the False value
print(true) #error because true is keyword it should be True
print(false) # error because false is a keyword it should be False

a = 0O6247 #assigns the decimal equivalent of object to the refernce value a
print(a) #internally converts the octal number to decimal number and prints it i.e 0O6247 is converted to decimal 3239 and is printed
print(type(a)) # as the octal object is converted to decimal integer type is <class int>
print(id(a)) # prints the address of object a
b = 0o6247  #assigns the decimal equivalent of object to the refernce value b
print(id(b)) # as the objects stored in refernce a and b is same b will have same id as a
print(b)  #internally converted to decimal number and prints it i.e 3239 is printed
c = 3239 #assigns the object to c
print(c)
print(id(c)) # as the objects stored in refernce a,b and c are same c will have same id as a,b
print(0o9248) #error because octal numbers have only integers from 0 to 7

a = 0XA7B9 #assigns the decimal equivalent of object to the refernce value a
print(a) #prints the decimal integer object stored in a
print(type(a)) #converts the hexa decimal to decimal integer internally so type is <class int>
b = 0xBEEF #assigns the decimal equivalent of object to the refernce value b
print(b) #prints the decimal integer object stored in b
print(A7B9) #converts the hexa decimal to decimal integer internally and prints it
print('A7B9') #error because prefix for hexadecimal ox should be there
print(0XBEER) #error because hexa decimal numbers have only integers from 0 to 9 and alpha numeric numbers from A to F (R is included)
print(0XHYD) #error because alpha numeric numbers in hexa decimal doesnt comtain H and D
print(0xA7G9B) # G is not a hexadecimal number but included in the number

a = 9248 #assigns the decimal integer of object to the refernce value a
print(a) #prints the object value assigned to a
print(type(a)) # as it is a decimal number type will be <class int>




