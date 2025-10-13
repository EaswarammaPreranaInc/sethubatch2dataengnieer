
#***************************************** #  Find  outputs  (Home  work)

def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')
'''
Begin
f2 function
f1 function
Back to f2 function
End
'''

#***************************************** #  Find  outputs  (Home  work)

def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')
'''
Begin
f1 function
f2 function
Error
'''

#***************************************** # Find  outputs (Home  work)

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
inner() #Error
'''
outer function
Hello
inner function
Bye
error
'''
#***************************************** # Find  outputs (Home  work)

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
'''
Ourt function
outer function
1st inner function
2nd inner function
'''
#***************************************** # Find  outputs  (Home  work)

def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
'''
Hi
Hello
'''

#***************************************** #  Find  outputs  (Home  work)

def   decor(fun):
	print(fun . __name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')
'''
f1
12
End
'''

#***************************************** #  How  to  call  f1()  function  when  @decor  tag  is  missing  ?

def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)
print(f1())
'''
12
'''

#***************************************** # Find  outputs(Home  work)

def   decor(fun):
	print(fun . __name__)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')
'''
wish
Hello Python
Hi Java
'''
#***************************************** # Find  outputs(Home  work)

def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
# print(inner(10 , 3))
'''
3.333333
Division by 0 is not prenitted
'''
#***************************************** # Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only

def  decor(fun):
	def inner(x,y):
		if x>y:
			return fun(x,y)
		else:
			return fun(y,x)
	return inner
	# How  to  decorate  the  function  such  that  4.5  is  returned
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))
'''
4.5
4.5
'''

#***************************************** #  Find  outputs (Home  work)

def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')
'''
Decoating f1 function
Hello
Decoration is finished
Bye
'''

#***************************************** #  Most  tricky   program

# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x)
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()
'''
f1
(10,)
f1 function: 10
End of decoration
f2
(25,10.58)
f2 function: 25,10.8
End of decoration
f3
(Hyd,True,3+4j)
f3 function: Hyd,True,3+4j
End of decoration
f4
()
f4 function
End of decoration
'''