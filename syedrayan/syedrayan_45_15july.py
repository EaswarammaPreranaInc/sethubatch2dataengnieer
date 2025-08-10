#1 float  object  demo  program (Home  work)
a = 10.8
print(a) # value of object 'a' i.e. 10.8
print(type(a)) # Type of object 'a' i.e. <class 'float'>
print(id(a)) #Address of object 'a'
b = 25.
print(b) # Value of object 'b' i.e. 25.0
print(type(b)) #type of object 'b' i.e. <class 'float'>
c = .689
print(c) # Value of object 'c' i.e. 0.689
d = 3.4E2
print(d)  #Value of object 'd' i.e. 340.0
print(type(d)) #Type of object 'd' <class 'float'>
e = 9.62e-2
print(e) # Value of object 'e' i.e. 0.0962
#print(9.8.2) #syntax error

# complex object demo program
a = 3 + 4j
print(a) #3 + 4j
print(type(a)) # Type of Object 'a' i.e. <class 'complex'>
print(id(a)) # address of object 'a' 
print(a . real) #3.0
print(a . imag) # 4.0
print(type(a . real)) # <class 'float'>
print(type(a . imag)) # <class 'float'>

# Find outputs (Home work)
a = 6j
print(a) #6j
print(type(a)) # <class 'complex'>
print(a.real) # 0.0
print(a.imag) # 6.0
#print(5 + j6) # Error j6 is not defined
#print(3 + 4i)  # Error 4i is not defined
#print(4+j) # Error j is not defined 
print(4 + 1j) # 4 + 1j
print(4 + 0j) # 4 + 0j

# bool object demo program  (Home  work)
a = True
print(a) #True
print(type(a)) #<class 'bool'>
print(id(a)) # Address of object 'a'
b = False
print(b) #False
print(type(b)) # <class 'bool'>
print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False)  # 0
print(True + True + True)  # 3
print(25 + 10.8 + True) #36.8
print(True > False) #1
print(True) #True
print(False) #False
#print(true) #name error it is True
#print(false)#name error it is False

# Find  outputs (Home  work)
a = 0O6247
print(a) # decimal value of object 'a' i.e. 3239
print(type(a)) #Type of  object<class 'int'>
print(id(a)) #address of object 'a'
b = 0o6247
print(id(b)) #address of object 'b'
print(b) # decimal value of object 'b' i.e. 3239
c = 3239
print(c) # value of object 'c' i.e. 3239
print(id(c))  #address of object 'c'
#print(0o9248) #Error octal do not have 8,9

# Find outputs (Home  work)
a = 9248
print(a) #value of object 'a' i.e. 9248
print(type(a)) # Type of object 'a' <class 'int'>

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) #decimal value of object 'a' i.e. 42937
print(type(a)) #<class 'int'>
b = 0xBEEF
print(b)#decimal value of object 'a' i.e. 48879
#print(A7B9) #ERROR need a prefix of 0x or 0X 
print('A7B9') #A7B9
#print(0XBEER)# ERROR R not in hexadecimal 
#print(0XHYD) # ERROR H,Y not in hexadecimal
#print(0xA7G9B) # ERROR G not in hexadecimal 