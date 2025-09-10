#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
	if n >= 1:
		toh(n-1, p1, p2, p3) #How to move (n - 1) disks from pole1 to pole2  and  pole3  is  intermediate  (Use  recursion)
		print(F'{p1} ---> {p3}') #How to move disk  from pole1 to pole3
		toh(n-1, p2, p3, p1) #How to move (n - 1) disks from  pole2 to pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :'))
toh(n, 1, 2, 3)#How to move 'n' disks from pole1 to pole3 and pole2 is intermediate
'''
How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3
'''









#  Find  outputs  (Home  work)
def outer():
	x = 10
	def inner():
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
print(x) # Error because there is no x and x in function cannot be accessed outside the function
'''
Outputs
10
15
20
25
'''









#  Find  outputs  (Home  work)
def outer():
	x = 10
	def inner():
		print(x) 
		nonlocal x # Error because nonloacl keyword cannot be used already x is before nonlocal keyword
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
Outputs
10
10
20
15
'''









#  Find   outputs(Home  work)
def outer():
	x = 10
	def inner():
		global x
		x = 20
		print(x) #20
		x += 5 #25
	# End  of  inner  function
	print(x) # 10
	x += 5 # 15
	inner()
	print(x) #15
# End  of  outer  function
outer()
print(x) # 25
'''
Outputs
10
20
15
25
'''









# Find  outputs(Home  work)
def outer():
	def inner():
		nonlocal x # Error becuse to use nonlocal keyword there should be a variable in outer function with name 'x'
		x = 20
		print(x) 
	# End  of  inner  function
	inner()
	print(x) # error because there is no variable 'x' in outer function
# End  of  the  function
outer()
print(x) # Error because there is no variable x and x in inner function cannot be accessed outside the function
'''
Outputs
20
'''









# Find  outputs(Home  work)
def outer():
	def inner():
		global x
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
Outputs
20
25
25
'''









#  Identify  Error
def   f1():
        nonlocal x # Error because nonlocal keyword cannot be used in outer function it should be used in inner function and there must be a variable with same name in outer function
		








# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def inner():
		nonlocal a
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
Outputs
10 20
100 200
100 20
'''









# Find  outputs (Home  work)
def  f1():
	x = 'John'
	def f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x 
#  End  of  f1()  function
print(f1()) 
'''
Output
Hello
'''









# Find  output(Home  work)
def fun():
	x = 10
	def gun():
		x =  x  +  20 # Error because without nonlocal keyword we cannot modify x
		print(x) # prints 10 because when there is variable 'x' in fun function 
	#end of inner function
	gun()
#end of outer function
fun()
'''
Output
10
'''









#  Identify  Error
x = 10
def  outer():
	x = 20
	def inner():
		global x # Error because conflict between global and nonlocal
		nonlocal x # Error because conflict between global and nonlocal
		








#  Find  outputs  (Home   work)
def f1():
	x = 10
	def f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()
'''
Output
10
'''