# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(30,40,50)
	


# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)#a:10<tab>b:20<tab>c:30
f1(25 , 10.8 , 'Hyd')#a:25<tab>b:10.8<tab>c:30
f1(b = 40.7 , a = 50.2 , c = 60.5)#a:50.2<tab>b:40.7<tab>c:60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a:Cyb<tab>b:Sec<tab>c:Hyd
f1(c = 3 + 4j , a = True , b = None)#a:True<tab>b:None<tab>c:(3+4j)
f1(25 , c = 10.8 , b = 'Hyd')#a:25<tab>b:hyd<tab>c:10.8
#f1(a = 100 , 200 , 300)  #  Error:due 'a' contain multiple arguments
#f1(True , None , b = 'Hyd')#error
#f1(10 , 20 , x = 30)#error :unexpected keyword
# #f1(10 , 20)#error due 1 postional argument is missing   



# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#empno:25<tab>ename:Rama Rao<tab>sal:10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#empno:35<tab>ename:sita<tab>sal:20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp:Rama Rao<tab>Emp Name:30000>.<tab>salary:20


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
from E.KARUNA_034_August_28 import prime
x = int(input("Enter a number: "))
count = 0
print("Prime numbers")
for i in range(2, x + 1):
    if prime(i):
        print(i)
        count += 1
print("Number of prime numbers:", count)






#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#16
#print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})#error bcz there is fuction calling
#print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))#error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))#error keyword argument followed by positional arugument
#print(sorted(a , rev = True))#error due to rev
#print(25 , 10.8 , 'Hyd' , separator = '\t')#error due to separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t')#error due to endofline
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#postional argument and keyword argument mixed not in order




# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a:10<tab>b:20
f1(b = 30 , a = 40)#a:40<tab>b:30
#f1(50 , 60)#error
#f1(70 , b = 80)#error
#f1(a = 15 , 25)#error


#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a:10<tab>b:20<tab>c:60
f1(a = 40 , b = 50 , c = 60)#a;40<tab>b:50<tab>c:60
f1(c = 100 , b = 90 , a = 80)#a:80<tab>b:90<tab>c:100
f1(70 , 80 , c = 90)#error
f1(70 , 80 , 90)#error
#f1(c = 15 , b = 25 , 35)#error

# Identify error (Home  work)
#def   f1(a  , b , *):#*does not defined at last argument in a function
pass



#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a:10<tab>b:20
f1(a = 30 ,  b = 40)#error not valid
f1(50 , b = 60)#error:one argument passed as keyword
f1(a = 70 , 80)#error:postional after keyword



# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a:10<tab>b:20<tab>c:30
f1(40 , 50 , c = 60)#a:40<tab>b:50<tab>c:60
f1(a = 70 , b = 80 , c = 90)#error :positional_only used as keyword
f1(a = 100 , b = 110 , 120)#error:postional after keyword
f1(a = 130 , 140 , c = 150)#error:postional after keyword
f1(160 , b = 170 , 180)#error:postional after keyword
f1(190 , b = 200 , c = 210)#error :positional_only used as keyword




# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a:10<tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error:'b' is positional only
f1(1 , 2 , 3 , 4 , 5 , f = 6)#error too many positional arguments
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#error positional arg after keyword arg
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a:10,tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60



# Identify error (Home  work)
def  f1(/ , a , b ,  c):#/ cannot be the first 
        pass
def   f2(a , b , c , *):#*cannot be the last
        pass



# Identify  error  (Home  work)
def  f4(* , a , b , c , /):#/must come before *
	        pass



# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)#z=10
f1(y = 20)#error:unexpected keyword
f1(x = 30)#error:unexpected keyword




# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))#150
print(add(100 , 200))#330
print(add(100 , 200 , 300))#600
print(add(100 , c = 200))#320
print(add(c = 100 , b = 200 , a = 300))#600
print(add(c = 100 , a = 200))#320
print(add())#error:missing required arument 'a'
print(add(a = 100 , 200))#error positional arg after keyword
print(add(100 ,  , 300))#error invalid
print(add(100 ,  b , 300))#error




# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):#default arguments not properly placed
	pass
def   f2(b , d , a = 10 , c = 20):
	pass



#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20
f1()#10
f1(a = 30)#30



# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#330
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#610
print(add(c = 100 , d = 200 , 300 , 400))#error:positional argument follows keyword argument
print(add(100 , 200 , c = 300 , x = 400))#error:unexpected keyword argument 'x'
print(add())#error:missing arguments




#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
print(f2())#error:missing 1 required positional argument:'x'


# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#error invalid operand
disp(7 , n = 6)#42
disp(ch = '!' ,  5)#error:positional argument follows keyword argument




# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#(-7+24j)
print(power(True))#1
def   power(b = 2 , a):#error:non-default argument follows default argument
 	 pass




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
print(add(10 , 20 , 30 , 40))#4-argument function
                             #100
print(add(50 , 60 , 70))#4-argument function
                        #184
print(add(80 , 90))#4-argument function
                   #177
print(add(100))#4-argument function
               #109
print(add())#4-argument function
            #10



# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)#3-argument function:10 20 30
disp(40 , 50 , 60 , 70)#error: 4 arguments
disp(80 , 90)#3-argument function:80 90 25



# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#30
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#error:add() takes 0 positional aguments but 2 arguments are there


# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
print(add(c = 25 , a = 43))#error :'b' is missing
print(add(1 , 2 , 3))#add()takes 0 positional arguments but 3 arguments are there
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):#error:non-default argument follows default argument
		pass