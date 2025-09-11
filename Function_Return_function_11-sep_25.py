# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()
print('Bye')
inner()

Output :
Outer  Function
Hello
Inner function
Bye

# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1
	else:
		return  inner2
#end of the function
f1 = outer(10)
f2 = outer(20)
f1()
f2()

Output :
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function

# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

Output :
Hi
Hello
