#Strings

#  Find  outputs  (Home  work)
a = "Rama Rao"             #Ref  'a'  points to  object  "Rama  Rao"
print(a)                   #Rama Rao
print(type(a))             #<class 'str'>
print(id(a))               #Address  of  object   "Rama  Rao"
b = 'Hyd'                  #Ref  'b'  points to  object   'Hyd'
print(b)                   # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''  #  Multi line  string, without reference it is multiline comment
print(c)                   # Hyd is green city.  <next  line>  Hyd is hitec city.  <next  line>  Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print('Hyd'[0])         #Char  at  index  0  of  object 'Hyd'  i.e.  'H'
print('Hyd'[1])         #Char  at  index  1   of  object 'Hyd'  i.e.  'y'
print('Hyd'[2])         #Char  at  index  2   of  object 'Hyd'  i.e.  'd'
#print(a[3])            #IndexError: string index out of range, Index  3  does  not  exist   in  'Hyd'
print('Hyd'[-1])        #Char  at  index   -1    of  object 'Hyd'  i.e.  'd'
print('Hyd'[-2])        #Char  at  index   -2    of  object 'Hyd'  i.e.  'y'
print('Hyd'[-3])        #Char  at  index   -3    of  object 'Hyd'  i.e.  'H'
#print(a[-4])           #IndexError: string index out of range, Index  -4  does  not  exist   in  'Hyd'
print(a[0] ==  a[-3])   #'H' == 'H'  is  True
#a[2] = 'c'             #TypeError: 'str' object does not support item assignment, 'd' can not be replaced with 'c' as str object  is  immutable
#print(25[0])           #TypeError: 'int' object is not subscriptable, Non-sequence  (such  as  int)  is  not  indexed
print('25'[0])          #Char at index 0 of object '25' i.e. '2'
#print(True[1])         #TypeError: 'bool' object is not subscriptable, Non-sequence  (such  as  bool)  is  not  indexed
print('True'[1])        #Char  at  index  1   of  'True'    i.e.  'r'

#  Find  outputs  (Home work)
a = 'Hyd'           #ref a points to object 'Hyd'
print(a * 3)        #Repeats  string  thrice  i.e.  HydHydHyd
print(a * 2)        #Repeats  string  twice   i.e.  HydHyd
print(a * 1)        #Repeats  string  once   i.e.  Hyd
print(a * 0)        #Repeats  string   0  times    i.e.   Empty  string
print(a * -1)       #Repeats  string   -1   times    i.e.   Empty  string
print(25 * 3)       #75
print('25' * 3)     #252525
print('25' * 4.0)   #TypeError: can't multiply sequence by non-int of type 'float', must be int only
print(3 * 'Hyd')    #HydHydHyd
print('25' * True)  #Repeats string once  i.e.  25

#  Find  outputs  (Home work)
a = 'Hyd'         #ref a points to object 'Hyd'
print(a , id(a))  #Hyd<space>Address  of  'Hyd'
a = a * 3         #Ref 'a'  is  modified  to  a  new  string   object 'HydHydHyd'
print(a , id(a))  #HydHydHyd<space>Address, new address

# len()  function  (Home  work)
print(len('Hyd'))      #3
print(len('Rama Rao')) #8
print(len('9247'))     #4
print(len(''))         #0  due  to  empty  string
print(len(' '))        #1  due to  space
#print(len(689))       #TypeError: object of type 'int' has no len(), len() function arg should only be a sequence not non-sequence

# Find  outputs  (Home  work)
a = """"Hyd"""     #Excess  opening  quote  is  a  char  of  the  string
print(a)           #"Hyd
print(len(a))      #4
print(a[0])        #"
#print("""Hyd"""") #Error  due  to  excess  closing  quote
b = """""Hyd"""    #Excess  opening  quotes  are   characters  of  the  string
print(b)           #""Hyd
print(len(b))      #5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])     #a[7 : 12 : 1]  --->  string from indexes 7 to 11 in steps of 1 i.e. Dayal
print(a[7 : ])       #a[7:18:1] ----> string from index 7 to 17 insteps of 1 i.e.Dayal Sarma
print(a[ : 6])       #a[0:6:1] ---> string from index 0 to 5 in step of 1 i.e. Sankar
print(a[ : ])        #a[0:18:1] ---> string from index 0 to 17 instep of 1 i.e. Sankar  Dayal  Sarma
print(a[:  : ])      #a[0 : 18 : 1]  --->  string  from  indexes  0  to  17   in  steps  of   1  i.e.  Sankar  Dayal  Sarma
print(a[1 : 10 : 2]) #a[1:10:2] ---> string from indexes 1 to 9 in steps of 2 i.e.akrDy
print(a[0 : : 2])    #a[0:18:2] ---> string from indexes 0 to 17 in steps of 2 i.e.Sna<space>aa<space>am
print(a[1 : : 2])    #a[1:18:2] ---> string from indexes 1 to 17 in steps of 2 i.e. akrDylSra
print(a[-5 : -1])    #a[-5:-1:1] ---> string from indexes -5 to  -2   insteps of 1 i.e.Sarm
print(a[::-1])       #a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18   in  steps  of   -1  i.e.  Reverse  string
print(a[-1:-5:-1])   #string from indexes -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2])    #a[-1:-19:-2]--->string from indexes -1 to -18 in steps of -2 i.e. arSlyDrka
print(a[3 : -3])     #a[3 : -3 : 1]  --->  string  from  indexes  3  to  -4  in  steps  of   1  i.e.  kar<space>Dayal<space>Sa
print(a[2 : -5])     #a[2:-5:1] --->string from indexes 2 to -6 in steps of 1 i.e. nkar<space>Dayal<space>
print(a[-1:-5])      #a[-1:-5:1]--->string from indexes -1 to  -6 in steps of 1 i.e.  Empty string
print(a[3 : 3])      #a[3:3:1]--->string from indexes 3 to 2 in steps of 1 i.e.  Empty string

#  Find  outputs  (Home  work)
a =  'A'
#print(a[1]) #Error  becoz  index 1  does  not  exist  in  'A'
print(a[1:]) #String  without   1st   char  i.e.  '', also slicing will never give error 





#Type Conversion Functions

# bin()  function  demo  program
print(bin(25))      #0b11001, Converts int object 25 to binary str 
print(bin(0O6247))  #0b110010100111, converts int object 0O6247 to binary str
print(bin(0XA7B9))  #0b1010011110111001, converts int object 0xA7B9 to binary str
x = 0xA             #assigns ref x to int class object 0xA
print(x, type(x))   #10<space><class 'int'>
a = bin(0xA)        #assigns ref a to str class object '0b1010'
print(a)            #'0b1010', prints str
print(type(a))      #<class 'str'>     

#0b, 0o, 0x are int class objects only represented in that way
#bin, oct, hex are functions that coverts given number to str class object of that representation


#  bool()  function  demo  program
print(bool(0))         #False  due  to  0
print(bool(10))        #True :   10  is  non-zero
print(bool(-25))       #True  :  -25   is  non-zero
print(bool(0.0))       #False  due to  0.0
print(bool(0.1))       #True  :  0.1  is non-zero
print(bool(0 + 0j))    #False :  Both  real  and  imag  are  zeroes
print(bool(10 + 20j))  #True :  real  is  non-zero
print(bool(-15j))      #True :  imag  is  non-zero
print(bool('False'))   #True :  'False'  is  non-empty  string
print(bool(''))        #False  due  to  empty  string
print(bool('Hyd'))     #True  :  'Hyd'  is  a  non-empty  string
print(bool(' '))       #True  : ' '  is  non-empty  string
print(bool('True'))    #True  :  'True'  is  non-empty  string



# complex()  function  demo  program
print(complex(3 , 4))        #(3+4j)
print(complex(0 , 4))        #4j
print(complex(3))            #(3+0j)
print(complex(3.8 , 4.6))    #(3.8 + 4.6j)
print(complex(3.8))          #(3.8+0j)
print(complex(3 , 4.5))      #(3 + 4.5j)
print(complex(True , False)) #(1+0j)
print(complex(True))         #(1+0j)
print(complex(False))        #0j
print(complex(True , 4))     #(1+ 4j)
print(complex('3'))          #(3+0j)
print(complex('3.8'))        #(3.8+0j)
#print(complex(3 , '4'))     #TypeError: complex() second arg can't be a string
#print(complex('3' , 4))     #TypeError: complex() can't take second arg if first is a string
#print(complex('3' , '4'))   #TypeError: complex() can't take second arg if first is a string
#print(complex('Ten'))       #ValueError: complex() arg is a malformed string 
#complex can take either one string or both numbers


# float()  function  demo  program
print(float(25))        #Converts 25 to 25.0
print(float(True))      #Converts True to 1.0
print(float(False))     #Converts False to 0.0
print(float('92'))      #Converts '92' to 92.0
print(float('36.4'))    #Converts '36.4' to 36.4
print(float('0075'))    #Converts '0075' to 75.0
print(float(0B1010101)) #Converts binary number to decimal number i.e.  64 + 16 + 4 + 1 = 85.0
print(float(0O6247))    #Converts octal number to decimal number i.e.  6*8^3 + 2*8^2 + 4*8^1 + 7*8^0 = 3239.0
print(float(0XA7B9))    #Converts hexa-decimal number to decimal number i.e.  10*16^3 + 7*16^2 + 11*16^1 + 9*16^0 = 42937.0
#print(float(3 + 4j))   #TypeError: float() argument must be a string or a real number, not 'complex'
#print(float('Ten'))    #ValueError: could not convert string to float: 'Ten'



# hex()  function  demo  program
print(hex(25))                #Converts  decimal  number  to  hexa-decimal  number str  i.e.  0X19
print(hex(0B10101111010111))  #Converts  binary represented decimal  number  to  hexa-decimal  number str  i.e.  0x2BD7
print(hex(0O6247))            #Converts  octal decimal number  to  hexa-decimal  number str  i.e. 0xca7
print(type(hex(0O6247)))      #<class 'str'>



# int()  function  demo  program
print(int(10.8))    #  Converts  10.8  to  10
print(int(True))    #  Converts   True  to   1
print(int(False))   # Converts False to 0
print(int('25'))    #  Converts  '25'  to  25
print(int('0075'))  #  Converts  '0075'  to   75
print(int(0B11010)) #  Converts binary number to decimal number  i.e.  16 + 8  + 2 = 26
print(0B11010)      #  Converts binary number to decimal number  i.e.  16 + 8  + 2 = 26
print(int(0O6247))  #  Converts octal number to decimal number  i.e.  6*8^3 + 2*8^2 + 4*8^1 + 7*8^0  = 3239
print(0O6247)       #  Converts octal number to decimal number  i.e.  6*8^3 + 2*8^2 + 4*8^1 + 7*8^0  = 3239
print(int(0XA7B9))  #  Converts hexa-decimal number to decimal number i.e. 10*16^3 + 7*16^2 + 11*16^1 + 9*16^0 = 42937
print(0XA7B9)       #  Converts hexa-decimal number to decimal number i.e. 10*16^3 + 7*16^2 + 11*16^1 + 9*16^0 = 42937
#print(int(3 + 4j)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(int('25.4')) #ValueError: invalid literal for int() with base 10: '25.4' 
#print(int('Ten'))  #ValueError: invalid literal for int() with base 10: 'Ten'


# oct()  function  demo  program
print(oct(195))            #Converts  decimal  number  to  octal number string  i.e.  '0O303'
print(oct(0B10101110010))  #Converts  binary represented decimal number to  octal number string  i.e. '0O2562'
print(oct(0xA7B9))         #Converts  hexadecimal represented decimal number to octal number string  i.e. '0O123671'
print(type(oct(0xA7B9)))   #<class 'str'>


# str()  function  demo  program
print(str(25))      #Converts   25   to  '25'
print(str(10.8))    #Converts  10.8  to  '10.8'
print(str(3 + 4j))  #Converts  3+4j  to  '3+4j'
print(str(True))    #Converts   True    to  'True'
print(str(False))   #Converts   False  to  'False'
print(str(None))    #Converts  None  to  'None'
