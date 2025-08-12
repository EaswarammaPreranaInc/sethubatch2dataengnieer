# 1) ++ and -- operators demo program

a = 25
print(++a)   #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)   #  -(-a) = +a  =  25
print(a--)   #  (a-)-  =  a+ =  25+  throws   error
print(a--1)  #  a-(-1)  =  a+1 =  26  
print(-a)    # -a  =  -25
print(+-a)   #  +(-a) = -25
print(-+a)   # -(+a) = -25



# 2) Semicolon  demo  program

print('One');	# output: One
print('Two');	# output: Two
print('Three');	# output: Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb')	 
# output: Hyd
	  Sec
	  Cyd



# 3) floor()  and  ceil()  functions  demo  program

import  math
print(math . floor(10.8))	# output: 10
print(math . ceil(10.8))	# output: 11
print(math . floor(25.0))	# output: 25
print(math . ceil(25.0))	# output: 25
print(math . floor(-3.5))	# output: -4
print(math . ceil(-3.5))	# output: -3
print(math . floor(-9.0))	# output: -9
print(math . ceil(-9.0))	# output: -9
print(math . floor(25.1))	# output: 25
print(math . ceil(25.1))	# output: 26
print(floor(3.5))		# throws error as python searches for the floor() which is not defined
print(ceil(3.5))		# throws error as python searches for the ceil() which is not defined



# 4) gcd()  function  demo  program

import  math
print(math . gcd(12 , 15))	# output: 3
print(math . gcd(12 , 18))	# output: 6
print(math . gcd(4 , 7))	# output: 1
print(math . gcd(7 , 7))	# output: 7
print(math . gcd(-18 , -27))	# output: 9
print(math . gcd(-4 , 6))	# output: 2
print(math . gcd(0 , 7))	# output: 7
print(math . gcd(3 , 0))	# output: 3
print(math . gcd(0 , 0))	# output: 0
print(gcd(5 , 15))		# throws error as python searches for the gcd() which is not defined



# 5) abs()  function  demo  program

from  builtins  import  abs
print(abs(-35.8))		# output: 35.8
print(abs(-27))			# output: 27
print(abs(29.5))		# output: 29.5
print(abs(32))			# output: 32
import  builtins
print(builtins . abs(-25))	# output: 25



# 6) max()  and  min()   functions  demo  program

from  builtins  import   max , min
print(max(10.8 , 20.6))				# output: 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))		# output: 5.9
print(max(25 , 10.8))				# output: 25
import  builtins
print(builtins . max(10 , 20 , 30))		# output: 30
print(builtins . min(10 , 20 , 15 , 5 , 12))	# output: 5



# 7) pow()  function  demo  program

from  builtins  import  pow
print(pow(10 , -2))		# When there is '-' for power value result will be divided by 1 output: 0.01
print(pow(4 , pow(3 , 2)))	# It calcultes inner call then outer call 4**(3**2) = 4**9 = 262144
import  builtins
print(builtins . pow(2 , 3))	# Output: 2**3 = 8
print(builtins . pow(-2 , -3))  # When there is '-' for power value result will be divided by 1 output: -0.125 as the value is in negative



# 8) Find  outputs

from keyword import kwlist
print(kwlist) 			# all the keywords in the form of list i.e. [true , false , none , and , or , not , in , is , if , else , yield , .....] 
print(len(kwlist)) 		# number of keywords i.e. 35 
print(type(kwlist)) 		# <class 'list'> 
print(keyword . kwlist) 	# error : keyword module is not imported and hence can not be used




# 9) Find  outputs  (Home  work)

import keyword 				# How  to  import  keyword
print(keyword.kwlist)			# How  to  print  kwlist
print(len(keyword.kwlist))		# How  to  print  number  of  keywords
Print(type(keyword.kwlist))		# How  to  print  type  of kwlist
print(kwlist)				# throws an error that it searches for the kwlist object which is not defined


