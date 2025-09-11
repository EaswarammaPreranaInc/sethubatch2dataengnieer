#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun): # fun = f1
	print('f2  function') # f2 function
	fun() # f1 function
	print('Back  to  f2  function') # Back to f2 function
# end of the function
print('Begin') # Begin
f2(f1) # f1 fun is pass to f2 fun
print('End') # End


#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun): # None
	print('f2  function') # f2 Function
	fun() # error
	print('Back  to  f2  function') # Back to f2 function
# end of the function
print('Begin') # Begin
f2(f1()) # result of f1 fun pass to f2
print('End')


# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer() # ref is assign to result of outer fun
print('Hello') # Hello
fun() # Inner Function
print('Bye') # Bye
inner() # error


# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function') # Outer Function
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1 # 
	else:
		return  inner2
#end of the function
f1 = outer(10) # return inner1 fun
f2 = outer(20) # return inner2
f1() # 1st inner fun
f2() # 2nd innner fun


# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') # Hi
hello_fun = outer('Hello') # Hello
hi_fun() # hi
hello_fun() # hello


#  Find  outputs  (Home  work)
def   decor(fun): #fun = f1
	print(fun . __name__) # f1
	def   inner():
		return   fun() +  2 # 10 + 2
	return  inner
@decor # decor = decor(f1) # decor = inner 
def   f1():
	return  10
# End of the function
print('End') # End


#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) # f1 fun is passed to decor
print(f1()) # 12


# Find  outputs(Home  work)
def   decor(fun): # fun = wish
	print(fun . __name__) # wish
	def    inner(name): 
		if   name  == 'Python':
			print('Hello' , name) # Hello Python
		else:
			fun(name)
	return  inner # inner  function  object
@decor # wish = decor(wish) # wish = inner
def    wish(name):
        print('Hi' , name) # Hi  Java
# End  of  the  function
wish('Python')
wish('Java')


# Find  outputs(Home  work)
def   decor(fun): # fun = div
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor # div = decor(div) 
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) # 3.3333333333333335
print(div(10 , 0)) # Division   by  0  is  not  permitted
#print(inner(10 , 3)) # error


# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(x , y):
		if x > y:
			return fun(x , y)
		else:
			return fun(y , x)	
	return inner # How  to  decorate  the  function  such  that  4.5  is  returned
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) # 4.5
print(div(2 , 9)) # 4.5


#  Find  outputs (Home  work)
def   decor(fun): # fun = f1
	def   inner():
		print(F'Decorating  {fun . _name_}  function') # Decorating f1 function
		fun() # Hello
		print('Decoration  is  finished') # Decoration is finished
	return  inner
@decor # f1 = decor(f1)
def   f1():
	print('Hello')
# End  of  the  function
f1() # Decorating f1 function  Hello  Decoration is finished
print('Bye') # Bye


#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun): # fun = f1
	print(fun . __name__) # f1
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x) # (10,) # (25 , 10.8) # ('Hyd' ,  True  , 3 + 4j) # ()  
		fun(*x)  #  *  unpacks  object  'x'
		print('End  of  decoration') # End  of  decoration
	return  inner
@decor # decorates  f1
def   f1(x):
	print('f1  function  :  ' , x)
@decor # decorates  f2
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor # decorates  f3
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor # decorates  f4
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()