#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x) # Error as there is no global variable x

'''
10
15
20
25
'''

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
		nonlocal  x # error as nonlocal is used after declaration of x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()

'''
10
'''

#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)

'''
10
20
15
25
'''

# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x # error as there no variable x in the outer function 
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)



# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)

'''
20
25
25
'''

#  Identify  Error
def   f1():
        nonlocal   x # Error as non local should be inside the inner function not outer function


# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)
	# End  of  inner  function
	print(a , b)
	inner()
	print(a , b)
#end of outer function
outer()

'''
10 <space> 20
100 <space> 200
100 <space> 20
'''

# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1()) # Hello 


# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20 # error as there is no x in inner function
		print(x)
	#end of inner function
	gun()
#end of outer function
fun() 


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x # error as there is contradiction 
		nonlocal  x # error as there is contradiction



#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()

'''
10
'''
