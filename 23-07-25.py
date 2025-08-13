
#first program
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)
#print(a--)
print(a--1)
print(-a)
print(+-a)
print(-+a)

#second program
#  Semicolon  demo  program
print('One');
print('Two');
print('Three');
print('Hyd')  ;   print('Sec')  ;  print('Cyb')

#third program
#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0))
print(math . ceil(25.0))
print(math . floor(-3.5))
print(math . ceil(-3.5))
print(math . floor(-9.0))
print(math . ceil(-9.0))
print(math . floor(25.1))
print(math . ceil(25.1))
#print(floor(3.5))
#print(ceil(3.5))

#fourth program
# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7))
print(math . gcd(-18 , -27))
print(math . gcd(-4 , 6))
print(math . gcd(0 , 7))
print(math . gcd(3 , 0))
print(math . gcd(0 , 0))
#print(gcd(5 , 15))

#fifth program
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))
print(abs(-27))
print(abs(29.5))
print(abs(32))
import  builtins
print(builtins . abs(-25))

#sixth program
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))
print(min(10.8 , 20.6 , 5.9 , 12.3))
print(max(25 , 10.8))
import  builtins
print(builtins . max(10 , 20 , 30))
print(builtins . min(10 , 20 , 15 , 5 , 12))

#seventh program
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))
print(pow(4 , pow(3 , 2)))
import  builtins
print(builtins . pow(2 , 3))
print(builtins . pow(-2 , -3))

#eighth program
from keyword import kwlist
print(kwlist)
print(len(kwlist))
print(type(kwlist))
#print(keyword.kwlist)

#ninth program
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
#print(kwlist)

