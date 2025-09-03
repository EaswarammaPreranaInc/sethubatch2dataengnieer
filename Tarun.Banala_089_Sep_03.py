#Tarun Banala.   03-09-2025
# Find outputs (Home work)
def f1():
	a = 20                  # 20
	print(a)               # prints 20
	dict = globals()
	print(dict['a'])       # prints 11 (global a before calling f1)
	a = 30
	dict['a'] = 40         # updates global 'a' to 40

a = 10                     # 10
print(a)                   # prints 10
a += 1                     # a = 11
f1()
print(a)                   # prints 40 (a was updated in globals by f1)

# Find outputs (Home work)
x = 10
def f1():
	print(x)              # prints 10 (x from global scope)
	print(globals()['x']) # prints 10 (same global x)
f1()

# Find outputs (Home work)
def f1():
	x = 20
	print(x)              # prints 20 (local x)
	print(globals()['x']) # prints 10 (global x)
f1()

# Find outputs (Home work)
def f1():
	a = 40
	b = 50
	c = 60
	print(a, b, c)        # prints 40 50 60 (local)
	dict = globals()
	print(dict['a'], dict['b'], dict['c'])  # prints 10 20 30 (global)
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300

def f2():
	print(a, b, c)        # prints a=100, b=200, c=300 (updated globals)

a = 10
b = 20
c = 30
f1()
f2()

# global keyword demo program (Home work)
def f1():
	x = 20
	print(x)              # prints 20 (local)

def f2():
	global x
	x = 30
	print(x)              # prints 30
	x += 1                # x becomes 31

def f3():
	global y
	y = 40
	print(y)              # prints 40
	y += 1                # y becomes 41

def f4():
	x = 50
	global x              # SyntaxError: name 'x' is assigned before global declaration

x = 10
print(x)                  # prints 10
x += 1                    # x = 11
f1()
print(x)                  # prints 11 (unchanged by f1)
f2()
print(x)                  # prints 31
x += 1                    # x = 32
f3()
print(y)                  # prints 41
# f4() This will cause a SyntaxError at runtime

# Find outputs (Home work)
def f1():
	global a
	a = 20
	print(a)              # prints 20
	print(globals()['a']) # prints 20
	a = 30

a = 10
print(a)                  # prints 10
f1()
print(a)                  # prints 30

# Find outputs (Home work)
def f1():
	global a
	print(a)              # prints 30 (from previous block)
	a = 10
	print(globals()['a']) # prints 10
	a = 20
	print(a)              # prints 20
	a = 30

def f2():
	print(a)              # prints 30

f1()
f2()
print(a)                  # prints 30

# Find outputs (Home work)
def f1():
	global a
	a = 10
	print(a)              # prints 10
	a = 20

def f2():
	global a
	print(a)              # prints 20
	a = 30

def f3():
	print(a)              # prints 30
	globals()['a'] = 40

f1()
f2()
f3()
print(a)                  # prints 40

# Find outputs (Home work)
def f1():
	global a
	a = 10
	print(a)              # prints 10
	a = 20

def f2():
	print(a)              # prints 20 (before a = 30)
	a = 30
	print(a)              # prints 30 (local)

def f3():
	print(a)              # prints 20 (before change)
	globals()['a'] = 40

f1()
f2()
f3()
print(a)                  # prints 40

# Find outputs (Home work)
def f1():
	a = 10
	global a              # SyntaxError: name 'a' is assigned before global declaration
	print(a)
	global b
	b = 20

# f1() will cause SyntaxError at runtime
# print(a)
# print(b)

# Find outputs (Home work)
def f1():
	global a
	print(a)              # prints 10
	a += 1                # a = 11

def f2():
	global a
	print(a)              # prints 11
	a += 1                # a = 12

a = 10
print(a)                  # prints 10
a += 1                    # a = 11
f1()
print(a)                  # prints 11
a += 1                    # a = 12
f2()
print(a)                  # prints 12

# Find outputs (Home work)
def f1():
	a = 20
	print(a)              # prints 20

def f2():
	print(a)              # prints 10
	a += 1                # UnboundLocalError (assignment to local variable without definition)

a = 10
print(a)                  # prints 10
f1()
a += 1                    # a = 11
# f2()  # UnboundLocalError

print(a)                  # prints 11

# Find outputs (Home work)
def f1():
	a = 20
	global a              # SyntaxError: name 'a' is assigned before global declaration
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40

# a = 10
# print(a)
# a += 1
# f1()  # SyntaxError
# print(a)

# Find outputs
def f1():
	x = x + 5             # UnboundLocalError: local variable 'x' referenced before assignment

def f2():
	x = globals()['x'] + 5
	print(x)              # prints 15

x = 10
# f1()  # UnboundLocalError
f2()
print(x)                  # prints 10
