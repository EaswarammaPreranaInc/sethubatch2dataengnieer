#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')#f1 function
def   f2(fun):#fun is f1
	print('f2  function')#f2 function
	fun()#fun()=f1()
	print('Back  to  f2  function')#Back to f2 function
# end of the function
print('Begin')#Begin
f2(f1)
print('End')#end
'''
Begin
f1 function
f2 function
Back to f2 function
end
'''


#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')   # f1 function
def   f2 (fun):
	print('f2  function')   # f2 function
	#fun()                  # Error as 'NoneType' object is not callable  
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')
'''
Begin
f1 function
f2 function
Back to f2 function
End
'''

# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
# outer() returns inner so fun=inner
fun=outer
print('Hello')                  # Hell
fun()                           # fun() is inner()
print('Bye')                    # Bye
#inner()                         # Error because inner function is not visible to outside the fuction


'''
outer function
Hello
Inner function
Bye
'''


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
'''
outer unction
outer function
1st inner function
2nd inner function
'''


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
'''
Hi
Hello

'''


#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor# f1=decor(f1),f1=inner
def   f1():
	return  10
# End of the function
print('End')
'''
f1
end
'''

#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
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

# Find  outputs(Home  work)
def   decor(fun):#f1 is wish
	print(fun . __name__)#wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)#hello python
		else:
			fun(name)#fun is wish
	return  inner
@decor #wish = decor(wish),wish = inner

def    wish(name):
        print('Hi' , name)#Hi java
# End  of  the  function
wish('Python')
wish('Java')
'''
wish
Hello python
Hi Java
'''


# Find  outputs(Home  work)
def   decor(fun):#fun is div
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
print(div(10 , 3))#3.33
print(div(10 , 0))#'Division   by  0  is  not  permitted
#print(inner(10 , 3))# error inner  function is not defined



# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(x,y):#How  to  decorate  the  function  such  that  4.5  is  returned
        if(x==9 and y==2)or(x==2 and y==9):
                 return 4.5
        return fun(x, y)  # fun is f1
    return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))#4,5
print(div(2 , 9))#4.5


#  Find  outputs (Home  work)
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
Decorating f1 function
Hello
Decoration is finished
Bye

'''

#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . _name_)
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
f1  function  :   10
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration
'''




