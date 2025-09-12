#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')   # prints f1 function
def   f2(fun):  # here fun is f1
	print('f2  function')   # prints f2 function
	fun() # function call f1
	print('Back  to  f2  function') # prints back to f2 function
# end of the function
print('Begin')  # prints begin
f2(f1)  # calling f2 function with arg f1
print('End')  # prints end
'''
Begin
f2  function
f1  function
Back  to  f2  function
End
'''

#  Find  outputs  (Home  work)
def  f1():  # returns  none
	print('f1  function')   # prints f1 function
def   f2 (fun):     # f2(none)
	print('f2  function')   # prints f2 function
	fun()   # error as fun is none it is a object not function
	print('Back  to  f2  function')   # prints back to f2 function
# end of the function
print('Begin')  # prints begin
f2(f1())    # function call f2 with result of f1 as arg
print('End')  # prints end
'''
Begin
f1  function
f2  function
Back  to  f2  function
End
'''

# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')    # prints outer function
	def  inner():
		print('Inner function') # prints inner function
	return   inner# returns inner fun to func call
# End  of  the  function
fun = outer()   # outer func is execued and result(inner) is assigned to fun
print('Hello')  # prints hello
fun()   #inner()
print('Bye')    # prints bye
inner()     # error as inner func isn not visible to outside
'''
Outer  Function
Hello
Inner function
Bye
'''
# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')    #prints outer function
	def  inner1():
		print('1st  inner  function')  #prints 1st inner function
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")  #prints 2nd inner function
	# End  of  inner2
	if   x == 10:   # true
		return  inner1  # returnd inner1 to func call and given to f1
	else:
		return  inner2  # returns inner2 to func call and given to f2
#end of the function
f1 = outer(10)  #outer function is executed and 10 is sent and inner1 is assigned to f1
f2 = outer(20) # outer function is executed and 20 is sent and inner2 is assigned to f2
f1() # inner1()
f2() # inner2()
'''
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''

# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner   # returns inner
# End  of  the  function
hi_fun = outer('Hi')    # outer func with hi is executed
hello_fun = outer('Hello') # outer func with hello is executed
hi_fun()    # prints hi
hello_fun()    # prints hello
'''
Hi
Hello
'''

#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__)   # prints f1 as fun points to f1
	def   inner():
		return   fun() +  2
	return  inner
@decor  # f1=decor(f1) go to decor func and inner is returned so f1 =inner
def   f1():
	return  10
# End of the function
print('End')    # prints 10

#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):   # fun is f1
	def   inner():
		x = fun()   # x=10
		return   x + 2  # returns 12
	return  inner   # returns inner
def  f1():
        return  10  # returns 10
#end  of  the  function
f1 = decor(f1)  # calling decor fun with arg f1 f1=inner
print(f1()) # inner() is executed and result is printed 12 is printed

'''
decor(fun)  fun=f1
return inner to func call
f1=inner
f1()=inner()
x=fun()=f1()
x=10
return x+2=12'''

# Find  outputs(Home  work)
def   decor(fun):   # fun=wish
	print(fun . __name__) # prints wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)   
		else:
			fun(name)
	return  inner   # returns inner
@decor  # wish=decor(wish)--> wish=inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')  # inner(python)=Hello python
wish('Java')    # inner(java)=fun(java)=hi java

'''
 wish=decor(wish)--> wish=inner
 fun=wish
 returns inner
 wish=inner
 wish(python)=inner(python)=Hello python
 wish(java)=inner(java)=fun(java)=hi java
'''

# Find  outputs(Home  work)
def   decor(fun):   # fun=div(a,b)
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner   # return inner
@decor  # div(a,b)=decor(div(a,b))=inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))  # inner(10,3)=return a/b=3.33
print(div(10 , 0))  # inner(10,0)=return 'Division   by  0  is  not  permitted'
#print(inner(10 , 3)) # error as inner is not visible to outside

'''
div(a,b)=decor(div(a,b))
 fun=div(a,b)
 div(a,b))=inner
 div(10 , 3)=inner(10,3)=return a/b=3.33
 div(10 , 0)= inner(10,0)=return 'Division   by  0  is  not  permitted'
'''


# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	#How  to  decorate  the  function  such  that  4.5  is  returned
    def inner(x,y):
        return max(x,y)/min(x,y)
    return inner

@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))

#  Find  outputs (Home  work)
def   decor(fun):   # fun is f1
	def   inner():
		print(F'Decorating  {fun . __name__}  function')  # Decorating  f1  function
		fun()   # f1() is called
		print('Decoration  is  finished')  # Decoration  is  finished
	return  inner   # return inner
@decor  # f1=decor(f1)=inner()
def   f1():
	print('Hello')  # Hello
# End  of  the  function
f1()    # inner()
print('Bye')    # bye

'''
f1=decor(f1)
return inner
decor(f1)=inner()
f1()=inner()
Decorating  f1  function
fun()  f1() is called Hello
Decoration  is  finished
Bye

'''

#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)   # prints f1,f2,f3,f4
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor # f1=decor(f1)=inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor # f2=decor(f2)=inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor # f3=decor(f3)=inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor # f4=decor(f4)=inner
def   f4():
	print('f4 function')
# end of function
f1(10) # inner(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()

'''
f1=decor(f1)
f2=decor(f2)
f3=decor(f3)
f4=decor(f4)

prints f1
prints f2
prints f3
prints f4

returns inner
f1=inner
f2=inner
f3=inner
f4=inner

f1(10)
f2(25,10.8)
f3('Hyd',True,3+4j)
f4()

prints (10,)
prints f1 function 10
prints end of decoration

prints (25,10.8)
prints f2 function 25 10.8
prints end of decoration

prints ('Hyd',True,(3+4j))
prints f3 function Hyd True (3+4j)
prints end of decoration

prints ()
prints f4 function
prints end of decoration
'''





