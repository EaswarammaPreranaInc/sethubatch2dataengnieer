: # Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)

############
output:-
10
20
11
40



: # Find  outputs (Home  work)
x = 10
def   f1():
	print(x)  # 10
	print(globals()['x']) # 10
# End of the function
f1()



: # Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) # 20
	print(globals()['x']) # error
# End  of  the  function
f1()


: # Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
########
40 50 60
10 20 30
100 200 300

: # global  keyword  demo  program (Home  work)
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
print(x)  # 10
x += 1    # 11
f1()
print(x)  # 20
f2()
print(x)  # 30
x += 1    # 31
f3()
print(y)  # 40
f4()
print(x)  # error 



: # Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a) ## 20
	print(globals()['a']) ## 20
	a = 30
# End of the function
a = 10
print(a) ## 10
f1()
print(a) ## 30


: # Find  outputs(Home  work)
def  f1():
	global  a
	print(a)
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a) ## error


: # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)
##########
10
20
30
40

: # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10
	a = 20
def  f2():
	print(a)
	a = 30
	print(a) # error
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)


: #  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)
############## error

: # Find outputs (Home  work)
def  f1():
        global  a
        print(a) # 10
        a += 1   # 11
def  f2():
        global  a
        print(a) # 13
        a += 1   # 14
# End  of  the  function
a = 10
print(a) # 10
a += 1   # 11
f1()    
print(a) # 11 
a += 1   # 12
f2()
print(a) # 14


: # Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a) # 10
f1()
a += 1   # 11
f2()
print(a) # error


: # Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1
f1()
print(a)
#########SyntaxError: name 'a' is assigned to before global declaration


: #  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()
print(x)
############
UnboundLocalError: local variable 'x' referenced before assignment
