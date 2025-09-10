# home work questions on 02/09/2025

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))

'''
 # answeres
10,20,30,18
<class 'tuple'>
4
''
()
<class 'tuple'>
0
''
([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3
''
('Hyd',)
<class 'tuple'>
1
''
((100,200,300))
<class 'tuple'>
1
''
error because t is keyword argument



--------------------------------------------------------
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
f1(b = (10 , 20 , 30) , a = 40)
f1()
f1(a = 10 , (20 , 30 , 40))
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)

# outputs
a:10 <tab> b:(20,30,40)
a:50 <tab> b:(60,)
a:70 <tab> b:()
a:80 <tab> b:()
error because keyword arguments ar not allowed for *b 
a:25 <tab> b:()
error because a we cannot assign a as keyword followed by positional arguments
error 
error giving multiple arguments to a and a is keyword argument 
a:((10 , 20 , 30) <> b:(10 , 20 , 30)
a:(10,20,30) b:(10,20,30)

------------------------

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
f1(b = 10 , a = (20 , 30 , 40))
f1(b = 10 , (20 , 30 , 40))
f1()
f1(10 , 20 , 30 , (10 , 20 , 30))
f1(10 , 20 , 30 , 40)
f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))


# outputs 
a:(10,20,30) <tab> b:40
a:(50,) <tab> b:60
a:() <tab> b:70
error *a cannot be keyword argument
error b keyword argument , positional argument is after keyword argument  
# error b is required here because no defalult value 
error all are positional argument and b is meising 
error b is missing no default value 
error b is missing no default value
a:(10 , 20 , 30) <tab> b: (10 , 20 , 30)

------------------------------------

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
f1(a = 1 , 2 , c = 3)
f1(1 , 2 , 3)
f1(a = 1 , b = 2 , c = 3)
f1(a = 25 , 100 , 200 , 300 , c = 35)

# outputs
a:10  <tab> b:(20,30,40) <tab> c:50
a:10 <tab>b:(70,) <tab>c:50
a:90 <tab>b:()<tab>c:100
error positional argument after the keyword argument 
error missing keyword argument 
error because *b takes only positional argument only 
error positional argument after the keyword argument


-------------------------------


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c):
       pass
def   f7(a , *b , c ,  /):
       pass

# outputs 
f2() is valid # because *a takes positional arguments and b takes keyword arguments these is valid

f3() is valid # because there can be two positional / keyword arguments in function call

f4() is valid # because because there can be two positional or two keyword arguments in function call

f5() is valid # it follows the positional and then keyword argument


--------------------------------------

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))


# outputs

([10 , 20] , {30 , 40} , (50 , 60))
<class 'tuple'>
([10 , 20])
<class 'list>
({30 , 40})
<class 'set'> 
((50 , 60))
<class 'tuple'>
--------------------------------------------------



# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
'''


# outputs
results
<class 'dict'>
{RollNo = 10 , StudName = 'Rama  Rao'}
''
results
<class 'dict'>
{EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0} 
''
results
<class 'dict'>
{AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm'}
''
results
<class 'dict'>
{}

----------------------------------------------------------
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

# outputs 
results
{Empno ... 25}
{Empname ... 'Rama  Rao'}
{Salary ... 10000.0}
{Gender ... m}
results

---------------------------------------------

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

# outputs 
<class 'tuple'>
(25 , 10.8 , 'Hyd' , True)
''
<class 'dict'>
{EmpNum:25 , EmpName:'Sita' , Salary:10000.0}


-----------------------------------------

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

# outputs
Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
#error because it should be empno 
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

--------------------------------------------------------


# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

#outputs 
25

Hyd
(10,20,30)

10.8
(25,'Hyd',True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

-----------------------------------------------
---------------------------------------------------------------------------------
find the outputs (Home work)
a = 10        # global a
def f1():
    b = 40    # local b
    print('a : ' , a)   # refers to global a
    print('b : ' , b)   # refers to local b
    print('c : ' , c)   # refers to global c
    print()

b = 20        # global b
def f2():
    a = 50    # local a
    print('a : ' , a)   # refers to local a
    print('b : ' , b)   # refers to global b
    print('c : ' , c)   # refers to global c

c = 30        # global c

print('a : ' , a)   # a=10
print('b : ' , b)   # b=20
print('c : ' , c)   # c=30
print()

a +=  1   # a=11
b +=  1   # b=21
c +=  1   # c=31

f1()

a +=  1   # a=12
b +=  1   # b=22
c +=  1   # c=32

f2()
print('Bye')
-------------
#OUTPUTS 
--f1 functiion outputs
a:10
b:20
c:30

11
21
31

call f1()
a → global = 11

b → local = 40

c → global = 31

a :  11
b :  40
c :  31

next 
a :12
b: 22
c: 32
 calling f2() functionns 
a → local = 50

b → global = 22

c → global = 32

a :  50
b :  22
c :  32

Bye

------------------------------------------------------------------------------------

# Find  outputs (Home  work)
def   f1():
	a = 20 # local a 
	print(a) # 20
	a += 1 # 21 # cannot used 
#End  of  the  function
a = 10 # global a 
print(a) # 10
a += 1 # 11 
f1() # 20 
print(a) # 20

#outputs 
10
20
11 
