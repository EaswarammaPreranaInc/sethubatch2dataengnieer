# Towers of Hanoi
def toh(n, p1, p2, p3):
    if n == 1:
        print(f"{p1}   --->  {p3}") # 
    else:
        toh(n-1, p1, p3, p2)    # How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
        print(f"{p1}   --->  {p3}")  # How  to  move  disk  from  pole1  to  pole3
        toh(n-1, p2, p1, p3)    # How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
n = int(input("How many disks ? : "))
toh(n, 1, 2, 3) # How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate


#  Find  outputs  (Home  work)
def  outer():
	x = 10  # local x is defined with value 10
	def  inner():
		nonlocal  x # treat x as variable of outer function
		print(x)    # prints 15
		x = 20  # x is modified to 20
		print(x)    # prints 20
		x += 5  # x is modified to 25
	# End  of  inner  function
	print(x)    # prints 10
	x += 5  # x is modified to 15
	inner() # inner func is called
	print(x)    # prints 25
	# End  of  outer  function
outer()     # calling outer function
print(x)    # error as there is no global variable

#  Find  outputs  (Home  work)
def  outer():
	x = 10  # local x of outer func is 10
	def  inner():
		print(x)    # prints 15
		nonlocal  x     # treates x as non local
		x = 20  # x is modified to 20
		print(x)    # prints 20
		x += 5  # x is modified to 25
	# End  of  inner  function
	print(x)    # prints 10
	x += 5  # x is modified to 15
	inner() # calls inner func
	print(x)    # prints 25
# End  of  outer  function
outer() # outer func is called

#  Find   outputs(Home  work)
def  outer():
	x = 10  # x is local variable with 10
	def  inner():
		global   x  # treat x as global variable
		x = 20  # x is created to 20 as global
		print(x)  # prints 20
		x += 5  # x is modified to 25
	# End  of  inner  function
	print(x)    # prints 10
	x += 5  # outer variable is modified to 15
	inner() # inner func is called
	print(x)# prints 15
# End  of  outer  function
outer() # calls outer func
print(x) # prints 25

# Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x # for a non local keyword there should be a local variable in outer func so error
		x = 20  # x is crerated as local variable
		print(x)    # prints 20
	# End  of  inner  function
	inner() # inner func is called
	print(x) # error as there is no x in outer func
# End  of  the  function
outer() # outer func is called
print(x)    # errorr as no global x

# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x  # treat x as global 
		x = 20  # as there is no existing x create a new gv x =20
		print(x) #prints 20
		x = x + 5   # x is modified to 25
	# End  of  inner  function
	inner() # inner func is called
	print(x)    # prints 25
# End  of  the  function
outer() # outer func is called
print(x)    # prints 25


#  Identify  Error
def   f1():
        nonlocal   x    # non local should always be in inner function

# Find  outputs (Home  work)
def  outer():
	a = 10  # local a of outer func is 10
	b = 20  # local b of outer func is 20
	def   inner():
		nonlocal   a    # treat a as outer func variable
		a = 100 # a is modified to 100
		b = 200 # new local variable b is created
		print(a , b) # prints 100 200
	# End  of  inner  function
	print(a , b) # prints 10 20
	inner() # inner func is called
	print(a , b) # prints 100 20
#end of outer function
outer() # outer func is called
print(a , b)    # error as a and b are not gv

# Find  outputs (Home  work)
def   f1():
	x = 'John'  # local variable of outer func
	def  f2():
		nonlocal  x # treat x as lv of outer func
		x =  'Hello'    # x is modified to hello
	#end of inner function
	f2()   # f2 is called
	return  x   # returns hello
#  End  of  f1()  function
print(f1()) # f1 func is calleed and prints hello

# Find  output(Home  work)
def  fun():
	x =  10   # lv of fun func
	def    gun():
		x =  x +  20    # error as ther is no lv x
		print(x)    # prints 10
	#end of inner function
	gun() # gun func is called
#end of outer function
fun()   # fun function is called

#  Identify  Error
x = 10  # gv x is 10
def   outer():
	x = 20  # lv of outer func
	def  inner():
		global   x  # here x is treated as gv
		nonlocal  x # x is already gv so error

#  Find  outputs  (Home   work)
def   f1():
	x = 10  # non local x is 10 
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x    # treats x as non local
			print(x)    # prints 10
		f3()    # f3 func is called
	f2()
f1()    # f1 func is called

