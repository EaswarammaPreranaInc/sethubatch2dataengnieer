#BinaryNumber
# Find  outputs
a = 0B10101    #Object  contains  decimal  equivalent  i.e.  16 + 4 + 1 = 21
print(a)       #21
print(type(a)) #<class   'int'>
print(id(a))   #Address  of  object   21  (say  1000)
b = 0b10101    #Ref  'b'  points  to  same  object  21
print(b)       #21
print(id(b))   #Same  address
c = 21         #Ref  'c'  points  to  same  object  21
print(c)       #21
print(id(c))   #Same  address
d = 10101      #Decimal  number
print(d)       #10101
#e = 0B1234    #SyntaxError: invalid digit '2' in binary literal,  due  to  2 , 3  and   4


#Binary Function
# bin()  function  demo  program
print(bin(25))      #0b11001, Converts int object 25 to binary str 
print(bin(0O6247))  #0b110010100111, converts int object 0O6247 to binary str
print(bin(0XA7B9))  #0b1010011110111001, converts int object 0xA7B9 to binary str
x = 0xA             #assigns ref x to int class object 0xA
print(x, type(x))   #10<space><class 'int'>
a = bin(0xA)        #assigns ref a to str class object '0b1010'
print(a)            #'0b1010', prints str
print(type(a))      #<class 'str'>     




#Bool Object
# bool object demo program
a = True                  #Ref 'a'  points  to  object  True
print(a)                  #Value  of  object  'a'   i.e. True
print(type(a))            #Type of object 'a' i.e.  <class  'bool'>
print(id(a))              #Address of object   True
b = False                 #Ref 'b'  points  to  object   False
print(b)                  #Value  of  object  'b'  i.e. False
print(type(b))            #Type of object 'b' i.e.  <class  'bool'>
print(True + True)        #1+1  = 2
print(True + False)       #1+0  = 1
print(False + True)       #0+1 = 1
print(False + False)      #0+0 = 0
print(True + True + True) #1+1+1  = 3
print(25 + 10.8 + True)   #36.8
print(True > False)       #1 > 0  is  True
print(True)               #True
print(False)              #False
#print(true)              #Error  due  to   't'
#print(false)             #Error  due  to   'f'



#Complex Object
# complex object demo program
a = 3 + 4j            #Ref  'a'  points  to  object  (3+4j)
print(a)	          #(3+4j)
print(type(a))        #Type of object 'a' i.e <class 'complex'>
print(id(a))          #Address of object  3 + 4j (may be 1000)
print(a . real)       #3.0, object of name real in object a
print(a . imag)       #4.0, object of name imag in object a
print(type(a . real)) #<class  'float'>, type of name in object a
print(type(a . imag)) #<class  'float'>, type of name in object a

# Find outputs (Home work)
a = 6j           #Ref  'a'  points  to  object  6j
print(a)         #6j
print(type(a))   #Type of object 'a' i.e. <class 'complex'>
print(a . real)  #0.0
print(a . imag)  #6.0
#print(5 + j6)   #NameError: name 'j6' is not defined, imag  can  not  be   after  'j'
#print(3 + 4i)   #SyntaxError: invalid decimal literal, due  to  'i'
#print(4+j)      #NameError: name 'j' is not defined, imag  is  missing
print(4 + 1j)    #(4+1j)
print(4 + 0j)    #(4+0j)


#Decimal Number

# Find outputs (Home  work)
a = 9248       #reference a is assigned to int class object
print(a)       #9248, value of object a is printed
print(type(a)) #<class 'int'>, class type of object a is printed


#Float Object
# float  object  demo  program (Home  work)
a = 10.8        #Ref  'a' points  to  float  object  10.8
print(a)        #Value  of  object  'a'  i.e.  10.8
print(type(a))  #Type  of object  'a'  i.e.  <class  'float'>
print(id(a))    #Address  of  object   10.8  (may  be   1000)
b = 25.         #Valid   and  interpreted  as  25.0
print(b)        #25.0
print(type(b))  #<class   'float'>
c = .689        #Valid   and  interpreted  as   0.689
print(c)        #0.689
d = 3.4E2       #3.4 * 10 ^ 2
print(d)        #340.0
print(type(d))  #<class   'float'>
e = 9.62e-2     #9.62 * 10 ^ -2
print(e)        #0.0962
#print(9.8.2)   #  Error:SyntaxError: invalid syntax. Perhaps you forgot a comma?,  due  to  more  than  one  decimal  point



#Hexadecimal Number
# Find  outputs  (Home  work)
a = 0XA7B9       #Object  contains  decimal  equivalent  i.e. int class object
print(a)         #42937
print(type(a))   #<class 'int'>
b = 0xBEEF       #Object  contains  decimal  equivalent  i.e. int class object
print(b)         #48879
#print(A7B9)     #Error :   Not  starting  with  0X
print('A7B9')    #A7B9
#print(0XBEER)   #SyntaxError: invalid hexadecimal literal, due to  'R' in hexa-decimal number
#print(0XHYD)    #SyntaxError: invalid hexadecimal literal, due to 'H'  and  'Y' in hexa-decimal number
#print(0xA7G9B)  #SyntaxError: invalid hexadecimal literal,  Error due to 'G'  in  hexa-decimal number



#Integer Object
# int  object  demo  program
a = 25          #Ref  'a'  points  to  object  25
print(a)        #Value  of  object  'a'  i.e.  25
print(type(a))  #Type  of  object  'a'  i.e.  <class  'int'>
print(id(a))    #Address  of   object  'a'  (may  be  1000)
b = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999 #   Valid
print(b)        #999999999999999999999999999999999999999999999999999999999999999999999999999999999999
#c = $75        #SyntaxError: invalid syntax, Error  due  to  $




#NoneType object
# NoneType  object  demo  program
a = None       #Ref  'a'  points  to  object  None
print(type(a)) #<class  'NoneType'>
print(a)       #None
print(id(a))   #Address  of  object  None
#print(none)   #Error due  to  'n'



#Octal Numebr
# Find  outputs (Home  work)
a = 0O6247     #Object  contains  decimal  equivalent  i.e.  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^  1 + 7 * 8 ^ 0 = 3239
print(a)       #3239
print(type(a)) #<class 'int'>
print(id(a))   #Address  of  object  3239  (may  be  2173646715760)
b = 0o6247     #Ref  'b'  points  to  same  object  (int  object  is   reusable)
print(id(b))   #Same  address
print(b)       #3239
c = 3239       #Ref  'c'  points  to  same  object   (int  object  is   reusable)
print(c)       #3239
print(id(c))   #Same  address
#print(0o9248)  #SyntaxError: invalid digit '9' in octal literal, Error due  to  9  and  8  in octal number


