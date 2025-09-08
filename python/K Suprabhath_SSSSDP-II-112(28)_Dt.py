# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)# Local  variable
	dict = globals()
	print(dict['a'])# Global  variable
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)# Global  variable
a += 1
f1()#  Function  call
print(a)# Global  variable

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)# Local  variable
	print(globals()['x'])# Global  variable
# End of the function
f1()# Function  call

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)# 10
	print(globals()['x'])# 10
# End of the function
f1()# 10

# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)# 20
	print(globals()['x'])# 20
# End  of  the  function
f1()# 20 10

# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)# 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])# 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)# 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()#100 200 300 
f2()#100 200 300

# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)
def   f2():
	global  x
	x = 30
	print(x)
	x += 1
def   f3():
	global  y
	y = 40
	print(y)
	y += 1
def   f4():
	x = 50
	global   x
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)
f4()
print(x)