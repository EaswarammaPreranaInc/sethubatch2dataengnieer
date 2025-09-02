#  Variable  number  of  arguments  demo  program
def f1(*t):
    print(t)
    print(type(t))
    print(len(t))
    print()
# End  of  the  function

f1(10, 20, 15, 18)  
# (10, 20, 15, 18)
# <class 'tuple'>
# 4

f1()
# ()
# <class 'tuple'>
# 0

f1([10, 20], (30, 40, 50), {60, 70, 80, 90})
# ([10, 20], (30, 40, 50), {80, 90, 60, 70})
# <class 'tuple'>
# 3

f1('Hyd')
# ('Hyd',)
# <class 'tuple'>
# 1

tpl = (100, 200, 150)
f1(tpl)
# ((100, 200, 150),)
# <class 'tuple'>
# 1

f1(t=(10, 20, 30))
# ()
# <class 'tuple'>
# 0


# Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)

def avg(*a):
    return sum(a) / len(a) if a else 0
# End  of  the  function
print(avg(10, 20, 15, 18))              # 15.75
print(avg(25, 10.8, True))              # 12.933333333333334
print(avg(10.8, 20.6, 15.2, 14.9, 9.8)) # 14.26
print(avg())                            # 0
print(avg(25))                          # 25.0
print(avg(3 + 4j, 5 + 6j))              # (4+5j)
tpl = (10, 20, 15, 18)
print(avg(*tpl))                        # 15.75


# Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)

def concat(*a):
    return ''.join(str(x) for x in a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))                  # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))                # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))    # PythonIsAGreatLanguage
print(concat())                                            # ''
print(concat('Python'))                                    # Python
print(concat(1, 2, 3))                                     # 123


#Find  outputs (Home  work)

def f1(a=25, *b):
    print(f'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10, 20, 30, 40)                  # a : 10     b : (20, 30, 40)
f1(50, 60)                          # a : 50     b : (60,)
f1(70)                              # a : 70     b : ()
f1(a=80)                            # a : 80     b : ()
f1(b=(10, 20, 30), a=40)            # a : 40     b : ()
f1()                                # a : 25     b : ()
f1((10, 20, 30), 10, 20, 30)        # a : (10, 20, 30)   b : (10, 20, 30)


#Find  outputs (Home  work)

def f1(*a, b):
    print(f'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10, 20, 30, b=40)                # a : (10, 20, 30)    b : 40
f1(50, b=60)                        # a : (50,)           b : 60
f1(b=70)                            # a : ()              b : 70
f1(10, 20, 30, (10, 20, 30), b=50)  # a : (10, 20, 30, (10, 20, 30))   b : 50
f1(25, b=100)                       # a : (25,)           b : 100
f1(10, 20, 30, b=(10, 20, 30))      # a : (10, 20, 30)    b : (10, 20, 30)


#Find  outputs (Home  work)

def f1(a, *b, c):
    print(f'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10, 20, 30, 40, c=50)            # a : 10   b : (20, 30, 40)   c : 50
f1(60, 70, c=80)                    # a : 60   b : (70,)          c : 80
f1(90, c=100)                       # a : 90   b : ()             c : 100
f1(25, 100, 200, 300, c=35)         # a : 25   b : (100, 200, 300) c : 35


# Which  of  the  following  are  valid  ?  (Home  work)

# def f1(*a , *b):                          #error
def f2(*a, b): pass                         #pass
def f3(a, *b): pass                         #pass
def f4(a, b): pass                          #pass
def f5(a, *b, c): pass                      #pass
# def f6(* , a , *b , c):                   #error
# def f7(a , *b , c ,  /):                  #error


# Find  outputs  (Home  work)

def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
# End  of  the  function

f1([10, 20], {30, 40}, (50, 60))
# ([10, 20], {40, 30}, (50, 60))
# <class 'tuple'>
# [10, 20]
# <class 'list'>
# {40, 30}
# <class 'set'>
# (50, 60)
# <class 'tuple'>


# Variable  number  of  keyword  arguments  demo  program

def disp(**a):
    print('Results')
    print(type(a))
    print(a)
    print()
#End  of  the  function

disp(RollNo=10, StudName='Rama Rao')
# Results
# <class 'dict'>
# {'RollNo': 10, 'StudName': 'Rama Rao'}

disp(EmpNo=25, EmpName='Sita', Salary=10000.0)
# Results
# <class 'dict'>
# {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')
# Results
# <class 'dict'>
# {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

disp()
# Results
# <class 'dict'>
# {}


# Find  outputs  (Home  work)

def f1(**a):
    print('Results')
    for k, v in a.items():
        print(k, v, sep=' ... ')
# End  of  the  function

f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m')
# Results
# Empno ... 25
# Empname ... Rama Rao
# Salary ... 10000.0
# Gender ... m

f1()
# Results


# Find  outputs (Home  work)

def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)
# End  of  the  function

f1(25, 10.8, 'Hyd', True)
# <class 'tuple'>
# (25, 10.8, 'Hyd', True)

print()
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)
# <class 'dict'>
# {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}


#  Find  outputs (Home work)

def f1(empno, ename, sal):
    print(f'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  : {sal}')
def f2(**a):
    print(a)
# End  of  the  function

f1(empno=25, ename='Sita', sal=10000.0)
# Emp Number : 25   Emp Name : Sita   Salary : 10000.0

f2(empno=25, ename='Sita', sal=10000.0)
# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}

f2(eno=25, empname='Sita', salary=10000.0)
# {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}


# Find  outputs   (Home  work)

def f1(a, *b, **c):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
# End  of  the  function

f1(25)
# 25

f1('Hyd', 10, 20, 30)
# Hyd
# (10, 20, 30)

f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)
# 10.8
# (25, 'Hyd', True)
# {'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}


'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop
'''

# Program to evaluate expression like a calculator

expr = input("Enter any expression terminated by = : ")

i = 0
a = ""  # to store the first number

# Read the first number (before any operator)
while expr[i].isdigit():
    a += expr[i]
    i += 1

a = float(a)   

while i < len(expr):
    op = expr[i]   # operator (+, -, *, /, =)
    if op == "=":
        break  # end of expression
    i += 1

    # read next number 'b'
    b = ""
    while expr[i].isdigit():
        b += expr[i]
        i += 1
    b = float(b)

    # perform operation
    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b

print("Result :", a)




#Write  a   program  to  print  roman  equivalent  of  a  number






def to_roman(num):
    values = [1000, 900, 500, 400,
              100, 90, 50, 40,
              10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0
    while num > 0:
        q = num // values[i]              
        roman += symbols[i] * q           
        num = num % values[i]            
        i += 1
    return roman


n = int(input("Enter a number : "))
print("Roman Equivalent :", to_roman(n))

'''

Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

'''
a = ['Zero', 'One', 'Two', 'Three', 'Four',
     'Five', 'Six', 'Seven', 'Eight', 'Nine']

num = input("Enter a number : ")

for ch in num:
    print(a[int(ch)], end=" ")



#Write  a  program  to  print  all  the  rotations  of  the  string


s = input("Enter a string : ")

n = len(s)

for i in range(n):
    rotated = s[i:] + s[:i]
    print(rotated)


# Write  a  program  to  print  mathematical  table  of  a  number


n = int(input("Enter a number : "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)





# Write a  program to print following pyramid


n = int(input("How many lines ? : "))

for i in range(1, n + 1):  
    # Print spaces before letters
    print(" " * (n - i), end="")

    # Print letters from 'A' to 'A' + i - 1
    for j in range(i):  
        print(chr(65 + j), end=" ")

    print()  

#find outputs
a = 10

def f1():
    b = 40
    print('a : ' , a)   # 11
    print('b : ' , b)   # 40
    print('c : ' , c)   # 31
    print()

b = 20
def f2():
    a = 50
    print('a : ' , a)   # 50
    print('b : ' , b)   # 22
    print('c : ' , c)   # 32

c = 30
print('a : ' , a)   # 10
print('b : ' , b)   # 20
print('c : ' , c)   # 30
print()

a +=  1   # a = 11
b +=  1   # b = 21
c +=  1   # c = 31
f1()

a +=  1   # a = 12
b +=  1   # b = 22
c +=  1   # c = 32
f2()

print('Bye')   # Bye


#find outputs
def f1():
    a = 20
    print(a)   # 20
    a += 1

a = 10
print(a)   # 10
a += 1     # a = 11
f1()
print(a)   # 11








