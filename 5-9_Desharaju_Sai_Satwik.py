

def change(b):
    b.append(25)
    b[2] = 17
    del b[1]
a = [10, 20, 15, 18]
print(a)  # [10, 20, 15, 18]
change(a)
print(a)  # [10, 17, 18, 25]


def change(b):
    b = [50, 60, 70, 80]
    print(b)  # [50, 60, 70, 80]
a = [10, 20, 30, 40]
print(a)  # [10, 20, 30, 40]
change(a)
print(a)  # [10, 20, 30, 40]


def f1(x):
    x = 20
    print(x)  # 20
x = 10
print(x)  # 10
f1(x)
print(x)  # 10


def f1(b):
    b[2] = 25
a = (10, 20, 15, 18)
print(a)  # (10, 20, 15, 18)
f1(a)  # error
print(a)


square = lambda x=10: x * x
print(square(5))  # 25
print(square())  # 100


print((lambda x: x * x)(7))  # 49
print(lambda x: x * x(7))  # error
print(lambda x: x * x)  # <function <lambda> at ...>
print((lambda x=25: x * x)())  # 625
square = lambda x: x * x
print(square(5))  # 25


# lambda sum function
add = lambda a, b: a + b
print(type(add))  # <class 'function'>
print(add(10, 20))  # 30
print(add(10.6, 20.8))  # 31.4
print(add('Hyder', 'abad'))  # Hyderabad
print(add(True, False))  # 1
print(add(25, 10.8))  # 35.8
print(add(3+4j, 5+6j))  # (8+10j)
print(add(10, '20'))  # error
print(add())  # error
print(add)  # <function <lambda> at ...>


add = lambda a=1, b=2: a + b
print(add(10, 20))  # 30
print(add())  # 3


print((lambda x, y: x + y)(10, 20))  # 30
print((lambda x, y: x + y)(10.8, 20.6))  # 31.4
print((lambda x, y: x + y)('Hyder', 'abad'))  # Hyderabad
print(lambda x, y: x + y('Hyder', 'abad'))  # error


large = lambda a, b: a if a > b else b
print(large(10, 20))  # 20
print(large(10.7, 5.6))  # 10.7
print(large('g', 's'))  # s
print(large('Rama', 'Rajesh'))  # Rama
print(large(True, False))  # True


power = lambda a=3.5, b=2: a ** b
print(power(2, 3))  # 8
print(power(4.5, 4))  # 410.0625
print(power())  # 12.25
print(power(9))  # 81.0


all = lambda a, b: (a+b, a-b, a*b, a/b)
x = all(10, 7)
print(type(x))  # <class 'tuple'>
print(x)  # (17, 3, 70, 1.4285714285714286)
p, q, r, s = all(9, 2)
print(p)  # 11
print(q)  # 7
print(r)  # 18
print(s)  # 4.5


a = lambda: 'Hyd'
print(a())  # Hyd
print(a)  # <function <lambda> at ...>


a = lambda: print('Hyd'); print('Sec'); print('Cyb')
print(a())  # Hyd\nSec\nCyb\nNone


a = lambda: 'Hyd'; print('Sec'); print('Cyb')
print(a())  # Sec\nCyb\nHyd


a = lambda: print('Hyd'), print('Sec'), print('Cyb')
print(type(a))  # <class 'tuple'>
print(a)  # (None, None, None)
for x in a:
    print(x)  # None\nNone\nNone
a()  # error
print(a[0]())  # error


s = 'Hyd'
print(lambda s: print(s))  # <function <lambda> at ...>
print(lambda x: print(x)(s))  # error
print((lambda x: print(x))(s))  # Hyd\nNone
(lambda x: print(x))(s)  # Hyd


x = 5
adder1 = lambda y, x=x: x + y
x = 10
adder2 = lambda y, x=x: x + y
x = 20
print(adder1(100))  # 105
print(adder2(200))  # 210
print(adder1(300, 400))  # error


a = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for fun in a:
    print(fun(5))  # 25\n125\n625


def f1():
    print('Hyd')
def f2():
    print('Sec')
a = [f1, f2]
for x in a:
    x()  # Hyd\nSec
a = [def f1(): print('Hyd'), def f2(): print('Sec')]  # error
print(a)


a = {'power_2': lambda x: x ** 2,
     'power_3': lambda x: x ** 3,
     'power_4': lambda x: x ** 4}
key = 'power_3'
print(a[key])  # <function <lambda> at ...>
print(a )  # 125


def f1(x):
    return lambda n: x ** n
lamb = f1(3)
print(type(f1))  # <class 'function'>
print(type(lamb))  # <class 'function'>
print(lamb(2))  # 9
print(lamb(5))  # 243
print(lamb)  # <function f1.<locals>.<lambda> at ...>
print(lamb())  # error


def eval(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2))  # 21
print(lam(2.5))  # 28.75
print(lam(4))  # 69


add = lambda x=10: (lambda y: x + y)
a = add()
print(a(20))  # 30
print(add(30)(40))  # 70


a = ((10, 'Rama', 1000.0), (20, 'Sita', 2000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0))
b = sorted(a)
print(b)  # sorted by first field then second etc
print()
c = sorted(a, reverse=True)
print(c)
print()
d = sorted(a, key=lambda x: x[1])
print(d)
print()
e = sorted(a, key=lambda x: x[2])
print(e)
print()
f = sorted(a, key=lambda x: x[0])
print(f)
print()
g = sorted(a, key=lambda x: x[1], reverse=True)
print(g)
print(sorted(a, key=x[1]))  # error


a = [{'Make': 'Ford', 'Model': 'Focus', 'Year': 2013},
     {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
     {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}]
b = sorted(a, key=lambda x: x['Year'])
print(b)  # sorted by Year
print(sorted(a))  # error


a = ((10, 'Rama', 1000.0), (20, 'Sita', 2800.0), (15, 'Vamsi', 2000.0), (25, 'Kiran', 1500.0), (5, 'Amar', 1300.0))
print(max(a, key=lambda x: x[0]))  # (25, 'Kiran', 1500.0)
print(max(a, key=lambda x: x[1]))  # (20, 'Sita', 2800.0)
print(max(a, key=lambda x: x[2]))  # (20, 'Sita', 2800.0)
print(max(a))  # (25, 'Kiran', 1500.0)


add = lambda x: x == 25
print(add(10))  # False
add = lambda x=25: x == 35
print(add())  # False
add = lambda x: x = 25  # error
add = lambda x: x := 25  # error



# Matchsticks game
n = 21
while n > 1:
    user = int(input("How many matchsticks would you like to pick (1 , 2 , 3 or 4) ? : "))
    while user < 1 or user > 4:
        user = int(input("Input can not be > 4 nor < 1,  Reenter : "))
    comp = 5 - user
    print(f"Computer picks {comp} matchsticks")
    n -= 5
print("You have lost the game and Computer wins")


# Roman to integer
def roman_to_int(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev = 0, 0
    for ch in reversed(s):
        cur = values[ch]
        if cur >= prev:
            total += cur
        else:
            total -= cur
        prev = cur
    return total

print(roman_to_int("III"))      # 3
print(roman_to_int("IV"))       # 4
print(roman_to_int("IX"))       # 9
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994
print(roman_to_int("MMMCDXXIV"))# 3424
