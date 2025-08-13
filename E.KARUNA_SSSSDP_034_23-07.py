#(23-07-2025)
a=25
print(++a)#25
#print(a++)#Error
print(a++1)#26
print(--a)#25
#print(a--)#Error
print(a--1)#26
print(-a)#-25
print(+-a)#-25
print(-+a)#-25
print()
print('One');#one
print('Two');#Two
print('Three');#Three
print('Hyd') ; #Hyd
print('Sec') ;#sec
print('Cyb')#cyb
print()
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
#print(floor(3.5))#Error
#print(ceil(3.5))#Error
print()
import  math
print(math . gcd(12 , 15))#3
print(math . gcd(12 , 18))#6
print(math . gcd(4 , 7)) #1
print(math . gcd(7 , 7))#7
print(math . gcd(-18 , -27))#9
print(math . gcd(-4 , 6))#2
print(math . gcd(0 , 7))#7
print(math . gcd(3 , 0))#3
print(math . gcd(0 , 0))#0
#print(gcd(5 , 15))
print()
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25
print()
from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10,20,15,5,12))#5
print()
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#262144
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2,-3))#-0.125
print()
import keyword #import list in the kwlist which is in keywords module
print(keyword .kwlist)#prints a list of all keywords in python
print(len(keyword . kwlist))#print the length of keywords
print(type( keyword . kwlist))#print the type of keyword
print()
from keyword import  kwlist#import the keyword module
print(kwlist)#prints a list of all keywords in python
print(len( kwlist))#print the length of keywords
print(type( kwlist))#print the type of keyword 
