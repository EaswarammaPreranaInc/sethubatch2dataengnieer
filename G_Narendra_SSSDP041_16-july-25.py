#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # Address of string object (varies)
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
		 # Hyd is hitec city.
		 # Hyd is beautiful city.


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a'# print(a[0])
print(How  to  print  'y'  of  object  'a')# print(a[1])
print(How  to  print  'd'  of  object  'a')# print(a[2])
print(a[3])# Error due to index
print(How  to  print  'd'  of  object  'a')# print(a[-1])
print(How  to  print  'y'  of  object  'a')# print(a[-2])
print(How  to  print  'H'  of  object  'a')# print(a[-3])
print(a[-4])# Error due to index
print(a[0] ==  a[-3]) #True
a[2] = 'c' # Error due to stings are immutable
print(25[0])# non-sequences like integer does not have index
print('25'[0]) # 2
print(True[1])# non-sequences like bool does not have index
print('True'[1]) # r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)                # HydHydHyd
print(a * 2)                # HydHyd
print(a * 1)                # Hyd
print(a * 0)                # ''
print(a * -1)               # ''
print(25 * 3)               # 75
print('25' * 3)             # 252525
print('25' * 4.0)           # TypeError: can't multiply sequence by non-int of type 'float'
print(3 * 'Hyd')            # HydHydHyd
print('25' * True)          # 25 (True is treated as 1)


#  Find  outputs  (Home work)
a = 'Hyd'
print(a, id(a))             # Hyd <address of string object hyd>
a = a * 3
print(a, id(a))             # HydHydHyd <address of string object hydhydhyd>

# len()  function  (Home  work)
print(len('Hyd'))           # 3
print(len('Rama Rao'))      # 8 (includes space)
print(len('9247'))          # 4
print(len(''))              # 0
print(len(' '))             # 1
print(len(689))             # Error due to integer not support len function 


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # Error due to mismatched quotes
print(len(a)) #a not defined
print(a[0]) #a  not defined
print("""Hyd"""")# Error due to mismatched quotes
b = """""Hyd""" 
print(b) #"Hyd
print(len(b)) #4

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7:12]) # Dayal
print(a[7:]) # Dayal Sarma
print(a[:6]) # Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[::]) # Sankar Dayal Sarma
print(a[1:10:2]) # aka a
print(a[0::2]) # SnkrDylSrm
print(a[1::2]) # aar aa aa
print(a[-5:-1]) # Sarm
print(a[::-1]) # amraS lay a raknaS
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3:-3]) # kar Dayal Sar
print(a[2:-5]) # nkar Dayal S
print(a[-1:-5]) # '' (empty string, step defaults to +1 and goes backward)
print(a[3:3]) # '' (start == end)

 
#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error due to index 
print(a[1:]) # ''

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(10.8)) # 10
print(int(True)) # 1
print(int(False)) # 0
print(int('25')) # 25
print(int('0075')) # 75
print(int(0B11010)) # 26
print(0B11010) # 26
print(int(0O6247)) # 3255
print(0O6247) # 3255
print(int(0XA7B9))# 42937
print(0XA7B9) # 42937
print(int(3 + 4j)) # Error can not convert complex to int
print(int('25.4'))# Error invalid literal for int()
print(int('Ten'))# Error invalid literal for int()





'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) # 0.0
print(float('92')) # 92.0
print(float('36.4')) # 36.4
print(float('0075')) # 75.0
print(float(0B1010101)) # 85.0
print(float(0O6247)) # 3255.0
print(float(0XA7B9)) # 42937.0
print(float(3 + 4j)) #  Error can not convert complex to  float
print(float('Ten')) #  Error can not convert complex string to float






'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float

# complex()  function  demo  program
print(complex(3 , 4)) # (3+4j)
print(complex(0 , 4)) # 4j
print(complex(3)) # (3+0j)
print(complex(3.8 , 4.6)) # (3.8+4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3+4.5j)
print(complex(True , False)) # (1+0j)
print(complex(True)) # (1+0j)
print(complex(False)) # 0j
print(complex(True , 4)) # (1+4j)
print(complex('3')) # (3+0j)
print(complex('3.8')) # (3.8+0j)
print(complex(3 , '4')) # Error complex() second arg must be a number
print(complex('3' , 4)) # Error complex() can't take str and int
print(complex('3' , '4')) # Error
print(complex('Ten')) # Error could not convert string to complex


#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) # True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) # True (non-empty string is always True)
print(bool('')) # False
print(bool('Hyd')) # True
print(bool(' ')) # True (space is also a character)
print(bool('True')) # True



'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ? --->  False
    What  about  non-zero ?  --->  True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  --->  False
    What  about  non-empty  string ?  --->	True

4) When  is  x + yj  treated  as  False ?  --->  When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''

# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))# '10.8'
print(str(3 + 4j))# '(3+4j)'
print(str(True))# 'True'
print(str(False))# 'False'
print(str(None))# 'None'


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''

# oct()  function  demo  program
print(oct(195))# 0o303
print(oct(0B10101110010))# 0o1352
print(oct(0xA7B9))# 0o123671













'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number
													
													
# hex()  function  demo  program
print(hex(25))# 0x19
print(hex(0B10101111010111)) # 0x2bd7
print(hex(0O6247))# 0xaaf














'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number			

													 