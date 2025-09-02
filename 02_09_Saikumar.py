#  Variable  number  of  arguments  demo  program

def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30)) # Error f1() Can't be an keyword argument

'''
Outputs:

(10, 20, 15, 18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10, 20], (30, 40, 50), {60, 70, 80, 90})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
1
'''


# Function to determine average of arguments

def avg(*a):
    try:
        return sum(a) / len(a) 
    except:
        return "Atleast 1 input is required"
# End of the function

print(avg(10, 20, 15, 18))
print(avg(25, 10.8, True))
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j, 5 + 6j))
tpl = (10, 20, 15, 18)
print(avg(tpl))          
print(avg(*tpl))


# Function to concatenate strings

def concat(*a):
    try:
        return "".join(a)
    except:
        return "Error Atleast 1 input is required and input should be a string"
# End of the function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))  


# Find outputs (Home work)

def f1(a = 25 , *b):
    print(f'a : {a}  \t   b  :  {b} ')
# End of the function
f1(10 , 20 , 30 , 40)                   # a : 10 	   b  :  (20, 30, 40) 
f1(50 , 60)                             # a : 50 	   b  :  (60,) 
f1(70)                                  # a : 70 	   b  :  () 
f1(a = 80)                              # a : 80 	   b  :  () 
f1(b = (10 , 20 , 30) , a = 40)         # a : 40 	   b  :  (10, 20, 30) 
f1()                                    # a : 25 	   b  :  () 
f1(a = 10 , (20 , 30 , 40))             # Error positional argument followed by keyword argument is invalid
f1(25 , b = (10 , 20 , 30))             # Error f1() got multiple values for argument 'b'
f1(25 , a = (10 , 20 , 30))             # Error f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30)       # a : (10, 20, 30) 	   b  :  (10, 20, 30) 
f1(a = (10 , 20 , 30) , 10 , 20 , 30)   # Error positional argument followed by keyword argument is invalid


# Find outputs (Home work)

def f1(*a, b):
    print(F'a  :  {a}   \t   b  :  {b}')
# End of the function
f1(10, 20, 30, b=40)            # a  :  (10, 20, 30)   	   b  :  40
f1(50, b=60)                    # a  :  (50,)   	   b  :  60
f1(b=70)                        # a  :  ()   	   b  :  70
# The following calls will give errors:
f1(b=10, a=(20, 30, 40))        # Error f1() got an unexpected keyword argument 'a'
f1(b=10, (20, 30, 40))          # Error positional argument followed by keyword argument is invalid
f1()                            # Error b must be provided as a keyword argument because it is defined after *a
f1(10, 20, 30, (10, 20, 30))    # Error b must be provided as a keyword argument because it is defined after *a
f1(10, 20, 30, 40)              # Error b must be provided as a keyword argument because it is defined after *a
f1(25)                          # Error b must be provided as a keyword argument because it is defined after *a
f1(10, 20, 30, b=(10, 20, 30))  # a  :  (10, 20, 30)   	   b  :  (10, 20, 30)


# Find outputs (Home work)

def f1(a, *b, c):
    print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End of the function
f1(10, 20, 30, 40, c=50)         # a  :  10 	  b  :  (20, 30, 40) 	  c  :  50
f1(60, 70, c=80)                 # a  :  60 	  b  :  (70,) 	  c  :  80
f1(90, c=100)                    # a  :  90 	  b  :  () 	  c  :  100
# The following calls will give errors:
f1(a=1, 2, c=3)                  # Error positional argument followed by keyword argument is invalid
f1(1, 2, 3)                      # Error c must be passed as a keyword argument
f1(a=1, b=2, c=3)                # Error *b can't be a keyword argument
f1(a=25, 100, 200, 300, c=35)    # Error positional argument followed by keyword argument is invalid


# Which of the following are valid? (Home work)

def f1(*a, *b):           # Invalid 
    pass
def f2(*a, b):            # Valid 
    pass
def f3(a, *b):            # Valid 
    pass
def f4(a, b):             # Valid
    pass
def f5(a, *b, c):         # Valid
    pass
def f6(*, a, *b, c):      # Invalid  *b cannot appear after *, only one *args allowed
    pass 
def f7(a, *b, c, /):      # Invalid /  must come before *b and keyword-only arguments
    pass


# Find  outputs  (Home  work)

def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50,60))

'''
Outputs:

([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''


# Find outputs (Home work)

def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
# End of the function
f1([10, 20], {30, 40}, (50, 60))

'''
Outputs:

disp(RollNo=10, StudName='Rama Rao')   
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama Rao'}

disp(EmpNo=25, EmpName='Sita', Salary=10000.0)
Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')
Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

disp()
Results
<class 'dict'>
{}
'''


# Find outputs (Home work)

def f1(**a):
    print('Results')
    for k, v in a.items():
        print(k, v, sep=' ... ')
# End of the function
f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m')
f1()

'''
Outputs:

Results
Empno ... 25
Empname ... Rama Rao
Salary ... 10000.0
Gender ... m

f1()
Results
(No key-value pairs, so nothing else is printed)
'''


# Find outputs (Home work)

def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)
# End of the function
f1(25, 10.8, 'Hyd', True)
print()
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)


'''
Outputs:

f1(25, 10.8, 'Hyd', True)
<class 'tuple'>
(25, 10.8, 'Hyd', True)

print()

f2(EmpNum=25, EmpName='Sita', Salary=10000.0)
<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''


# Find outputs (Home work)

def f1(empno, ename, sal):
    print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :  {sal}')
def f2(**a):
    print(a)
# End of the function
f1(empno=25, ename='Sita', sal=10000.0)          # Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :  10000.0
f1(eno=25, empname='Sita', salary=10000.0)       # Error f1 only accepts empno, ename, sal as keyword arguments
f2(empno=25, ename='Sita', sal=10000.0)          # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno=25, empname='Sita', salary=10000.0)       # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}


# Find outputs (Home work)
def f1(a, *b, **c):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
# End of the function
f1(25)
print()
f1('Hyd', 10, 20, 30)
print()
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)

'''
Outputs:

25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}
'''


# Find outputs (Home work)

a = 10
def f1():
    b = 40
    print('a : ' , a)    # a : 11
    print('b : ' , b)    # b : 40
    print('c : ' , c)    # c : 31
    print()
b = 20
def f2():
    a = 50
    print('a : ' , a)    # a : 50
    print('b : ' , b)    # b : 22
    print('c : ' , c)    # c : 32
c = 30
print('a : ' , a)        # a : 10
print('b : ' , b)        # b : 20
print('c : ' , c)        # c : 30
print()
a += 1   # a = 11
b += 1   # b = 21
c += 1   # c = 31
f1()
a += 1   # a = 12
b += 1   # b = 22
c += 1   # c = 32
f2()
print('Bye')             # Bye


# Find outputs (Home work)

def f1():
    a = 20
    print(a)             # 20
    a += 1
a = 10
print(a)                 # 10
a += 1                   # a = 11
f1()
print(a)                 # 11






