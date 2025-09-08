#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	try:
		return sum(a) / len(a) # Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
	except ZeroDivisionError:
		return 'Division by zero is not permited'
	except TypeError:
		return 'Cannot be added'
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # 15.25
print(avg(25 , 10.8 , True)) # 12.66
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # Division by zero is not permited
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # 4 + 5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Cannot be added

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	# Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
	try:
		return ' ' . join(a)
	except TypeError:
		return 'Cannot concatinate integers'
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) # 'Sankar Dayal Sarma'
print(concat('Hyd', 'Is', 'Green', 'City')) # 'Hyd Is Green City'
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat())  # ''
print(concat('Python')) # Python 
print(concat(1,2,3)) # Cannot concatinate integers


#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 25 <tab> b : (20 , 30 , 40)
f1(50 , 60) # a : 50 <tab> b : (60,)
f1(70) # a: 70 <tab> b : ()
f1(a = 80) # a : 80 <tab> b : ()
f1(b = (10 , 20 , 30) , a = 40) # Error as b cannot be kew word argument
f1() # Error as b cannot be kew word argument
f1(a = 10 , (20 , 30 , 40)) # Error as PA is followed by KA
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a=(10,20,30),10,20,30) #Error as PA is followed by KA

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a : (10 , 20 , 30) <tab> b : 40
f1(50 , b = 60) # a : (50,) <tab> b : 60
f1(b = 70) # a : () <tab> b : 70
f1(b = 10 , a = (20 , 30 , 40)) # Error as argument a is keyword argument
f1(b = 10 , (20 , 30 , 40)) #Error as PA is followed by KA
f1() # Error as there is no argument for b
f1(10 , 20 , 30 , (10 , 20 , 30))# Error as there is no argument for b
f1(10 , 20 , 30 , 40) # Error as there is no argument for b
f1(25) # Error as there is no argument for b
f1(10,20,30,b=(10,20,30)) #Error as PA is followed by KA

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a : 10 <tab> b : (20,30,40) <tab> c : 50
f1(60 , 70 , c = 80) # a : 60 <tab> b : (70,) <tab> c : 80
f1(90 , c = 100) # a : 90 <tab> b : () <tab> c : 100
f1(a = 1 , 2 , c = 3)  #Error as PA is followed by KA
f1(1 , 2 , 3) # Error as there is no argument for c
f1(a = 1 , b = 2 , c = 3) # Error as there shpuld be no keyword argument for b
f1(a=25,100,200,300,c=35)  #Error as PA is followed by KA

def   f1(*a , *b): # Error as there should be only 1 *
        pass
def  f2(*a , b):# Error as there should be only 1 *
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c): # Error as there should be only 1 *
       pass
def f7(a , *b , c , /): # Only / or * should be there 
	pass

# Which  of  the  following  are  valid  ?  (Home  work)
# Find  outputs  (Home  work)
def   f1(*a):
	print(a) # ([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a)) # <class 'tuple'>
	for  x  in  a:
		print(x) 
		print(type(x)) 
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

'''
[10 , 20] 
<class 'list'> 
{30 , 40} 
<class 'set'> 
(50 , 60)
<class 'tuple'>
'''

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
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

'''
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results

'''

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
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

'''


#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error as there no keyword eno
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

'''
Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

'''



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
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

'''




