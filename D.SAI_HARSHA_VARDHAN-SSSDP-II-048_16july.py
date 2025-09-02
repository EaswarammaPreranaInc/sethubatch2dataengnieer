# Find outputs (Home work)
a = "Rama Rao"
print(a) # prints the value of string object ‘a’ i.e. “Rama Rao”
print(type(a)) # prints the type of object a i.e. <class ‘str’>
print(id(a)) # prints the address of object a i.e. 212891287399 (Random Number)
b = 'Hyd'
print(b) # prints the value of string object ‘b’ i.e. “Hyd”
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # prints the value of multi line string object ‘c’ 
# Index demo program (Home work)0
a = 'Hyd'
#print(How to print 'H' of object 'a') # error invalid syntax the string should be in quotes (single, double, triple)
#print(How to print 'y' of object 'a') # error invalid syntax the string should be in quotes (single, double, triple)
#print(How to print 'd' of object 'a') # error invalid syntax the string should be in quotes (single, double, triple)
#print(a[3]) # error because the index is exceeded 
print(a[2])#How to print 'd' of object 'a'
print(a[1]) # How to print 'y' of object 'a'
print(a[0]) # How to print 'H' of object 'a'
#print(a[-4]) # error because the index is exceeded it is only implement up to a[-3]
print(a[0] == a[-3]) # prints True because a[0] == a[-3] i.e. ‘H’
#a[2] = 'c' # error because string does not support updating it is immutable
#print(25[0]) #error because indexing is not work on int type 
print('25'[0]) # prints the value 2 as it is the first index value
#print(True[1]) #error because indexing is not in bool type
print('True'[1]) #prints r as it is the value of ‘True’[1]
# Find outputs (Home work)
a = 'Hyd'
print(a * 3) #prints the ‘Hyd’*3 i.e. ‘HydHydHyd’
print(a * 2) #prints the ‘Hyd’*2 i.e. ‘HydHyd’
print(a * 1) #prints the ‘Hyd’*1 i.e. ‘Hyd’
print(a * 0) # prints empty string because ‘Hyd’*0 is zero
print(a * -1) # prints empty string because ‘Hyd’*-1 is invalid
print(25 * 3) #prints the value 75 because 25*3 = 75
print('25' * 3) #prints the ‘25’*3 i.e. ‘252525’
#print('25' * 4.0) # error because string * float is invalid
print(3 * 'Hyd') #prints the 3 * ‘Hyd’i.e. ‘HydHydHyd’
print('25' * True) #prints 25 as True is treated as 1
# Find outputs (Home work)
a = 'Hyd'
print(a , id(a)) #prints the value of string object ‘a’ and address of object ‘a’ i.e. Hyd 1499724703792
a = a * 3
print(a , id(a)) #print the value of string object ‘a’ and address of object ‘a’ i.e. HydHydHyd 1499717968496
# len() function (Home work)
print(len('Hyd')) #prints the length of string object i.e. 3
print(len('Rama Rao')) #prints the length of string object i.e. 8
print(len('9247')) #prints the length of string object i.e. 4
print(len('')) # prints empty string object i.e. 0
print(len(' ')) #prints empty string object space character counts i.e. 1
#print(len(689)) #error because string should be in quotes
# Find outputs (Home work)
a = """"Hyd"""
print(a) #print H y d
print(len(a)) #3
print(a[0]) #H
#print("""Hyd"""") # error because the double quotes are not balanced
b = """""Hyd"""
print(b) # error because the double quotes are not balanced
print(len(b)) #this line wont work because of above statement
# Find outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #prints the value of string object ‘a’ from index 7 to 12 i.e. Dayal
print(a[7 : ]) #prints the value of string object ‘a’ from index 7 to len(a)+1 i.e. Dayal Sharma
print(a[ : 6]) #prints the value of string object ‘a’ from index 0 to 6 i.e. Sankar
print(a[ : ]) # a[ 0 : 18 : 1] ---> string from indexes 0 to 17 in steps of 1 i.e. Sankar<space>Dayal<space>Sarma
print(a[: : ]) # print from default values from index 0 to len(a)+1 in steps of 1 i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2]) #prints the value of string object ‘a’ from index 1 to 10 in steps of 2 i.e. akrDy
print(a[0 : : 2]) #prints the value of string object ‘a’ from index 0 to len(a)+1 in steps of 2 i.e. Sna<space>aa<space>am
print(a[1 : : 2]) #prints the value of string object ‘a’ from index 1 to len(a)+1 in steps of 2 i.e. akrDylSra
print(a[-5 : -1]) #prints the value of string object ‘a’ from index -5 to -len(a)-1 in steps of -1 i.e. Sarm
print(a[::-1]) #prints reverse of the entire string i.e. amraS layaD raknaS
print(a[-1:-5:-1]) #prints the value of string object ‘a’ from index -1 to -5 in steps of -1 i.e. amra
print(a[ : : -2]) # a[-1 : -19 : -2] ---> string from indexes -1 to -18 in steps of -2 i.e. arSlyDrka
print(a[3 : -3]) # prints 'kar Dayal Sar'
print(a[2 : -5]) # prints 'nkar Dayal S'
print(a[-1:-5]) # prints empty string
print(a[3 : 3]) # prints empty string
# Find outputs (Home work)
a = 'A'
#print(a[1]) # error index out of range
print(a[1:]) # prints an empty string
# int() function demo program
print(int(10.8)) # Converts float object 10.8 to int object 10
print(int(True)) # Converts bool object True to int object 1
print(int(False)) # Converts bool object False to int object 0
print(int('25')) # converts string object ‘25’ to int object 25
print(int('0075')) # converts string object ‘0075’ to int object 0075
print(int(0B11010)) # converts binary object to int object 26
print(0B11010) #26
print(int(0O6247)) #3247
print(0O6247) #3247
print(int(0XA7B9)) #42937
print(0XA7B9) #42937
#print(int(3 + 4j)) #Error
#print(int('25.4')) #Error
#print(int('Ten')) #Error
# float() function demo program
print(float(25)) # Converts int object 25 to float object 25.0
print(float(True)) # Converts bool object True to float object 1.0
print(float(False)) # 0.0
print(float('92')) #92.0
print(float('36.4')) # 36.4
print(float('0075')) #75.0
print(float(0B1010101)) #85.0
print(float(0O6247)) #3247
print(float(0XA7B9)) # 42937
#print(float(3 + 4j)) #Error can't convert
#print(float('Ten')) #Error can,t convert
# complex() function demo program
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
#print(complex('Ten')) #Error
# bool() function demo program
print(bool(0)) # False
print(bool(10)) # True : 10 is non-zero
print(bool(-25)) #True
print(bool(0.0)) # False
print(bool(0.1)) #True
print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) #True
print(bool('')) #False
print(bool('Hyd')) # True
print(bool(' ')) #False
print(bool('True')) #True
# str() function demo program
print(str(25)) # Converts 25 to '25'
print(str(10.8)) # Converts 10.8 to '10.8'
print(str(3 + 4j)) # Converts 3+4j to '3+4j'
print(str(True)) # Converts True to 'True'
print(str(False)) # Converts False to 'False'
print(str(None))# Converts None to 'None'
# oct() function demo program
print(oct(195)) #0o303
print(oct(0B10101110010)) #0o25562
print(oct(0xA7B9)) #0o12371
# hex() function demo program
print(hex(25)) #0x19
print(hex(0B10101111010111)) #0x15ea7
print(hex(0O6247)) # 0xcc7
