# float  object  demo  program (Home  work)
a = 10.8
print(a) # prints the value of a //output:10.8
print(type(a))#prints the objecttype of a //output:'class'= float
print(id(a))#prints the address of the object //output:EX13247687
b = 25.
print(b)# as the decimal value is not specified it gives output as:25.0
print(type(b))#prints the objecttype of a //output:'class'= float
c = .689
print(c)#as there is no number specified before point it prints :0.689
d = 3.4E2
print(d)#10^2 is:3.4*10^2 // output=340
print(type(d))#class float // the value of d is in decimal points
e = 9.62e-2
print(e)#e^-2 // 9.62*10^-2 output = 0.0962
print(9.8.2)#error because 2 decimal places are placed in print statement
# complex object demo program
a = 3 + 4j
print(a)#prints the value of a // output : 3+4j
print(type(a))#prints the object type of a // output : class = complex
print(id(a))#prints the address/reference of the object
print(a . real)#prints the real side value through .(object)operation // output :3.0(its default covertion is float)
print(a . imag)#prints the imaginary side value through .(object)operation // output :4.0(its default covertion is float)
print(type(a . imag))# output : class = float //(its default covertion is float)
print(type(a . real))# output : class = float //(its default covertion is float)
# Find outputs (Home work)
a = 6j
print(a)#prints the value of a // output = 6j
print(type(a))#prints the object type of a // o/p : class complex
print(a.real) # as the real part is not given it takes default 0.0 as output because by default itconverts to float value.
print(a.imag) # output : 6.0 // by default it converts to float type
print(5 + j6) # invalid output because the imagvalue should be before j in python.
print(3 + 4i) # error  because only j should be sqrt(-1) for imagside
print(4+j) #error because imagside should be written as 4+1j 
print(4 + 1j) #prints 4 + 1j
print(4 + 0j) #prints 4+ 0j
# bool object demo program  (Home  work)
a = True
print(a) # prints True because the operation is not done.
print(type(a)) # output : class = boolean
print(id(a)) #Ex: 1375487
b = False
print(b) # prints False because the operation is not done.
print(type(b)) # output : class = boolean
print(True + True) # output : 1 + 1 = 2 as '+' operation is performed 
print(True + False)# output : 1 + 0 = 1 as '+' operation is performed 
print(False + True) # output : 0 + 1 = 1 as '+' operation is performed 
print(False + False)# 0 + 0 = 1 as '+' operation is performed 
print(True + True + True)# output : 1 + 1 + 1 = 3 as '+' operation is performed 
print(25 + 10.8 + True) # output : 36.8 //25 + 10.8 + True = 1 
print(True > False) #output : returns True bcoz 1 > 0
print(True) #prints True
print(False)#prints Flase
print(true) # gives error because keyword is True
print(false) # gives error because keyword is False
# Find  outputs (Home  work)
a = 0O6247
print(a) #prints decimal value of a i.e ; 3239
print(type(a)) #prints the converted type of octa decimal i,e ; class = int
print(id(a)) # prints reference/address of a.
b = 0o6247
print(id(b)) # prints the address of b.
print(b) # prints decimal coverted number.
c = 3239
print(c) # prints value of c.
print(id(c)) #prints address of c.
print(0o9248) #octal number contaions 0 to 8 so its gives error
# Find  outputs  (Home  work)
a = 0XA7B9
print(a) #prints the converted value of hexadecimal number to decimal number i.e ; 42937
print(type(a)) #prints converted object type of the value i.e; 48879
b = 0xBEEF
print(b) 
print(A7B9) # hexa decimal value should start with 0X so it gives error
print('A7B9') #prints the string as output : A7B9
print(0XBEER) # error due to R is not between a to F
print(0XHYD)# error due to Y is not between a to F
print(0xA7G9B)# error due to G is not between a to F
# Find outputs (Home  work)
a = 9248
print(a) # prints the value of a.
print(type(a))# class object type = int as output.