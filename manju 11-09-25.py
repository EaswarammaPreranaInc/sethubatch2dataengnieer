#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')#f2 function
	fun()#f1 function
	print('Back  to  f2  function')#Back to f2 function 
# end of the function
print('Begin')#Begin
f2(f1)
print('End')#End
 

#second program
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')#f1 function
def   f2 (fun):
	print('f2  function')#f2 function 
	#fun()#Error None type object is not callable
	print('Back  to  f2  function')#Back to f2 function 
# end of the function
print('Begin')#Begin
f2(f1())
print('End')#End


#3rd program
# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')#Outer function 
	def  inner():
		print('Inner function')#Inner function
	return   inner
# End  of  the  function
fun = outer()
print('Hello')#Hello
fun()
print('Bye')#Bye
#inner()


#4th program
# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
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

'''#op
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function'''

#5th program
# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)#Hi  Hello
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

