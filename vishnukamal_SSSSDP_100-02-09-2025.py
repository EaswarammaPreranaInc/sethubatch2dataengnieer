# 1) Variable  number  of  arguments  demo  program

def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
'''
(10,20,15,18)
<class 'tuple'>
4
'''
f1()
'''
()
<class 'tuple'>
0
'''
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
'''
([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3
'''
f1('Hyd')
'''
('Hyd',)
<class 'tuple'>
1
'''
tpl = (100 , 200 , 150)
f1(tpl)
'''
((100, 200, 150),)
<class 'tuple'>
1
'''
f1(t = (10 , 20 , 30)) # Error we cannot give keyword argument due to '*'




# 2) Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)

def  avg(*a):
	return sum(a)/len(a)# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # Output: 15.75
print(avg(25 , 10.8 , True)) # Output: 12.266666666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # Output: 14.26
print(avg()) # Error as it is a zero division error 
print(avg(25)) # Output: 25.0
print(avg(3 + 4j , 5 + 6j)) # Output: (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Error as we cannot add int(0) and tuple (10 , 20 , 15 , 18)



# 3) Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)

def  concat(*a):
	return ' '.join(a) # Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) # Output: Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Output: Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Output: Python Is A Great Language
print(concat()) # Output: empty string
print(concat('Python')) # Output: Python 
print(concat(1, 2, 3)) # Error as integers cannot be concatenate



# 4) Find  outputs (Home  work)

def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # Output: a : 10      b  :  (20, 30, 40)
f1(50 , 60) # Output: a : 50    b  :  (60,)
f1(70) # Output: a : 70     b  :  ()
f1(a = 80) # Output: a : 80     b  :  ()
f1(b = (10 , 20 , 30) , a = 40) # Output: a : 40    b : (10, 20, 30)
f1() # Output: a : 25     b : ()
f1(a = 10 , (20 , 30 , 40)) # Error as Non-keyword argument follows keyword argument.
f1(25 , b = (10 , 20 , 30)) # Error as mixing positional with keyword for a *args parameter 
f1(25 , a = (10 , 20 , 30)) # Error as f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) # Output: a : (10, 20, 30)    b : (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # Error as Positional arguments cannot follow keyword argument



# 5) Find  outputs (Home  work)

def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # Output: a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60) # Output: a  :  (50,)   	   b  :  60
f1(b = 70) # Output: a  :  ()   	   b  :  70
f1(b = 10 , a = (20 , 30 , 40)) # Error as 'a' connot keyword argument due to star
f1(b = 10 , (20 , 30 , 40)) # Error as positional argument follows keyword argument 
f1() # Error as f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , (10 , 20 , 30)) # Error as f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , 40) # Error as f1() missing 1 required keyword-only argument: 'b' 
f1(25) # # Error as f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # Output: a  :  (10, 20, 30)   	   b  :  (10, 20, 30)



# 6) Find  outputs (Home  work)

def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # Output: a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
f1(60 , 70 , c = 80) # Output: a  :  60  	  b  :  (70,)  	  c  :  80
f1(90 , c = 100) # Output: a  :  90  	  b  :  ()  	  c  :  100
f1(a = 1 , 2 , c = 3) # Error as positional argument follows keyword argument
f1(1 , 2 , 3) # Error as f1() missing 1 required keyword-only argument: 'c'
f1(a = 1 , b = 2 , c = 3) # Error as f1() missing 1 required keyword-only argument: 'c'
f1(a = 25 , 100 , 200 , 300 , c = 35) # Error as positional argument follows keyword argument
5 , 100 , 200 , 300 , c = 35)



# 7) Which  of  the  following  are  valid  ?  (Home  work)

def   f1(*a , *b): # Invalid as Multiple *args are not allowed
        pass
def  f2(*a , b): # valid
        pass
def  f3(a , *b): # valid
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c): # valid
        pass
def   f6( * , a , *b , c): # Invalid as only one starred parameter is allowed
       pass
def   f7(a , *b , c ,  /): # Invalid as positional only argument / should come before *arg
       pass



# 8) Find  outputs  (Home  work)

def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
# Output: 
([10, 20], {30, 40}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{30, 40}
<class 'set'>
(50, 60)
<class 'tuple'>
'''


# 9) Variable  number  of  keyword  arguments  demo  program

def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
'''
# Output: 
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}
'''
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
'''
# Output: 
Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
'''
# Output: 
Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
'''
disp()
'''
# Output: 
Results
<class 'dict'>
{}
'''



# 10) Find  outputs  (Home  work)

def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
'''
# Output: 
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
'''
f1() # Output: Results



# 11) Find  outputs (Home  work)

def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
'''
# Output:
<class 'tuple'>
(25, 10.8, 'Hyd', True)
'''
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''
# Output: 
<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''


# 12) Find  outputs (Home work)

def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Output:Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error as f1() got an unexpected keyword arguments which is not defined
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # Output:{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # Output:{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}



# 13) Find  outputs   (Home  work)

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
'''
# Output:
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''



# 14) Find  outputs (Home  work)

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
print('a : ' , a) # Output: 10
print('b : ' , b) # Output: 20
print('c : ' , c) # Output: 30
print()
a +=  1
b +=  1
c +=  1
f1()
'''
# Output: 
11
40
31
'''
a +=  1
b +=  1
c +=  1
f2()
'''
# Output: 
50
22
32
'''
print('Bye') # Output: Bye



# 15) Find  outputs (Home  work)

def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a) # Output: 10
a += 1
f1()
'''
# Output: 
20
'''
print(a) # Output: 11