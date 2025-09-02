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
#f1(t = (10 , 20 , 30)) #Error

'''
(10,20,15,18)
<class 'tuple'>
4
()
<class 'tuple'>
0
([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3
('Hyd',)
<class 'tuple'>
1
((100 , 200 , 150),)
<class 'tuple'>
1
'''

#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)

def  avg(*a):
	    return sum(a)/len(a)
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function

print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg()) #Error
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) #Error

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	return ' '.join(a)
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) #a : 10  \t   b  :  (20,30,40)
f1(50 , 60) #a : 50  \t   b  :  (60,)
f1(70) #a : 70  \t   b  :  ()
f1(a = 80) #a : 80  \t   b  :  ()
f1(b = (10 , 20 , 30) , a = 40) #Error
f1() #a : 25 \t   b  :  ()
f1(a = 10 , (20 , 30 , 40)) #Error
f1(25 , b = (10 , 20 , 30)) #Error
f1(25 , a = (10 , 20 , 30)) #Error
f1((10 , 20 , 30) , 10 , 20 , 30) #a : (10,20,30)  \t   b  :  (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) #Error

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) #a : (10,20,30)  \t   b  :  40
f1(50 , b = 60) #a : (50,)  \t   b  :  60
f1(b = 70) #a : ()  \t   b  :  70
f1(b = 10 , a = (20 , 30 , 40)) #Error
f1(b = 10 , (20 , 30 , 40)) #Error
f1() #Error
f1(10 , 20 , 30 , (10 , 20 , 30)) #Error
f1(10 , 20 , 30 , 40) #Error
f1(25) #Error
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #a : (10,20,30)  \t   b  :  (10,20,30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) #a  :  10  \t  b  :  (20,30,40)  \t  c  :  50
f1(60 , 70 , c = 80) #a  :  60  \t  b  :  (70,)  \t  c  :  80
f1(90 , c = 100) #a  :  90  \t  b  :  ()  \t  c  :  100
f1(a = 1 , 2 , c = 3) #Error
f1(1 , 2 , 3) #Error
f1(a = 1 , b = 2 , c = 3) #Error
f1(a = 25 , 100 , 200 , 300 , c = 35) #Error


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b): #Invalid
        pass
def  f2(*a , b): #Valid
        pass
def  f3(a , *b): #Valid
        pass
def  f4(a , b): #Valid
        pass
def    f5(a , *b , c): #Valid
        pass
def   f6( * , a , *b , c): #Invalid
       pass
def   f7(a , *b , c ,  /): #InValid
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

'''
([10 , 20] , {30 , 40} , (50 , 60))
<class 'tuple'>
[10 , 20]
<class 'list>
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
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
Results
<class  'dict'>
{'EmpNo' : 25 , 'EmpName' : 'Sita', 'Salary' : 10000.0}
Results
<class  'dict'>
{'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , 'Gender' : 'm'}
Results
<class  'dict'>
{}
'''

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''
Results
Empno...25 
Empname...Rama Rao
Salary...10000.0
Gender...m
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
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''
<class 'tuple'>
(25 , 10.8 , 'Hyd' , True)

<class 'dict'>
{'EmpNum' : 25 , 'EmpName' :  'Sita' , 'Salary' : 10000.0}
'''
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) #Emp  Number  :  25  \t  Emp  Name  :  Sita  \t  Salary  :	10000.0')
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) #Error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) #{'empno' : 25 , 'ename' : 'Sita' , 'sal' : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) #{'eno' : 25 , 'empname' : 'Sita' , 'salary' : 10000.0}


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
'''
25

Hyd
(10,20,30)

10.8
(25,'Hyd',True)
{'EmpNo' : 12 , 'EmpName' : 'Rama  Rao' , 'Salary' : 10000.0}
'''

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
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')
'''
a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32

Bye

'''

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)

'''
10
20
11
'''