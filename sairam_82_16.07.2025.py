#1)  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  # Rama Rao
print(type(a))  # <class 'str'>
print(id(a))  # <memory address of a>
b = 'Hyd'
print(b)  # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)  # Hyd is green city.
          # Hyd is hitec city.
          # Hyd is beautiful city.

#2) Index   demo  program  (Home  work)
a = 'Hyd'
print("How to print 'H' of object 'a'")  # a[0]
print("How to print 'y' of object 'a'")  # a[1]
print("How to print 'd' of object 'a'")  # a[2]
print(a[3])  # Error: Index 3 is out of range
print("How to print 'd' of object 'a'")  # a[-1]
print("How to print 'y' of object 'a'")  # a[-2]
print("How to print 'H' of object 'a'")  # a[-3]
print(a[-4])  # Error: Index -4 is out of range
print(a[0] == a[-3])  # True
a[2] = 'c'  # Error: Strings are immutable in Python
print(25[0])  # Error: int object is not subscriptable
print('25'[0])  # '2'
print(True[1])  # Error: bool object is not subscriptable
print('True'[1])  # 'r'

#3) Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)  # HydHydHyd
print(a * 2)  # HydHyd
print(a * 1)  # Hyd
print(a * 0)  # (Empty string: multiplication by 0 gives empty string)
print(a * -1)  # (Empty string: negative multiplication does not work as expected, gives empty string)
print(25 * 3)  # 75
print('25' * 3)  # 252525
print('25' * 4.0)  # Error: can't multiply sequence by non-int of type 'float'
print(3 * 'Hyd')  # HydHydHyd
print('25' * True)  # 25,since true will be 1

#4) Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))        # Hyd <some_id1>
a = a * 3
print(a , id(a))        # HydHydHyd <some_id2>, not the same as previous one

#5) len()  function  (Home  work)
print(len('Hyd'))         # 3
print(len('Rama Rao'))    # 8
print(len('9247'))        # 4
print(len(''))            # 0
print(len(' '))           # 1
print(len(689))           # Error: int object has no length

#6) Find  outputs  (Home work)
a = """"Hyd"""            # Error: quotes are not given properly
print(a)                  # Error: won't run because of mistake in the line above
print(len(a))             # Error: won't run because of mistake in the line above
print(a[0])               # Error: won't run because of mistake in the line above
print("""Hyd"""")         # Error: extra quote is written by mistake

b = """""Hyd"""           # Error: quotes are not given properly
print(b)                  # Error: won't run because of mistake in the line above
print(len(b))             # Error: won't run because of mistake in the line above

#7) Find  outputs  (Home work)
a = 'Sankar Dayal Sarma'
print(a[7 : 12])        # Dayal
print(a[7 : ])          # Dayal Sarma
print(a[ : 6])          # Sankar
print(a[ : ])           # Sankar Dayal Sarma
print(a[:  : ])         # Sankar Dayal Sarma
print(a[1 : 10 : 2])    # aka a
print(a[0 : : 2])       # SnkrDylSrm
print(a[1 : : 2])       # aka aa aa
print(a[-5 : -1])       # Sarm
print(a[::-1])          # amraS lay aD raknaS
print(a[-1:-5:-1])      # amra
print(a[ : : -2])       # arSlyDrka
print(a[3 : -3])        # kar Dayal Sar
print(a[2 : -5])        # nkar Dayal Sa
print(a[-1:-5])         # (empty string)
print(a[3 : 3])         # (empty string)

#8) Find  outputs  (Home work)
a = 'A'
print(a[1])       # Error:  string has only 1 character at index 0
print(a[1:])      # ''  (empty string, because slicing from index 1 returns nothing)

#9) int()  function  demo  program
print(int(10.8))       # 10
print(int(True))       # 1
print(int(False))      # 0
print(int('25'))       # 25
print(int('0075'))     # 75
print(int(0B11010))    # 26
print(0B11010)         # 26
print(int(0O6247))     # 3231
print(0O6247)          # 3231
print(int(0XA7B9))     # 42937
print(0XA7B9)          # 42937
print(int(3 + 4j))     # Error: Can't convert complex number to int
print(int('25.4'))     # Error: String contains decimal, not a valid int
print(int('Ten'))      # Error: String is not a number

#10) float()  function  demo  program
print(float(25))          # 25.0
print(float(True))        # 1.0
print(float(False))       # 0.0
print(float('92'))        # 92.0
print(float('36.4'))      # 36.4
print(float('0075'))      # 75.0
print(float(0B1010101))   # 85.0
print(float(0O6247))      # 3231.0
print(float(0XA7B9))      # 42937.0
print(float(3 + 4j))      # Error: Can't convert complex number to float
print(float('Ten'))       # Error: String is not a number



#11) complex()  function  demo  program
print(complex(3 , 4))         # (3+4j)
print(complex(0 , 4))         # 4j
print(complex(3))             # (3+0j)
print(complex(3.8 , 4.6))     # (3.8+4.6j)
print(complex(3.8))           # (3.8+0j)
print(complex(3 , 4.5))       # (3+4.5j)
print(complex(True , False)) # (1+0j)
print(complex(True))          # (1+0j)
print(complex(False))         # 0j
print(complex(True , 4))      # (1+4j)
print(complex('3'))           # (3+0j)
print(complex('3.8'))         # (3.8+0j)
print(complex(3 , '4'))       # Error: Second argument must be a number, not a string
print(complex('3' , 4))       # Error: Can't pass string as first argument with second arg
print(complex('3' , '4'))     # Error: Can't pass strings as both arguments
print(complex('Ten'))         # Error: 'Ten' is not a number

#12) bool()  function  demo  program
print(bool(0))           # False           
print(bool(10))          # True          
print(bool(-25))         # True            
print(bool(0.0))         # False           
print(bool(0.1))         # True            
print(bool(0 + 0j))      # False          
print(bool(10 + 20j))    # True            
print(bool(-15j))        # True            
print(bool('False'))     # True            
print(bool(''))          # False           
print(bool('Hyd'))       # True            
print(bool(' '))         # True           
print(bool('True'))      # True

#!3) str()  function  demo  program
print(str(25))        # '25'         
print(str(10.8))      # '10.8'      
print(str(3 + 4j))    # '(3+4j)'     
print(str(True))      # 'True'       
print(str(False))     # 'False'      
print(str(None))      # 'None'

#14) oct()  function  demo  program
print(oct(195))             # 0o303
print(oct(0B10101110010))   # 0o1272
print(oct(0xA7B9))          # 0o24771

#15) hex()  function  demo  program
print(hex(25))                  # 0x19
print(hex(0B10101111010111))    # 0xafd7
print(hex(0O6247))              # 0xcaf
