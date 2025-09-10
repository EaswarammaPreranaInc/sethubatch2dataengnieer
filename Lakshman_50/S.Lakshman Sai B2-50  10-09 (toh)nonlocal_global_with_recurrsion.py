
def toh(n, p1, p2, p3):
    if n == 1:
        print(f'{p1} ---> {p3}')
    else:
        # Move (n-1) disks from pole1 to pole2 using pole3 as intermediate
        toh(n-1, p1, p3, p2)
        # Move the nth disk from pole1 to pole3
        print(f'{p1} ---> {p3}')
        # Move (n-1) disks from pole2 to pole3 using pole1 as intermediate
        toh(n-1, p2, p1, p3)
n = int(input('How many disks? : '))
toh(n, 1, 2, 3)

# How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
# How many disks ? : 3
# 1   --->  3
# 1   --->  2
# 3   --->  2
# 1   --->  3
# 2   --->  1
# 2   --->  3
# 1   --->  3

#*************************************** #  Find  outputs  (Home  work)

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
print(x)  #error
'''
10
15
20
25
'''

#*************************************** #  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		# print(x)
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
10
20
25

'''

#*************************************** #  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global  x
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

#*************************************** # Find  outputs(Home  work)
def  outer():
	def  inner():
		nonlocal  x #Error becoz there is no local variable
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
'''
error
20
Error
Error
'''

#*************************************** # Find  outputs(Home  work)
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

#*************************************** #  Identify  Error
def   f1():
        nonlocal   x
'''
there is no local variable
'''

#*************************************** # Find  outputs (Home  work)
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
(10,20)
(100,200)
(100,20)
'''

#*************************************** # Find  outputs (Home  work)
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
Hello
'''

#*************************************** # Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
'''
Error becoz in gun() x is not declared
'''

#*************************************** #  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		nonlocal  x

'''
Error
'''
#****************************** #  Find  outputs  (Home   work)
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