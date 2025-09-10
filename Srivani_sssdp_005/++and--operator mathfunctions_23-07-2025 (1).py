#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a) # -(-a) = a = 25
print(a--) # (a-)- = a- = 25- throws error because '-' should not be there after a
print(a--1) # a - (-1) = a + 1 = 25 + 1 = 26
print(-a) # -a = -25
print(+-a) # +(-a) = +(-25) = -25
print(-+a) # -(+a) = -(25) = -25



#  Semicolon  demo  program
print('One'); # prints 'One'
print('Two'); # prints 'Two'
print('Three'); # prints 'Three'
print('Hyd')  ;   print('Sec')  ; print('Cyb') # prints 'Hyd'<nextline>'Sec'<nextline>'Cyb'



#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8)) # prints 10 because previous number of 10.8
print(math . ceil(10.8)) # prints 11 because next number of 10.8
print(math . floor(25.0)) # prints 25 because previous number of 25.0
print(math . ceil(25.0)) # prints 25 because next number of 25.0
print(math . floor(-3.5)) # prints -4 because previous number of -3.5
print(math . ceil(-3.5)) # prints -3 because next number of -3.5
print(math . floor(-9.0)) # prints -9 because previous number of -9.0
print(math . ceil(-9.0)) # prints -9 because next number of -9.0
print(math . floor(25.1)) # prints 25 because previous number of 25.1
print(math . ceil(25.1)) # prints 26 because next number of 25.1
print(floor(3.5)) # Error, we should import math explicitly
print(ceil(3.5)) # Error, we should import math explicitly



# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) # prints 3 because greatest common divisor of 12 and 15 is 3
print(math . gcd(12 , 18)) # prints 6 because greatest common divisor of 12 and 18 is 6
print(math . gcd(4 , 7)) # prints 1 because greatest common divisor of 4 and 7 is 1
print(math . gcd(7 , 7)) # prints 3 because greatest common divisor of 12 and 15 is 3
print(math . gcd(-18 , -27)) # prints -9 because greatest common divisor of -18 and -27 is -9
print(math . gcd(-4 , 6)) # prints 2 because greatest common divisor of -4 and 6 is 2
print(math . gcd(0 , 7)) # prints 7 because greatest common divisor of 0 and 7 is 3
print(math . gcd(3 , 0)) # prints 3 because greatest common divisor of 3 and 0 is 3
print(math . gcd(0 , 0)) # prints 0 because greatest common divisor of 0 and 0 is 0
print(gcd(5 , 15)) # Error because there is no gcd function in current module, so we should use should math.gcd()



#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # converts negative integer into positive integer and prints 35.8
print(abs(-27)) # converts negative integer into positive integer and prints 27
print(abs(29.5)) # it is already a positive integer so it prints 29.5
print(abs(32)) # it is already a positive integer so it prints 32
import  builtins # importing builtins module
print(builtins . abs(-25)) # searches for abs function in builtins module and converts negative integer to positive integer and prints 25



#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # prints maximum value of 10.8 and 20.6 i.e., 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  # prints minimum value of 10.8, 20.6, 5.9 and 12.3 i.e., 5.9
print(max(25 , 10.8)) # prints maximum value of 25 and 10.8 i.e., 25
import  builtins # imports builtins module
print(builtins . max(10 , 20 , 30)) # it searches for max() function in builtins module and prints maximum value of 10, 20 and 30 i.e., 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # it searches for min() function in builtins module and prints minimum value of 10, 20, 15, 5 and 12 i.e., 5



# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 10 ^ -2 i.e., 0.01
print(pow(4 , pow(3 , 2))) # first evaluates inner power i.e., 3 ^ 2 = 9 and next evaluates 4 ^ 9 = 262144
import  builtins # imports builtins module
print(builtins . pow(2 , 3)) # it searches for pow() function in builtins module and evaluates power 2 ^ 3 = 8
print(builtins . pow(-2 , -3)) # it searches for pow() function in builtins module and evaluates power -2 ^ -3 = -0.125



# Find  outputs
from keyword import kwlist # imports kwlist from keyword module
print(kwlist) # prints keywords in kwlist i.e., 
print(len(kwlist)) # prints number of keywordd in kwlist i.e., 35
print(type(kwlist)) # prints type of kwlist i.e., <class 'list'>
print(keyword . kwlist) # Error because cannot use keyword module without importing keyword module



#  Find  outputs  (Home  work)
import keyword # imports keyword module
print(keyword.kwlist) # searches for kwlist in keyword module and prints all keywords in kwlist i.e., 
print(keyword.len(kwlist)) # searches for kwlist in keyword module and prints number of keywords in kwlist i.e., 35
print(keyword.type(kwlist)) # searches for kwlist in keyword module and prints type of kwlist i.e., <class 'list'>
print(kwlist) # Error because we cannot access kwlist unless keyword module is imported explicitly