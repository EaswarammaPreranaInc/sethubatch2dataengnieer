# How to print dictionary in different ways
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#'Dictionary with print function'
print(a.keys())#'Keys of dictionary'
print(a.values())#'Values of dictionary'
print(a.items())#'All the tuples of dict_items object'
print("Elements of each tuple:")
for item in a.items():
    print(item) # prints (Keys, value)
print("Keys and values of dictionary:")
for k, v in a.items():
    print(f"Key: {k}, Value: {v}")


# Find outputs (Home work)
a = {
print('Hyd') , #prints Hyd and returns None
print('Sec') , #prints Sec and returns None
print('Cyb') #prints Cyb and returns None
}
print(type(a))#<class 'set'>
print(a) #prints {None}
print(len(a)) # 1


# Anonymous object demo program
_ = 25
print(_) #prints 25
print(type(_)) #<class 'int'>
a , _ , c = 10 , 20 , 30
print(a) #10
print(_)#20
print(c)#30
for _ in range(5):
    print(_ , 'Hello') 
    ''' prints 0 Hello
    1 Hello
    2 Hello
    3 Hello
    4 Hello'''


# Find outputs
a = 25
print(id(a))#prints reference address
a = 35
print(id(a))#prints different reference address


# Find outputs (Home work)
a = 25.7
print(id(a))#print reference address
print(a)#prints 25.7
a = 35.6
print(id(a))#prints new reference address
print(a) # prints 35.6
b = True
print(id(b))#prints new reference address
b = False
print(id(b))#prints new reference address
c = None
print(id(c))#prints new reference address
c = None
print(id(c))#prints same reference address


# Find outputs (Home work)
a = 'Hyd'
print(id(a))# prints address
#a[1] = 'e' # error string is immutable
a = 'Sec'
print(id(a)) #print address
b = (10 , 20 , 15 , 18)
print(id(b)) #print address
#b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))#error
c = range(5)
print(id(c))#print address
#c[3] = 10 # error
c = range(5)
print(id(c)) #print address


# Find outputs (Home work)
a = 25
b = 25
print(a is b)#True
c = 'Hyd'
d = 'Hyd'
print(c is d)#True
e = False
f = False
print(e is f)#True
g = range(10)
h = range(10)
print(g is h)#False


#Find outputs(Home work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a is b)#False
c = {10 : 20, 30 : 40}
d = {10 : 20, 30 : 40}
print(c is d)#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e is f)#True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g is h)#False
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10, 20, 30] + [1, 2, 3]) # [10, 20, 30, 1, 2, 3]
print((25, 10.8, 'Hyd') + (3 + 4j, True, None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
#print({10, 20} + {30, 40}) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10: 'Hyd'} + {20: 'Sec'}) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#print(range(4) + range(5)) # TypeError: unsupported operand type(s) for +: 'range' and 'range'
#print(10 + '20') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print([10, 20, 30] + 5) # TypeError: can only concatenate list (not "int") to list
#print([10, 20, 30] + (40, 50, 60)) # TypeError: can only concatenate list (not "tuple") to list
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10, 20, 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10, 20, 15] * 3.0) # TypeError: can't multiply sequence by non-int of type 'float'
#print({10, 20, 15} * 2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'
#print({10: 20, 30: 40} * 2) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
#print([10] * [20]) # TypeError: can't multiply sequence by non-int of type 'list'
print(9.0 / 2) # 4.5
print(9 / 2.0) # 4.5
print(9.0 / 2.0) # 4.5
print(9 / 2) # 4.5
print(10.5 / 2) # 5.25
print(10 / 3) # 3.3333333333333335
print(10 / 2) # 5.0
print(9 // 2) # 4
print(9.0 // 2) # 4.0
print(9 // 2.0) # 4.0
print(9.0 // 2.0) # 4.0
print(10.5 // 2) # 5.0
print(10 // 3) # 3
print(10.0 // 3) # 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4) # -5
print(-(18 // 4)) # -4
print(9 % 5) # 4
print(9.0 % 5) # 4.0
print(9 % 5.0) # 4.0
print(9.0 % 5.0) # 4.0
print(10.5 % 2) # 0.5
print(8.9 % 3) # 2.9
#print(7 / 0) # ZeroDivisionError: division by zero
#print(7 // 0) # ZeroDivisionError: division by zero
#print(7 % 0) # ZeroDivisionError: modulo by zero
print(3 ** 4) # 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # 3 + 20 - 32 / 8 # 3 + 20 - 4 # 19
print(9 >= 5) # True
print(9 >= 9) # True
print(9 >= 12) # False
print(6 <= 8) # True
print(6 <= 6) # True
print(6 <= 4) # False
print(9 != 7) # True
print(6 == 8) # False
print(True > False) # True (True is equivalent to 1, False is equivalent to 0)
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
#print(3 + 4j > 3 + 4j) # TypeError: '>' not supported between instances of 'complex' and 'complex'
print('Rama' > 'Rajesh') # True (because 'm' > 'j')
print('Rama' < 'Sita') # True (because 'R' < 'S')
print('Hyd' == 'Hyd') # True
print('Rama' <= 'Ramana') # True (because 'Rama' is a prefix of 'Ramana')
print('Rama Rao' >= 'Rama') # True (because 'Rama' is a prefix of 'Rama Rao')
print('Hyd' != 'Sec') # True
print('HYD' < 'hyd') # True (because 'H' < 'h', due to Unicode values 72 < 104)
print(10 < 20 < 30) # True
print(10 >= 20 < 30) # False
print(10 < 20 > 30) # False (because 20 is not > 30)
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 3 > 1) # False (because 2 is not > 3)
print(4 > 3 >= 3 > 2) # True
print(True or False) # True
print(False or True) # True
print(True or True) # True
print(False or False) # False
print(10 or 20) # 10
print(0 or 20) # 20
print(-25 or 0) # -25
print('' or 35) # 35
print(6j or 'Hyd') # 6j
print(0.0 or 3 + 4j) # (3+4j)
print('Hyd' or 10.8) # Hyd
print(not True) # False
print(not False) # True
print(not 25) # False (because 25 is considered True in a boolean context)
print(not 0) # True (because 0 is considered False in a boolean context)
print(not 'Hyd') # False (because non-empty string is considered True)
print(not '') # True (because empty string is considered False)
print(not -10) # False (because non-zero number is considered True)
print(not not 'Hyd') # True (because 'Hyd' is considered True, and not not True is True)
i = 10
i = not i > 14
print(i) # True (because i > 14 is False, and not False is True)
print(not(6 < 4 or 9 >= 5 and 6 != 6))
'''1. Evaluate 6 < 4: False
2. Evaluate 9 >= 5: True
3. Evaluate 6 != 6: False
4. Evaluate True and False: False
5. Evaluate False or False: False
6. Finally, not False: True
So, print(not(6 < 4 or 9 >= 5 and 6 != 6)) # True'''
