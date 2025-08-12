# ===================================== Non-Sequence(int,float,complex,bool,none) ===========================================

#===========================================float=============================== 
a = 10.8
print(a) # 10.8
print(type(a))# <class 'float'>
print(id(a)) # Address of object 'a'
b = 25.
print(b)# 25.0
print(type(b))# <class 'float'>
c = .689
print(c)# 0.689
d = 3.4E2
print(d)#340.0
print(type(d))# <class 'float'>
e = 9.62e-2
print(e)#0.0962
#print(9.8.2)#Error  SyntaxError: invalid syntax.


#===========================================Complex=============================== 
a = 3 + 4j
print(a)#(3 + 4j
print(type(a))#<class 'complex'>
print(id(a))# Address of object 'a'
print(a.real)#3.0
print(a.imag)#4.0
print(type(a.real))# <class 'float'>
print(type(a.imag))# <class 'float'>

b = 6j
print(b)# 6j
print(type(b))#<class 'complex'>
print(b.real)#0.0
print(b.imag)#6.0
#print(5 + j6)#Error (a+bj) NameError: name 'j6' is not defined
#print(3 + 4i)#Error (a+bj)NameError: name '4i' is not defined
#print(4+j)#Error (a+bj) where j>=0 NameError: name 'j' is not defined
print(4+1j)#4+1j 
print(4+0j)#4+0j


#===========================================Bool=============================== 
a-True
print(a)#True
print(type(a))#<class 'bool'>
print(id(a))# Address of object 'a'
b = False
print(b)#False
print(type(b))#<class 'bool'>
#True - 1 and False - 0
print(True + True) # 1 + 1 = 2
print(True + False)# 1 + 0 = 1
print(False + True)# 0 + 1 = 1
print(False + False)# 0 + 0 = 0
print(True + True + True)# 1 + 1 + 1 = 3
print(25 + 10.8 + True) # 25 + 10.8 + 1 = 36.8
print(True > False) # True (1 > 0 = 1)
print(True)#True
print(False)#False
#print(true)#Error  NameError: name 'true' is not defined.
#print(false)#Error NameError: name 'true' is not defined.


#===========================================Types of Number Systerm(binary,decimal,octal,Hexa-Decimal)=============================== 

#===========================================Octal(0 to 7)=============================== 
a = 0O6247
print(a)
''' 8^3 8^2 8^1 8^0 
    6   2   4   7 
    512*6 + 64 * 2 + 8*4 + 1*7 = 3072 + 128 + 32 + 7 = 3239
'''
print(type(a))# <class 'int'>
print(id(a))# Address of object 'a'
b = 0o6247 
print(id(b)) # Same Address
print(b) # 3239
c = 3239
print(c) # 3239
print(id(c))# Same Address
#print(0o9248)# Error


#===========================================Hexa-Decimal(0 to 9 and A-10,B-11,C-12,D-13,E-14,F-15)=============================== 
a = 0XA7B9
print(a)
''' 16^3 16^2 16^1 16^0 
      A   7    B    9
    4096*10 + 256 * 7 + 16*11 + 1*9 = 40960 + 1792 + 176 + 9 = 42937
'''
print(type(a))
b = 0xBEEF
print(b)
''' 16^3 16^2 16^1 16^0 
      B   E    E    F
    4096*11 + 256 * 14 + 16*14 + 1*15 = 48879
'''
#print(A7B9)#Error
print('A7B9')#A7B9 
#print(0XBEER)#Error 'R'
#print(0XHYD)#Error 'H'
#print(0xA7G9B)#Error 'G'


#===========================================TypeCastingFunctions (int,float,complex,bool,oct,hex)=============================== 

#===========================================int()=============================== 
print(int(10.8))  # 10 -  Converts  float   object  10.8  to  int  object  10
print(int(True))  # 1  -  Converts  bool   object    True  to  int  object 1
print(int(False)) # 0  -  Converts  bool   object    False  to  int  object 0
print(int('25'))  # 25 -  Converts  bool   object    str  to  int  object 25
print(int('0075'))# 75 -  Converts  bool   object    str  to  int  object 75
print(int(0B11010))#  Converts  binary  object 11010  to  int  object 1
'''
    2^4  2^3  2^2  2^1  2^0
     1    1    0    1    0
    16*1 + 8*1 + 4*0 + 2*1 + 1*0 = 16 + 8 + 2 = 26

'''
print(0B11010)     # 26 
print(int(0O6247)) #  Converts  Octal   object 6247  to  int  object 3239
''' 8^3 8^2 8^1 8^0 
    6   2   4   7 
    512*6 + 64 * 2 + 8*4 + 1*7 = 3072 + 128 + 32 + 7 = 3239
'''
print(0O6247)      #  3239
print(int(0XA7B9)) #  Converts  Hexa-Decimal   object  A7B9  to  int  object 42937
''' 16^3 16^2 16^1 16^0 
      A   7    B    9
    4096*10 + 256 * 7 + 16*11 + 1*9 = 40960 + 1792 + 176 + 9 = 42937
'''
print(0XA7B9)      # 42937
#print(int(3 + 4j)) #Error  TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(int('25.4')) #Error  ValueError: invalid literal for int() with base 10: '25.4'
#print(int('Ten'))  #Error   ValueError: invalid literal for int() with base 10: 'Ten'


#===========================================float()=============================== 
print(float(25))     #25.0 - Converts  int  object  25  to  float  object   25.0
print(float(True))   #1.0 - Converts  bool  object   True   to  float  object   1.0
print(float(False))  #0.0 - Converts  bool  object   False   to  float  object   0.0
print(float('92'))   #92.0 - Converts  str  object   '92'   to  float  object   92.0
print(float('36.4')) #36.4 - Converts  str  object   '36.4'   to  float  object   36.4
print(float('0075')) #75.0 - Converts  str  object   '75'   to  float  object   75.0
print(float(0B1010101)) #  Converts  binary  object  1010101    to  float  object   85.0
'''
    2^6  2^5  2^4  2^3  2^2  2^1  2^0
     1    0    1    0    1    0    1
    64*1 + 32*0 + 16*1 + 8*0 + 4*1 + 2*0 + 1*1      = 64 + 16 + 4 + 1 = 85.0

'''
print(float(0O6247)) # Converts  Octal  object   6247   to  float  object   3239.0
print(float(0XA7B9)) # Converts  Hexa-Decimal  object   A7B9  to  float  object   42937.0
#print(float(3 + 4j)) # Error TypeError: float() argument must be a string or a real number, not 'complex'
#print(float('Ten'))  # Error  ValueError: could not convert string to float: 'Ten'


#===========================================complex()=============================== 
print(complex(3,4))#(3+4j)
print(complex(0,4))#4j
print(complex(3))#(3+0j)
print(complex(3.8,4.6))#(3.8+4.6j)
print(complex(3.8))#(3.8+0j)
print(complex(3,4.5))#(3+4.5j)
print(complex(True , False))#(1+0j)
print(complex(True))#(1+0j)
print(complex(False))#0j
print(complex(True , 4))#(1+4j)
print(complex('3'))#(3+0j)
print(complex('3.8'))#(3.8+0j)
#print(complex(3,'4'))#Error TypeError: complex() second arg can't be a string
#print(complex('3',4))#Error  TypeError: complex() can't take second arg if first is a string
#print(complex('3','4'))#Error TypeError: complex() can't take second arg if first is a string
#print(complex('Ten'))#Error    ValueError: complex() arg is a malformed string


#===========================================bool()=============================== 
print(bool(0)) #   False
print(bool(10)) #  True :  10  is  non-zero
print(bool(-25))#  True
print(bool(0.0))#  False
print(bool(0.1))#  True
print(bool(0 + 0j))# False
print(bool(10 + 20j))# True
print(bool(-15j))# True
print(bool('False'))# True 
print(bool(''))# False
print(bool('Hyd'))# True
print(bool(' '))# True 
print(bool('True'))# True 


#===========================================oct()=============================== 
print(oct(195))#0O303
'''
Number Quotient Reminder
195/8  24        3
24/8   3         0
3/8    0         3

Octal Number is 303 - Decimal to Octal   
'''
print(oct(0B10101110010))#0O2562
''' 421    421     421     421
    010    101     110     010 = 2562 - Binary to Octal
'''
print(oct(0xA7B9))#0O123671
'''
     8 4 2 1    8 4 2 1    8 4 2 1    8 4 2 1
        A         7           B          9
     1 0 1 0    0 1 1 1    1 0 1 1    1 0 0 1 - Hexa-Decimal to Binary 
     
     
     4 2 1    4 2 1     4 2 1      4 2 1      4 2 1     4 2 1
     
     0 0 1    0 1 0     0 1 1      1 1 0      1 1 1     0 0 1 = 123671 -  Binary to Octal
'''

#===========================================Hexa-Decimal()=============================== 

print(hex(25))#0X19
'''
Number Quotient Reminder
25/16  1         9
1/16   0         1

Hexa-Decimal Number is 19 - Decimal to Hexa-Decimal 
'''
print(hex(0B10101111010111))#0X2BD7
'''
    8 4 2 1   8 4 2 1   8 4 2 1    8 4 2 1
    0 0 1 0   1 0 1 1   1 1 0 1    0 1 1 1 = 2BD7 - Binary to Hexa-Decimal
'''
print(hex(0O6247))#0XCA7
'''
    4 2 1   4 2 1   4 2 1   4 2 1
      6       2       4       7
    1 1 0   0 1 0   1 0 0   1 1 1 - Octal to Binary

    
    8 4 2 1    8 4 2 1    8 4 2 1
    1 1 0 0    1 0 1 0    0 1 1 1 - CA7 - Binary to Hexa-Decimal 
'''













