#  Find  outputs  (Home  work)

a = "Rama Rao"
print(a)         # Prints the String Rama Rao
print(type(a))   # Prints the type of a, which is <class 'str'>
print(id(a))     # Prints the address of the object a
b = 'Hyd'
print(b)         # Prints the String Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)         # Prints the Multi line String of C Which is 
		   Hyd is green city.
		   Hyd is hitec city.
		   Hyd is beautiful city.


# Index   demo  program  (Home  work)

a = 'Hyd'
print(How  to  print  'H'  of  object  'a')  # a[0]
print(How  to  print  'y'  of  object  'a')  # a[1]
print(How  to  print  'd'  of  object  'a')  # a[2]
print(a[3])                                  # Error due to string index out of range
print(How  to  print  'd'  of  object  'a')  # a[-1] 
print(How  to  print  'y'  of  object  'a')  # a[-2] 
print(How  to  print  'H'  of  object  'a')  # a[-3] 
print(a[-4])                                 # Error due to string index out of range
print(a[0] ==  a[-3])                        # Prints True because 'H' == 'H'
a[2] = 'c'                                   # Error because strings are immutable
print(25[0])                                 # Error because of int object
print('25'[0])                               # prints '2' from the string '25'
print(True[1])                               # Error because of bool object
print('True'[1])                             # prints 'R' from the string 'TRUE'


#  Find  outputs  (Home work)

a = 'Hyd'               
print(a * 3)           # Prints 'HydHydHyd'
print(a * 2)           # Prints 'HydHyd'
print(a * 1)           # Prints 'Hyd'
print(a * 0)           # Prints empty String ''
print(a * -1)          # Prints empty String '' negative repetition
print(25 * 3)          # Prints 75
print('25' * 3)        # Prints '252525'
print('25' * 4.0)      # Error because float can't be multiply with the string
print(3 * 'Hyd')       # Prints 'HydHydHyd' 
print('25' * True)     # '25' → True = 1, so string is repeated once


#  Find  outputs  (Home work)

a = 'Hyd'              
print(a , id(a))       # Prints the value of 'a' and its address
a = a * 3              # Reassigns 'a' to a new string: 'HydHydHyd'
print(a , id(a))       # Prints the value of 'a' and its new address


# len()  function  (Home  work)

print(len('Hyd'))        # Prints the Length of 'Hyd' which is 3
print(len('Rama Rao'))   # Prints the Length of 'Rama Rao' which is 7 
print(len('9247'))       # Prints the Length of '9247' which is 4
print(len(''))           # Prints the 0 because of the empty string
print(len(' '))          # Prints the Length of ' ' <space> which is 1
print(len(689))          # Error because of int doesn't have length property 


# Find  outputs  (Home  work)

a = """"Hyd"""           # Error because starts with 4 double quotes
print(a)                 # This line will never execute because the code above has a error
print(len(a))            # This line will never execute because the code above has a error
print(a[0])              # This line will never execute because the code above has a error
print("""Hyd"""")        # Error because ends with 4 double quotes
b = """""Hyd"""          # Error because starts with 5 double quotes
print(b)                 # This line will never execute because the code above has a error
print(len(b))            # This line will never execute because the code above has a error


# Find  outputs

a = 'Sankar Dayal Sarma'
print(a[7 : 12])         # Prints characters from index 7 to 11 in steps of 1 i.e. 'Dayal'
print(a[7 : ])           # Prints characters from index 7 to end in steps of 1 i.e. 'Dayal Sarma'
print(a[ : 6])           # Prints characters from start to index 5 in steps of 1 i.e. 'Sankar'
print(a[ : ])            #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])          #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2])     # Prints characters from index 1 to 9 in steps of 2 ---> 'akrDy'
print(a[0 : : 2])        # Prints characters from index 0 to end in steps of 2 ---> 'Sna<space>aa<space>am'
print(a[1 : : 2])        # Prints characters from index 1 to end in steps of 2 ---> 'akrDylSra'
print(a[-5 : -1])        # Prints characters from index -5 to -2 in steps of -1 ---> 'Sarm'
print(a[::-1])           # Prints reverse of the string → 'amraS lay aD raknaS'
print(a[-1:-5:-1])       # Prints characters from index -1 to -4 in steps of -1 ---> 'amra'
print(a[ : : -2])        # a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])         # Prints characters from index 3 to index 14 excluding -3 ---> 'ayal<space>Sa'
print(a[2 : -5])         # Prints characters from index 2 o index 14 excluding -5---> 'nkar<space>Daya'
print(a[-1:-5])          # Prints empty string
print(a[3 : 3])          # Prints empty string


#  Find  outputs  (Home  work)

a =  'A'
print(a[1])     # Error because string index out of range
print(a[1:])    # prints empty string


# int()  function  demo  program

print(int(10.8))        #  Converts  float   object  10.8  to  int  object  10
print(int(True))        #  Converts  bool   object    True  to  int  object 1
print(int(False))       #  Converts  bool   object    False to int  object 0
print(int('25'))        #  Converts string '25' to int 25
print(int('0075'))      #  Converts string '0075' to int  75
print(int(0B11010))     #  Converts Binary literal 0B11010 to  int  object 26
print(0B11010)          #  Prints decimals equivalent of 0B11010 = 26
print(int(0O6247))      #  Converts Octal literal 0O6247 to  int  object 3247
print(0O6247)           #  Prints decimals equivalent of 0O6247 = 3247
print(int(0XA7B9))      #  Converts Hex literal 0xA7B9 to  int  object 42937
print(0XA7B9)           #  Prints decimals equivalent of 0xA7B9 = 42937
print(int(3 + 4j))      #  Error can't convert complex to int
print(int('25.4'))      #  Error because string '25.4' is not a valid integer
print(int('Ten'))       #  Error because string 'Ten' is not a valid integer


# float()  function  demo  program
print(float(25))           # Converts int object  25  to  float  object   25.0
print(float(True))         # Converts bool object True to float object 1.0
print(float(False))        # Converts bool False object to float object 0.0
print(float('92'))         # Converts string object '92' to float object 92.0
print(float('36.4'))       # Converts string object '36.4' to float object 36.4
print(float('0075'))       # Error leading zeros in strings are not allowed unless it's '0'
print(float(0B1010101))    # Binary 0B1010101 = 85  converts to float  85.0
print(float(0O6247))       # Octal 0O6247 = 3247  converts to float 3247.0
print(float(0XA7B9))       # Hex 0xA7B9 = 42937  converts to float 42937.0
print(float(3 + 4j))       # Error can't convert complex to float
print(float('Ten'))        # Error string 'Ten' is not a valid number


# complex() function demo program

print(complex(3 , 4))           # Prints complex number: (3+4j)
print(complex(0 , 4))           # Prints complex number: (0+4j)
print(complex(3))               # Prints Only real part given (3+0j)
print(complex(3.8 , 4.6))       # Prints Both parts are floats (3.8+4.6j)
print(complex(3.8))             # Prints Only real part  (3.8+0j)
print(complex(3 , 4.5))         # Prints (3+4.5j)
print(complex(True , False))    # True = 1, False = 0 → (1+0j)
print(complex(True))            # True = 1 → (1+0j)
print(complex(False))           # False = 0 → (0+0j)
print(complex(True , 4))        # True = 1 → (1+4j)
print(complex('3'))             # Prints complex number: (3+0j)


# bool() function demo program

print(bool(0))            # False = 0 is considered False in boolean context
print(bool(10))           # True = Any non-zero number is True
print(bool(-25))          # True = Negative numbers are also non-zero, so True
print(bool(0.0))          # False = 0.0 is false
print(bool(0.1))          # True = Non-zero float is True
print(bool(0 + 0j))       # False = Complex number with 0 real and imaginary parts is False
print(bool(10 + 20j))     # True = Non-zero complex number is True
print(bool(-15j))         # True = Imaginary part is non-zero  True
print(bool('False'))      # True = Non-empty string  True 
print(bool(''))           # False = Empty string is False
print(bool('Hyd'))        # True = Non-empty string is True
print(bool(' '))          # True = A space is still a non-empty string is True
print(bool('True'))       # True = Non-empty string is True


# str() function demo program

print(str(25))           # Converts int 25 to string '25'
print(str(10.8))         # Converts float 10.8 to string '10.8'
print(str(3 + 4j))       # Converts complex number to string '(3+4j)'
print(str(True))         # Converts boolean True to string 'True'
print(str(False))        # Converts boolean False to string 'False'
print(str(None))         # Converts NoneType to string 'None'


# oct() function demo program

print(oct(195))               # Converts decimal 195 to octal '0o303'
print(oct(0B10101110010))     # Binary 0B10101110010 to octal '0o2612'
print(oct(0xA7B9))            # Hex 0xA7B9 to octal '0o123671'


# hex() function demo program

print(hex(25))                   # Converts decimal 25 to hex = '0x19'
print(hex(0B10101111010111))     # Binary 0B10101111010111 = 5615 → hex of 5615 = '0x15d7'
print(hex(0O6247))               # Octal 0O6247 = 3247 (decimal) → hex of 3247 = '0xcbf'
