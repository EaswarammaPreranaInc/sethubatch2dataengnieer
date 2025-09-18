def f1():
	a = 20
	print(a)  # 20
	dict = globals()
	print(dict['a'])  # 11
	a = 30
	dict['a'] = 40
a = 10
print(a)  # 10
a += 1
f1()
print(a)  # 40

x = 10
def f1():
	print(x)  # 10
	print(globals()['x'])  # 10
f1()

def f1():
	x = 20
	print(x)  # 20
	print(globals()['x'])  # 10
f1()

def f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)  # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])  # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def f2():
	print(a , b , c)  # 100 200 300
a = 10
b = 20
c = 30
f1()
f2()

def f1():
	x = 20
	print(x)  # 20
def f2():
	global x
	x = 30
	print(x)  # 30
	x += 1
def f3():
	global y
	y = 40
	print(y)  # 40
	y += 1
def f4():
	x = 50
	global x  # error
x = 10
print(x)  # 10
x += 1
f1()
print(x)  # 11
f2()
print(x)  # 31
x += 1
f3()
print(y)  # 41
f4()
print(x)

def f1():
	global a
	a = 20
	print(a)  # 20
	print(globals()['a'])  # 20
	a = 30
a = 10
print(a)  # 10
f1()
print(a)  # 30

def f1():
	global a
	print(a)  # 10
	a = 10
	print(globals()['a'])  # 10
	a = 20
	print(a)  # 20
	a = 30
def f2():
	print(a)  # 30
f1()
f2()
print(a)  # 30

def f1():
	global a
	a = 10
	print(a)  # 10
	a = 20
def f2():
	global a
	print(a)  # 20
	a = 30
def f3():
	print(a)  # 30
	globals()['a'] = 40
f1()
f2()
f3()
print(a)  # 40

def f1():
	global a
	a = 10
	print(a)  # 10
	a = 20
def f2():
	print(a)  # 20
	a = 30  # error
	print(a)
def f3():
	print(a)
	globals()['a'] = 40
f1()
f2()
f3()
print(a)

def f1():
	a = 10
	global a  # error
	print(a)
	global b
	b = 20
f1()
print(a)
print(b)

def f1():
	global a
	print(a)  # 11
	a += 1
def f2():
	global a
	print(a)  # 12
	a += 1
a = 10
print(a)  # 10
a += 1
f1()
print(a)  # 12
a += 1
f2()
print(a)  # 13

def f1():
	a = 20
	print(a)  # 20
def f2():
	print(a)  # 11
	a += 1  # error
a = 10
print(a)  # 10
f1()
a += 1
f2()
print(a)

def f1():
	a = 20
	global a  # error
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
a = 10
print(a)  # 10
a += 1
f1()
print(a)

def f1():
	x = x + 5  # error
def f2():
	x = globals()['x'] + 5
	print(x)  # 15
x = 10
f1()
f2()
print(x)  # 10
