#Modify  following  program  such  that  every  function  should  be  executed
def f1():
    print('I am overwritten')
def f1(x):
    print('I am also overwritten')
def f1(x , y , z):
	print('Three argument function : ' , x , y , z)
f1(10, 20, 30) 


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

How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)
'''
 
def   prime(n):
    c=[]
	for i in range(2 , n//2 + 1):
		if n % i == 0:
			continue
		else:
			c.append(i)
    for j in c:
        return j
n=int(input("Enter a number : "))
x=prime(n)
print(x)



# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10	b : 20	c : 30 
f1(25 , 10.8 , 'Hyd')  #  a : 10	b : 20	c : 30 
f1(b = 40.7 , a = 50.2 , c = 60.5)  #  a  :  50.2        b  :  40.7      c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  #  a  :  Cyb         b  :  Sec       c :  Hyd
f1(c = 3 + 4j , a = True , b = None)  #  a  :  True        b  :  None      c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')  #   a  :  25          b  :  Hyd       c :  10.8
f1(a = 100 , 200 , 300)  #  Error
f1(True , None , b = 'Hyd')  #  Error
f1(10 , 20 , x = 30)  #  Error
f1(10 , 20)  #  Error 



# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)  #  Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  #  Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)  #  Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20



# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))  #  23
print(f1(*[6 , 7 , 8]))  #  62
print(f1([6 , 7 , 8]))  #  Error 
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  #  16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  #  Error 
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  #  Error
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})  #  Error
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))  #  Error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))  #   Error due to argument after key word
print(sorted(a , rev = True))  #   Error due to sorted not have rev key word
print(25 , 10.8 , 'Hyd' , separator = '\t')  #  25	10.8	'Hyd' 
print(25 , 10.8 , 'Hyd' , endofline = '\t')  #  Error due to endofline 
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  #  Error due to positional argument before have keyword argument



# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  #  a : 10	b : 20
f1(b = 30 , a = 40)  #  a : 40	b : 30
f1(50 , 60)  #  Error
f1(70 , b = 80)  #  Error
f1(a = 15 , 25)  #  Error due to cannot use cannot apply after key word arguement


#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)  #  a  :  10          b :  20         c  :  30 
f1(a = 40 , b = 50 , c = 60)  #  a  :  40          b :  50         c  :  60 
f1(c = 100 , b = 90 , a = 80)  #  a  :  80          b :  90         c  :  100
f1(70 , 80 , c = 90)  #  Error due to its takes one argument
f1(70 , 80 , 90)  #  Error due to it not taking argument
f1(c = 15 , b = 25 , 35)  #  Error due to key word argument should before positional argument


# Identify error (Home  work)
def   f1(a  , b , *):  #  Error due to  can you use 1st arg
        pass


#  Identify error (Home  work)
 def   f1(a  , b , *): 
        pass
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  #  a  :  10          b  :  20
f1(a = 30 ,  b = 40)  #  Error
f1(50 , b = 60)  #  Error
f1(a = 70 , 80)  #  Error due to provisional arhument cant follow keyword argument


# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)  #  a  :  10          b :  20         c  :  30 
f1(40 , 50 , c = 60)  #  a  :  40          b :  50         c  :  60
f1(a = 70 , b = 80 , c = 90)  #  Error
f1(a = 100 , b = 110 , 120)  #  error due to before provisional argument cant use key word argument
f1(a = 130 , 140 , c = 150)  #  error due to before provisional argument cant use key word argument
f1(160 , b = 170 , 180)  #  #  error due to before provisional argument cant use key word argument
f1(190 , b = 200 , c = 210)   #  Error


def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  #  a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)  #  Error
f1(1 , 2 , 3 , 4 , 5 , f = 6)  #  Error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)   #  error due to before provisional argument cant use key word argument
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)  #  a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60


# Identify error (Home  work)
def  f1(/ , a , b ,  c):  #   Error due / not use in 1st
        pass
def   f2(a , b , c , *):  #  Error due to *
        pass


# Identify  error  (Home  work)
def  f4(* , a , b , c , /):  #   / must appear before *
	        pass


# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)  #   3rd  function :  , 10
f1(y = 20)  #  Error due to f1 used for z so y get error
f1(x = 30)  #  Error due to f1 used for z so x get error


# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))  #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #  600
print(add(100 , c = 200))  #  320
print(add(c = 100 , b = 200 , a = 300))  #  600
print(add(c = 100 , a = 200))  #  320
print(add())  #  Error due to give atlkeast one argument
print(add(a = 100 , 200))  #  error due to before provisional argument cant use key word argument
print(add(100 ,  , 300))  #  Error due to epmty
print(add(100 ,  b , 300))  #  Error due to b


#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  #  10
print(f1())  #  25
print(f2(20))  #  20
print(f2())  #  Error due to x is requred
