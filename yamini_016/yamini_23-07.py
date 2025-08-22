a = 25
print(++a)  #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a) # -(-a)=-*(-25)=+25
print(a--) # error (a-)-=(25-)*-=-(25-)
print(a--1) # a - (-1) = 25 -(-1) =25+1=26
print(-a) # -a=-(25)=-25
print(+-a) #+(-a)=+(-25)=-25
print(-+a) #-(+25)=-25

print('One'); # semiolon is optional in Python so prints one and defaultly goes to next line
print('Two'); # semicolon is optional in Python so prints two and defaultly goes to next line
print('Three'); # semicolon is optional in Python so prints three and defaultly goes to next line
print('Hyd')  ;   print('Sec') ;print('Cyb') # prints Hyd in a line then goes to next line and prints Sec then goes to next line and prints Cyb

import math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0)) #25
print(math . ceil(25.0))#25
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0))   # -9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) # 26
print(floor(3.5)) # error floor is not defined AND Math should be there
print(ceil(3.5)) # error ceil is not defined AND Math should be there


import math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7)) #  7
print(math . gcd(-18 , -27)) # 9
print(math . gcd(-4 , 6)) # 2
print(math . gcd(0 , 7)) # 7
print(math . gcd(3 , 0)) # 3
print(math . gcd(0 , 0))    # 0
print(gcd(5 , 15)) # error gcd is not defined AND Math should be there
          
          from  builtins  import  abs # importing abs function from builtins module and just use it by abs()
print(abs(-35.8)) # 35.8 
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins # importing builtin module and using one of its functions abs by builtin.abs()
print(builtins.abs(-25)) # 25

from  builtins  import   max , min # importing max and min functions from builtins module
print(max(10.8 , 20.6))  # 20.6 as it is the maximum value
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9 as it is the minimum value
print(max(25 , 10.8)) # 25 as it is the maximum value
import  builtins # importing builtin module and using one of its functions max by builtin.max()
print(builtins . max(10 , 20 , 30)) # 30 as it is the maximum value
print(builtins . min(10 ,20,15,5,12)) # 5 as it is the minimum value

from  builtins  import  pow # importing pow function from builtins module and just use it by pow()
print(pow(10 , -2)) # 0.01 as we write it as 10^-2 
print(pow(4 , pow(3 , 2))) # 1st inside the brackets 3^2 = 9 then 4^9 
import  builtins # importing builtin module and using one of its functions pow by builtin.pow()
print(builtins . pow(2 , 3)) # 8 as we write it as 2^3
print(builtins.pow(-2,-3)) # -0.125 as we write it as -2^-3

How  to  import   kw  list
#from keyword import kwlist # importing kwlist from keyword module
How  to  print  kwlist
#print(kwlist) # prints the list of keywords in Python
How  to  print  number  of  keywords
#print(len(kwlist))
How  to  print  type  of kwlist
#print(type(kwlist))
#import keyword # importing keyword module
#print(keyword.kwlist)

How  to  import   keyword  module
#import keyword  # importing keyword module
How  to  print  kwlist
#print(keyword.kwlist) # prints the list of keywords in Python
How  to  print  number  of  keywords
#print(len(keyword.kwlist))
How  to  print  type  of kwlist
#print(type(keyword.kwlist))
#from keyword import kwlist # importing kwlist from keyword module
print(kwlist)
