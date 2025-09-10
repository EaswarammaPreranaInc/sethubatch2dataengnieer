#  Find  outputs
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
#print(x) # error : No 'x' is  defined  globally
'''
o/p:
10
15
20
25
'''


#  Find  outputs 
def  outer():
	x = 10
	def  inner():
		#print(x) # error :  cannot use 'x' before declaring it nonlocal
		nonlocal  x
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
o/p:
10
20
25
'''


#  Find   outputs
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
25'''


# Find  outputs
def  outer():
	def  inner():
		#nonlocal  x : error : no variable 'x' in outer
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	#print(x) # error : 'x' is not defined
# End  of  the  function
outer()
#print(x) # error : 'x' is not defined
'''
o/p:
20
'''


# Find  outputs
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
o/p:
20
25
25
'''


#  Identify  Error
def   f1():
        #nonlocal   x # error : f1() is not nested inside another function
		pass


# Find  outputs 
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
10 20
100 200
100 20
'''


# Find  outputs 
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())
'''
o/p:
Hello
'''


# Find  output
def  fun():
	x = 10
	def    gun():
		#x =  x +  20 # error : cannot modify the value without nonlocal
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
'''
o/p:
10'''


#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		#global   x  #  error :python doesn't allow both global and nonlocal declaration for the same variable in the same scope
		#nonlocal  x
		pass
	

#  Find  outputs  
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
o/p:
10'''