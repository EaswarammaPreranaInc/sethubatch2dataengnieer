a = "Rama Rao"
print(a)#Rama Rao
print(type(a))#<class 'str'>
print(id(a))#addess of the object
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#Hyd is green city<next line>Hyd is hitec city<next line>Hyd is beautiful city.
print() #nothing
a= 'Hyd'
print(a * 3)#Repeats sring thrice i.e HydHydHyd
print(a * 2)#Repeats sring twice i.e HydHyd
print(a * 1)#Repeats sring once i.e Hyd
print(a * 0)#Repeats sring 'o' times i.e empty string
print(a * -1)#Repeats sring 'o' times i.e empty string
print(25 * 3)#75
print('25' * 3)#252525
#print('25' * 4.0)#error due to float operand 4.0
print(3 * 'Hyd')#HydHydHyd
#print('25' * True)#error
print() #nothing
a = 'Hyd'
print(a , id(a))#address of the object
a = a * 3#Ref 'a' modifies to new string object
print(a ,id(a))#HydHydHyd,address of the object
print()#nothing
# len()  function  (Home  work)
print(len('Hyd'))#3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0 because empty string
print(len(' '))#1 because space is there
#print(len(689))#error:argument should be a sequence
print()#nothing
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)#"Hyd
print(len(a))#4
print(a[0])#"
#print("""Hyd"""")#error due to excess closing quote 
b = """""Hyd"""#excess opening quote 
print(b)#""Hyd
print(len(b))#5
print()# nothing
a = 'Sankar Dayal Sarma'
print(a[7 : 12])#a[7:12:1] i.e Dayal
print(a[7 : ])#a[7:18:1] i.e Danial sarma
print(a[ : 6])#a[0:6:1] i.e Sankar
print(a[ : ])  #a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])#a[0:18:1] i.e Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2])#akrDy
print(a[0 : : 2])#a[0:18:2] i.e Sna<space>aa<space>am
print(a[1 : : 2])#a[1:18:2] i.e aKrDylSra
print(a[-5 : -1])#a[-5:-1:1] i.e sarm
print(a[::-1])#a[-1:-19:-1] i.e amraS<space>layaD<space>raknaS
print(a[-1:-5:-1])#amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])#a[3:-3:1] i.e kar<space>Dayal<space>Sa
print(a[2 : -5])#a[2:-5:1]i.e nkar<space>Dayal
print(a[-1:-5])#a[-1:-5:-1]i.e empty string
print(a[3 : 3])#[3:3:1] i.e empty string
print()#nothing
#  Find  outputs  (Home  work)
a =  'A'
#print(a[1])#error due index '1'does not exist
print(a[1:])#string without first char
print()#nothing
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #  Converts  bool   object    Flase  to  int  object 0
print(int('25')) #  Converts  '25'   object    True  to  int  object 25
print(int('0075'))# Converts  '0075'   object    True  to  int  object 75
print(int(0B11010))#converts binary number to decimal number i.e 26
print(int(0O6247))#converts octal number to decimal number i.e 3239
print(0O6247)#3239
print(int(0XA7B9))#converts hexa decimal number to decimal number i.e 42937
print(0XA7B9)#42937
#print(int(3 + 4j))#error :complex number cannot be converted to int
#print(int('25.4'))#error:string,float cannot be converted to int
#print(int('Ten'))#error
print()#nothing
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #  Converts  bool  object   False  to  float  object   0.0
print(float('92')) # Converts  '92  to  float object   92.0
print(float('36.4')) # Converts  '36.4' to  float object  36.4
print(float('0075'))# Converts  '0075' to  float object  75.0
print(float(0B1010101))#converts binary number to decimal number i.e 85.0
print(float(0O6247))#converts octal number to decimal number i.e 3239.0
print(float(0XA7B9))#converts hexa decimal number to decimal number i.e 42937.0
#print(float(3 + 4j))#error:complex number cannot be converted to float
#print(float('Ten'))#error:'Ten' cannot be converted to float
print()#nothing
# complex()  function  demo  program
print(complex(3 , 4))#(3+4j)
print(complex(0 , 4))#4j
print(complex(3))#(3+0j)
print(complex(3.8 , 4.6))#(3.8+4.6j)
print(complex(3.8))#(3.8+0j)
print(complex(3 , 4.5))#(3+4.5j)
print(complex(True , False))#(1+0j)
print(complex(True))#(1+0j)
print(complex(False))#0j
print(complex(True , 4))#(1+4j)
print(complex('3'))#(3+0j)
print(complex('3.8'))#(3.8+0j)
#print(complex(3 , '4'))#error:2nd argument is cannot be string
#print(complex('3' , 4))#error
#print(complex('3' , '4'))#error
#print(complex('Ten'))#errror
print()
#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))#True
print(bool(0.0))#False
print(bool(0.1))#True
print(bool(0 + 0j))
print(bool(10 + 20j))#True
print(bool(-15j))#True
print(bool('False'))#True
print(bool(''))#False
print(bool('Hyd'))#True
print(bool(' '))#True
print(bool('True'))#True
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))#  Converts   10.8 to  '10.8'
print(str(3 + 4j))#  Converts   3+4j  to  '3+4j'
print(str(True))#  Converts   True to  'True'
print(str(False))#  Converts   False  to  'False'
print(str(None))#  Converts   None to  'None'
print()#nothing
# oct()  function  demo  program
print(oct(195))#0o303
print(oct(0B10101110010))#0o2562
print(oct(0xA7B9))#0o123671
print()
# hex()  function  demo  program
print(hex(25))#0x19
print(hex(0B10101111010111))#0x2bd7
print(hex(0O6247))#0xca7
print()#nothing
