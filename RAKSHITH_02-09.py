
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  (10,20,15,18) <nextline> <class 'tuple'> <nextline> 4
f1()        # () <nextline> <class 'tuple'> <nextline> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})    #  ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <nextline> <class 'tuple'> <nextline> 3
f1('Hyd')       # 'Hyd' <nextline> <class 'tuple'> <nextline> 1
tpl = (100 , 200 , 150)
f1(tpl)         # ((100,200,150),) <nextline> <class 'tuple'> <nextline> 1
f1(t = (10 , 20 , 30))      # Error f1()  got an unexpected keyword argument 't'


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    return sum(a)/len(a)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))   # 15.75
print(avg(25 , 10.8 , True))    # 12.26666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg())    # Error ZeroDivisionError  
print(avg(25))  # 25.0
print(avg(3 + 4j , 5 + 6j)) # (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Error unpack the tuple

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
    return " ".join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))   # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Languages
print(concat())     # nothing
print(concat('Python'))     # Python
print(concat(1, 2, 3))  #  Error expected str instance, int found

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)   # a : 10    b : (20,30,40)
f1(50 , 60)             # a : 50     b : (60,)
f1(70)                  # a : 70    b : ()
f1(a = 80)              # a : 80    b : ()
f1(b = (10 , 20 , 30) , a = 40)     # got an unexpected keyword argument 'b'
f1()                    # a : 25    b : ()
f1(a = 10 , (20 , 30 , 40))     #   Positional arguments follows keyword arguent
f1(25 , b = (10 , 20 , 30))     #   got an unexpected keyword argument 'b'
f1(25 , a = (10 , 20 , 30))     #    got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30)   # a : (10,20,30)    b : (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)   #  Positional arguments follows keyword arguent

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)   # a : (10,20,30)    b : 40
f1(50 , b = 60)             # a : (50,)   b : 60
f1(b = 70)                  # a : ()    b : 70
f1(b = 10 , a = (20 , 30 , 40))     # got an unexpected argument  'b'
f1(b = 10 , (20 , 30 , 40))         # positional argument follows keyword argument
f1()                                # Error missing one keyword-only argument 'b'
f1(10 , 20 , 30 , (10 , 20 , 30))   # Error missing one keyword-only argument 'b'
f1(10 , 20 , 30 , 40)               # Error missing one keyword-only argument  'b'
f1(25)                              # Error missing one keyword-only argument 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30))   # a : (10,20,30)    b : (10,20,30)


#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)  # a : 10    b : (20,30,40)  c : 50
f1(60 , 70 , c = 80)            # a : 60    b : (70,)  c : 80
f1(90 , c = 100)                # a : 90    b : ()  c : 100     
f1(a = 1 , 2 , c = 3)           # positional argument follows keyword argument
f1(1 , 2 , 3)                   # Error missing one keyword-only argument 'c'
f1(a = 1 , b = 2 , c = 3)       # Error got an unexpected argument 'b'
f1(a = 25 , 100 , 200 , 300 , c = 35)   # positional argument follows keyword argument

# Which  of  the  following  are  valid  ?  (Home  work)

def   f1(*a , *b):  # * argument may appear only once
        pass
def  f2(*a , b):    # Valid
        pass
def  f3(a , *b):    # Valid
        pass
def  f4(a , b): # Valid
        pass
def    f5(a , *b , c):  # Valid
        pass

def   f6( * , a , *b , c):  # * argument may appear only once
       pass

def   f7(a , *b , c ,  /):  # Not valid
       pass
 

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))   


output:- 
([10 , 20] , {30 , 40} , (50 , 60))
<class 'tuple'>
[10,20]
<class 'list'>
{30,40}
<class 'set'>
(50,60)
<class 'tuple'>


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


output:-
Results
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}

Results
<class 'dict'>
{'Empno' : 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}

Results
<class 'dict'>
{'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , 'Gender' : 'm'}

Results
<class 'dict'>
{}


# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()


output:-
Results
'EmpNo'...25
'EmpName'...'Rama Rao'
'Salary'...10000.0
'Gender'...'m'
Results


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


output:-
<class 'tuple'>
(25,10.8,'Hyd',True)

<class 'dict'>
{'EMpNum': 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}


#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)


output:-
Emp Number : 25     Emp Name : 'Sita'   Salary : 10000.0
Error unexpected keyword argument 'eno'
{'empno' : 25 , 'ename' : 'Sita' , 'sal' : 10000.0}
{'eno' : 25 , 'empname' : 'sita' , 'salary' : 10000.0}


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


output:-
25

'Hyd'
(10,20,30)

10.8
(25,'Hyd',True)
{'EmpNo': 12 , 'EmpName': 'Rama Rao' , 'Salary' : 10000.0}


#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)   # a : 10
print('b : ' , b)   # b : 20
print('c : ' , c)   # c : 30
print()     # nothing
a +=  1
b +=  1
c +=  1
f1()    # a : 11 <nextline> b : 40 <nextline> c : 31
a +=  1
b +=  1
c +=  1
f2()    # a : 50 <nextline> b : 22 <nextline> c : 32
print('Bye')    # Bye


# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)    # 10
a += 1
f1()    # 20
print(a)    # 11

