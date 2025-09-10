
 #  Variable  number  of  arguments  demo  program
def f1(*t):
    print(t) # prints the tuple of arguments
    print(type(t))# always <class 'tuple'>
    print(len(t)) # number of arguments
    print()
# End of the function

f1(10, 20, 15, 18) # tuple of 4 elements
f1() # empty tuple
f1([10, 20], (30, 40, 50), {60, 70, 80, 90}) # tuple with 3 elements (list, tuple, set)
f1('Hyd') # tuple with 1 string element
tpl = (100, 200, 150)
f1(tpl)# ((100, 200, 150),)  # tuple containing 1 element (another tuple inside)
f1(t = (10, 20, 30)) # TypeError, because function takes only positional args (*t),


(10,20,15,18)
<class 'tuple'>
4


def avg(*a):
    return sum(a) / len(a) if len(a) > 0 else 0
# End of the function

print(avg(10, 20, 15, 18))          
# (10+20+15+18)/4 = 63/4 = 15.75

print(avg(25, 10.8, True))          
# True = 1 → (25+10.8+1)/3 = 36.8/3 = 12.266666...

print(avg(10.8, 20.6, 15.2, 14.9, 9.8))  
# (10.8+20.6+15.2+14.9+9.8)/5 = 71.3/5 = 14.26

print(avg())                        
# no arguments → returns 0

print(avg(25))                      
# only one element → 25/1 = 25.0

print(avg(3+4j, 5+6j))              
# works with complex numbers → ( (3+4j)+(5+6j) ) / 2 = (8+10j)/2 = (4+5j)

tpl = (10, 20, 15, 18)
print(avg(tpl)) # TypeError → because passing tuple as a single arg, so a = ((10,20,15,18),)
# sum() fails since it can’t add int and tuple
#to have output you have to use *operator like (*tpl)


def concat(*a):
    return ' '.join(a) if len(a) > 0 else ''   # join all args into one string
# End of the function

print(concat('Sankar', 'Dayal', 'Sarma'))
# Sankar Dayal Sarma

print(concat('Hyd', 'Is', 'Green', 'City'))
# Hyd Is Green City

print(concat('Python', 'Is', 'A', 'Great', 'Language'))
# Python Is A Great Language

print(concat())
# ''  (empty string, since no args)

print(concat('Python'))
# Python

#print(concat(1, 2, 3))
# TypeError: sequence item 0: expected str instance, int found

def f1(a = 25, *b):
    print(f'a : {a}  \t   b  :  {b} ')
# End of the function

f1(10, 20, 30, 40)
# a = 10 , b = (20, 30, 40)
# Output: a : 10      b  :  (20, 30, 40) 

f1(50, 60)
# a = 50 , b = (60,)
# Output: a : 50      b  :  (60,)

f1(70)
# a = 70 , b = ()
# Output: a : 70      b  :  ()

f1(a = 80)
# a = 80 , b = ()
# Output: a : 80      b  :  ()

f1(b = (10, 20, 30), a = 40)
# a = 40 , b = (10, 20, 30)  ← b is passed as keyword arg
# Output: a : 40      b  :  (10, 20, 30)

f1()
# a = 25 (default), b = ()
# Output: a : 25      b  :  ()

f1(a = 10, (20, 30, 40))
# SyntaxError → positional argument (tuple) follows keyword argument

f1(25, b = (10, 20, 30))
# TypeError → multiple values for argument 'b'
# because 25 goes to `a`, and b=(10,20,30) conflicts with *b

f1(25, a = (10, 20, 30))
# TypeError → multiple values for argument 'a'

f1((10, 20, 30), 10, 20, 30)
# a = (10,20,30), b = (10,20,30)
# Output: a : (10, 20, 30)      b  :  (10, 20, 30)

f1(a = (10, 20, 30), 10, 20, 30)
# SyntaxError → positional argument follows keyword argument


def f1(*a, b):
    print(f'a  :  {a}   \t   b  :  {b}')
# End of the function


f1(10, 20, 30, b=40)
# a = (10, 20, 30), b = 40
# Output: a  :  (10, 20, 30)   b  :  40


f1(50, b=60)
# a = (50,), b = 60
# Output: a  :  (50,)   b  :  60


f1(b=70)
# a = (), b = 70
# Output: a  :  ()    b  :  70


f1(b=10, a=(20, 30, 40))
# TypeError → f1() got an unexpected keyword argument 'a'
# Because `a` only accepts positional args, not keyword.


f1(b=10, (20, 30, 40))
# SyntaxError → positional argument follows keyword argument


f1()
# TypeError → missing 1 required keyword-only argument: 'b'


f1(10, 20, 30, (10, 20, 30))
# TypeError → missing required keyword-only argument: 'b'
# (all went into *a, but b was not given)


f1(10, 20, 30, 40)
# TypeError → missing required keyword-only argument: 'b'


f1(25)
# TypeError → missing required keyword-only argument: 'b'


f1(10, 20, 30, b=(10, 20, 30))
# a = (10, 20, 30), b = (10, 20, 30)
# Output: a  :  (10, 20, 30)    b  :  (10, 20, 30)


def f1(a, *b, c):
    print(f'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')

f1(10, 20, 30, 40, c=50)
# a = 10
# b = (20, 30, 40)
# c = 50
# Output: a  :  10    b  :  (20, 30, 40)    c  :  50


f1(60, 70, c=80)
# a = 60
# b = (70,)
# c = 80
# Output: a  :  60    b  :  (70,)    c  :  80


f1(90, c=100)
# a = 90
# b = ()
# c = 100
# Output: a  :  90    b  :  ()    c  :  100


f1(a=1, 2, c=3)
# SyntaxError → positional argument follows keyword argument

f1(1, 2, 3)
# TypeError → missing required keyword-only argument: 'c'

f1(a=1, b=2, c=3)
# TypeError → f1() got an unexpected keyword argument 'b'
# (because *b only collects positionals, not keyword args)

f1(a=25, 100, 200, 300, c=35)
# SyntaxError → positional argument follows keyword argument


def f1(*a, *b):
    pass
#invalid cannot have two'*'

def f2(*a, b):
    pass
#Valid *a collects positional args
#b is keyword only

def f3(a, *b):
    pass
#Valid a is normal positional args
#b collects the rest

def f4(a, b):
    pass
#Valid Normal function with either positional or keyword also non-default

def f5(a, *b, c):
    pass
#Valid
#a is positional only
#*b collects the rest of positional args
#c only keyword args(c=value)

def f6(*, a, *b, c):
    pass
#Invalid
#cannot place *b after a bare *

def f7(a, *b, c, /):
    pass
#Invalid
#'/' states only positional args , but there is a '*b'


def f1(*a):
    print(a) # prints the tuple of arguments
    print(type(a)) # type of a (always tuple)
    for x in a:  # iterate over the tuple
        print(x) # print each element
        print(type(x))# print type of each element

# Function call
f1([10, 20], {30, 40}, (50, 60))


#Outputs
#([10, 20], {40, 30}, (50, 60))
#<class 'tuple'>

#[10, 20] #first element
#<class 'list'>

#{40, 30} #second element
#<class 'set'>

#(50, 60) #third element
#<class 'tuple'>


# Variable  number  of  keyword  arguments  demo  program
def   disp(**a): #(**a) pass the variable keyword arguement
	print('Results')
	print(type(a)) #always gives <class 'dict'>
	print(a) #dictionary content
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
#Results
#<class 'dict'>
#{'RollNo': 10, 'StudName': 'Rama  Rao'}

disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
#Results
#<class 'dict'>
#{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
#Results
#<class 'dict'>
#{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

disp()
#Results
#<class 'dict'>
#{} empty dictionary


# Find  outputs  (Home  work)
def  f1(**a): #collects all keyword arguments into a dict
	print('Results')
	for  k , v   in   a . items(): #returns key-value pairs
		print(k , v , sep = ' ... ') #seperate key from values with ...
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
#{'Empno': 25, 'Empname': 'Rama  Rao', 'Salary': 10000.0, 'Gender': 'm'}
#Results
#Empno ... 25
#Empname ... Rama  Rao
#Salary ... 10000.0
#Gender ... m

f1()
#Results

# Find  outputs (Home  work)
def   f1(*a): #Collects all positional argument into tuple
	print(type(a)) #<class 'tuple'>
	print(a)
def   f2(**a): #Collects all Keyword arguments into dictionary
	print(type(a)) #<class 'dict'>
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
# <class 'tuple'> 
#Printed as it is as (25 , 10.8 , 'Hyd' , True)

print()


f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#<class 'dict'>
#{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}



#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  : 10000.0
#Matches parameter

f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
#Error 
#Mismatch parameter

f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
#{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}

f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
#{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}



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

#25
#rest are not printed 
f1('Hyd' , 10 , 20 , 30)
print()
#Hyd
#(10,20,30)

f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
#(a)10.8
#(b=)(25, 'Hyd', True)
#(c){'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}
