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
print(a)						
a += 1
f1()
print(a)
	
	# output
 # 10
 # 20						
 # 11
 # 40


 # Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# End of the function
f1()

	#output
 # 10
 # 10


 # Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()

	#output
	# 20
	# error


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
f1()
f2()

	# output
	# 40 , 50 ,60
  	# 10 , 20 ,30
	# 100 , 200 ,300

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
	global   x					# error
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
	 #output
	# 10
	# 20
	# 11
	# 30
	# 31
	# 40
	# 41
	# 32



 # Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)
f1()
print(a)
	# output
	# 10
	# 20
	# 20
	# 30



 # Find  outputs(Home  work)
def  f1():
	global  a
	print(a)					# error 
	a = 10
	print(globals()['a'])				# error
	a = 20
	print(a)					# error
	a = 30
def  f2():
	print(a)					# error
# End  of   f2   function
f1()
f2()
print(a)						# error



 # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)					# 10
	a = 20
def  f2():
	global  a
	print(a)					# 20
	a = 30
def  f3():
	print(a)					# 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)						# 40

	# output
	# 10
	# 20
	# 30
`	# 40


 # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)
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
	# output
	# 10
	# 20
	# 30
	# 40


 #  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a						# error
        print(a)						# 10
        global  b						# error
        b = 20				
# End  of  f1()  function
f1()
print(a)							# 20
print(b)							# error
	# output
	# 10
	# error
	# 20
	


 # Find outputs (Home  work)
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
	# output
	# 10
	# 11
	# 12
	# 13
	# 14



 # Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)					# 20
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a)						# 10					
f1()
a += 1
f2()							# error cannot accesslocal variable 'a' where it is not associate with a value
print(a)						# 11		

	# outputs
	# 10
	# 20
	# error 
	# 11


 # Find outputs (Home  work)
def  f1():
	a = 20
	global   a							# error
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
	# outputs
	# 10
	# 20
	# 11
	# 40


 #  Find   outputs
def   f1():
	x = x + 5							# error
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5				
	print(x)							# 15
# End of f2  function
x = 10
f1()
f2()									# error
print(x)								# error

 		# output
	# error
	# 15
	# error