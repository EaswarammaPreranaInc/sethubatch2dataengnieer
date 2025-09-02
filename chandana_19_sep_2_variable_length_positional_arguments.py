#  Variable  number  of  arguments  
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple of 4 elements (or) args are passed to the function
'''
(10,20,15,18)
<class 'tuple'>
4'''

f1()
'''
()
<class 'tuple'>
0'''

f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
'''
([10,20],(30,40,50),{80,90,60,70})
<class 'tuple'>
3'''

f1('Hyd')
'''
('Hyd',)
<class 'tuple'>
1'''

tpl = (100 , 200 , 150)
f1(tpl)
'''
((100,200,150),)
<class 'tuple'>
1'''

#f1(t = (10 , 20 , 30))  #  Error : can pass only positional arguments to function because of *


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  
def  avg(*a):
        return sum(a)/len(a) if len(a) != 0 else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # 15.75
print(avg(25 , 10.8 , True)) # 12.66666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg())  #  0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j))  # (4+5j)
tpl = (10 , 20 , 15 , 18) 
#print(avg(tpl)) # error : cannot add list and tuple

#  Write  a  function  to  concatenate  strings  passed  to  the  function  
def  concat(*a):
        return ''.join(str(x) for x in a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))  #  HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  #  PythonIsAGreatLanguage
print(concat()) # empty
print(concat('Python')) # Python
print(concat(1, 2, 3))  # 123


#Find  outputs 
def   f1(a = 25  , *b):  # a=25 is default argument for a and *b collects extra positional arguments into a tuple
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)  #  a:10   b:(20,30,40)
f1(50 , 60) # a:50  b:(60,)
f1(70)  #  a:70  b:()
f1(a = 80)  # a:80 b:()
#f1(b = (10 , 20 , 30) , a = 40) # error :b takes only positional arguments
f1() # a:25 b:()
#f1(a = 10 , (20 , 30 , 40)) # error: cannot pass positional arguments after keyword arguments
#f1(25 , b = (10 , 20 , 30)) # error : b is not keyword argument
#f1(25 , a = (10 , 20 , 30)) # error : got multiple values for 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) # a:(10,20,30) b:(10,20,30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30) # error: cannot pass positional arguments after keyword arguments



#Find  outputs 
def    f1(*a , b):  #  *a collects all positional arguments into a tuple and b must be keyword argument 
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a:(10,20,30)  b:40
f1(50 , b = 60)  #  a:(50,)  b:60
f1(b = 70) # a:() b:70
#f1(b = 10 , a = (20 , 30 , 40))  # error : a cannot be passed as keyword argument
#f1(b = 10 , (20 , 30 , 40)) # error: cannot pass positional arguments after keyword arguments
#f1() # error : keyword argument 'b' is missing
#f1(10 , 20 , 30 , (10 , 20 , 30))  # error : keyword argument 'b' is missing
#f1(10 , 20 , 30 , 40)  # error : keyword argument 'b' is missing
#f1(25) # error : 'b' keyword argument is missing
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a:(10,20,30)  b:(10,20,30)


#Find  outputs 
def   f1(a , *b , c): # a can be keyword or positional argument , *b collects extra positional arguments,  c must be passed keyword argument
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a:10  b:(20,30,40)  c:50
f1(60 , 70 , c = 80) #  a:60  b:(70,)  c:80
f1(90 , c = 100)  #  a:90 b:() c:100
#f1(a = 1 , 2 , c = 3) # error : cannot pass positional arguments after keyword arguments
#f1(1 , 2 , 3) # error : keyword arg 'c' is missing
#f1(a = 1 , b = 2 , c = 3) # error : 'b' takes only positional arguments
#f1(a = 25 , 100 , 200 , 300 , c = 35)  #  error : cannot pass positional arguments after keyword arguments


# Which  of  the  following  are  valid  ? 
#def   f1(*a , *b): # error : cannot pass two * args
#        pass
def  f2(*a , b): # a collects all positional arg and 'b' should be keyword arg
        pass
def  f3(a , *b): # 'a' can be positional or keyword and *b collects extra positional arg
        pass
def  f4(a , b): # a and b can be positional or keyword arg
        pass
def    f5(a , *b , c):  #  'a' can be keyword or positional arg, *b collects extra positional args, 'c' must be keyword arg
        pass
#def   f6( * , a , *b , c): # error : only one * parameter is allowed
#       pass
#def   f7(a , *b , c ,  /):  #  error
#       pass


# Find  outputs  
def   f1(*a): # *a collects all positional arguments
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
output:
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>'''


