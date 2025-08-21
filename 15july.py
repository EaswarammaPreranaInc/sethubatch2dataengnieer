# float  object  demo  program (Home  work)
a = 10.8  
print(a)  #10.8
print(type(a))  #<class 'float'>
print(id(a))  #136544589596816 address of object 10.8
b = 25.  
print(b)   #25.0
print(type(b))   #<class 'float'>
c = .689 
print(c)  #0.689
d = 3.4E2 
print(d)  #3.4*10^2=3.4*100=340.0
print(type(d)) #<class 'float'>
e = 9.62e-2
print(e)  #9.62*10^-2  #0.0962
print(9.8.2)  #we get error as there are two decimal points in a number


# complex object demo program
a = 3 + 4j
print(a)  #3+4j
print(type(a))  #<class 'complex'>
print(id(a))  #address of complex object 3+4j 133964146470544
print(a . real)  #3.0
print(a . imag)  #4.0
print(type(a . real))   #<class 'float'> 
print(type(a . imag))	#<class 'float'>


# Find outputs (Home work)
a = 6j
print(a)  #6j
print(type(a))   #<class 'complex'>
print(a.real)  #0.0
print(a.imag)  #6.0
print(5 + j6)  #error as the format of imag is incorrect, it should be 6j
print(3 + 4i)  #error as the format of imag is incorrect, it should be 4j but not i
print(4+j)  #error as the imag is incorrect, there should be a number before j, just j is not correct, if there is no value , then zero0 should be added before j
print(4 + 1j)  #4+1j
print(4 + 0j)  #4+0j


a = True
print(a)   #True  
print(type(a))   #<class 'bool'>
print(id(a))    #133571041949120
b = False   
print(b)    #False
print(type(b))   #<class 'bool'>
print(True + True)    #1+1=2  bool in arithemteic operations gives int 
print(True + False)   #1+0=1
print(False + True)    #0+1=1
print(False + False)     #0+0=0
print(True + True + True)    #1+1+1=3
print(25 + 10.8 + True)    #25+10.8+1=36.8
print(True > False)    #True
print(True)    #True
print(False)   #False
print(true)    #error   #in true, t should be 'T', it should be True
print(false)    #error    #in flase, f should be 'F', it should be False



# Find  outputs (Home  work)
a = 0O6247
print(a)  #O means octal, hence 6*8^3+2*8^2+4*8^1+7*8^0=3239
print(type(a))  <class 'int'>
print(id(a))  #address of 3239 object is 138266053242512
b = 0o6247   #for octal, it can be either small case o or upper case O
print(id(b))  #address of 3239 object is 138266053242512
print(b)  # 6*8^3+2*8^2+4*8^1+7*8^0=3239
c = 3239
print(c)
print(id(c))  #3239
print(0o9248)   #octal range is 0-7, but here in digits we have 9and 8 which is out of range of octal, hence we get error




# Find  outputs  (Home  work)
a = 0XA7B9
print(a)   #X means hexa decimal, in hexa decimal A means 10 like wise till F means 15
		10*16^3+7*16^2+11*16*1+9*16^0=42937
print(type(a))  #<class 'int'>
b = 0xBEEF 
print(b)   # 11*16^3+14*16^2+14*16^1+15*16^0= 48879
print(A7B9)  #error
print('A7B9')  #A7B9
print(0XBEER)  #R is present which is out of hexa decimal
print(0XHYD)  #Y is present which is out of hexa decimal
print(0xA7G9B) #G is out of hexa decimal



# Find outputs (Home  work)
a = 9248
print(a)   #9248
print(type(a))   #<class 'int'>





















