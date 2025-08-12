#String
a="Rama Rao"
print(a)#Rama Rao
print(type(a))#<class 'str'>
print(id(a))#1320874296496
b='Hyd'
print(b)#Hyd
c='''Hyd is grren city.
Hyd is hitec city.
Hyd is Beautiful city.'''
print(c)
'''Hyd is grren city.
Hyd is hitec city.
Hyd is Beautiful city.'''

#Indexing
print(a[0])#H
print(a[1])#y
print(a[2])#d
print(a[3])#IndexError: string index out of range
print(a[-1])#d
print(a[-2])#y
print(a[-3])#H
print(a[-4]) #IndexError: string index out of range
print(a[0]==a[-3])#True
a[2]='c'#TypeError: 'str' object does not support item
print(25[0])#TypeError: 'int' object is not subscriptable
print('25'[0])#2
print(True[1])#TypeError: 'bool' object is not subscriptable
print('True'[1])#r

#Star Operator as Repeater
a='Hyd'
print(a*3)#HydHydHyd
print(a*2)#HydHyd
print(a*1)#Hyd
print(a*0)#Empty

print(a*-1)#empty

print(25*3)#75
print('25'*3)#252525
print('25'*4.0)#TypeError: can't multiply sequence by non-int of type 'float'
print(3*'Hyd')#HydHydHyd
print('25'*True)#25

#Length Function
print(3*'Hyd')#HydHydHyd
print('25'*True)#25
a='Hyd'
print(a,id(a))#Hyd 1635613762544
a=a*3
print(a,id(a))#HydHydHyd 1635613152432
print(len('Hyd'))#3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0
print(len(' '))#1
print(len(689))#TypeError: object of type 'int' has no len()

#multiple quotes
a=""""Hyd"""
print(a)#"Hyd
print(len(a))#4
print(a[0])#"
print("""Hyd"""")#SyntaxError: unterminated string literal (detected at line 1)
b=""""""Hyd"""
print(b)
print(len(b))#"""
#Slicing

a = 'Sankar Dayal Sarma'
print(a[7 : 12])#Dayal
print(a[7 : ])#Dayal Sarma
print(a[ : 6])#Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])#Sankar Dayal Sarma
print(a[1 : 10 : 2])#akrDy
print(a[0 : : 2])#Sna aa am
print(a[1 : : 2])#akrDylSra
print(a[-5 : -1])#Sarm
print(a[::-1])#amraS layaD raknaS
print(a[-1:-5:-1])#amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])#kar Dayal Sa
print(a[2 : -5])#nkar Dayal
print(a[-1:-5])#empty
print(a[3 : 3])#empty

#Input Functions
print(int(10.8))  #  Converts  float object  10.8  to  int  object  10
print(int(True))  #  Converts  bool object    True  to  int  object 1
print(int(False)) #0
print(int('25'))#25
print(int('0075'))#75
print(int(0B11010))#26
print(0B11010)#26
print(int(0O6247))#3239
print(0O6247)#3239
print(int(0XA7B9))#42937
print(0XA7B9)#42937
print(int(3 + 4j))#ERROR!TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print(int('25.4'))#ERROR!ValueError: invalid literal for int() with base 10: '25.4'

print(int('Ten'))#ValueError: invalid literal for int() with base 10: 'Ten'


print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))#0.0
print(float('92'))#92.0
print(float('36.4'))#36.4
print(float('0075'))#75.0
print(float(0B1010101))#85.0
print(float(0O6247))#3239.0
print(float(0XA7B9))#42937.0
print(float(3 + 4j))#TypeError: float() argument must be a string or a real number, not 'complex'

print(float('Ten'))#ValueError: could not convert string to float: 'Ten'


print(complex(3 , 4))#3+4j
print(complex(0 , 4))#4j
print(complex(3))#3+0j
print(complex(3.8 , 4.6))#3.8+4.6j
print(complex(3.8))#3.8+0j
print(complex(3 , 4.5))#3+4.5j
print(complex(True , False))#1+0j
print(complex(True))#1+0j
print(complex(False))#0j
print(complex(True , 4))#1+4j
print(complex('3'))#3+0j
print(complex('3.8'))#3.8+0j
print(complex(3 , '4'))#TypeError: complex() second arg can't be a string
print(complex('3' , 4))#TypeError: complex() can't take second arg if first is a string

print(complex('3' , '4'))#TypeError: complex() can't take second arg if first is a string
print(complex('Ten'))#ValueError: complex() arg is a malformed string      

print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))#True
print(bool(0.0))#False
print(bool(0.1))#True
print(bool(0 + 0j))#False
print(bool(10 + 20j))#True
print(bool(-15j))#True
print(bool('False'))#True
print(bool(''))#False
print(bool('Hyd'))#True
print(bool(' '))#True
print(bool('True'))#True
      
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))#10.8
print(str(3 + 4j))#3+4j
print(str(True))#True
print(str(False))#False
print(str(None))#None
      
print(oct(195))#0o303
print(oct(0B10101110010))#0o2562
print(oct(0xA7B9))#0o123671


print(hex(25))#0x19
print(hex(0B10101111010111))#0x2bd7
print(hex(0O6247))#0xca7
