# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
()
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1()
def  f1(x , y , z):
	print('Three  argument  function : ', x, y, z)	   
f1()









'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
2
3
5
7
Number  of   prime  numbers : 
How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers : ', ???)
'''
from prog3a import prime
def f2():
    a = []
    for i in range(2, n):
        if prime(i):
            a.append(i)
    return a
n = int(input("Enter any number:"))
a = f2(n)
print("Prime numbers")
for p in a:
    print(p)
print("Number of prime numbers :", len(a))









# Find  outputs  (Home  work)
def f1(a , b , c):
    print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # prints a : 10 \t b : 20 \t c : 30
f1(25 , 10.8 , 'Hyd') # prints a : 25 \t b : 10.8 \t c : 'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5) # prints a : 50.2 \t b : 40.7 \t c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # prints a : 'Cyb' \t b : 'Sec' \t c : 'Hyd'
f1(c = 3 + 4j , a = True , b = None) # prints a : True \t b : None \t c : (3 + 4j)
f1(25 , c = 10.8 , b = 'Hyd') # prints a : 25 \t b : 'Hyd' \t c : 10.8
f1(a = 100 , 200 , 300)  #  Error
f1(True , None , b = 'Hyd') # Error 
f1(10 , 20 , x = 30) # Error
f1(10, 20) # Error
   






# Find  outputs (Home  work)
def disp(empno , ename , sal):
    print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) 
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x, y, z)
'''
Outputs:

Emp Number : 25 \t Emp Name : Rama Rao \t Salary : 10000.0
Emp Number : 35 \t Emp Name : Sita \t Salary : 20000.0
Emp Number : Rama Rao \t Emp Name : 30000.0 \t Salary : 20
'''









#  Tricky  program
# Find  outputs (Home  work)
def f1(a , b , c):
    return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # prints 23
print(f1(*[6 , 7 , 8])) # prints 62
print(f1([6 , 7 , 8])) # Error because there is only one positional argument buut we need 3 positional arguments
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # prints 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error because there is only one positional argument buut we need 3 positional arguments
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error because there is only one positional argument buut we need 3 positional arguments
print({{'c' : 2 , 'b' :  4 , 'a' : 6}}) # Error
print(f1({'c' : 2 , 'a' : 4, 'x' : 6})) # Error because there is only one positional argument buut we need 3 positional arguments
		  












# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12] # Ref 'a' points to list of 5 elements
print(sorted(reverse = True , a)) # Error becuase keyword argument should be next to positional argument
print(sorted(a , rev = True)) # Error because there is no keyword rev
print(25 , 10.8 , 'Hyd' , separator = '\t') # Error because there is no keyword separator
print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error because there is no keyword endoflline
print(25 ,  sep = '\t' , 10.8 , end = '\t', 'Hyd') # Error because keyword arguments should be after positional arguments
	  








# Keyword  only   arguments  demo  program
def   f1(* , a , b):
    print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # prints a : 10 \t b : 20
f1(b = 30 , a = 40) # prints a : 40 \t b : 30
#f1(50 , 60) # Error because arguments must be keyword arguments
#f1(70 , b = 80) # Error because arguments must be keyword arguments
f1(a=15 , 25) # Error because arguments must be keyword arguments









#Find  outputs (Home  work)
def f1(a , * , b , c):
    print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # prints a : 10 \t b : 20 \t c : 30
f1(a = 40 , b = 50 , c = 60) # prints a : 40 \t b : 50 \t c : 60
f1(c = 100 , b = 90 , a = 80) # prints a : 80 \t b : 90 \t c : 100
f1(70 , 80 , c = 90) # Error because argument 'b' should be keyword argument
f1(70 , 80 , 90) # Error because b and c arguments should be keyword arguments
f1(c = 15, b = 25, 35) # a :  35 \t b : 25 \t c : 15









 # Identify error (Home  work)
def f1(a  , b , *): # Error because * should be before keyword arguments but not after keyword arguments
    pass









#  Positional  only  arguments  demo  program
def f1(a , b , /):
    print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # prints a : 10 \t b : 20
f1(a = 30 ,  b = 40) # Error because it only takes positional arguments
f1(50 , b = 60) # Error because it only takes positional arguments
f1(a = 70 , 80) # Error because it only takes positional arguments
   








# Find  outputs (Home  work)
def f1(a , b , / , c):
    print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # prints a : 10 \t b : 20 \t c :30
f1(40 , 50 , c = 60) # prints a : 40 \t b : 50 \t c : 60
f1(a = 70 , b = 80 , c = 90) # Error because it requires two positional arguments but given keyword arguments
f1(a = 100 , b = 110 , 120) # Error because a and b should be positional arguments
f1(a = 130 , 140 , c = 150) # Error because a should be positional argument
f1(160 , b = 170 , 180) # Error because b should be positional argument
f1(190 , b = 200 , c = 210) # Error because b should be positional argument
   








# Find outputs(Home  work)
def f1(a , b , / , c , d , * , e  , f):
    print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # prints a : 10 \t b : 20 \t c : 30 \t d : 40 \t e : 50 \t f : 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error because b should be positional argument only
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error because e should be keyword argument only
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error because keyword arguments should be followed by positional arguments
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # prints a : 10 \t b : 20 \t c : 30 \t d : 40 \t e : 50 \t f : 60
   








# Identify error (Home  work)
def f1(/ , a , b ,  c): # Error because / should be followed by parameters in function header
    pass
def f2(a , b , c , *): # Error because * should be before paramenters in function header
    pass









# Identify  error  (Home  work)
def f4(* , a , b , c , /): # Error because keyword arguments should be followed by positional arguments but not vice versa
    pass
	








# Find  outputs  (Home  work)
def f1(x):
    print('1st  function : ' , x)
def f1(y):
    print('2nd  function : ' , y)
def f1(z):
    print('3rd  function : ' , z)
f1(z = 10) # prints 3rd function : 10
f1(y = 20) # Error 
f1(x = 30) # Error 


   






# Default  arguments  demo  program
def add(a  , b = 20 , c = 30):
    return   a + b + c
#end  of  the  functiom
print(add(100)) # prints 150
print(add(100 , 200)) # prints 330
print(add(100 , 200 , 300)) # prints 600
print(add(100 , c = 200)) # prints 320
print(add(c = 100 , b = 200 , a = 300)) # prints 600
print(add(c = 100 , a = 200)) # prints 320
print(add()) # Error because it requires one positional argument 'a'
print(add(a = 100 , 200)) # Error because keyword argument should be followed by positional argument but not vice versa
print(add(100 ,  , 300)) # Error
print(add(100, b , 300)) # Error
		  








# Identify  Error
def f1(a = 10 ,  b ,  c = 20 ,  d): # Error because keyword arguments should be followed by positional arguments but not vice versa
    pass
def f2(b , d , a = 10 , c = 20): 
    pass
	








#  Find  outputs (Home  work)
def f1(a = 10):
    print(a)
# End  of  the  function
f1(20) # prints 20
f1() #  prints 10
f1(a = 30) # prints 30
   








# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # prints 330
print(add(100 , 200 , 300)) # prints 620
print(add(100 , 200 , 300 , 400)) # prints 1000
print(add(b = 100 , a = 200)) # prints 330
print(add(100 , 200 , d = 300)) # prints 710
print(add(d = 100 , a = 200 , b = 300)) # prints 610
print(add(c = 100 , d = 200 , 300 , 400)) # Error because keyword argument should be followed by positional argument but not vice versa
print(add(100 , 200 , c = 300 , x = 400)) # Error because 'x' is not defined
print(add()) # Error 









#  Find  outputs (Home  work)
def f1(x = 25):
    return  x
def f2(x):
    return  x
# End  of  the  function
print(f1(10)) # prints 10
print(f1()) # prints 25
print(f2(20)) # prints 20
print(f2()) # Error because needs argument









# Find  outputs (Home  work)
def disp(ch = '*' , n = 4):
    print(ch *  n)
# End of the function
disp('-' , 6) # prints ------
disp('$') # prints $$$$
disp() # prints ****
disp(n = 5) # prints *****
disp(5) # prints 20
disp(n = 7 , ch = '%') # prints %%%%%%%
disp(7 , '@') # prints @@@@@@@
disp(7 , n = 6) # prints 42
disp(ch = '!' , 5) # Error because keyword argument should be followed by positional argument but not vice versa.  
	 








# Find  outputs (Home  work)
def power(a , b  =  2):
    return  a ** b
#end of the function
print(power(2 , 6)) # prints 64
print(power(5)) # prints 25
print(power(b = 3 , a = 4.5)) # prints 91.125
print(power(3 + 4j)) # prinst (-7+24j)
print(power(True)) # prints 1
def power(b = 2 , a): # Error because keyword arguments should be followed by positional arguments but not vice versa
    pass









# Find outputs  (Home  work)
def add(a , b):
    print('2-argument  function')
    return a + b
def add(a , b , c):
    print('3-argument  function')
    return a + b + c
def add(a  = 1 , b  = 2 , c   = 3 , d = 4):
    print('4-argument  function')
    return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) # prints 4-argument<nextline>100
print(add(50 , 60 , 70)) # prints 4-argument<nextline>184
print(add(80 , 90)) # prints 4-argument<nextline>177
print(add(100)) # prints 4-argument<nextline>109
print(add()) # prints 4-argument<nextline>10









# Find outputs  (Home  work)
def disp(a , b):
    print('2-argument function  :  ' , a , b)
def disp(a , b , c , d):
    print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
    print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # prints 3-argument<nextline>10 20 30
disp(40 , 50 , 60 , 70) # Error because it requires only 3 arguments
disp(80, 90) # Error because it requires 3 arguments
	 








# Find outputs(Home  work)
def add(* , a = 10 , b = 20):
    return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # prints 70
print(add()) # prints 30
print(add(a = 50)) # prints 70
print(add(b = 60 , a = 70)) # prints 130
print(add(80 , 90)) # Error because arguments must be keyword arguments
		  








# Find  outputs(Home  work)
def add(a = 10 , b , c): # Error because keyword arguments must be followed by positional arguments but not vice versa
    #pass
def add( * , a = 10 , b , c ):
    return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # prints 120
print(add(b = 60 , c = 70)) # prints 140
print(add(c = 80 , b = 90 , a = 100)) # prints 270
print(add(c = 25 , a = 43)) # 
print(add(1 , 2 , 3))
def add(a , b = 10 ,  c ,  * , d  , e = 20, f): # Error because keyword arguments must be followed by positional arguments but not vice versa
    pass