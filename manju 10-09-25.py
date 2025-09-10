
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)#15
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)#25
# End  of  outer  function
outer()
#print(x)#Error

#2nd program
#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)#error
		nonlocal  x
		x = 20
		print(x)#20
		x += 5#25
	# End  of  inner  function
	print(x)#10
	x += 5#15
	inner()
	print(x)#25
# End  of  outer  function
outer()

#3rd program
#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)#20
		x += 5
	# End  of  inner  function
	print(x)#10
	x += 5
	inner()
	print(x)#15
# End  of  outer  function
outer()
print(x)#25


#4th program
# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal x#error
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)


#5th program
# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)#20
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)#25
# End  of  the  function
outer()
print(x)#25


#6th program
#  Identify  Error
def   f1():
        nonlocal   x#error due to there is no outer function varieble
      

#7th program
# # Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)#100 200
	# End  of  inner  function
	print(a , b)#10 20
	inner()
	print(a , b)#100 20
#end of outer function
outer() 


#8th program
# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x#Hello
#  End  of  f1()  function
print(f1())


#9th program
# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)#Error
	#end of inner function
	gun()
#end of outer function
fun()#10


#10th program
#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x#Error 
      

#12th program
#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)#10
		f3()
	f2()
f1()