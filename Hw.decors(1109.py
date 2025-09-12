1


#  Find  outputs  (Home  work)
def  f1():		# f 1 function header
	print('f1  function')	#f1  function
def   f2(fun):	# f2 function header and fun is f1
	print('f2  function') 	#f2 function
	fun()	#call the f1 function i.e. fun is f1 and stacks store s the next stmt id
	print('Back  to  f2  function')	#Back  to  f2  function'
# end of the function
print('Begin') # Begin
f2(f1)	#pass the f1 function to f2 
print('End')	#End

2

#  Find  outputs  (Homework)
def  f1():	#f1 function header
	print('f1  function')   #f1 function and returns the none
def   f2 (fun):	#here f2 function header and fun is f1 function result
	print('f2  function')	#f2  function
	#fun()       #here fun is result of the f1 function f1 function  returns the None so there no None function
	print('Back  to  f2  function')     #Back  to  f2  function
# end of the function
print('Begin')	#Begin
f2(f1())	#pass the result of f1 function to the f2 function and call the f2 function
print('End')    #End

3

#3# Find  outputs (Homework)
def   outer():
	print('Outer  Function')	#Outer function prints
	def  inner():
		print('Inner function') #inner function
	return   inner	#returns the inner to function call
# End  of  the  function
fun = outer()	# reference fun points to the outer() function # after returns the inner fun is inner
print('Hello')	#Hello
fun()	#here fun is inner so here call the inner function 
print('Bye')	#Bye
#inner()	#Error

4

# Find  outputs (Home  work)
def  outer(x):	#function header  here x is 10 	# now x is 20
	print('Outer  Function')	#Outer  Function	# again  Outer  Function prints
	def  inner1():
		print('1st  inner  function')	#1st  inner  function
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:	# checks the x is 10 yes true because x is 10 	# again checks the x is 10 or not , now condition false
		return  inner1	#returns the inner 1  to the function call 
	else:	# else part is executed 
		return  inner2	# returns the inner2 function to function call
#end of the function
f1 = outer(10)	# f1 is the outer function and call the outer function	#so  later outer function f1 is  inner1
f2 = outer(20)	# f2 is the outer function and call the outer function with x is 20 	# now here f2 is inner2 function
f1()		# call the inner1 function due to f1 is inner1  function
f2()		#call the inner1 function due to f2 is inner2 function


5

# Find  outputs  (Home  work)
def   outer(msg):	# outer function header # msg is Hi  # msg is  Hello
	def  inner():
		print(msg)	# Hi	#Hello  
	return  inner	# return the inner to the function call of outer	#  again return the inner to the function call of outer
# End  of  the  function
hi_fun = outer('Hi')	# ref hi_fun points to the outer () with actual parameter Hi # so now here hi_fun is inner 
hello_fun = outer('Hello')	#hello_fun is points the outer function with actual parameter hello  again the call the outer function
hi_fun()	# hi_fun is inner  so here we call the  inner function
hello_fun()	#again hello_fun is inner so we call the inner function again 


6

#  Find  outputs  (Home  work)
def   decor(fun):	# here fun is f1
	print(fun . _name_)	# fun._name_ means it gives the string of funcion name	#f1
	def   inner():
		return   fun() +  2	#  fun is f1 so 10+2 =12 Returns to the funcion call
	return  inner	# returns the inner to the function call
@decor	#f1 = decor(f1)	# here f1 is fun # f1 is inner  here inner is pass to the  decor
def   f1():
	return  10		
# End of the function
print('End')	# End


7



# Find  outputs(Home  work)
def   decor(fun):	# fun is wish
	print(fun . _name_)	#wish
	def    inner(name):	#here name is python	# name java
		if   name  == 'Python': 	# checks the name is python or not, so condition is true	# here condition is false
			print('Hello' , name)	# Hello python
		else:	# else part is executed 
			fun(name)	# Hi java  because here fun is wish so wish (name)
	return  inner	# returns the inner to function call
@decor	#wish =decor(wish) 	# here wish is inner
def    wish(name):
        print('Hi' , name)	#Hi java
# End  of  the  function
wish('Python')	# call the inner function here wish is inner with actual parameter python
wish('Java')	# call the inner function here wish is inner with actual parameter java


9


#  Find  outputs (Home  work)
def   decor(fun):	# here fun is f1
	def   inner():
		print(F'Decorating  {fun . _name_}  function')	#Decorating f1 function 
		fun()	#call the f1  function 
		print('Decoration  is  finished')		#Decoration  is  finished
	return  inner	# returns the inner to the function call
@decor	# f1 = decor(f1) 	#  now fun is f1  	# f1 is inner
def   f1():
	print('Hello')	# Hello
# End  of  the  function
f1()	# now call the inner function
print('Bye')	#Bye
