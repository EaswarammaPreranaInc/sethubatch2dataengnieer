#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)# Rama Rao 
print(type(a)) # <class 'str'>
print(id(a)) #address of object Rama Rao
b = 'Hyd' 
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#  Hyd is green City.
  #Hyd is hitec city.
  #Hyd is beautiful city.

a = 'Hyd'

print(a[0])     # H
print(a[1])     # y
print(a[2])     # d

# print(a[3])   # IndexError

print(a[-1])    # d
print(a[-2])    # y
print(a[-3])    # H

print(a[0] == a[-3])  # True

# a[2] = 'c'    # TypeError

# print(25[0])  # TypeError

print('25'[0])  # 2

# print(True[1])# TypeError

print('True'[1]) # r

a = 'Hyd'
print(a * 3)# 'HydHydHyd'
print(a * 2)      # 'HydHyd'
print(a * 1)      # 'Hyd'
print(a * 0)      # ''
print(a * -1)     # '' 

print(25 * 3)  # 25 * 3->75

print('25' * 3)#'25'*3->'252525'

# print('25' * 4.0)  # TypeError

print(3 * 'Hyd')  #'HydHydHyd'
print('25'*True) #'25'

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))# 0
print(int('25'))#25
print(int('0075')) #75
print(int(0B11010)) #26
print(0B11010) #26
print(int(0O6247)) #3247
print(0O6247) #3247
print(int(0XA7B9)) #42937
print(0XA7B9) #42937
#print(int(3 + 4j)) # Error
#print(int('25.4')) #Error
#print(int('Ten')) #Error

# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) # 0.0
print(float('92')) #92.0
print(float('36.4')) # 36.4
print(float('0075')) #75.0
print(float(0B1010101)) #85.0
print(float(0O6247)) #3247
print(float(0XA7B9)) # 42937
#print(float(3 + 4j)) #Error can't convert
#print(float('Ten')) #Error can't convert

print(hex(25)) #0x19
print(hex(0B10101111010111)) #0x15ea7
print(hex(0O6247)) # 0xcc7

print(oct(195)) # 0o303
print(oct(0B10101110010)) # 0o25562
print(oct(0xA7B9)) #0o123571

# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))  #  Converts   10.8  to  '10.8'
print(str(3 + 4j))  #  Converts   3+4j  to  '3+4j'
print(str(True))  #  Converts   True  to  'True'
print(str(False)) #  Converts   False  to  'False'
print(str(None))#  Converts   None  to  'None'

print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) #True
print(bool(0.0)) # False
print(bool(0.1)) #True
print(bool(0 + 0j))  # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) #True
print(bool('')) #False
print(bool('Hyd')) # True
print(bool(' ')) #False
print(bool('True')) #True

print(complex(3 , 4)) #3+4j
print(complex(0 , 4)) #4j
print(complex(3)) # 3+0j
print(complex(3.8 , 4.6)) # 3.8+4.6j
print(complex(3.8)) #3.8+0j
print(complex(3 , 4.5)) #3+4.5j
print(complex(True , False)) #1+0j
print(complex(True)) # 1+0j
print(complex(False)) #0j
print(complex(True , 4)) #1+4j
print(complex('3')) #3+0j
print(complex('3.8')) #3.8+0j
#print(complex(3 , '4')) #Error
#print(complex('3' , 4)) #Error
#print(complex('3' , '4')) #Error
#print(complex('Ten')) #Error











# Find outputs (Home work)
a = 'A'
#print(a[1])      # IndexError
print(a[1:]) # ''

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])        # Dayal
print(a[7 : ])          # Dayal Sarma
print(a[ : 6])          # Sankar
print(a[ : ])           # Sankar Dayal Sarma
print(a[:  : ])         # Sankar Dayal Sarma
print(a[1 : 10 : 2])    # aka a
print(a[0 : : 2])       # SnkrDylSrm
print(a[1 : : 2])       # aa a aa aa
print(a[-5 : -1])       # Sarm
print(a[::-1])          # amraS lay aD raknaS
print(a[-1:-5:-1])      # amra
print(a[ : : -2])       # aamSlyaaknS
print(a[3 : -3])        # kar Dayal Sa
print(a[2 : -5])        # nkar Dayal 
print(a[-1:-5])         # 
print(a[3:3])           #

# len() function (Home work)
print(len('Hyd')) # 3 
print(len('Rama Rao')) # 8 
print(len('9247'))  # 4 
print(len('')) # 0 
print(len(' ')) # 1
#print(len(689))#TypeError

# Find outputs (Home work)
a = 'Hyd'
print(a, id(a))    # Hyd address

a = a * 3
print(a, id(a))    # HydHydHyd address
