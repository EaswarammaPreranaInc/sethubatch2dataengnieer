
def f1(*t):
    print(t)
    print(type(t))
    print(len(t))
    print()
f1(10, 20, 15, 18)    # (10, 20, 15, 18)\n<class 'tuple'>\n4
f1()                  # ()\n<class 'tuple'>\n0
f1([10, 20], (30, 40, 50), {60, 70, 80, 90})  # ([10, 20], (30, 40, 50), {60, 70, 80, 90})\n<class 'tuple'>\n3
f1('Hyd')             # ('Hyd',)\n<class 'tuple'>\n1
tpl = (100, 200, 150)
f1(tpl)               # ((100, 200, 150),)\n<class 'tuple'>\n1
f1(t = (10, 20, 30))  # error



def avg(*a):
    return sum(a) / len(a) if a else 0
print(avg(10, 20, 15, 18))                  # 15.75
print(avg(25, 10.8, True))                  # 12.933333333333334
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))     # 14.26
print(avg())                                # 0
print(avg(25))                              # 25.0
print(avg(3+4j, 5+6j))                      # (4+5j)
tpl = (10, 20, 15, 18)
print(avg(tpl))                             # error


# Concatenate strings
def concat(*a):
    return ''.join(a)
print(concat('Sankar', 'Dayal', 'Sarma'))          # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))        # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  # PythonIsAGreatLanguage
print(concat())                                    # ''
print(concat('Python'))                            # Python
print(concat(1, 2, 3))                             # error



def f1(a=25, *b):
    print(f'a : {a} \t   b  : {b}')
f1(10, 20, 30, 40)                   # a : 10   b  : (20, 30, 40)
f1(50, 60)                           # a : 50   b  : (60,)
f1(70)                               # a : 70   b  : ()
f1(a=80)                             # a : 80   b  : ()
f1(b=(10, 20, 30), a=40)             # a : 40   b  : ((10, 20, 30),)
f1()                                 # a : 25   b  : ()
f1(a=10, (20, 30, 40))               # error
f1(25, b=(10, 20, 30))               # error
f1(25, a=(10, 20, 30))               # error
f1((10, 20, 30), 10, 20, 30)         # a : (10, 20, 30)   b  : (10, 20, 30)
f1(a=(10, 20, 30), 10, 20, 30)       # error




def f1(*a, b):
    print(f'a  :  {a}   \t   b  :  {b}')
f1(10, 20, 30, b=40)                 # a : (10, 20, 30)   b : 40
f1(50, b=60)                         # a : (50,)   b : 60
f1(b=70)                             # a : ()   b : 70
f1(b=10, a=(20, 30, 40))             # error
f1(b=10, (20, 30, 40))               # error
f1()                                 # error
f1(10, 20, 30, (10, 20, 30))         # error
f1(10, 20, 30, 40)                   # error
f1(25)                               # error
f1(10, 20, 30, b=(10, 20, 30))       # a : (10, 20, 30)   b : (10, 20, 30)



def f1(a, *b, c):
    print(f'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
f1(10, 20, 30, 40, c=50)             # a:10 b:(20,30,40) c:50
f1(60, 70, c=80)                     # a:60 b:(70,) c:80
f1(90, c=100)                        # a:90 b:() c:100
f1(a=1, 2, c=3)                      # error
f1(1, 2, 3)                          # error
f1(a=1, b=2, c=3)                    # error
f1(a=25, 100, 200, 300, c=35)        # error



def f1(*a, *b): pass   # error
def f2(*a, b): pass    # valid
def f3(a, *b): pass    # valid
def f4(a, b): pass     # valid
def f5(a, *b, c): pass # valid
def f6(*, a, *b, c): pass  # error
def f7(a, *b, c, /): pass  # error



def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
f1([10, 20], {30, 40}, (50, 60))  
# ([10,20], {40,30}, (50,60))
# <class 'tuple'>
# [10,20]
# <class 'list'>
# {40,30}
# <class 'set'>
# (50,60)
# <class 'tuple'>



def disp(**a):
    print('Results')
    print(type(a))
    print(a)
    print()
disp(RollNo=10, StudName='Rama  Rao')   
# Results\n<class 'dict'>\n{'RollNo':10, 'StudName':'Rama  Rao'}
disp(EmpNo=25, EmpName='Sita', Salary=10000.0)
disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')
disp()    # Results\n<class 'dict'>\n{}



def f1(**a):
    print('Results')
    for k,v in a.items():
        print(k, v, sep=' ... ')
f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m') 
# Results\nEmpno ... 25\nEmpname ... Rama Rao\nSalary ... 10000.0\nGender ... m
f1() # Results



def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)
f1(25, 10.8, 'Hyd', True)
# <class 'tuple'>\n(25, 10.8, 'Hyd', True)
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)
# <class 'dict'>\n{'EmpNum':25,'EmpName':'Sita','Salary':10000.0}


# -------------------------------
# Keyword args mismatch
def f1(empno, ename, sal):
    print(f'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
def f2(**a):
    print(a)
f1(empno=25, ename='Sita', sal=10000.0)  # Emp Number : 25  Emp Name : Sita  Salary : 10000.0
f1(eno=25, empname='Sita', salary=10000.0)  # error
f2(empno=25, ename='Sita', sal=10000.0)    # {'empno':25, 'ename':'Sita', 'sal':10000.0}
f2(eno=25, empname='Sita', salary=10000.0) # {'eno':25, 'empname':'Sita', 'salary':10000.0}



def f1(a, *b, **c):
    print(a)
    if b: print(b)
    if c: print(c)
f1(25)                             # 25
f1('Hyd', 10, 20, 30)              # Hyd\n(10,20,30)
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)
# 10.8\n(25,'Hyd',True)\n{'EmpNo':12,'EmpName':'Rama Rao','Salary':10000.0}


# Calculator program
expr = "3+4*5-6/2="
expr = expr[:-1]  # remove '='
print(eval(expr))   # 14.0  (Note: their logic steps give 14.5 but Python eval gives 14.0 due to operator precedence)


# Roman numeral program
def to_roman(n):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms= ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res=""
    for i in range(len(val)):
        res += syms[i]*(n//val[i])
        n %= val[i]
    return res
print(to_roman(3878))   # MMMDCCCLXXVIII


# Digits to words
def num_to_words(n):
    arr = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    return ' '.join(arr[int(ch)] for ch in str(n))
print(num_to_words(9247))   # Nine Two Four Seven



a = 10
def f1():
    b = 40
    print('a :', a)
    print('b :', b)
    print('c :', c)
    print()
b = 20
def f2():
    a = 50
    print('a :', a)
    print('b :', b)
    print('c :', c)
c = 30
print('a :', a)  # a : 10
print('b :', b)  # b : 20
print('c :', c)  # c : 30
print()
a += 1
b += 1
c += 1
f1()             # a : 11\nb : 40\nc : 31
a += 1
b += 1
c += 1
f2()             # a : 50\nb : 22\nc : 32
print('Bye')     # Bye



def f1():
    a = 20
    print(a)
    a += 1
a = 10
print(a)   # 10
a += 1
f1()       # 20
print(a)   # 11
