# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)                          #10
a += 1
f1()                              #20
                                  #11
print(a)                          #40


 # Find  outputs (Home  work)
x = 10
def   f1():
	print(x)                     
	print(globals()['x'])
# End of the function
f1()                         #10
                             #10


# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)                             #20
	print(globals()['x'])                #not defined     
# End  of  the  function
f1()


# Find outputs (Home  work)
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
f1()                            # 40 50 60    #10 20 30
f2()                            #100 200 300

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
	#global   x
#  End  of  the  functions
x = 10
print(x)                                      #10
@@ -161,7 +161,7 @@
#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
      z#  global  a
        print(a)
        global  b
        b = 20
@@ -210,7 +210,7 @@
# Find outputs (Home  work)
def  f1():
	a = 20
	global   a                        
	#global   a                        
	print(a)                          #
	print(globals()['a'])
	a = 30
@@ -219,7 +219,7 @@
a = 10
print(a)                           #10
a += 1 
f1()                               #20 #10 
f1()                               #20 #10
print(a)                           #40
