
 #  Find  outputs  (Home  work)
a = "Rama Rao" 
print(a) # output (Rama Rao)
print(type(a)) # class<str>
print(id(a)) # prints the address of a
b = 'Hyd'
print(b) # output (Hyd)
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # output (Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.)

 # Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')  # print (a(0))
print(How  to  print  'y'  of  object  'a')  # print (a(1))
print(How  to  print  'd'  of  object  'a')  # print (a(2))
print(a[3]) #error
print(How  to  print  'd'  of  object  'a')
print(How  to  print  'y'  of  object  'a')
print(How  to  print  'H'  of  object  'a')
print(a[-4])  # error
print(a[0] ==  a[-3]) 
a[2] = 'c' # error due to strings are immutable
print(25[0]) # error
print('25'[0]) # output 2
print(True[1]) # error
print('True'[1]) # output r

 #  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #output (HydHydHyd)
print(a * 2) # output (HydHyd)
print(a * 1)   #output (Hyd)
print(a * 0)  # output empty
print(a * -1) # output empty
print(25 * 3) # output 75
print('25' * 3) # output (252525)
print('25' * 4.0) # error 
print(3 * 'Hyd') # output (HydHydHyd)
print('25' * True) # output 25

 #  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # output (Hyd) and address of the str
a = a * 3
print(a , id(a)) # output (HydHydHyd) and address of this str

 # len()  function  (Home  work)
print(len('Hyd')) #output 3
print(len('Rama Rao')) #output 8
print(len('9247')) # output 4
print(len('')) #output 0
print(len(' ')) # output 1
print(len(689)) #output error

 # Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # output Hyd
print(len(a)) # output 3
print(a[0])  #output H
print("""Hyd"""") # output error
b = """""Hyd"""
print(b) # output Hyd
print(len(b))

 # Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ]) # Dayal Sarma
print(a[ : 6])# Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])  # Sankar Dayal Sarma
print(a[1 : 10 : 2]) # akrDy
print(a[0 : : 2])  # Sna<space>aa<space>am
print(a[1 : : 2]) # akrDylSra
print(a[-5 : -1]) # Sarm
print(a[::-1])  # amraS<space>layaD<space>raknaS
print(a[-1:-5:-1])  # amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])  # kar<space>Dayal<space>Sa
print(a[2 : -5])  #  nkar<space>Dayal<space>S
print(a[-1:-5])
print(a[3 : 3])  


#      0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#      S      a      n      k      a       r                       D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12         -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

 #  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # error
print(a[1:])
[16-07-2025 22:51] Nithish Dharmakari: # int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))  # converts bool object False to int object 0
print(int('25'))  # converts str to int 25
print(int('0075'))  # converts str to int 75
print(int(0B11010)) #converts binary to int
print(0B11010)  # converts binary to int 28
print(int(0O6247)) #  converts ocatal to int 3239
print(0O6247) 
print(int(0XA7B9))  # converts hexa decimal to int 42937
print(0XA7B9) 
print(int(3 + 4j)) 
print(int('25.4')) # error
print(int('Ten')) # error

 # complex()  function  demo  program
print(complex(3 , 4)) # output real 3 and imag 4
print(complex(0 , 4)) # real 0 and imag 4
print(complex(3)) # real 0
print(complex(3.8 , 4.6)) # real 3.8 and imag 4.6
print(complex(3.8)) # real 3.8
print(complex(3 , 4.5)) # real 3 and imag 4.5
print(complex(True , False)) # real 1 and imag 0
print(complex(True)) # real 1
print(complex(False)) # imag 0
print(complex(True , 4)) # real 1 and imag 4
print(complex('3')) # real 1
print(complex('3.8')) # real 3.8
print(complex(3 , '4')) # error  no because 2nd arg cannot be string
print(complex('3' , 4)) # error no because arg 2 is not permitted when arg1 is string
print(complex('3' , '4')) # error no because arg 2 is not permitted when arg1 is string
print(complex('Ten')) # error

 # float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))  # converts bool object False to float object 0.0
print(float('92'))  # converts string object 92 to float object 92.0
print(float('36.4')) # converts string object 36.4 to float 36.4
print(float('0075')) # converts string 75 to float 75.0
print(float(0B1010101)) # converts binary to float 85.0
print(float(0O6247)) # converts octal to float 3239.0
print(float(0XA7B9))  # converts hexa decimal to float 42937.0
print(float(3 + 4j)) # error complex cannot convert to float
print(float('Ten')) # error

#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) # True  non zero(negative)
print(bool(0.0)) # False float 0
print(bool(0.1)) # True non float
print(bool(0 + 0j)) # False zero complex numbers
print(bool(10 + 20j)) # True non zero complex number
print(bool(-15j)) # True non zero complex number
print(bool('False')) # True non empty string
print(bool('')) # False empty string
print(bool('Hyd')) # True non empty string
print(bool(' ')) # True non empty string
print(bool('True')) # True non empty string

 # str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # convert float to string '10.8'
print(str(3 + 4j)) # convert complex to string '3 + 4j'
print(str(True)) # convert bool to string 'True'
print(str(False)) # convert bool to string 'False'
print(str(None)) # convert none type to string 'None'