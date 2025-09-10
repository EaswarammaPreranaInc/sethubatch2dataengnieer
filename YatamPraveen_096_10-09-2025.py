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
outer()                                 #10<next_line>15<next_line>20<next_line>25
print(x)                                #Throws error as x is not available outside the outer function





#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		print(x)
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
outer()                                     #Throws error. We are using nonlocal, so x can't be used prior to nonlocal declaration





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
outer()                                 #10<>20<>15
print(x)                                #25





# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x               #Throws error as x is not present in outer()
		x = 20
		print(x)
	# End of inner function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)                            #Throws error as x is not present outside function





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
outer()                                 #20<>25
print(x)                                #25





#  Identify  Error
def   f1():
        nonlocal x                	#nonlocal can be used only in inner functions not outer





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
outer()                                     #10 20<next_line>100 200<next_line>100 20





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
print(f1())                             #Hello





# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20                        #Throws error as x is undefined since we aren't using nonlocal
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()





#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x                     #x can't be considered as global and non local both at the same time





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
f1()                                    #10