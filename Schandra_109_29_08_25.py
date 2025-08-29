: # Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
###########
def f1(*args):
    if len(args) == 0:
        print('No-argument function')
    elif len(args) == 1:
        print('Single argument function:', args[0])
    elif len(args) == 2:
        print('Two argument function:', args[0], args[1])
    elif len(args) == 3:
        print('Three argument function:', args[0], args[1], args[2])
    else:
        print('Function with more than three arguments:', args)

# Test calls
f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)
f1(1, 2, 3, 4)   # optional extra case




: '''

Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		  Number  of   prime  numbers : 4
'''
How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)

############
# Assume prime() is already defined elsewhere
# Example:
# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

n = int(input("Enter a number: "))
count = 0

print("Prime numbers")

for k in range(2, n+1):
    if prime(k):
        print(k)
        count += 1

print("Number of prime numbers :", count)





: # Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  ## valid  
f1(25 , 10.8 , 'Hyd')   ## valid
f1(b = 40.7 , a = 50.2 , c = 60.5)   ## valid
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  ## valid
f1(c = 3 + 4j , a = True , b = None)  ## valid
f1(25 , c = 10.8 , b = 'Hyd')   ## valid
f1(a = 100 , 200 , 300)  #  Error
f1(True , None , b = 'Hyd')  #  Error
f1(10 , 20 , x = 30) #  Error
f1(10 , 20) #  Error 



: # Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)
###########
Emp Number :   25 	 Emp Name : Rama Rao       	 Salary : 10000.0
Emp Number :   35 	 Emp Name : Sita           	 Salary : 20000.0
Emp Number : Rama  Rao 	 Emp Name : 30000.0        	 Salary : 20



: #  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))  ## 23
print(f1(*[6 , 7 , 8])) ## 62
print(f1([6 , 7 , 8])) ## error  
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  ## 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) ## error
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) ## error
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})  ## error
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6})) ## error



: # Identify  Error (Home  work)
a = [10, 20, 15, 5, 12]
print(sorted(reverse=True, a))          # Error: positional argument after keyword
print(sorted(a, rev=True))              # Error: wrong keyword 'rev'
print(25, 10.8, 'Hyd', separator='\t')  # Error: 'separator' should be 'sep'
print(25, 10.8, 'Hyd', endofline='\t')  # Error: 'endofline' should be 'end'
print(25, sep='\t', 10.8, end='\t', 'Hyd') # SyntaxError: positional args after keyword



: # Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) ## valid
f1(b = 30 , a = 40) ## valid
f1(50 , 60)     ## error
f1(70 , b = 80) ## error
f1(a = 15 , 25) ## error




: #Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)     ## valid
f1(a = 40 , b = 50 , c = 60) ## valid
f1(c = 100 , b = 90 , a = 80)## valid
f1(70 , 80 , c = 90)     ## error
f1(70 , 80 , 90)         ## error
f1(c = 15 , b = 25 , 35) ## error



: # Identify error (Home  work)
def   f1(a  , b , *):
        pass
  ##########( can not * at the end,) error

: #  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) ## valid
f1(a = 30 ,  b = 40) ## error
f1(50 , b = 60)      ## error
f1(a = 70 , 80)      ## error


: # Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) ## valid
f1(40 , 50 , c = 60) ## valid
f1(a = 70 , b = 80 , c = 90) ## error
f1(a = 100 , b = 110 , 120) ## error
f1(a = 130 , 140 , c = 150) ## error
f1(160 , b = 170 , 180) ## error
f1(190 , b = 200 , c = 210) ## error



: # Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) ## a: 10 b: 20 c: 30 d: 40 e: 50 f: 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) ## error
f1(1 , 2 , 3 , 4 , 5 , f = 6) ## error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) ## error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)  ## a: 10 b: 20 c: 30 d: 40 e: 50 f: 60


: # Identify error (Home  work)
def  f1(/ , a , b ,  c):
        pass
 ## Error: / must be after parameter names.
def   f2(a , b , c , *):
        pass
## Error: * must be followed by arguments or *args.

: # Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass
 Error: / cannot appear after *.

: # Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) ## 10
f1(y = 20) ## error
f1(x = 30) ## error



: # Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))  ## 150
print(add(100 , 200)) ## 330
print(add(100 , 200 , 300)) ## 600
print(add(100 , c = 200)) ## 320
print(add(c = 100 , b = 200 , a = 300)) ## 600
print(add(c = 100 , a = 200))  ## 320
print(add()) ## error
print(add(a = 100 , 200)) ## error
print(add(100 ,  , 300))  ## error
print(add(100 ,  b , 300))## error


: # Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass
 ##Error: SyntaxError: non-default argument follows default argument
def   f2(b , d , a = 10 , c = 20):
	pass
## valid


: #  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)  ## 20
f1()  ## 10
f1(a = 30) ## 30


: # Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) ## 330
print(add(100 , 200 , 300)) ## 620
print(add(100 , 200 , 300 , 400))## 1000
print(add(b = 100 , a = 200)) ## 330
print(add(100 , 200 , d = 300)) ## 610
print(add(d = 100 , a = 200 , b = 300))## 610
print(add(c = 100 , d = 200 , 300 , 400)) ## error
print(add(100 , 200 , c = 300 , x = 400)) ## error
print(add()) ## error


: #  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))## 10
print(f1())  ## 25
print(f2(20))## 20
print(f2())  ## error


: # Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)  ## ------
disp('$') ## $$$$
disp() ## ****
disp(n = 5) ## *****
disp(5) ## error
disp(n = 7 , ch = '%') ## %%%%%%%
disp(7 , '@') ## error
disp(7 , n = 6) ## error
disp(ch = '!' ,  5) ## error



: # Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) ## 64
print(power(5)) ## 25
print(power(b = 3 , a = 4.5))## 91.125
print(power(3 + 4j))## -7+24j
print(power(True)) ## 1
def   power(b = 2 , a):
 	 pass
## error


: # Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40)) ## 100
print(add(50 , 60 , 70)) ## 184
print(add(80 , 90)) ## 177
print(add(100)) ## 109
print(add()) ## 10


: # Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) ## 10 20 30
disp(40 , 50 , 60 , 70) ## error
disp(80 , 90) ## 80 90 25


: # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) ## 70
print(add()) ## 30
print(add(a = 50)) ## 70
print(add(b = 60 , a = 70)) ## 130
print(add(80 , 90)) ## error


: # Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
## Invalid because parameters with defaults must follow positional ones.
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) ## 120
print(add(b = 60 , c = 70))          ## 140
print(add(c = 80 , b = 90 , a = 100))## 270
print(add(c = 25 , a = 43)) ## missing b
print(add(1 , 2 , 3)) ## postional not allowed
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass
##  Invalid: parameter c (non-default) after b=10 (default) is not allowed.
