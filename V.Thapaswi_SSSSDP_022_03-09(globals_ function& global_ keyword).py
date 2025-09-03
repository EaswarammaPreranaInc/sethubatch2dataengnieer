# global  keyword  
#1) Find outputs 
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


# 2) Find outputs 
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



#3)  Find  outputs
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


# 4) Find outputs 
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


# 5) Find outputs 
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


# 6)  Find  outputs 
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



# 7) Find outputs 
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


# 8) Find  outputs 
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


#9)  Find outputs 
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


# 10)  Find   outputs
'''
def   f1():
	x = x + 5  # error
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


#globals()_function


#11) Find  outputs  
def   f1():
	a = 20
	print(a) # print local variable 'a'
	dict = globals() # get the dictionary of global variables
	print(dict['a']) # print global variable 'a'
	a = 30 # change local variable 'a'
	dict['a'] = 40 # change global variable 'a'
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)
'''
o/p:
10
20
11
40'''


# 12) Find  outputs 
x = 10
def   f1():
	print(x) # print global variable 'x'
	print(globals()['x']) # print global variable 'x'
# End of the function
f1()
'''
10
10'''


# 13) Find  outputs 
def  f1():
	x = 20
	print(x) 
	print(globals()['x']) # error: beacuse there is already local variable 'x'.so, 'x' cannot be treated as global variable
# End  of  the  function
f1()
'''
10'''



# 14) Find outputs 
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals() # get the dictionary of global variables
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100 # change global variable 'a'
	dict['b'] = 200 # change global variable 'b'
	dict['c'] = 300 # change global variable 'c'
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
'''
40 50 60
10 20 30
100 200 300
'''
