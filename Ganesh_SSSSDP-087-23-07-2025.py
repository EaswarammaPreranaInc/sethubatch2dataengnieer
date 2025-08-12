#  outputs

  print({10 , 20}  |  {30 , 20})                                     # {10,20,30}
  print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})      # {10:'Hyd',20:'Vja',30:'Cyb'}
  print(range(4) | range(5))                                         # error
  print([10 , 20]  |  [30 , 20])                                     # error

 #  Assignment  operators  demo  program  (Home  work)  outputs

 a = 25
 print(a)                       # 25
 b =  a 
 print(b)                       # 25
 print(a  is  b)                # True
 x = 4
 y = 5
 z = x + y * 6
 print(z)                       # 34
 25 = a
 a + b = x + y                  # error

 # Find outputs (Home work)

 a = b = c = 25
 print(id(a))
 print(id(b))
 print(id(c))
 print(a , b , c)

 # Find outputs (Home work)

 a = b = c = 25
 print(id(a))                            # address of the reference a
 print(id(b))                            # address of the reference  b 
 print(id(c))                            # address of the reference c 
 print(a , b , c)                        # 25 25 25

 # Multiple  Assignment (Home work) outputs
 x , y , z = 25 , 10.8 , 'Hyd'
 print(x)                            # 25
 print(y)                            # 10.8
 print(z)                            # 'Hyd'

 # Find outputs (Home work)
 a , b , c = 3 , 4 , 5
 a *= b + c
  print(a)                             # 27

 # Find outputs (Home work)
 a = 20
 a %= 3 + 2 * 4
 print(a)                                # 9

 # # Find outputs (Home work)
 a = 3
 a **= 4
 print(a)                               # 81

# Find ouputs

 a = 25
 b = 25
 print(a  is  b)                       # True
 print(a  is  not  b)                  # False
 print(a == b)                         # True

 # Find outputs (Home work)
 a = 25
 b = 25.0
 print(a  is  b)                      # False
 print(a  is  not  b)                 # True
 print(a == b)                        # True

 # Find outputs (Home work)
 a = 'Hyd'
 b = 'Hyd'
 print(a  is  b)         # True
 print(a  is  not  b)    # False
 print(a == b)           # True
 print()                 # " "
 x = [1 , 2 , 3 , 4]  
 y = [1 , 2 , 3 , 4]
 print(x is y)           # False
 print(x  is  not  y)    # True
 print(x == y)           # True
 print()
 m = (1 , 2 , 3 , 4)
 n = (1 , 2 , 3 , 4)
 print(m  is  n)          # True
 print(m  is  not  n)     # False
 print(m == n)            # True
 print(x == m)            # False

# Membership operators demo program (Home work)
 list = [10 , 20 , 15 , 12 , 18]
 print(15 in list)                # True
 print(19 in list)                # False
 print(14 not in list)            # True
 print(15 not in list)           # False
 s = 'Hyd is green city'
 print( 'is' in s)               # True
 print('was' in s)               # false
 print('g' in s)                 # True
 print('z' in s)                 # False
 print(' ' in s)                # True
 print('gre' in s)               # True
 print('yd i' in s)               # True 
 print('' in s)                 # True
 print('' not in s)             # error

#  ++  and  --  operators  demo  program
 a = 25
 print(++a)  #  +(+a) = +a  =  25
 print(a++)   #  (a+)+  =  a+ =  25+  throws   error
 print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
 print(--a)  # -(-a)+a=25
 print(a--) # (a-)-=a+ throws error
 print(a--1) # a-(-1)=a+1=25+1=26
 print(-a) # -25
 print(+-a) # +(-a)=-25
 print(-+a) # -(+a)=-25

#  Semicolon  demo  program  outputs
 print('One'); # one
 print('Two'); # Two
 print('Three'); # Three
 print('Hyd')  ;   print('Sec')  ;  print('Cyb') 
 # Hyd
 # Sec
 # Cyb

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #10
print(math . ceil(10.8))  # 11
print(math . floor(25.0))  # 25
print(math . ceil(25.0)) # 25
print(math . floor(-3.5))  #  -4
print(math . ceil(-3.5))  # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1))  # 25 
print(math . ceil(25.1))  # 26
print(floor(3.5))  # error
print(ceil(3.5))  # error


'''
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'
'''


# gcd()  function  demo  program outputs
 import  math
  print(math . gcd(12 , 15))   #   3
  print(math . gcd(12 , 18))   #  6
 print(math . gcd(4 , 7))      #   1
 print(math . gcd(7 , 7))       #  7
 print(math . gcd(-18 , -27))  # 9
 print(math . gcd(-4 , 6))     # 2
 print(math . gcd(0 , 7))      # 7
 print(math . gcd(3 , 0))      #  3
 print(math . gcd(0 , 0))      #  0
 print(gcd(5 , 15))            #  error

#  abs()  function  demo  program
 from  builtins  import  abs
 print(abs(-35.8))    #  35.8
 print(abs(-27))       #  27
 print(abs(29.5))      #  29.5
 print(abs(32))        #  32
 import  builtins
 print(builtins . abs(-25))   # -25

#  max()  and  min()   functions  demo  program
  from  builtins  import   max , min
  print(max(10.8 , 20.6))  # 20.6
  print(min(10.8 , 20.6 , 5.9 , 12.3))   # 5.9
  print(max(25 , 10.8))   # 25
 import  builtins
  print(builtins . max(10 , 20 , 30))   # 30
  print(builtins . min(10 , 20 , 15 , 5 , 12))    #  5


# pow()  function  demo  program
from  builtins  import  pow     outputs
print(pow(10 , -2))      #  0.01
print(pow(4 , pow(3 , 2)))  # 262144
import  builtins
print(builtins . pow(2 , 3))   # 8
print(builtins . pow(-2 , -3))  # -0.0125

