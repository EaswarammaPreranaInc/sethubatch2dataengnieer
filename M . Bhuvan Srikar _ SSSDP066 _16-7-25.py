#  Find  outputs  (Home  work)
a = "Rama Rao" # reference a is assigned with string object 'Rama Rao' 
print(a) # Rama<space>Rao
print(type(a)) # <class 'str'>
print(id(a)) # address of Rama Rao
b = 'Hyd' # reference b is assigned with string object 'Hyd' 
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) 
 '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''

# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0]) #  How  to  print  'H'  of  object  'a')
print(a[1]) # How  to  print  'y'  of  object  'a')
print(a[2]) # How  to  print  'd'  of  object  'a')
print(a[3]) # error as index is out of range
print(a[-3]) # How  to  print  'd'  of  object  'a')
print(a[-2]) # How  to  print  'y'  of  object  'a')
print(a[-1]) # How  to  print  'H'  of  object  'a')
print(a[-4]) # error as index is out of range
print(a[0] ==  a[-3]) # True
a[2] = 'c' # error as string object cannot be modified
print(25[0]) # error as int object is not sub-scriptable
print('25'[0]) # 2
print(True[1]) # error as bool object is not sub-scriptable
print('True'[1]) # r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # 'HydHydHyd'
print(a * 2) # 'HydHyd'
print(a * 1) # 'Hyd'
print(a * 0) # '' (empty string)
print(a * -1) # '' (empty string)
print(25 * 3) # 75 
print('25' * 3) # '252525'
print('25' * 4.0) # error as repetition can be done with integer only 
print(3 * 'Hyd') # integer cannot be multiplied with string object
print('25' * True) # error as repetition can be done with integer only 


#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # 'Hyd' , address of Hyd
a = a * 3 # Hyd is repeated 3 times
print(a , id(a)) # 'HydHydHyd', address of 'HydHydHyd'


# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # error as len function is for only sequence


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # "
print("""Hyd"""") # error as there is one extra "
b = """""Hyd"""
print(b) # ""Hyd
print(len(b)) # 5


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # a[7 : 12 : 1] ---> string from indexes 7 to 11 in step of 1 i.e. Dayal
print(a[7 : ]) # a[7  : 18 : 1] ---> string from indexes 7 to 17 in step of 1 i.e. Dayal<space>Sarma
print(a[ : 6]) # a[0 :6 :1] ---> string from 0 to 5 in step of 1 i.e. Sankar
print(a[ : ])  # a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])  # a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2]) # a[1 : 10 : 2] ---> string from indexes 1 to 9 in step of 2 i.e. akrDy
print(a[0 : : 2]) # a[0 : 18 : 2] ---> string from 0 to 17 in steps of 2 i.e. Sna<space>aa<space>am
print(a[1 : : 2]) # a[1 : 18 : 2] ---> string from 1 to 17 in steps of 2 i.e. akrDylSra
print(a[-5 : -1]) # a[-5 : -1 : 1] ---> string from -5 to -1 in step of 1 i.e. Sarma
print(a[::-1]) # a[-1 : -19 : -1] ---> string from -1 to -18 in step of -1 i.e. amraS<space>layaD<space>raknaS
print(a[-1:-5:-1]) # a[-1 : -5 : -1] ---> string from -1 to -4 in step of -1 i.e. amra 
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) # a[3 : -3 : 1] ---> string from 3 to -2 in step of 1 i.e. kar<space>Dayal<space>Sa
print(a[2 : -5]) # a[2 : -5 : 1] --> string from 2 to -4 in step of 1  i.e. nkar<space>Dayal<space>Sa
print(a[-1:-5]) # a[-1 : -5 : 1] ---> '' (empty string)
print(a[3 : 3]) # a[3 : 3 : 1] ---> '' (empty string)



#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # error as index is out of range
print(a[1:]) # '' (empty string)


# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))  #  Converts  bool   object False  to  int  object 0
print(int('25')) # converts string 25 to int object 25
print(int('0075')) # converts string 0075 to int object 0075
print(int(0B11010)) # converts to 26
print(0B11010) # 26
print(int(0O6247)) # 3236
print(0O6247) # 3236
print(int(0XA7B9)) # converts to int 42937
print(0XA7B9) # converts to int 42937
print(int(3 + 4j)) # error as complex number cannot be converted to integer
print(int('25.4')) # error as 25.4 is float
print(int('Ten')) # error as there is no object Ten


# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))   #  Converts  bool   object False  to  float  object 0.0
print(float('92')) # converts string 92 to float 92
print(float('36.4')) # converts string '36.4' to float 36.4
print(float('0075')) # converts to float 75.0
print(float(0B1010101)) # converts to float 85.0
print(float(0O6247)) # converts to float 3236
print(float(0XA7B9)) # converts to float 42937
print(float(3 + 4j)) # error as complex number cannot be converted to float
print(float('Ten')) # error as there is no object Ten



# complex()  function  demo  program
print(complex(3 , 4)) # converts to complex number 3 + 4j
print(complex(0 , 4)) # converts to complex number 4j
print(complex(3)) # converts to complex number 3 + 0j
print(complex(3.8 , 4.6)) # converts to complex number 3.8 + 4.6j
print(complex(3.8)) # converts to complex number 3.8 + 0j
print(complex(3 , 4.5)) # converts to complex number 3 + 4.5j
print(complex(True , False)) # converts to complex number 1 + 0j
print(complex(True)) # converts to complex number 1 + 0j
print(complex(False)) # converts to complex number 0j
print(complex(True , 4)) # converts to complex number 1 + 4j
print(complex('3')) # converts to complex number 3 + 0j
print(complex('3.8')) # converts to complex number 3.8 + 0j
print(complex(3 , '4')) # error as 2nd argument is string
print(complex('3' , 4)) # converts to complex number 3 + 4j
print(complex('3' , '4')) # error as both arguments are strings
print(complex('Ten')) # error as there is no Ten object


#  bool()  function  demo  program
print(bool(0)) # False
print(bool(10)) # True :  10  is  non-zero
print(bool(-25)) # True :  10  is  non-zero
print(bool(0.0)) # False
print(bool(0.1)) # True :  0.1  is  non-zero
print(bool(0 + 0j)) # False
print(bool(10 + 20j))  # True :  10 + 20j  is  non-zero
print(bool(-15j)) # True :  -15j is  non-zero
print(bool('False')) # False
print(bool('')) # False
print(bool('Hyd')) # True :  Hyd  is  non-zero
print(bool(' ')) # True becoz of space
print(bool('True')) # True



# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # converts 10.8 to '10.8'
print(str(3 + 4j)) # converts 3 + 4j to '3 + 4j'
print(str(True)) # converts True to 'True'
print(str(False)) # converts False to 'False'
print(str(None)) # converts None to 'None'



# oct()  function  demo  program
print(oct(195)) # converts to octal number 0o303
print(oct(0B10101110010))  # converts to octal number 0o2562
print(oct(0xA7B9)) # converts to octal number 0o123671


# hex()  function  demo  program
print(hex(25)) # converts to hexa decimal 0x19
print(hex(0B10101111010111))  # converts to hexa decimal 0x2bd7
print(hex(0O6247))  # converts to hexa decimal 0xca7



