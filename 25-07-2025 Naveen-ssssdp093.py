#pow() function demo program
import math
print(math.pow(2,3))                # 2^3=8
print(math.pow(-2,-3))              # -2^-3=0.125
print(math.pow(10,-2))              # 10^-2=0.01
print(math.pow(4,math.pow(3,2)))    # 4^3^2=262,144


#sqrt() function demo program
import math
print(math.sqrt(25))                # 5.0
print(math.sqrt(10))                # 3.16
print(math.sqrt(6.25))              # 2.5
print(math.sqrt(True))              # 1.0
#print(math.sqrt(3+4j))             # error sqrt(comlex number) cannot be determined
print(math.sqrt(math.sqrt(256)))    # math.sqr(16.0)=4.0
print(math.sqrt(math.pow(3,4)))     # math.sqr(81.0)=9.0
#print(math.sqrt(-16))              # error sqrt(negative) cannot be determined
#print(sqrt(49))                    # error no sqrt() function in current module


#fabs() function demo program
import math
print(math.fabs(-10))           # 10.0
print(math.fabs(-25.6))         # 25.6
print(math.fabs(20))            # 20.0
print(math.fabs(35.8))          # 35.8
#print(fabs(-25))               # error no fabs() function in current module


#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))           # 10
print(math . ceil(10.8))            # 11
print(math . floor(25.0))           # 25
print(math . ceil(25.0))            # 25
print(math . floor(-3.5))           # -4
print(math . ceil(-3.5))            # -3
print(math . floor(-9.0))           # -9
print(math . ceil(-9.0))            # -9
print(math . floor(25.1))           # 25
print(math . ceil(25.1))            # 26
#print(floor(3.5))                  # no floor() in current module
#print(ceil(3.5))                   # no ceil () in current module



#degree radians
import math
print(math.pi)                      # 22/7=3.14159
print(math.degrees(math.pi))        # converts pi radians to 180 degrees
print(math.degrees(math.pi/2))      # converts pi/2 radians to 90 degrees
print(math.radians(180))            # converts 180 degrees to pi radians = 3.14159
print(math.radians(90))             # converts 90 degrees to pi/2 radians = 1.57
#print(pi)                          # error no object pi in current module



# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15))          # 3
print(math . gcd(12 , 18))          # 6
print(math . gcd(4 , 7))            # 1
print(math . gcd(7 , 7))            # 7
print(math . gcd(-18 , -27))        # 9
print(math . gcd(-4 , 6))           # 2
print(math . gcd(0 , 7))            # 7
print(math . gcd(3 , 0))            # 3
print(math . gcd(0 , 0))            # 0
#print(gcd(5 , 15))                 # error no gcd() function in current module



#factorial() function
import math
print(math.factorial(5))             # 1*2*3*4*5=120
print(math.factorial(0))             # 1
print(math.factorial(100))           # 100!
#print(math.factorial(-5))           # error factorial(negative) cannot be determined



#exp() function
import math
print(math.exp(1))                  # e^1 ----> e=2.71828
print(math.exp(2))                  # e^2
print(math.exp(0))                  # e^0=1
print(math.exp(-2))                 # e^-2



#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))                   # 35.8
print(abs(-27))                     # 27
print(abs(29.5))                    # 29.5
print(abs(32))                      # 32
import  builtins                    # mandetory bultins module is not imported automatically
print(builtins . abs(-25))          # 25


#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))                         # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))            # 5.9
print(max(25 , 10.8))                           # 25
import  builtins                                # mandetory not imported automatically
print(builtins . max(10 , 20 , 30))             # 30
print(builtins . min(10 , 20 , 15 , 5 , 12))    # 5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))                         # 10^-2=0.01
print(pow(4 , pow(3 , 2)))                  # 4^3^2=262,144
import  builtins                            # mandetory not imported automatically
print(builtins . pow(2 , 3))                # 2^3=8
print(builtins . pow(-2 , -3))              # -2^-3