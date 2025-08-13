
#first program
a = "Rama Rao"
print(a)
print(type(a))
print(id(a))
b = 'Hyd'
print(b)
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)

#second program
# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])
print(a[1])
print(a[2])
#print(a[3])
print(a[-1])
print(a[-2])
print(a[-3])
#print(a[-4])
print(a[0] ==  a[-3])
#a[2] = 'c'
#print(25[0])
print('25'[0])
#print(True[1])
print('True'[1])

#third program
a = 'Hyd'
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
print(25 * 3)
print('25' * 3)
#print('25' * 4.0)
print(3 * 'Hyd')
print('25' * True)

#fourth program
a = 'Hyd'
print(a , id(a))
a = a * 3
print(a , id(a))

#fifth program
# len()  function  (Home  work)
print(len('Hyd'))
print(len('Rama Rao'))
print(len('9247'))
print(len(''))
print(len(' '))
#print(len(689))

#sixth program
a = """"Hyd"""
#print(a)
print(len(a))
print(a[0])
#print("""Hyd"""")
b = """""Hyd"""
print(b)
print(len(b))

#seventh program
a = 'Sankar Dayal Sarma'
print(a[7 : 12])
print(a[7 : ])
print(a[ : 6])
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])
print(a[1 : 10 : 2])
print(a[0 : : 2])
print(a[1 : : 2])
print(a[-5 : -1])
print(a[::-1])
print(a[-1:-5:-1])
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])
print(a[2 : -5])
print(a[-1:-5])
print(a[3 : 3])


#eighth program
a =  'A'
#print(a[1])
print(a[1:])

#ninth program
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))
print(int('25'))
print(int('0075'))
print(int(0B11010))
print(0B11010)
print(int(0O6247))
print(0O6247)
print(int(0XA7B9))
print(0XA7B9)
#print(int(3 + 4j))
#print(int('25.4'))
#print(int('Ten'))

# tenth program
# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))
print(float('92'))
print(float('36.4'))
print(float('0075'))
print(float(0B1010101))
print(float(0O6247))
print(float(0XA7B9))
#print(float(3 + 4j))
#print(float('Ten'))

# eleventh program
# complex()  function  demo  program
print(complex(3 , 4))
print(complex(0 , 4))
print(complex(3))
print(complex(3.8 , 4.6))
print(complex(3.8))
print(complex(3 , 4.5))
print(complex(True , False))
print(complex(True))
print(complex(False))
print(complex(True , 4))
print(complex('3'))
print(complex('3.8'))
#print(complex(3 , '4'))
#print(complex('3' , 4))
#print(complex('3' , '4'))
#print(complex('Ten'))

# twelfth program
#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))
print(bool(0.0))
print(bool(0.1))
print(bool(0 + 0j))
print(bool(10 + 20j))
print(bool(-15j))
print(bool('False'))
print(bool(''))
print(bool('Hyd'))
print(bool(' '))
print(bool('True'))


#thirteenth program
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))
print(str(3 + 4j))
print(str(True))
print(str(False))
print(str(None))


#fourteenth program
# oct()  function  demo  program
print(oct(195))
print(oct(0B10101110010))
print(oct(0xA7B9))

# fifteenth program
# hex()  function  demo  program
print(hex(25))
print(hex(0B10101111010111))
print(hex(0O6247))

