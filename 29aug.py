1.

# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)

Ans.)

def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(20)	
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(20,30)	
def  f1(x , y , z):
	print('Three  argument  function :',x,y,z)
f1(20,30,30)

o/p = 
No-argument  function
Single  argument  function  :  20
Two  argument  function :  20 30
Three  argument  function : 20 30 30


2.# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)   #a: 10 b: 20 c: 30
f1(25 , 10.8 , 'Hyd')   #a: 25 b: 10.8 c: Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)  ##a: 50.2 b: 40.7 c: 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  ##a: Cyb b: Sec c: Hyd
f1(c = 3 + 4j , a = True , b = None)            ##a: True b: None c: (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')   #a: 25 b: Hyd c: 10.8
f1(a = 100 , 200 , 300)  #Error
f1(True , None , b = 'Hyd') #error
f1(10 , 20 , x = 30)   #error we don't have x 
f1(10 , 20)   #error as we have only 2 argument inpiuts where we need 3


3.
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)   #Emp Number :  25  Emp Name :       Rama Rao Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  #Emp Number :  35  #Emp Name :           Sita salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)   #Emp Number :Rama Rao Emp Name :        30000.0  Salary : 20


4.
#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))   #23
print(f1(*[6 , 7 , 8]))  #unpacks list--> f1(6,7,8)--->62
print(f1([6 , 7 , 8]))  #error, we just have a list of numbers which is just 'a', we also need b, c
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  #dict unpacks only key which are 1, 3, 5 --> 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #error, passing only 1 dictionary is not sufficient, we also need b, c
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  #same as above error
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})    #error, there is no reference with whatever is enclosed in print, either it should be in double quotes to print the same
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))  #error passing only 1 argument which is dict


5.
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #error In Python, positional arguments must come before keyword arguments.
print(sorted(a , rev = True)) #error, rev is not correct, it should be reverse
print(25 , 10.8 , 'Hyd' , separator = '\t')  #error, it is not separator, it is sep
print(25 , 10.8 , 'Hyd' , endofline = '\t')  #error, it is not end of line, it is end
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  # positional arguments must come before keyword arguments. like print(25 ,  , 10.8 ,  'Hyd',  sep = '\t', end = '\t' )


6.
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)   #a : 10 <tab> b : 20
f1(b = 30 , a = 40)   #a : 40 <tab> b : 30
f1(50 , 60)   #error, as it is a positional argument, after * there can be only keyword arguments
f1(70 , b = 80)   #error 70 is positional argument and is not permitted because f1(* , a , b) there can be only key word ags after *
f1(a = 15 , 25) #error 25 is positional argument and is not permitted because f1(* , a , b) there can be only key word ags after *

7.
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)  #a : 10 <tab> b : 20 <tab> c : 30
f1(a = 40 , b = 50 , c = 60) #a : 40 <tab> b : 50 <tab> c : 60
f1(c = 100 , b = 90 , a = 80) #a : 80 <tab> b : 90 <tab> c : 100
f1(70 , 80 , c = 90)   #error, 80 cannot be PA, 
f1(70 , 80 , 90) #error  arguments preceding * can only be KA, but here it is PA, hence error
f1(c = 15 , b = 25 , 35) # error as 35 which is postitional argument placed after kA

8.
# Identify error (Home  work)
def   f1(a  , b , *):  #error, * cannot be placed at the end, atleast there should be 1 argument after *
        pass

9.
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)   #a:10 <tab> b:20
f1(a = 30 ,  b = 40)  #error because there should be PA's only for arguments preceding '/'
f1(50 , b = 60)  #error, there is KA, which is not permitted before '/'
f1(a = 70 , 80)#error, there is KA, which is not permitted before '/'


10.
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)   #a:10<tab>b:20<tab>c:30<tab>
f1(40 , 50 , c = 60) #a:40<tab>b:50<tab>c:60<tab>
f1(a = 70 , b = 80 , c = 90)  #error: arguments preceeding '/' are KA, which is not permitted
f1(a = 100 , b = 110 , 120)  #error: PA after KA, which is not permitted
f1(a = 130 , 140 , c = 150) #error: PA after KA, which is not permitted
f1(160 , b = 170 , 180) #error: PA is not permitted after KA
f1(190 , b = 200 , c = 210)  #error: KA is not permitted preceeding /


11.
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  #a:10<tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60<tab>
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)  #error :as arguments predceeding  / must be PA
f1(1 , 2 , 3 , 4 , 5 , f = 6)  # error: arguments following * must be KA
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  #PA 40 is not permitted after KA
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)  #a:10<tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60<tab>


12.
# Identify error (Home  work)
def  f1(/ , a , b ,  c):  #error: there should be atleast one argument before '/'
        pass
def   f2(a , b , c , *): #error:  there should be atleast one argument after '*'
        pass

13.
# Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass  Error: if There is * before arguments it means all following * must be KA, precedding / must be PA, hence error


14.

# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)  #calling function f1 with keyword argument z = 10, --> 3rd function : 10
f1(y = 20)  #error, function with same name, the last defined function overwrites previous one, no parameter names y in f1(z)
f1(x = 30)  #error, function with same name, the last defined function overwrites previous one, no parameter names x in f1(z)


15.

# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))  #a becomes 100, b=20, c=30, a+b+c=150
print(add(100 , 200))  #a become 100, b=200, c is default 30, 330
print(add(100 , 200 , 300))  #600
print(add(100 , c = 200)) #320
print(add(c = 100 , b = 200 , a = 300)) #600
print(add(c = 100 , a = 200)) #320
print(add())  #error
print(add(a = 100 , 200))  #error
print(add(100 ,  , 300))  #error
print(add(100 ,  b , 300))  #error

16.

# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):  #non default arguments b, c are not permitted after default arg
	pass
def   f2(b , d , a = 10 , c = 20): #no error
	pass

17.

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)  #20
f1()  #defaukt value 10 will remain
f1(a = 30) #30

18.
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))  #330
print(add(100 , 200 , 300))  #620
print(add(100 , 200 , 300 , 400))  #1000
print(add(b = 100 , a = 200)) #330
print(add(100 , 200 , d = 300)) #610
print(add(d = 100 , a = 200 , b = 300))  #610
print(add(c = 100 , d = 200 , 300 , 400)) #positional argument 300 and 400 are not permitted after keyword argument c=100, d=200
print(add(100 , 200 , c = 300 , x = 400)) #error, there is no argument x
print(add())  #args are not passed for a and b

19.

#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  #x is 10 and result is 10
print(f1())  #x is 25 and result is 25
print(f2(20))  #x is 20 and result is 20
print(f2())  #error: argument is not passed for x


20.

# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)  #-*6--> 6 times repeatition --> ------
disp('$') #$$$$
disp() #****
disp(n = 5) #*****
disp(5) #20
disp(n = 7 , ch = '%') #%%%%%%%
disp(7 , '@')  #@@@@@@@
disp(7 , n = 6) #42
disp(ch = '!' ,  5)  #error: positional arg 5 is not permitted after keyword arg


21.

# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) #64
print(power(5)) #25
print(power(b = 3 , a = 4.5))  #4.5^3
print(power(3 + 4j)) #3+4j ^2
print(power(True)) #1^2
def   power(b = 2 , a): #non def arg a is not permitted after def arg
 	 pass


22.

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
print(add(10 , 20 , 30 , 40))  #100
print(add(50 , 60 , 70)) #184
print(add(80 , 90)) #177
print(add(100)) #109
print(add())  #10


23.

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)  #3-argument  function  :  10 , 20 , 30
disp(40 , 50 , 60 , 70)  #error
disp(80 , 90) #error


24.

# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))  #70
print(add())  #30
print(add(a = 50)) #70
print(add(b = 60 , a = 70)) #130
print(add(80 , 90))  #error: positional arguments cannot be passed  due to *

25.

# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  #120
print(add(b = 60 , c = 70))  #140
print(add(c = 80 , b = 90 , a = 100)) #270
print(add(c = 25 , a = 43))  #error: argument is not passed for b
print(add(1 , 2 , 3))  #error positional arguments cannot be passed to keyword due to *
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass  #non default arg c is not permitted after default b=10
