#Home Work-1
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1()
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1()
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1()
#Home Work-2
'''
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
# How  to  read  a  number
from 28_08_kamuju_sushma import prime
n=int(input("Enter number: "))
# How  to  print  all  prime  numbers  between  2  and  user  input
c=0
for i in range(2,n+1):
	if(prime(i)):
		print(i)
		c=c+1
print('Number  of  prime numbers  :  ' ,  c)
#Home Work-3
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a:10  b:20    c: 30
f1(25 , 10.8 , 'Hyd') #a:25 b:10.8  c:Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5) #a: 50.2 b:40.7  c:60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a:true    b:None  c:Hyd
f1(c = 3 + 4j , a = True , b = None) #a:True    b:None  c:3+4j
f1(25 , c = 10.8 , b = 'Hyd') #a:25 b:Hyd   c:10.8
# f1(a = 100 , 200 , 300)  #  Error,no positional args after key word args
f1(True , None , b = 'Hyd') #error, c value is not passed
f1(10 , 20 , x = 30)#error, no parameter with 'x'
f1(10 , 20)#error, c value is not passed
#Home Work-4
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) #Emp Number: 25:4   Emp name: Rama Rao  Salary: 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
##Emp Number: 35:4   Emp name: Sita  Salary: 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #Emp Number: Rama Rao:4   Emp name: 30000.0  Salary: 20
#Home Work-5
#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #23
print(f1(*[6 , 7 , 8])) #62
print(f1([6 , 7 , 8])) #error, we need to pass 3 values
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # '+' and '*' among key:value is not possible
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error, we need to pass 3 values
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) #{'c' : 2 , 'b' :  4 , 'a' : 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))# '+' and '*' among key:value is not possible
#Home Work-6
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
# print(sorted(reverse = True , a))# no positional args after key word args
print(sorted(a , rev = True)) #[20,15,12,10,5]
print(25 , 10.8 , 'Hyd' , separator = '\t') #25 10.8    Hyd
print(25 , 10.8 , 'Hyd' , endofline = '\t')#25 10.8    Hyd
# print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')# no positional args after key word args
#Home Work-7
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a:10    b:20
f1(b = 30 , a = 40)#a:40    b:30
f1(50 , 60)#error, has to key word args
f1(70 , b = 80)#error, has to be key word args
# f1(a = 15 , 25) #positional arg after keyword is wrong in any scenario 
#Home Work-8
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a:10   b:20    c:30
f1(a = 40 , b = 50 , c = 60)#a:40   b:50    c:60
f1(c = 100 , b = 90 , a = 80)#a:80  b:90    c:100
f1(70 , 80 , c = 90)#error, b has to be key word argument
f1(70 , 80 , 90) #error, b,c has to be key word args
# f1(c = 15 , b = 25 , 35) #key positional arg after key word arg
#Home Work-9
# Identify error (Home  work)
# def   f1(a  , b , *): #atleast arg after '*' is mandatory
        # pass
#Home Work-10
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) #a:10   b:20
f1(a = 30 ,  b = 40) #error, a,b has to be poitional args only
f1(50 , b = 60) #error, a,b has to be poitional args only
# f1(a = 70 , 80) #no positional arg after key-word arg

#Home Work-11
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) #a:10  b:20    c:30
f1(40 , 50 , c = 60) #a:40  b:50    c:60
# f1(a = 70 , b = 80 , c = 90)#error, a,b has to be positional args only
# f1(a = 100 , b = 110 , 120) #error, no positional arg after key-word arg
# f1(a = 130 , 140 , c = 150)#error, no positional arg after key-word arg
# f1(160 , b = 170 , 180)#error, no positional arg after key-word arg
# f1(190 , b = 200 , c = 210)#error, 'b' has to be positional arg

#Home Work-12
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) #a:10   b:20    c:30    d:40    e:50    f:60
# f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)##error, 'b' should be positional arg
# f1(1 , 2 , 3 , 4 , 5 , f = 6)#'e' should be key-word arg
# f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) #no positional arg after key-word arg
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) #a:10   b:20    c:30    d:40    e:50    f:60

#Home Work-13
# Identify error (Home  work)
# def  f1(/ , a , b ,  c): #atleast 1 arg before '/'
#         pass
# def   f2(a , b , c , *): #atleast 1 arg after '*'
#         pass

#Home Work-14
# Identify  error  (Home  work)
# def  f4(* , a , b , c , /): #atleast 1 arg before '/'
# 	        pass

#Home Work-15
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) #3rd function: 10
f1(y = 20) #3rd function: 20
f1(x = 30) #3rd function: 30

#Home Work-16
# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100)) #150
print(add(100 , 200)) #330
print(add(100 , 200 , 300))#600
print(add(100 , c = 200))#320
print(add(c = 100 , b = 200 , a = 300))#600
print(add(c = 100 , a = 200))#320
print(add())#error, a value should be passed
# print(add(a = 100 , 200)) #no positional arg after key-word arg
# print(add(100 ,  , 300)) #b value is not passed
# print(add(100 ,  b , 300)) #'b' is not given any value

#Home Work-17
# Identify  Error
# def   f1(a = 10 ,  b ,  c = 20 ,  d): #error, no non-default arg after default arg
# 	pass
def   f2(b , d , a = 10 , c = 20):#no error 
	pass

#Home Work-18
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) #20
f1()#10
f1(a = 30)#30

#Home Work-19
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) #330
print(add(100 , 200 , 300)) #620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
# print(add(c = 100 , d = 200 , 300 , 400))#error, no positional arg after key-word arg
# print(add(100 , 200 , c = 300 , x = 400))#x key word arg is not present
print(add())#error, a and b values should be passed

#Home Work-20
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) #10
print(f1())#25
print(f2(20))#20
print(f2())#error, there is not default value in function header

#Home Work-21
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) #------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
# disp(ch = '!' ,  5) #no positional arg after key-word arg

#Home Work-22
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#error
print(power(True))#1
# def   power(b = 2 , a): #no non default args after default args
 	#  pass
         
#Home Work-23
# Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40)) #100
print(add(50 , 60 , 70))#184
print(add(80 , 90)) #173
print(add(100))#109
print(add())#10

#Home Work-24
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) #3-argument  function  :  10 20 30
disp(40 , 50 , 60 , 70)#error, has to pass only 3 values
disp(80 , 90)#3-argument  function  :  80 90 25

#Home Work-25
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) #70
print(add()) #30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#error, has to be key-word arg only 

#Home Work-26
# Find  outputs(Home  work)
# def   add(a = 10 , b , c): #no non default arg after deafult args
#         pass
def   add( * , a = 10 , b , c ): # no non default arg after deafult args is ignored after '*'
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #120
print(add(b = 60 , c = 70)) #140
print(add(c = 80 , b = 90 , a = 100)) #270
# print(add(c = 25 , a = 43))#b is not passed error
print(add(1 , 2 , 3))#6
# def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): #no non default arg after deafult args
# 		pass 