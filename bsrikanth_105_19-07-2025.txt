#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)			#prints string Rama Rao
print(type(a))			#class str
print(id(a))			#prints address of object Rama Rao
b = 'Hyd'		
print(b)			#prints Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)			#Hyd is green city.
				 Hyd is hitec city.
				 Hyd is beautiful city.




# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')	#a[0]
print(How  to  print  'y'  of  object  'a')	#a[1]	
print(How  to  print  'd'  of  object  'a')	#a[2]
print(a[3])					#error
print(How  to  print  'd'  of  object  'a')	#a[-1]
print(How  to  print  'y'  of  object  'a')	#a[-2]
print(How  to  print  'H'  of  object  'a')	#a[-3]
print(a[-4])					#Error index out of range
print(a[0] ==  a[-3])				#True
a[2] = 'c'					#Error
print(25[0])					#Error
print('25'[0])					#prints 2
print(True[1])					#Error
print('True'[1]) 				#prints 2





#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)			#prints 'HydHydHyd'
print(a * 2)			#prints 'HydHyd'
print(a * 1)			#prints 'Hyd'
print(a * 0)			#prints nothing
print(a * -1)			#prints nothing
print(25 * 3)			#prints 75
print('25' * 3)			#prints '252525'
print('25' * 4.0)		#error cannot multipy string with float
print(3 * 'Hyd')		#prints 'HydhydHyd'
print('25' * True)		#25





#  Find  outputs  (Home work)
a = 'Hyd'			#Hyd, address of the object 'Hyd'
print(a , id(a))
a = a * 3
print(a , id(a))		#HydHydHyd address of the object "HydHydHyd"




# len()  function  (Home  work)
print(len('Hyd'))		#prints 3
print(len('Rama Rao'))		#prints 8
print(len('9247'))		#prints 4
print(len(''))			#prints 0
print(len(' '))			#prints 1
print(len(689))			#object int has not length




# Find  outputs  (Home  work)
a = """"Hyd"""		#prints "Hyd
print(a)
print(len(a))		#prints 4
print(a[0])             #prints '"'
print("""Hyd"""")	#error
b = """""Hyd"""		#prints ""Hyd
print(b)
print(len(b))		#prints 5



# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])		#Dayal
print(a[7 : ])			#Dayal Sarma
print(a[ : 6])			#Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])			#Sankar Dayal Sarma
print(a[1 : 10 : 2])		#aka a
print(a[0 : : 2])		#SnkrDylSra
print(a[1 : : 2])		#aar aa am
print(a[-5 : -1])		#Sarm
print(a[::-1])			#amraS lay aD raknaS
print(a[-1:-5:-1])		#amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])		#kar Dayal Sa	
print(a[2 : -5])		#nkar Dayal 
print(a[-1:-5])			#empty string 
print(a[3 : 3])			#empty string


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1





#  Find  outputs  (Home  work)
a =  'A'
print(a[1])		#A	
print(a[1:])		#empty string
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) 	#0
print(int('25'))	#25
print(int('0075'))	#0075
print(int(0B11010))	#26
print(0B11010)		#26
print(int(0O6247))	#3239
print(0O6247)		#3239
print(int(0XA7B9))	#42937
print(0XA7B9)		#42937
print(int(3 + 4j))	#error
print(int('25.4'))	#error
print(int('Ten'))	#error





# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))	#converts bool object False into float object 0.0
print(float('92'))	#92.0
print(float('36.4'))	#36.4
print(float('0075'))	#75.0
print(float(0B1010101)) #85.0
print(float(0O6247))	#3239.0
print(float(0XA7B9))	#42937.0
print(float(3 + 4j))    #error because cannot convert complex object into float object
print(float('Ten'))	#error





#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))	#True
print(bool(0.0))	#False
print(bool(0.1))	#True
print(bool(0 + 0j))	#False
print(bool(10 + 20j))	#True
print(bool(-15j))	#True
print(bool('False'))	#True
print(bool(''))		#False
print(bool('Hyd'))	#True
print(bool(' '))	#True
print(bool('True'))	#True




# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))	#'10.8'
print(str(3 + 4j))	#3+4j
print(str(True))	#True
print(str(False))	#False
print(str(None))	#None




# oct()  function  demo  program
print(oct(195))			#0O303
print(oct(0B10101110010))	#0O2562
print(oct(0xA7B9))		#0O123671




# hex()  function  demo  program
print(hex(25))			#0x19
print(hex(0B10101111010111))	#0x2bd7
print(hex(0O6247))		#0xca7

