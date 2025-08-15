#Home Work-1
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a  =  25
# print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a) #-(-a)=> +a =>25
# print(a--) #(a-)- => a+ =>25+ throws error
print(a--1) #(a-)-1 =>a+1 => 26
print(-a) #-25
print(+-a) #+(-a)=>-a=>-25
print(-+a) #-(+a)=>-a => -25

#Home work-2
#  Semicolon  demo  program
print('One'); #One
print('Two'); #Two
print('Three'); #Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') #Hyd <new line> Sec <nl> Cyb

#Home Work-3
#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0))#25
print(math . ceil(25.0))#25
print(math . floor(-3.5))#-4
print(math . ceil(-3.5))#-3
print(math . floor(-9.0))#-9
print(math . ceil(-9.0))#-9
print(math . floor(25.1))#25
print(math . ceil(25.1))#26
# print(floor(3.5)) error, becoz we are importing module not members, so we need to use 
# print(ceil(3.5)) floor or ceil functions with module only ..i.e, math.floor(x)


'''
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'
'''

#Home Work-4
# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7))#7
print(math . gcd(-18 , -27))#9, ignore the signs and take the result
print(math . gcd(-4 , 6))#2, ignore the signs and take the result 
print(math . gcd(0 , 7))#7
print(math . gcd(3 , 0))#3
print(math . gcd(0 , 0))#0
# print(gcd(5 , 15))#error, we should use members of math with module only 

#Home Work-5
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))# 35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32
import  builtins
print(builtins . abs(-25)) #25

#Home Work-6
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #10.8
import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5

#Home Work-7
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #10^2, 0.01
print(pow(4 , pow(3 , 2))) # 4^(3^2)=>4^9 
import  builtins
print(builtins . pow(2 , 3)) #2^3 =>8
print(builtins . pow(-2 , -3)) #-2^(-3)=> -1*(1/2^3) =>-0.125

#Home Work-8
# Find  outputs
# How  to  import   kw  list
from keyword import kwlist
# How  to  print  kwlist
print(kwlist)
# How  to  print  number  of  keywords
print(len(kwlist))
# How  to  print  type  of kwlist
print(type(kwlist))
# print(keyword . kwlist)

#Home Work-9
#  Find  outputs  (Home  work)
# How  to  import   keyword  module
import keyword
# How  to  print  kwlist
print(keyword.kwlist)
# How  to  print  number  of  keywords
print(len(keyword.kwlist))
# How  to  print  type  of kwlist
print(type(keyword.kwlist))
# print(kwlist)