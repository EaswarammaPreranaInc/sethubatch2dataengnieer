# 1) Modify  following  program  such  that  every  function  should  be  executed

def  f1():
	print('No-argument  function')
f1() # Output: No-argument  function    
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60) # Output: Single  argument  function : 60 
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40 , 50) # Output: Two  argument  function : 40 50  
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Output: Three  argument  function :  10 20 30



''' 2) Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		  Number  of   prime  numbers : 4
'''
''' 
previous.py :
def prime(n):
    for i in range(2, (n // 2) + 1): 
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n < 2:
        print("Invalid input")
    elif prime(n):
        print("Prime number")
    else:
        print("Composite number")
'''
from previous import prime  # Import only the prime function from previous.py
n = int(input("Enter a number: "))
if n < 2:
    print("Invalid input")
else:
    count = 0
    print("Prime numbers")
    for i in range(2, n + 1):
        if prime(i):
            print(i)
            count += 1
    print("Number of prime numbers:", count)

'''
# Output:
Enter a number: 11
Prime numbers
2
3
5
7
11
Number of prime numbers: 5
'''



# 3) Find  outputs  (Home  work)

def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # Output: a  :  10          b  :  20        c :  30
f1(25 , 10.8 , 'Hyd') # Output: a  :  25          b  :  10.8      c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5) # Output: a  :  50.2        b  :  40.7      c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # Output: a  :  Cyb         b  :  Sec       c :  Hyd
f1(c = 3 + 4j , a = True , b = None) # Output: a  :  True        b  :  None      c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # Output: a  :  25          b  :  Hyd       c :  10.8
f1(a = 100 , 200 , 300) # Error as we cannot pass positional arguments after keyword arguments
f1(True , None , b = 'Hyd') # Error as we cannot give multiple values for argument 'b'
f1(10 , 20 , x = 30) # error as there is no keyword argument 'x'
f1(10 , 20) # Error as 1 argument is missing

        
        
# 4) Find  outputs (Home  work)

def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Output: Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Output: Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Output: Emp  Number : Rama  Rao         Emp  Name : 30000.0         Salary : 20



# 5) Tricky  program
# Find  outputs (Home  work)

def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # Output: 23
print(f1(*[6 , 7 , 8])) # Output: 62
print(f1([6 , 7 , 8])) # Error as missing 2 positional arguments
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # Output: 16 
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # Output: 14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error as missing 2 positional arguments 
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # Output: {'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # Error as there is no argument of 'x'



# 6) Identify  Error (Home  work)

a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) # Error as we cannot pass positional arguments after keyword arguments 
print(sorted(a , rev = True)) # Error as 'rev' is not a valid keyword
print(25 , 10.8 , 'Hyd' , separator = '\t') # Error as 'separator' is not a valid keyword
print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error as 'endofline' is not a valid keyword 
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # Error as we cannot pass positional arguments after keyword arguments  



# 7) Keyword  only   arguments  demo  program

def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # Output: a  :  10          b :  20
f1(b = 30 , a = 40) # Output: a  :  40          b :  30
f1(50 , 60) # Error as cannot pass positional arguments when only keyword allowed
f1(70 , b = 80) # Error as cannot pass positional arguments when only keyword allowed
f1(a = 15 , 25) # Error as cannot pass positional arguments when only keyword allowed 



# 8) Find  outputs (Home  work)

def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # Output: a  :  10          b :  20         c  :  30
f1(a = 40 , b = 50 , c = 60) # Output: a  :  40          b :  50         c  :  60
f1(c = 100 , b = 90 , a = 80) # Output: a  :  80          b :  90         c  :  100
f1(70 , 80 , c = 90) # Error as keyword only arguments are allowed after star
f1(70 , 80 , 90) # Error as keyword only arguments are allowed after star
f1(c = 15 , b = 25 , 35) # Error as keyword only arguments are allowed after star



# 9) Identify error (Home  work)

def   f1(a  , b , *):
        pass
# Error as there is no arguments after star



# 10) Positional  only  arguments  demo  program

def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # Output: a: 10	    b: 20
f1(a = 30 ,  b = 40) # Error as we cannot use keywords for positional-only arguments
f1(50 , b = 60) # Error as we cannot use keywords for positional-only arguments
f1(a = 70 , 80) # Error as we cannot pass positional arguments after keyword arguments



# 11) Find  outputs (Home  work)

def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # Output: a: 10	b: 20	c: 30
f1(40 , 50 , c = 60) # Output: a: 40	b: 50	c: 60
f1(a = 70 , b = 80 , c = 90) # Error as we cannot use keyword argument for positional-only arguments
f1(a = 100 , b = 110 , 120) # Error as we cannot pass positional arguments after keyword arguments
f1(a = 130 , 140 , c = 150) # Error as we cannot pass positional arguments after keyword arguments
f1(160 , b = 170 , 180) # Error as we cannot pass positional arguments after keyword arguments
f1(190 , b = 200 , c = 210) # Error as we cannot use keyword argument for positional-only arguments



# 12) Find outputs(Home  work)

def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # Output: a: 10	b: 20	c: 30	d: 40	e: 50	f: 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error as b is positional-only, cannot use keyword
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error as keyword-only argument 'e' is missing
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error as we cannot use keyword argument for positional-only arguments
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # Output: a: 10	b: 20	c: 30	d: 40	e: 50	f: 60



# 13) Identify error (Home  work)

def  f1(/ , a , b ,  c): # Error as '/' cannot be placed before arguments
        pass
def   f2(a , b , c , *): # Error as '*' cannot be placed after arguments
        pass



# 14) Identify  error  (Home  work)

def  f4(* , a , b , c , /): # Error as '/' cannot come after keyword-only arguments
	        pass



# 15) Find  outputs  (Home  work)

def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # Output: 3rd function: 10
f1(y = 20) # Output: 3rd function: 20
f1(x = 30) # Output: 3rd function: 30



# 16) Default  arguments  demo  program

def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100)) # Output: 100 + 20 + 30 = 150
print(add(100 , 200)) # Output: 100 + 200 + 30 = 330
print(add(100 , 200 , 300)) # Output: 100 + 200 + 300 = 600
print(add(100 , c = 200)) # Output: 100 + 20 + 200 = 320
print(add(c = 100 , b = 200 , a = 300)) # Output: 300 + 200 + 100 = 600
print(add(c = 100 , a = 200)) # Output: 200 + 20 + 100 = 320
print(add()) # Error as required positional argument is missing
print(add(a = 100 , 200)) # Error as we cannot pass positional arguments after keyword arguments
print(add(100 ,  , 300)) # Error as the value is missing between commas
print(add(100 ,  b , 300)) # Error as 'b' is not defined



# 17) Identify  Error

def   f1(a = 10 ,  b ,  c = 20 ,  d): # Error as we cannot pass non default arguments after default argument
	pass
def   f2(b , d , a = 10 , c = 20): # Valid as here used default arguments after non default argument
	pass



# 18) Find  outputs (Home  work)

def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # Output: 20
f1()  # Output: 10
f1(a = 30) # Output: 30



# 19) Find  outputs (Home  work)

def add(a, b, c=10, d=20):
    return a + b + c + d
# End  of  the  function
print(add(100, 200)) # Output: 100 + 200 + 10 + 20 = 330
print(add(100, 200, 300)) # Output: 100 + 200 + 300 + 20 = 620
print(add(100, 200, 300, 400)) # Output: 100 + 200 + 300 + 400 = 1000
print(add(b=100, a=200)) # Output: 200 + 100 + 10 + 20 = 330
print(add(100, 200, d=300)) # Output: 100 + 200 + 10 + 300 = 610
print(add(d=100, a=200, b=300)) # Output: 200 + 300 + 10 + 100 = 710
print(add(c=100, d=200, 300, 400)) # Error as we cannot use positional argument after keyword argument
print(add(100, 200, c=300, x=400)) # Error as keyword argument 'x' is not defined
print(add()) # Error as required positional arguments: 'a', 'b' are missing



# 20) Find  outputs (Home  work)

def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # Output: 10
print(f1()) # Output: 25
print(f2(20)) # Output: 20
print(f2()) # Error as required positional arguments: 'x'



# 21) Find  outputs (Home  work)

def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # Output: ------
disp('$') # Output: $$$$
disp() # Output: ****
disp(n = 5) # Output: *****
disp(5) # Output: 20
disp(n = 7 , ch = '%') # Output: %%%%%%%
disp(7 , '@') # Output: @@@@@@@@
disp(7 , n = 6) # Output: 42 
disp(ch = '!' ,  5) # Error as we cannot use positional argument after keyword argument



# 22) Find  outputs (Home  work)

def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # Output: 2**6 = 64
print(power(5)) # Output: 5**2 = 25
print(power(b = 3 , a = 4.5)) # Output: 4.5 ** 3 = 91.125
print(power(3 + 4j)) # Output: (3+4j) ** 2 = (-7+24j)
print(power(True)) # Output: True ** 2 = 1
def   power(b = 2 , a): # Error as we cannot use non-default argument after default argument
 	 pass



# 23) Find outputs  (Home  work)

def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) 
''' Output: 
4-argument function
10+20+30+40 = 100 '''
print(add(50 , 60 , 70)) 
''' Output: 
4-argument function
50+60+70+4 = 184 '''
print(add(80 , 90))
''' Output: 
4-argument  function
80+90+3+4 = 177 '''
print(add(100)) 
''' Output: 
4-argument  function
100+2+3+4 = 109 '''
print(add())
''' Output: 
4-argument  function
1+2+3+4 = 10 '''



# 24) Find outputs  (Home  work)

def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # Output: 3-argument function: 10 20 30
disp(40 , 50 , 60 , 70) # Error as it takes 3 arguments, 4 is given
disp(80 , 90) # Output: 3-argument function: 80 90 25



# 25) Find outputs(Home  work)

def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # Output: 30+40 = 70
print(add()) # Output: 10+20 = 30
print(add(a = 50)) # Output: 50+20 = 70
print(add(b = 60 , a = 70)) # Output: 70+60 = 140
print(add(80 , 90)) # Error as we cannot use positional arguments in keywords only arguments 



# 26) Find  outputs(Home  work)

def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # Output: 120
print(add(b = 60 , c = 70)) # Output: 140
print(add(c = 80 , b = 90 , a = 100)) # Output: 270
print(add(c = 25 , a = 43)) # Error as keyword-only argument: 'b' is missing
print(add(1 , 2 , 3)) # Error as we cannot use positional arguments in keywords only arguments
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass   # Error as we cannot use non-default argument 'c' after default argument 'b'
        
   