
16/07/25


#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)        # Rama Rao
print(type(a))  # <class 'str'>   
print(id(a))    # Some Number 
b = 'Hyd'
print(b)        # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)  # Hyd is green city.
            Hyd is hitec city.
            Hyd is beautiful city.


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')   # a[0]
print(How  to  print  'y'  of  object  'a')   # a[1]
print(How  to  print  'd'  of  object  'a')   # a[2]
print(a[3])                                   # error len of string is 3
print(How  to  print  'd'  of  object  'a')   # a[2]
print(How  to  print  'y'  of  object  'a')   # a[1]
print(How  to  print  'H'  of  object  'a')   # a[0]
print(a[-4])                                  # error len of string is 3
print(a[0] ==  a[-3])                         # True
a[2] = 'c'
print(25[0])      # error i.e int has one value 
print('25'[0])    # 2
print(True[1])    # error i.e bool has only one value
print('True'[1])  # r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)  #HydHydHyd
print(a * 2)  #HydHyd
print(a * 1)  #Hyd
print(a * 0)  #
print(a * -1) #
print(25 * 3) #75
print('25' * 3)  #252525
print('25' * 4.0) #error str cannot multiply with float
print(3 * 'Hyd')  #HydHydHyd
print('25' * True)  #25


#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  # Hyd  some Number
a = a * 3
print(a , id(a))  # HydHydHyd some Number


# len()  function  (Home  work)
print(len('Hyd'))      # 3
print(len('Rama Rao')) # 8
print(len('9247'))     # 4
print(len(''))         # 0
print(len(' '))        # 1
print(len(689))        # error int has no length


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)      # "Hyd
print(len(a))  # 4
print(a[0])    # "
print("""Hyd"""")  # error
b = """""Hyd"""    
print(b)        # ""Hyd
print(len(b))   # 5


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  # Dayal
print(a[7 : ])    # Dayal Sarma
print(a[ : 6])    # Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])   # Sankar Dayal Sarma
print(a[1 : 10 : 2]) # ankar Daya
print(a[0 : : 2])    # Sna aa am
print(a[1 : : 2])    # akrDylSra
print(a[-5 : -1])    # S layaD raknaS
print(a[::-1])       # amraS layaD raknaS
print(a[-1:-5:-1])   # amraS
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])  # kar Dayal Sa
print(a[2 : -5])  # nkar Dayal 
print(a[-1:-5])   # empty due to default step is 1 but values are -ve
print(a[3 : 3])   # empty due to same begin and end

#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a     l                  S       a         r       m       a
#  -18    -17    -16   -15     -14    -13     -12           -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1 


#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # error due length is 1 but access 2 nd value
print(a[1:]) # empty


# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #  Converts bool object False to int object 0
print(int('25'))  # 25
print(int('0075')) # 75
print(int(0B11010)) # 26
print(0B11010)       # 26
print(int(0O6247))   # 3239
print(0O6247)        # 3239
print(int(0XA7B9))  # 42937
print(0XA7B9)       # 42937
print(int(3 + 4j))  # 
print(int('25.4'))
print(int('Ten'))


# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))  # 0.0
print(float('92'))   # 92.0
print(float('36.4')) # 36.4
print(float('0075')) # 75.0
print(float(0B1010101)) # 85
print(float(0O6247))   # 3239
print(float(0XA7B9))  # 42937
print(float(3 + 4j))  # error 
print(float('Ten'))  # error  


float()   function
# complex()  function  demo  program
print(complex(3 , 4))  # 3+4j
print(complex(0 , 4)) # 4j
print(complex(3))     # 3+0j
print(complex(3.8 , 4.6)) # 3.8+4.5j
print(complex(3.8))       # 3.8+0j
print(complex(3 , 4.5))   # 3+4.5j
print(complex(True , False)) # 1+0j
print(complex(True))          # 1+0j
print(complex(False))        # 0j
print(complex(True , 4))    # 1+4j
print(complex('3'))        #3+0j
print(complex('3.8'))      # 3.8+0j
print(complex(3 , '4'))    # error second cannot be str
print(complex('3' , 4))    # error if first is str second should not be given
print(complex('3' , '4'))  # error if first is str second should not be given
print(complex('Ten'))      # error


#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) # True
print(bool(0.0)) # False
print(bool(0.1))  #True
print(bool(0 + 0j)) #False
print(bool(10 + 20j)) # True
print(bool(-15j))     # True
print(bool('False')) # True
print(bool(''))      # False 
print(bool('Hyd'))   # True
print(bool(' '))     # True
print(bool('True'))  # True


bool()  function
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))   # 10.8
print(str(3 + 4j)) # 3+4j
print(str(True))   # True
print(str(False))  # False
print(str(None))   # None


What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
# oct()  function  demo  program
print(oct(195))          #  0o303
print(oct(0B10101110010)) # 0o2562
print(oct(0xA7B9)) # 42937
  

oct()  function
# hex()  function  demo  program
print(hex(25))    # 0o19
print(hex(0B10101111010111)) # 0010 1011 1101 0111
print(hex(0O6247))      # 1100 1010 0111