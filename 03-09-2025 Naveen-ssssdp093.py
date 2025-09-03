# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)                    # 20
	dict = globals()
	print(dict['a'])            # 11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)                        # 10
a += 1                          # 11
f1()
print(a)                        # 40



# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)                        # 10
	print(globals()['x'])           # 10
# End of the function
f1()



# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)                        # 20
	print(globals()['x'])           # error x is not global variable
# End  of  the  function
f1()



# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)                            # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])    # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)                            # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()



# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)                    # 20
def   f2():
	global  x
	x = 30
	print(x)                    # 30
	x += 1                      # 31
def   f3():
	global  y
	y = 40
	print(y)                    # 40
	y += 1                      # 41
def   f4():
	x = 50
#	global   x                  # error x is local variable it cannot be declared as global
#  End  of  the  functions
x = 10
print(x)                        # 10
x += 1                          # 11
f1()
print(x)                        # 11
f2()
print(x)                        # 31
x += 1                          # 32
f3()
print(y)                        # 41
f4()                            # error
print(x)                        # cannot be executed because f4() is error




# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)                        # 20
	print(globals()['a'])           # 20
	a = 30
# End of the function
a = 10
print(a)                            # 10
f1()
print(a)                            # 30



# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)                        # a is not declared
	a = 10
	print(globals()['a'])           # 10
	a = 20
	print(a)                        # 20
	a = 30
def  f2():
	print(a)                        # 30
# End  of   f2   function
f1()
f2()
print(a)                            # 30



# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)                        # 10
	a = 20
def  f2():
	global  a
	print(a)                        # 20
	a = 30
def  f3():
	print(a)                        # 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)                            # 40



# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)                        # 10
	a = 20
def  f2():
	print(a)                        # 20 
	a = 30                          # error 
	print(a)
def  f3():
	print(a)                        # 20
	globals()['a'] = 40
# End  of  the  function
f1()                                # prints 10
f2()                                # throws error
f3()
print(a)                            # 40



#  Find  outputs (Home  work)
def  f1():
        a = 10
#        global  a               # error cannot be declared after declaring local variable
        print(a)                # 10
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)                        # 20



# Find outputs (Home  work)
def  f1():
        global  a
        print(a)                # 11
        a += 1                  # 12
def  f2():
        global  a
        print(a)                # 13
        a += 1                  # 14
# End  of  the  function
a = 10
print(a)                        # 10
a += 1                          # 11
f1()
print(a)                        # 12
a += 1                          # 13
f2()
print(a)                        # 14



# Find outputs (Home  work)
def  f1():
	a = 20
#	global   a                      # error a is local variable it cannot be declared as global variable
	print(a)                        # 20
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)                            # 10
a += 1                              # 11
f1()
print(a)                            # 11



#  Find   outputs
def   f1():
	x = x + 5                   # error
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)                    # 15
# End of f2  function
x = 10
f1()                            # error
f2()
print(x)                        # 10