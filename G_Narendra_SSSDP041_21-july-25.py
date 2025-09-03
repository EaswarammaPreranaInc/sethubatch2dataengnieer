# How to print dictionary in different ways
a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(a)  # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
for i in a:
    print(i,a[i])
print('Keys of dictionary')
print(a.keys())  # dict_keys([10, 20, 15, 18])
for i in a.keys():
    print(i)
print('Values of dictionary')
print(a.values())  # dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
for i in a.values():
    print(i)
print('Key-Value pairs:')
print(a.items())  # dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
for i in a.items():
    print(*i)
print('Each key and value:')
for k, v in a.items():
    print(k, v)  # 10 Ramesh ...

a = {
    print('Hyd'),  # Hyd
    print('Sec'),  # Sec
    print('Cyb')   # Cyb
}
print(type(a))  # <class 'set'>
print(a)        # {None}
print(len(a))   # 1


# Anonymous object (using variable _)
_ = 25
print(_)        # 25
print(type(_))  # <class 'int'>
a, _, c = 10, 20, 30
print(a)        # 10
print(_)        # 20
print(c)        # 30

for _ in range(5):
    print(_, 'Hello')  # 0 Hello ... 4 Hello


# id() and reassignment
a = 25
print(id(a))  # address of object 25
a = 35
print(id(a))  # address of object 35
a = 25.7
print(id(a))
print(a)       # 25.7
a = 35.6
print(id(a))
print(a)       # 35.6
b = True
print(id(b))   # id of True
b = False
print(id(b))   # id of False
c = None
print(id(c))
c = None
print(id(c))


a = 'Hyd'
print(id(a))
# a[1] = 'e'  #  Error: 'str' object does not support item assignment
a = 'Sec'
print(id(a))
b = (10, 20, 15, 18)
print(id(b))
# b[2] = 19  #  Error: 'tuple' object does not support item assignment
b = (30, 40, 35, 32)
print(id(b))
c = range(5)
print(id(c))
# c[3] = 10  #  Error: 'range' object does not support item assignment
c = range(5)
print(id(c))


a = 25
b = 25
print(a is b)  # True
c = 'Hyd'
d = 'Hyd'
print(c is d)  # True (string interning)
e = False
f = False
print(e is f)  # True
g = range(10)
h = range(10)
print(g is h)  # False
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
print(a is b)  # False
c = {10: 20, 30: 40}
d = {10: 20, 30: 40}
print(c is d)  # False
e = (10, 20, 15, 18)
f = (10, 20, 15, 18)
print(e is f)  # True
g = {10, 20, 15, 18}
h = {10, 20, 15, 18}
print(g is h)  # False


print(10 + 20)                         # 30
print(10.8 + 20.6)                     # 31.4
print(3 + 4j + 5 + 6j)                 # (8+10j)
print(True + False)                   # 1
print('Hyder' + 'abad')               # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')   # SankarDayalSarma
print('10' + '20')                    # 1020
print([10, 20, 30] + [1, 2, 3])       # [10, 20, 30, 1, 2, 3]
print((25, 10.8, 'Hyd') + (3 + 4j, True, None)) 

print({10, 20} + {30, 40})               # TypeError: unsupported operand type(s) for +
print({10: 'Hyd'} + {20: 'Sec'})         # TypeError: unsupported operand type(s) for +
print(range(4) + range(5))               # TypeError: unsupported operand types
print(10 + '20')                         # TypeError: unsupported operand
print([10, 20, 30] + 5)                  # TypeError
print([10, 20, 30] + (40, 50, 60))       # TypeError


print(25 * 3)                             # 75
print(10.8 * 25.6)                        # 276.48
print(True * False)                       # 0
print((3 + 4j) * (5 + 6j))                # (-9+38j)
print(3 + 4j * 5 + 6j)                    # (3+26j)
print('25' * 3)                           # '252525'
print(3 * '25')                           # '252525'
print('Hyd' * 4)                          # HydHydHydHyd
print([10, 20, 15] * 2)                   # [10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)        # (25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10, 20, 15] * 3.0)               # TypeError: can't multiply sequence by non-int
print({10, 20, 15} * 2)                 # TypeError
print({10: 20, 30: 40} * 2)             # TypeError
print([10] * [20])                     # TypeError


print(9.0 / 2)       # 4.5
print(9 / 2.0)       # 4.5
print(9.0 / 2.0)     # 4.5
print(9 / 2)         # 4.5
print(10.5 / 2)      # 5.25
print(10 / 3)        # 3.333...
print(10 / 2)        # 5.0


print(9 // 2)        # 4
print(9.0 // 2)      # 4.0
print(9 // 2.0)      # 4.0
print(9.0 // 2.0)    # 4.0
print(10.5 // 2)     # 5.0
print(10 // 3)       # 3
print(10.0 // 3)     # 3.0
print(8.5 // 3)      # 2.0
print(18 // 4)       # 4
print(-18 // 4)      # -5
print(-(18 // 4))    # -4


print(9 % 5)         # 4
print(9.0 % 5)       # 4.0
print(9 % 5.0)       # 4.0
print(9.0 % 5.0)     # 4.0
print(10.5 % 2)      # 0.5
print(8.9 % 3)       # 2.9


print(7 / 0)       # ZeroDivisionError
print(7 // 0)      # ZeroDivisionError
print(7 % 0)       # ZeroDivisionError


print(3 ** 4)           # 81
print(10 ** -2)         # 0.01
print(4 ** 3 ** 2)      # 262144
print(3 + 4 * 5 - 32 / 2 ** 3)  # 19.0


print(9 >= 5)       # True
print(9 >= 9)       # True
print(9 >= 12)      # False
print(6 <= 8)       # True
print(6 <= 6)       # True
print(6 <= 4)       # False
print(9 != 7)       # True
print(6 == 8)       # False
print(True > False)               # True
print(3 + 4j == 3 + 4j)           # True
print(3 + 4j == 5 + 6j)           # False
print(3 + 4j != 5 + 6j)           # True
print(10 == 10.0)                 # True
# print(3 + 4j > 3 + 4j)          # Error: can't compare complex numbers


print('Rama' > 'Rajesh')     # True
print('Rama' < 'Sita')       # True
print('Hyd' == 'Hyd')        # True
print('Rama' <= 'Ramana')    # True
print('Rama Rao' >= 'Rama')  # True
print('Hyd' != 'Sec')        # True
print('HYD' < 'hyd')         # True (uppercase < lowercase)


print(10 < 20 < 30)          # True
print(10 >= 20 < 30)         # False
print(10 < 20 > 30)          # False
print(1 < 2 < 3 < 4)         # True
print(1 < 2 > 3 > 1)         # False
print(4 > 3 >= 3 > 2)        # True


print(True or False)         # True
print(False or True)         # True
print(True or True)          # True
print(False or False)        # False
print(10 or 20)              # 10
print(0 or 20)               # 20
print(-25 or 0)              # -25
print('' or 35)              # 35
print(6j or 'Hyd')           # 6j
print(0.0 or 3 + 4j)         # (3+4j)
print('Hyd' or 10.8)         # Hyd


print(not True)              # False
print(not False)             # True
print(not 25)                # False
print(not 0)                 # True
print(not 'Hyd')             # False
print(not '')                # True
print(not -10)               # False
print(not not 'Hyd')         # True


i = 10
i = not i > 14
print(i)  # True

print(not (6 < 4 or 9 >= 5 and 6 != 6))  # True
