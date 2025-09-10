## Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)    # prints 20 as local variable has high preference
	dict = globals()    # dict={'a':11}
	print(dict['a'])  # prints 11
	a = 30  # local variable is updated to 30
	dict['a'] = 40  # global variable a is updated to 40
#  End  of  f1()  function
a = 10 # function starts here a is global variable 10
print(a) # prints 10
a += 1  # a is updated to 11
f1() # function call
print(a)    # prints 40 Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)    # prints 20 as local variable has high preference
	dict = globals()    # dict={'a':11}
	print(dict['a'])  # prints 11
	a = 30  # local variable is updated to 30
	dict['a'] = 40  # global variable a is updated to 40
#  End  of  f1()  function
a = 10 # function starts here a is global variable 10
print(a) # prints 10
a += 1  # a is updated to 11
f1() # function call
print(a)    # prints 40


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)    # prints global x value 10
	print(globals()['x']) # prints global x value 10 from dictionary
# End of the function
f1()


# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)    # prints local x value 20
	print(globals()['x'])   # error as there is no global x
# End  of  the  function
f1()

# Find outputs (Home  work)
def  f1():
	a = 40  # local variable 40
	b = 50  # local variable 50
	c = 60  # local variable 40
	print(a , b , c)    # 40  50  60
	dict = globals()    # dictionary
	print(dict['a'] , dict['b'] , dict['c']) # 10  20 30
	dict['a'] = 100 # modifying global a to 200
	dict['b'] = 200 # modifying global b to 300
	dict['c'] = 300 # modifying global c to 400
	print(a , b , c)   # 40  50  60
def  f2():
	print(a , b , c)    # 100  200  300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)    # prints local x 20
def   f2():
	global  x
	x = 30  # modifying global x to 30
	print(x)    # prints 30
	x += 1  # x value is updated to 31
def   f3():
	global  y   # mentions y as global variable
	y = 40  # as there is no existing a global variable y with value 40 is created
	print(y)    # prints 40
	y += 1  # y=41
def   f4(): 
	x = 50  # x is a local variable 50
	#global   x  # error as ale=ready x became local variable
#  End  of  the  functions
x = 10
print(x)    # prints 10
x += 1 # x value is updated to 11
f1()    # goes to function f1
print(x)    # prints 11
f2()    # goes to function f2
print(x)    # prints 31
x += 1  # x is 32
f3()    # goes to function f3
print(y)# 41
f4()    # goes to function f4
print(x)    # 32

# Find outputs (Home  work)
def  f1():
	global  a   # requesting to treat a as global
	a = 20  # modifying a value to 20
	print(a)    # prints 20
	print(globals()['a']) # 20
	a = 30  # modyfing a to 30
# End of the function
a = 10  # a is global variable 10
print(a) # a is 10
f1()# function is called
print(a)    # prints 30

# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)    # error as there is no a
	a = 10  # new global variable of a with value 10 is created
	print(globals()['a'])   # prints value of a i.e 10
	a = 20  # a is modified to 20
	print(a)    # prints 20
	a = 30  # a is modified to 30
def  f2():
	print(a) # prints 30
# End  of   f2   function
f1()    # function call f1
f2()    # function call f2
print(a) # prints 30

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10  # a global variable with value 10 is created
	print(a)    # prints 10
	a = 20  # modifies the value of a to 20
def  f2():
	global  a
	print(a)    # prints 20
	a = 30  # modifies the value of a to 30
def  f3():
	print(a)    # prints 30
	globals()['a'] = 40  # modifies the value of a to 40
# End  of  the  function
f1()    # function call f1
f2()    # function call f2
f3()    # function call f3
print(a)    # prints 40

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10  # a global variable is created with value 10
	print(a)    # prints 10
	a = 20  # modifies the value of a to 20
def  f2():
	#print(a)    # error because we havent used global function here
	a = 30 # creates a local variable with value 30
	print(a)    # prints 30
def  f3():
	print(a)    # prints 20
	globals()['a'] = 40 # modifies the global variable to 40
# End  of  the  function
f1()    # function call f1
f2()    # function call f2
f3()    # function call f3
print(a)# prints 40

#  Find  outputs (Home  work)
def  f1():
        a = 10  # a local variable a is created
        global  a   # error because there is a local variable with name a
        print(a)    # 10
        global  b   # intimates that a global variable b
        b = 20  # b is created a global variable
# End  of  f1()  function
f1()    # function call f1
print(a)    # error as a is local variable and cant be accesed outside the function
print(b)    # 20


# Find outputs (Home  work)
def  f1():
        global  a   # intimates a as global variable
        print(a)    # 11
        a += 1  # 12
def  f2():
        global  a   # intimates a as global variable
        print(a)    # 12 is printed
        a += 1  # 13  
# End  of  the  function
a = 10  # Global  variable
print(a)    # 10
a += 1  # 11
print(a)    # 11
f1()    # function call f1
print(a)    # prints 11
a += 1  # a=12
f2()    # function call f2
print(a)    # 13 is printed

# Find  outputs (Home  work)
def   f1():
	a = 20  # a local variable 20 is created
	print(a)    # prints 20
def  f2():
	print(a)    # error as there is no globals function
	a += 1  #error as there is no a as local variable
# End of the function
a = 10   # global variable a
print(a)    # prints 10
f1()    # function call f1
a += 1  # a=11
f2()    # function call f2
print(a)    # prints 12

# Find outputs (Home  work)
def  f1():
	a = 20  # lv a
	global   a  # error as already a lv is created
	print(a)    # prints 20
	print(globals()['a'])   # prints 11
	a = 30  # lv a
	globals()['a'] = 40 # gv a
#  End  of  f1()   function
a = 10  # gv a 
print(a)    # prints 10
a += 1  # a=11
f1()    # function call f1
print(a)    # prints 40

#  Find   outputs
def   f1():
	x = x + 5   # error as global keyword is not used and no lv x
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5  # x=10+5=15 a lv is created
	print(x)    # prints 15
# End of f2  function
x = 10  # gv 1=x is 10
f1() # function call f1
f2() # function call f2
print(x)    # prints 10 gv