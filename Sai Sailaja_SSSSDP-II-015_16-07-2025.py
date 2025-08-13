
#  Find  outputs  (Home  work)
a = "Rama Rao" # Ref 'a' points to object "Rama Rao"
print(a)  # Value of object 'a' i.e., "Rama Rao"
print(type(a))  # Type of the object 'a' i.e., <class 'str'>
print(id(a))  # Address of the object "Rama Rao"
b = 'Hyd' # Ref 'b' points to object 'Hyd'
print(b)  # Value of object 'b' i.e., 'Hyd'
c = '''Hyd is green city. 
Hyd is hitec city.
Hyd is beautiful city.''' # Ref 'c' points to object 'Hyd is green city.<nextline> Hyd is hitec city.<nextline>Hyd is beautiful city.'
print(c)  # Value of object 'c' i.e., 'Hyd is green city.<nextline> Hyd is hitec city.<nextline>Hyd is beautiful city.'



# Index   demo  program  (Home  work)
a = 'Hyd'  # Ref 'a' points to the object 'Hyd'
print(a[0])  # prints element of the string at index 0 i.e., 'H'
print(a[1])   # prints element of the string at index 1 i.e., 'y'
print(a[2])   # prints element of the string at index 2 i.e., 'd'
print(a[3])  # Error because object 'a' has only 3 characters i.e., index 0 to index 2,index 3 is out of range
print(a[-1])  # prints the element of the string at index -1 i.e., 'd'
print(a[-2])  # prints the element of the string at index -2 i.e., 'y'
print(a[-3])  # prints the element of the string at index -3 i.e., 'H'
print(a[-4])  # Error because object 'a' has only 3 characters i.e., index -1 to index -3,index -4 is out of range
print(a[0] ==  a[-3])  # prints 'True' because a[0] = 'H' and a[-3] = 'H'
a[2] = 'c' # Error because strings are immutable
print(25[0])  # Error because 25 should be enclosed by quotes to access the characters and 25 is int object and a non-sequence,non-sequence no index
print('25'[0])  # prints '2' because the index 0 of the string '25' is '2'
print(True[1])  #Error because True should be enclosed by quotes to access the characters and True is bool object and it is non-sequence, so it has no index
print('True'[1])  # prints 'r' because the index 1 of the string 'True' is 'r'



#  Find  outputs  (Home work)
a = 'Hyd' # Ref 'a' points to the object 'Hyd' 
print(a * 3)  # prints object 'a' thrice i.e.,'HydHydHyd'
print(a * 2)  # prints object 'a' twice i.e., 'HydHyd'
print(a * 1)  # prints object 'a' once i.e., 'Hyd'
print(a * 0)  # prints object 'a' 0 times i.e., ''
print(a * -1)  # prints object 'a' -1 times i.e., ''
print(25 * 3)  # 25 is multiplied by 3 and prints 75
print('25' * 3) # String '25' is repeated 3 times and prints 252525
print('25' * 4.0) # Error because it can not be multiplied by a float number 
print(3 * 'Hyd')  # prints 'Hyd' object 3 times i.e., 'HydHydHyd'
print('25' * True)  # prints '25' once because boolean True is treated as 1



#  Find  outputs  (Home work)
a = 'Hyd' # Ref 'a' points to the object 'Hyd'
print(a , id(a))  # prints 'Hyd' and address of the object 'Hyd'
a = a * 3 # String Hyd repetition and creates new address for the object 'HydHydHyd'
print(a , id(a)) # prints HydHydHyd<space>Address of object HydHydHyd



# len()  function  (Home  work)
print(len('Hyd')) # prints '3'
print(len('Rama Rao')) # prints '8'
print(len('9247'))  # prints '4'
print(len('')) # prints '0' because of empty string
print(len(' ')) # prints '1' because of space
print(len(689)) # Error because int has no length,'689' should be enclosed by quotes



# Find  outputs  (Home  work)
a = """"Hyd"""  # Ref 'a' points to object """"Hyd"""
print(a)  # prints "Hyd because it treates the extra " in the beginning as a character in string
print(len(a)) # prints '4' because object """"Hyd""" has 4 characters
print(a[0])  # prints " because the index 0 of the object """"Hyd""" is "
print("""Hyd"""") # Error because of quotes at the start can exceed but not at the end string
b = """""Hyd"""  # Ref 'b' points to object """""Hyd"""
print(b)  # prints ""Hyd because it treates the extra quotes in the beginning as characters in string
print(len(b)) # prints '5' because object """""Hyd""" has 5 characters



# Find  outputs
a = 'Sankar Dayal Sarma' # Ref 'a' points str object 'Sankar Dayal Sarma'
print(a[7 : 12]) # a[7 : 11 : 1] prints string from indexes 7 to 11 in steps of 1 i.e., Dayal
print(a[7 : ]) # a[7 : 18 : 1] prints string from indexes 7 to 17 steps of 1 i.e., Dayal<space>Sarma 
print(a[ : 6]) # a[0 : 6 : 1] prints string from indexes 0 to 5 in steps of 1 i.e., Sankar
print(a[ : ])  # a[0 : 18 : 1] prints string from indexes 0 to 17 in steps of 1 i.e., Sankar<space>Dayal<space>Sarma
print(a[:  : ]) # a[0 : 18 : 1] prints string from indexes 0 to 17 in steps of 1 i.e., Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2]) # a[1 : 10 : 2] prints string from indexes 1 to 9 in steps of 2  i.e., akrDy
print(a[0 : : 2]) # a[0 : 18 : 2] prints string from indexes 0 to 17 in steps of 2  i.e., Sna<space>aa<space>am
print(a[1 : : 2]) # a[1 : 18 : 2] prints string from indexes 1 to 17 in steps of 2 i.e., akrDylSra
print(a[-5 : -1]) # a[-5 : -1 : 1] prints string from indexes -5 to -2 in steps of 1 i.e., Sarm
print(a[::-1]) # a[-1 : -19 : -1] prints string from indexes -1 to -18 in steps of -1 i.e., amraS<space>layaD<space>raknaS
print(a[-1:-5:-1]) # a[-1 : -5 : -1] prints string from indexes -1 to -4 in steps of -1 i.e., amra
print(a[ : : -2]) # a[-1 :  -19 : -2] prints string from indexes -1 to -18 in steps of -2 i.e., arSlyDrka
print(a[3 : -3]) # a[3 : -3 : 1] prints string from indexes 3 to -2 in steps of 1 i.e., kar<space>Dayal<space>Sa
print(a[2 : -5]) # a[2 : -5 : 1] prints string from indexes 2 to -4 in steps of 1 i.e., nkar<space>Dayal
print(a[-1:-5]) # a[ -1 : -5 : 1]prints string from indexes -1  to -4 in steps of 1  i.e., <space> 
print(a[3 : 3]) # a[3 : 3 : 1] prints string from indexes 3 to 2 in steps of 1 i.e., <space>



#  Find  outputs  (Home  work)
a =  'A'  # Ref 'a' points to object 'A'
print(a[1]) # Error because index 1 is out of range and there is only one character in string and its index is 0
print(a[1:]) # prints space as the string has only one character and has index is 0



# int()  function  demo  program
print(int(10.8))  #  Converts float object  10.8  to  int  object  10
print(int(True))  #  Converts bool object True to int object 1
print(int(False)) #  Converts bool object False to int object 0
print(int('25'))  #  Converts str object '25' to  int  object 25
print(int('0075')) #  Converts str object '0075' to int object 75
print(int(0B11010))  #  Converts bin object 0B11010 to int object 26
print(0B11010)  # prints bin object 0B11010 directly to int object 26
print(int(0O6247)) #  Converts bin object 0O6247 to int object 3239
print(0O6247) # prints bin object 0O6247 directly to int  object 3239
print(int(0XA7B9)) #  Converts Hex object 0XA7B9 to int object 42937
print(0XA7B9) # prints hex object 0XA7B9 directly to int object 42937
print(int(3 + 4j))  # Error because complex number cannot be converted to int
print(int('25.4')) # Error because '25.4' is string float, so it cannot be converted to int
print(int('Ten'))  # Error because 'Ten' cannot be converted to int



# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) # converts bool object False to float object 0.0
print(float('92')) # converts str object '92' to float object 92.0
print(float('36.4')) # converts str object '36.4' to float object 36.4
print(float('0075')) # converts str object '0075' to float object 75.0
print(float(0B1010101)) # converts bin object 0B1010101 to float object 85.0
print(float(0O6247)) # converts octal object 0O6247 to float object 3239.0
print(float(0XA7B9)) # converts hex object 0XA7B9 to float object 42937.0
print(float(3 + 4j)) # Error because argument must be string or real number but not complex
print(float('Ten')) # Error because invalid string format cannot be converted to complex



# complex()  function  demo  program 
print(complex(3 , 4)) # Convert int object(3, 4) to  complex object i.e.,(3 + 4j)
print(complex(0 , 4)) # Converts int object(0, 4) to complex object i.e., 4j
print(complex(3))  # converts int object 3 to complex object i.e., (3 + 0j)
print(complex(3.8 , 4.6))  # converts float object (3.8, 4.6) to complex i.e., (3.8 + 4.6j)
print(complex(3.8))  # converts float object 3.8 to complex object i.e., (3.8 + 0j)
print(complex(3 , 4.5)) # converts to 3 + 4.5j
print(complex(True , False)) #converts bool object (True, False) to complex object i.e.,(1 + 0j)
print(complex(True)) # converts bool object True to complex object i.e., (1 + 0j)
print(complex(False)) # converts bool object False to complex object i.e., 0j
print(complex(True , 4))  # converts bool and int object (True, 4) to complex object i.e., (1 + 4j)
print(complex('3'))  # converts str object '3' to complex object i.e., (3 + 0j)
print(complex('3.8'))  # converts str object '3.8 to complex object i.e., (3.8 + 0j)
print(complex(3 , '4')) # Error because second argument cannot be a string
print(complex('3' , 4)) # Error because if first argument is string then second argument is not permitted
print(complex('3' , '4'))  # Error because if first argument is string then second argument is not permitted
print(complex('Ten'))  # Error because cannot convert string that has alphabets to complex ,invalid string format



#  bool()  function  demo  program
print(bool(0)) #   False because it is 0
print(bool(10)) # True :  10  is  non-zero
print(bool(-25))  # True : -25 is non-zero
print(bool(0.0)) #False because it is 0
print(bool(0.1)) # True because 0.1 is non-zero
print(bool(0 + 0j)) # False because both real and imag are zeroes
print(bool(10 + 20j)) # True because argument is non-zero
print(bool(-15j)) # True because argument is non-zero
print(bool('False'))  # True because argument is non empty string
print(bool('')) # False: empty string treated as zero
print(bool('Hyd')) # True because argument is non-empty string
print(bool(' ')) # True : space in string treated as non-zero
print(bool('True')) # True because argument is non-empty string



# oct()  function  demo  program
print(oct(195)) # converts int object 195 to octal object 0O303
print(oct(0B10101110010))  # converts bin object 0B10101110010 to octal object 0O2562
print(oct(0xA7B9)) # converts hex object 0xA7B9 to octal object 0O123671



# str()  function  demo  program
print(str(25))  #  Converts int object 25 to string object '25'
print(str(10.8)) # converts float object 10.8 to str object '10.8'
print(str(3 + 4j)) # converts complex object 3 + 4j to str object '(3 + 4j)'
print(str(True)) # converts bool object True to str object 'True'
print(str(False)) # converts bool object False to str object 'False'
print(str(None)) # converts NoneType object None to str object 'None'



# hex()  function  demo  program
print(hex(25)) # converts int object 25 to hex object 0X19
print(hex(0B10101111010111)) # converts bin object 0B10101111010111 to hex object 0X2bd7
print(hex(0O6247))  # converts octal object 0O6247 to hex object 0Xca7
 
