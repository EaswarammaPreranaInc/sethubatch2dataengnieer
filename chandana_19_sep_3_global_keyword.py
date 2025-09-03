# global  keyword  
def    f1():
	x = 20
	print(x)
def   f2():
	global  x # declare 'x' as global variable
	x = 30 # change global variable 'x'
	print(x)
	x += 1 # increment global variable 'x'
def   f3():
	global  y # declare 'y' as global variable
	y = 40 # change global variable 'y'
	print(y)
	y += 1
def   f4():
	x = 50 
#	global   x # error : there is already local variable 'x'. 'x' cannot be treated as global variable
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
'''
o/p:
10
20
11
30
31
40
41
32
'''


# Find outputs 
def  f1():
	global  a # declare 'a' as global variable
	a = 20
	print(a)
	print(globals()['a']) # print global variable 'a'
	a = 30
# End of the function
a = 10
print(a)
f1()
print(a)
'''
10
20
20
30'''



# Find  outputs
def  f1():
	global  a
#	print(a) # error : 'a' is not defined
	a = 10
	print(globals()['a']) # print global variable 'a'=10
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a)
'''
10
20
30
30'''


# Find outputs 
def  f1():
	global   a # declare 'a' as global variable
	a = 10
	print(a)
	a = 20
def  f2():
	global  a 
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40 # change global variable 'a'=40
# End  of  the  function
f1()
f2()
f3()
print(a)
'''
10
20
30
40'''


# Find outputs 
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
#	print(a) # Error : 'a' is not defined
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)
'''
10
30
20
40'''


#  Find  outputs 
def  f1():
        a = 10
#       global  a # Error: there is already local variable 'a'.so, 'a' cannot be treated as global variable
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a) # Error : 'a' is not defined
print(b)
'''
10
20'''



# Find outputs 
def  f1():
        global  a
        print(a)
        a += 1
def  f2():
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)
'''
10
11
12
13
14'''


# Find  outputs 
def   f1():
	a = 20
	print(a)
'''
def  f2():
	print(a) # error: 'a' is not defined
	a += 1 # error 
	'''
# End of the function
a = 10
print(a)
f1()
a += 1 
#f2()
print(a)
'''
10
20
11'''


# Find outputs 
def  f1():
	a = 20
#	global   a # error : there is already local variable 'a'.so, 'a' cannot be treated as global variable
	print(a)
	print(globals()['a']) # print global variable 'a'
	a = 30
	globals()['a'] = 40 # change global variable 'a'
#  End  of  f1()   function
a = 10
print(a)
a += 1
f1()
print(a)
'''
10
20
11
40'''


#  Find   outputs
'''
def   f1():
	x = x + 5  # error:
# End  of  f1  function
'''
def  f2():
	x = globals()['x'] + 5 # change global variable 'x'=15
	print(x)
# End of f2  function
x = 10
#f1()
f2()
print(x)
'''
15
10'''
