#Variable number of keyword arguments  
def   disp(**a): # **a collects keyword args into a dictionary
	print('Results')
	print(type(a))
	print(a)
	print()
#End of the function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
'''
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

'''
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
'''
Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

'''
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
'''
Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

'''
disp()
'''
Results
<class 'dict'>
{}

'''

# Find  outputs 
def  f1(**a):  #  **a collects keyword arguments into a dictionary
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
'''
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m'''
f1() # Results


# Find  outputs 
def   f1(*a): # *a collects all positional arg into a tuple
	print(type(a))
	print(a)
def   f2(**a): # **a collects all keyword arguments into a dictionary
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}'''


#  Find  outputs 
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)  #  Emp Number : 25 	Emp Name : Sita		Salary:  10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}


# Find  outputs   
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)  #  25
print()
f1('Hyd' , 10 , 20 , 30)

print()
'''
Hyd
(10,20,30)

'''
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
'''
10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}'''
