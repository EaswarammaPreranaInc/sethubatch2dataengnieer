#Ramu 15-07-25

# float  object  demo  program (Home  work)
a = 10.8
print(a) # prints output:10.8
print(type(a)) #prints objecttype of a -output:'class'= float
print(id(a)) #prints the address of the object ex:1000
b = 25.
print(b) # prints 25.0
print(type(b)) #prints output:'class'= float
c = .689
print(c) #prints :0.689
d = 3.4E2
print(d) #prints output=340
print(type(d)) #class float 
e = 9.62e-2
print(e) #prints output = 0.0962
print(9.8.2)#error

# complex object demo program

a = 3 + 4j
print(a) #prints output : 3+4j
print(type(a)) #prints class = complex
print(id(a)) #prints the address of a
print(a . real) #prints the real side value through .(object)operation , output :3.0
print(a . imag) #prints the imaginary side value through .(object)operation , output :4.0
print(type(a . real))# output : class = float 
print(type(a . imag)) # output : class = float

# Find outputs (Home work)

a = 6j
print(a) #prints o/p = 6j
print(type(a ))#prints o/p : class complex
print(a.real) # as the real part is not given it takes default 0.0 as o/p
print(a.imag) # output : 6.0 
print(5 + j6) # invalid
print(3 + 4i) # error  because only j should be sqrt(-1) for imagside
print(4+j) #error
print(4 + 1j) #prints 4 + 1j
print(4 + 0j) #prints 4+ 0j

# bool object demo program  (Home  work)

a = True
print(a) # prints True
print(type(a)) # o/p : class = boolean
print(id(a)) #Ex: 1000
b = False
print(b) # prints False
print(type(b)) # o/p: class = boolean
print(True + True)  #output : 1 + 1 = 2
print(True + False)# output : 1 + 0 = 1
print(False + True) # output : 0 + 1 = 1
print(False + False)# 0 + 0 = 0
print(True + True + True)# output : 1 + 1 + 1 = 3
print(25 + 10.8 + True) # output : 36.8 //25 + 10.8 + True = 1 
print(True > False) #output : returns True 
print(True) #prints True
print(False)#prints Flase
print(true) #error because keyword is True
print(false) # error because keyword is False

# Find  outputs (Home  work)

a = 0O6247
print(a) #prints decimal value of a i.e ; 3239
print(type(a)) #prints the converted typ e of octa decimal i,e ; class = int
print(id(a)) # prints address of a.
b = 0o6247
print(id(b)) # prints the address of b.
print(b) # prints decimal coverted number.
c = 3239
print(c) # prints value of c.
print(id(c)) #prints address of c.
print(0o9248) #error

# Find  outputs  (Home  work)

a = 0XA7B9
print(a) #prints o/p: 42937
print(type(a)) #prints converted object type of the value i.e; 48879
b = 0xBEEF
print(b) #o/p;48879
print(A7B9) # error
print('A7B9') #prints o/p: A7B9
print(0XBEER) # error
print(0XHYD)# error
print(0xA7G9B)# error

# Find outputs (Home  work)

a = 9248
print(a) # prints the value of a.
print(type(a)) # prints class=int as output.
