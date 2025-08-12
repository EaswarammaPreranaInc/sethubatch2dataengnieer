# float  object  demo  program (Home  work)

a = 10.8 #assign reference a to float object 10.8
print(a) # 10.8
print(type(a)) # <class 'float'>
print(id(a)) #Address of a ex:10000  
b = 25. #assign reference b to float object 25.
print(b) #25.0
print(type(b)) # <class 'float>
c = .689 #assign reference c to float object .689
print(c) # 0.689
d = 3.4E2 # assign reference d to float object 3.4E2
print(d) # 340.0
print(type(d)) # <class float>
e = 9.62e-2 # assign reference e to float object 9.62e-2
print(e) # 0.0962
print(9.8.2) # Invalid,only one point accepted in float number 

 # complex object demo program

a = 3 + 4j # a reference is assigning to complex object 3+4j
print(a) # 3+4j
print(type(a)) #<class 'complex'> 
print(id(a)) # Address of a object
print(a . real) # prints the real part 3
print(a . imag) # prints the imag part 4
print(type(a . real)) # <class 'float'>
print(type(a . imag)) # <class 'float>

 # Find outputs (Home work)
a = 6j #a reference is assigned to complex object 6j(0+6j)
print(a)#6j
print(type(a))#<class 'complex'>
print(a.real)#0.0
print(a.imag)#6.0
print(5 + j6)#invalid statement due to j should be after the integer value(5+6j)
print(3 + 4i)#invalid statement due to i is not considerd as imag part in python 
print(4+j)#invalid statement due to no number before j
print(4 + 1j)#valid 4+1j
print(4 + 0j)#invalid statement due to 0 is not  imag part 

 # bool object demo program  (Home  work)
a = True #a is assigned to the bool obj True
print(a) #True
print(type(a))#<class 'bool'>
print(id(a))#address of obj a
b = False # b is assigned to bool obj False
print(b)#False
print(type(b))#<class 'bool'>
print(True + True) #2(it consider True as 1 False as 0)
print(True + False) #1(1+0)
print(False + True) #1(0+1)
print(False + False #0(0+0)
print(True + True + True)#3(1+1+1)
print(25 + 10.8 + True)#prints 36.8
print(True > False)#True
print(True)#True
print(False) #False
print(true)#invalid due to t should be T because True is a keyword
print(false)#invalid due to t should be T because True is a keyword


 # Find  outputs (Home  work)
a = 0O6247 # a is assigned to decimal equivalent object 0O6247
print(a) #prints the decimal equivalent number(3239)
print(type(a))#<class 'int'>
print(id(a)) # address will be printed ex:1000
b = 0o6247 #b is assigned to decimal equivalent object 0O6247
print(id(b)) #points to same address of a 1000
print(b)#prints the decimal equivalent number(3239)
c = 3239 #c is assigned to  object 3239
print(c) #3239
print(id(c)) #points to same address of a 1000
print(0o9248) #invalid due to 8 and 9 are not octal numbers

# Find  outputs  (Home  work)
a = 0XA7B9 # a reference is holding the decimal equivalent object 0XA7B9 
print(a) #prints the decimal equivalent 42937
print(type(a)) #<class 'int'>
print(A7B9) #invalid statement numbers not allow alphabets 
print('A7B9')# it returns the str value A7B9
print(0XBEER) #Invalid statement hexadecimal allowed up to 0-9 and  A-F
print(0XHYD) #Invalid statement hexadecimal allowed up to 0-9 and  A-F
print(0xA7G9B)#Invalid statement hexadecimal allowed up to 0-9 and  A-F

 # Find outputs (Home  work)
a = 9248 # a is assigned to object 9248
print(a) #9248
print(type(a)) #<class 'int'>