# Modify  following  program  such  that  every  function  should  be  executed

def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1('x')
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1('x','y')
def  f1(x , y , z):
	print('Three  argument  function : ',x,y,z)
f1('x','y','z')


# Find  outputs  (Home  work)

def f1(a , b , c):
    print(f'a : {a}\t b : {b}\t c : {c}')
# End of the function
f1(a = 10 , b = 20 , c = 30)            # a : 10     b : 20     c : 30
f1(25 , 10.8 , 'Hyd')                   # a : 25     b : 10.8   c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)      # a : 50.2   b : 40.7   c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')   # a : Cyb    b : Sec    c : Hyd
f1(c = 3 + 4j , a = True , b = None)    # a : True   b : None   c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')           # a : 25     b : Hyd    c : 10.8
f1(a = 100 , 200 , 300)                 # Error: positional argument followed by the keyword argument is invalid
f1(True , None , b = 'Hyd')             # Error: b is passed as positional argument and also declared as keyword argument
f1(10 , 20 , x = 30)                    # Error: keyword argument 'x' is not defined
f1(10 , 20)                             # Error: f1() is having only 2 arguments required 3


# Find  outputs (Home  work)

def disp(empno , ename , sal):
    print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

'''
outputs:
Emp  Number :   25    Emp  Name : Rama Rao    Salary : 10000.0
Emp  Number :   35    Emp  Name : Sita        Salary : 20000.0
Emp  Number : Rama  Rao     Emp  Name : 30000.0     Salary : 20
'''


# Tricky program
# Find outputs (Home work)

def f1(a, b, c):
    return a + b * c
# end of the function
print(f1(3 , 4 , 5))        # 3 + 4*5 = 3 + 20 = 23
print(f1(*[6 , 7 , 8]))     # f1(6, 7, 8) → 6 + 7*8 = 6 + 56 = 62
print(f1([6 , 7 , 8]))      # Error: f1 is hacing only one positional arguments missing b and c
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))          # f1(1, 3, 5) = 1 + 3*5 = 1 + 15 = 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))    # Error: f1 is hacing only one positional arguments missing b and c
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))    # Error: f1 is hacing only one positional arguments missing b and c
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})      # Error: set consist of dictionary (set doesn't content mutable objects)
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))     # Error: f1 is hacing only one positional arguments missing b and c


# Identify  Error (Home  work)

a = [10, 20, 15, 5, 12]
print(sorted(reverse = True , a))        # Error: positional argument a cannot followed by the keyword arguments
print(sorted(a , rev = True))            # Error: 'rev' is a invalid keyword argument
print(25 , 10.8 , 'Hyd' , separator = '\t')  # Error: 'separator' is a invalid parameter  
print(25 , 10.8 , 'Hyd' , endofline = '\t')  # Error: 'endofline' is a invalid parameter  
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')  # Error: positional argument (10.8, 'Hyd') after keyword arguments in invalid


# Keyword only arguments demo program

def f1(* , a , b):
    print(f'a : {a}\t b : {b}')
# End of the function
f1(a = 10 , b = 20)       # a : 10    b : 20
f1(b = 30 , a = 40)       # a : 40    b : 30
f1(50 , 60)               # Error: due to 2 positional arguments is invalid
f1(70 , b = 80)           # Error: due to positional argument followed by keyword argument is invalid
f1(a = 15 , 25)           # Error: due to keyword argument followed by positional argument is invalid


# Find outputs (Home work)

def f1(a , * , b , c):
    print(f'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End of function
f1(10 , b = 20 , c = 30)       # a : 10    b : 20    c : 30
f1(a = 40 , b = 50 , c = 60)   # a : 40    b : 50    c : 60
f1(c = 100 , b = 90 , a = 80)  # a : 80    b : 90    c : 100
f1(70 , 80 , c = 90)           # Error: got multiple values for argument 'a' is invalid
f1(70 , 80 , 90)               # Error: takes 1 positional argument but 3 were given is invalid
f1(c = 15 , b = 25 , 35)       # Error: positional argument followed by keyword argument is invalid


# Identify error (Home  work)

def f1(a , b , *):              # Error: at least one keyword-only argument after * 
        pass             


#  Positional only arguments demo program

def f1(a , b , /):
    print(f'a : {a}\t b : {b}')
# End of the function
f1(10 , 20)               # a : 10    b : 20
f1(a = 30 ,  b = 40)      # Error: 'a' and 'b' are positional-only, can't be passed as keywords
f1(50 , b = 60)           # Error: 'b' is positional-only, can't be passed as keyword
f1(a = 70 , 80)           # Error: positional argument followed by keyword argument is invalid


# Find  outputs (Home  work)

def f1(a , b , / , c):
    print(f'a : {a}\t b : {b}\t c : {c}')
# End of function
f1(10 , 20 , 30)                  # a : 10    b : 20    c : 30
f1(40 , 50 , c = 60)              # a : 40    b : 50    c : 60
f1(a = 70 , b = 80 , c = 90)      # Error: 'a','b' and 'c' are positional-only argument, cannot be passed as keyword arguments
f1(a = 100 , b = 110 , 120)       # Error: 'a' and 'b' are positional-only argument, cannot be passed as keyword arguments
f1(a = 130 , 140 , c = 150)       # Error: 'a' is positional-only, cannot be passed as keyword arguments, also positional 140 follows keyword argument
f1(160 , b = 170 , 180)           # Error: 'b' is positional-only, cannot be passed as keyword, also positional 180 follows keyword arguments
f1(190 , b = 200 , c = 210)       # Error: 'b' is positional-only, cannot be passed as keyword argument


# Find outputs (Home work)

def f1(a, b, /, c, d, *, e, f):
    print(f'a : {a}\t b : {b}\t c : {c}\t d : {d}\t e : {e}\t f : {f}')
# End of the function
f1(10, 20, 30, d=40, e=50, f=60)      # a : 10   b : 20   c : 30   d : 40   e : 50   f : 60
f1(1, b=2, c=3, d=4, e=5, f=6)        # Error: b is positional-only, cannot be passed as keyword arguments
f1(1, 2, 3, 4, 5, f=6)                # a : 1   b : 2   c : 3   d : 4   e : 5   f : 6
f1(10, 20, c=30, 40, e=50, f=60)      # Error: positional argument followed by keyword argument is invalid
f1(10, 20, 30, 40, e=50, f=60)        # a : 10   b : 20   c : 30   d : 40   e : 50   f : 60


# Identify error (Home work)

def f1(/ , a , b , c):  # Error: '/' must followed after at least one parameter. 
    pass
def f2(a , b , c , *):  # Error: '*' must be followed by at least one keyword-only argument
    pass


# Identify error (Home work)

def f4(* , a , b , c , /):   # Error: '*' and '/' can't be together
    pass


# Find outputs (Home work)

def f1(x):
    print('1st function :', x)
def f1(y):
    print('2nd function :', y)
def f1(z):
    print('3rd function :', z)
f1(z = 10)   # 3rd function : 10
f1(y = 20)   # 3rd function : 20
f1(x = 30)   # 3rd function : 30


# Default arguments demo program

def add(a , b = 20 , c = 30):
    return a + b + c
# End
print(add(100))                        # 150
print(add(100 , 200))                  # 330
print(add(100 , 200 , 300))            # 600
print(add(100 , c = 200))              # 320
print(add(c = 100 , b = 200 , a = 300))# 600
print(add(c = 100 , a = 200))          # 320
print(add())                           # Error: arguments are not defined
print(add(a = 100 , 200))              # Error: positional argument follows keyword argument is invalid
print(add(100 ,  , 300))               # Error: 1 argument is not defined
print(add(100 ,  b , 300))             # Error: 'b' is not defined


# Identify Error

def f1(a = 10 , b , c = 20 , d):  # Error: non-default argument followed by default argument is invalid
    pass
def f2(b , d , a = 10 , c = 20):  # Valid
    pass


# Find outputs (Home work)

def f1(a = 10):
    print(a)
# End
f1(20)      # 20
f1()        # 10
f1(a = 30)  # 30


# Find outputs (Home work)

def add(a , b , c = 10 , d = 20):
    return a + b + c + d
# End
print(add(100 , 200))                       # 330
print(add(100 , 200 , 300))                 # 620
print(add(100 , 200 , 300 , 400))           # 1000
print(add(b = 100 , a = 200))               # 330
print(add(100 , 200 , d = 300))             # 600
print(add(d = 100 , a = 200 , b = 300))     # 610
print(add(c = 100 , d = 200 , 300 , 400))   # Error: positional argument followed keyword argument is invalid
print(add(100 , 200 , c = 300 , x = 400))   # Error: keyword argument 'x' is not defined
print(add())                                # Error: positional arguments: 'a' and 'b' are not defined


# Find outputs (Home work)

def f1(x = 25):
    return x
def f2(x):
    return x
# End
print(f1(10))   # 10
print(f1())     # 25
print(f2(20))   # 20
print(f2())     # Error: positional argument 'x' is not defined


# Find outputs (Home work)

def disp(ch = '*' , n = 4):
    print(ch * n)
# End
disp('-' , 6)                # ------
disp('$')                    # $$$$
disp()                       # ****
disp(n = 5)                  # *****
disp(5)                      # 5555
disp(n = 7 , ch = '%')       # %%%%%%%
disp(7 , '@')                # @@@@@@@
disp(7 , n = 6)              # Error: multiple values for argument 'n'
disp(ch = '!' , 5)           # Error: positional argument follows keyword argument is not defined


# Find outputs (Home work)

def power(a , b = 2):
    return a ** b
# End
print(power(2 , 6))          # 64
print(power(5))              # 25
print(power(b = 3 , a = 4.5))# 91.125
print(power(3 + 4j))         # (-7+24j)
print(power(True))           # 1
def power(b = 2 , a):        # Error: non-default argument follows default argument is invalid
    pass


# Find outputs (Home work)

def add(a , b):
    print('2-argument function')
    return a + b
def add(a , b , c):
    print('3-argument function')
    return a + b + c
def add(a = 1 , b = 2 , c = 3 , d = 4):
    print('4-argument function')
    return a + b + c + d
# last function is active
print(add(10 , 20 , 30 , 40)) # 4-argument: 100
print(add(50 , 60 , 70))      # 4-argument: 136
print(add(80 , 90))           # 4-argument: 179
print(add(100))               # 4-argument: 106
print(add())                  # 4-argument: 10


# Find outputs (Home work)

def disp(a , b):
    print('2-argument function:', a , b)
def disp(a , b , c , d):
    print('4-argument function:', a , b , c , d)
def disp(a , b , c = 25):
    print('3-argument function:', a , b , c)
# last def is active
disp(10 , 20 , 30)        #  10 20 30
disp(40 , 50 , 60 , 70)   # Error: takes from 2 to 3 positional arguments but 4 were given
disp(80 , 90)             # 80 90 25


# Find outputs (Home work)

def add(* , a = 10 , b = 20):
    return a + b
# End
print(add(a = 30 , b = 40))    # 70
print(add())                   # 30
print(add(a = 50))             # 70
print(add(b = 60 , a = 70))    # 130
print(add(80 , 90))            # Error: takes 0 positional arguments but 2 were given


# Find outputs (Home work)

def add(a = 10 , b , c):    # Error: non-default argument followed by default argument is invalid
    pass
def add(* , a = 10 , b , c):
    return a + b + c
# End
print(add(a = 30 , b = 40 , c = 50))    # 120
print(add(b = 60 , c = 70))             # 140
print(add(c = 80 , b = 90 , a = 100))   # 270
print(add(c = 25 , a = 43))             # Error: add() missing 1 required keyword-only argument that is 'b'
print(add(1 , 2 , 3))                   # Error: add() takes 0 positional arguments but 3 were given
def add(a , b = 10 , c , * , d , e = 20 , f):
    pass   # Error: non-default argument followed by default argument is invalid


'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
									    			   2
													   3
													   5
													   7
													  Number  of   prime  numbers : 4
'''

def prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1): 
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
count = 0
print("Prime numbers")
for i in range(2, n + 1):
    if prime(i):
        print(i)
        count += 1
print("Number of prime numbers :", count)

