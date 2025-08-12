

a = 25
print(++a)  #  +(+a) = +a  =  25
#print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)# -(-a) = +a = 25
#print(a--)# a-(-) # error 
print(a--1)# a-(-1) = a+1 = 26
print(-a)#-25
print(+-a)#+(-a) = -25
print(-+a)#-(+a) = -25
print()

print('One');#One 
print('Two');#Two 
print('Three');#Three 
print('Hyd');print('Sec');print('Cyb')
print()

import  math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0))#25
print(math . ceil(25.0))#25
print(math . floor(-3.5))#-3
print(math . ceil(-3.5))#-4
print(math . floor(-9.0))#-9
print(math . ceil(-9.0))#-9
print(math . floor(25.1))#25 
print(math . ceil(25.1))#26 
#print(floor(3.5))#error
#print(ceil(3.5))#error
print() 

from  builtins  import  abs
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins.abs(-25))#25
print()

from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins.max(10,20,30))#30
print(builtins.min(10,20,15,5,12))#5
print()

from  builtins  import  pow
print(pow(10,-2))#0.01
print(pow(4,pow(3,2)))#4^3^2
import  builtins
print(builtins.pow(2,3))#8
print(builtins.pow(-2,-3))#-0.125
print()

from keyword import kwlist # How  to  import   kw  list
print(kwlist)#How  to  print  kwlist
print(len(kwlist))#How  to  print  number  of  keywords
print(type(kwlist))#How  to  print  type  of kwlist

#  Find  outputs  (Home  work)
import keyword #How  to  import   keyword  module
print(keyword.kwlist)#How  to  print  kwlist
print(len(keyword.kwlist))#How  to  print  number  of  keywords
print(type(keyword.kwlist))#How  to  print  type  of kwlist
