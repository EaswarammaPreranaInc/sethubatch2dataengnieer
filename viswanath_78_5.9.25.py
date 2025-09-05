def change(b):
    b.append(25)
    b[2] = 17
    del b[1]
# End of the function
a = [10, 20, 15, 18]
print(a)  # [10, 20, 15, 18]
change(a)
print(a)  # [10, 17, 18, 25]

def change(b):
    b = [50, 60, 70, 80]
    print(b)  # [50, 60, 70, 80]
# End of the function
a = [10, 20, 30, 40]
print(a)  # [10, 20, 30, 40]
change(a)
print(a)  # [10, 20, 30, 40]

def f1(x):
    x = 20
    print(x)  # 20
# End of the function
x = 10
print(x)  # 10
f1(x)
print(x)  # 10

def f1(b):
    b[2] = 25
# end of the function
a = (10, 20, 15, 18)
print(a)  # (10, 20, 15, 18)
f1(a)  # Error: tuple object does not support item assignment
print(a)  # (10, 20, 15, 18)

square = lambda x=10: x * x
print(square(5))   # 25
print(square())    # 100

print((lambda x: x * x)(7))      # 49
print(lambda x: x * x(7))        # <function <lambda> at 0x...>
print(lambda x: x * x)             # <function <lambda> at 0x...>
print((lambda x=25: x * x)())      # 625
square = lambda x: x * x
print(square(5))                   # 25

add = lambda a, b: a + b  # How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))                 # <class 'function'>
print(add(10, 20))               # 30
print(add(10.6, 20.8))           # 31.4
print(add('Hyder', 'abad'))      # Hyderabad
print(add(True, False))          # 1   (True=1, False=0 → 1+0=1)
print(add(25, 10.8))             # 35.8
print(add(3+4j, 5+6j))           # (8+10j)
print(add(10, '20'))             # Error: int and str cannot be added
print(add())                     # Error: missing 2 required arguments
print(add)                       # <function <lambda> at 0x...>

add = lambda a=1, b=2: a + b
print(add(10, 20))  # 30
print(add())        # 3

print((lambda x, y: x + y)(10, 20))          # 30
print((lambda x, y: x + y)(10.8, 20.6))      # 31.4
print((lambda x, y: x + y)('Hyder', 'abad')) # Hyderabad
print(lambda x, y: x + y('Hyder', 'abad'))   # <function <lambda> at 0x...>

large = lambda a, b: max(a, b)  # How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10, 20))           # 20
print(large(10.7, 5.6))        # 10.7
print(large('g', 's'))         # s
print(large('Rama', 'Rajesh')) # Rama   
print(large(True, False))      # True   

power = lambda a=3.5, b=2: a ** b
print(power(2, 3))     # 8
print(power(4.5, 4))   # 410.0625
print(power())         # 12.25   (a and b takes default values 3.5 ** 2)
print(power(9))        # 81     ( b takes default=2)

all = lambda a, b: (a + b, a - b, a * b, a / b)

x = all(10, 7)
print(type(x))   # <class 'tuple'>
print(x)         # (17, 3, 70, 1.4285714285714286)
p, q, r, s = all(9, 2)
print(p)         # 11
print(q)         # 7
print(r)         # 18
print(s)         # 4.5

a = lambda: 'Hyd'
print(a())  # Hyd
print(a)    # <function <lambda> at 0x...>

a = lambda: print('Hyd'); print('Sec'); print('Cyb')
print(a()) # Sec
  #  Cyb
  #  Hyd
  #  None

a = lambda: 'Hyd' ; print('Sec') ; print('Cyb')
print(a())  #  Sec
   #  Cyb
   #  Hyd

a = lambda: print('Hyd'), 
print('Sec')  # Sec
 print('Cyb')  # Cyb
print(type(a))  # <class 'tuple'>
print(a)  # (<function <lambda> at 0x...>, None, None)
for x in a:
    print(x)  # <function <lambda> at 0x...>
     # None
     # None
a()  # Error: 'tuple' object is not callable
print(a[0]())  # Hyd
        # None

s = 'Hyd'
print(lambda s : print(s))              # <function <lambda> at 0x...>
print(lambda x : print(x) (s))          # Error: invalid syntax
print((lambda x : print(x)) (s))        # Hyd  \n  # None
(lambda x : print(x)) (s)               # Hyd

x = 5
adder1 = lambda y, x = x : x + y
x = 10
adder2 = lambda y, x = x : x + y
x = 20
print(adder1(100))      # 105
print(adder2(200))      # 210
print(adder1(300, 400)) # 700

a = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]
for fun in a:
    print(fun(5))  # 25  \n  #125  \n  #625

def f1():
    print('Hyd')  # Hyd
def f2():
    print('Sec')   # Sec
a = [f1, f2]
for x in a:
    x()  # Hyd, Sec
a = [def f1(): print('Hyd'), def f2(): print('Sec')]  # Error : You cannot define functions inside a list directly
print(a)  # Error: Function definitions cannot be written as expressions inside a list

a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])       # <function <lambda> at 0x...>
print(a )    # 125

def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))     # <class 'function'>
print(type(lamb))   # <class 'function'>
print(lamb(2))      # 9
print(lamb(5))      # 243
print(lamb)         # <function f1.<locals>.<lambda> at 0x...>
print(lamb())       # Error: missing required argument 'n'

def eval(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2))    # 25
print(lam(2.5))  # 33.75
print(lam(4))    # 69

add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()

print(a(20))        # 30
print(add(30)(40))  # 70

a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) , (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()  # prints empty space
c = sorted(a , reverse = True)
print(c)  # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()  # prints empty space
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d) # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()  # prints empty space
e = sorted(a , key =  lambda   x  :  x[2])
print(e) # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()  # prints empty space
f = sorted(a , key = lambda   x  :  x[0])
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()  # prints empty space
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # Error: x is not defined, must use lambda x : x[1]

a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)  # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, 
 #  {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, 
 #  {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a))  # Error: '<' not supported between instances of 'dict' and 'dict'

a = ((10 , 'Rama' , 1000.0), (20 , 'Sita' , 2800.0), (15 , 'Vamsi' , 2000.0), (25 , 'Kiran' , 1500.0), (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))  # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))  # (15, 'Vamsi', 2000.0)

print(max(a , key = lambda  x  :  x[2] ))  # (20, 'Sita', 2800.0)
print(max(a))  # (25, 'Kiran', 1500.0)

add = lambda  x  :   x == 25
print(add(10))  # False
add = lambda  x = 25 :   x == 35
print(add())  # False
add = lambda  x  :   x = 25  # Error: cannot use assignment '=' inside lambda
add = lambda x : x := 25 # Error: invalid syntax, assignment expression (:=) not allowed like this in lambda

q)There  are  21  matchsticks. User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins
Logic:  Total  should  be  5
Hint: Use while  loop
Ans)  n = 21
while True:
    # get valid user pick
    while True:
        try:
            u = int(input("How many matchsticks would you like to pick (1 , 2 , 3 or 4) ?  : "))
        except ValueError:
            print("Invalid input. Reenter : ", end="")
            continue
        if u < 1 or u > 4:
            print("Input can not be > 4 nor < 1, Reenter : ", end="")
            continue
        if u > n:
            print(f"Only {n} matchsticks left. Reenter : ", end="")
            continue
        break
    n -= u
    # if user took last -> user loses
    if n == 0:
        print("You have picked the last matchstick")
        print("You have lost the game  and  Computer  wins")  # user loses
        break
    # computer's strategy: try to make (user + computer) = 5
    desired = 5 - u
    # choose computer pick safely (1..4), avoid taking last if possible
    if desired <= 0:
        c = 1
    else:
        if desired >= n:
            # if taking 'desired' would take all remaining, avoid if possible
            if n == 1:
                c = 1  # forced to take last (computer will lose)
            else:
                c = min(4, n - 1)  # take up to n-1 (avoid last)
        else:
            c = desired
    # ensure c at least 1 and not more than available
    if c < 1:
        c = 1
    if c > n:
        c = n
    print(f"Computer picks {c} matchsticks")  # dynamic output
    n -= c
    # if computer took last -> computer loses
    if n == 0:
        print("Computer picked the last matchstick")
        print("Computer has lost the game  and  You  win")
        break

q)Write  a  program  to  convert  roman number to  arabic  number
 What is the output  if  input  is  MMMCDXXIV --->  3424
Ans) # Program to convert Roman number to Arabic number
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
roman = input("Enter Roman number: ").upper()
rev = roman[::-1]
print("Reversed Roman string:", rev)
total = 0
prev = 0
for ch in rev:
    value = roman_dict[ch]
    if value >= prev:
        total += value        # Rule 8
    else:
        total -= value        # Rule 9
    prev = value
print("Arabic number:", total)

