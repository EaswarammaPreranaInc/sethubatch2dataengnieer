#  Find  outputs  (Home  work)
def  f1(): #Here f1() is defined 
	print('f1  function') 
def   f2(fun): #fun is f1 function
	print('f2  function') #Prints the f2 function
	fun() #f1 function #Prints the f1 function
	print('Back  to  f2  function') #Print the Back to f2 function
# end of the function
print('Begin') #Print Begin
f2(f1) #Here we are passing the f1 function to f2 function
print('End') #Prints End

'''outputs:
Begin
f2 function
f1 function
Back to f2 function
End'''




#  Find  outputs  (Home  work)
def  f1(): #Here f1 function is defined
	print('f1  function') #Prints the f1 function
def   f2 (fun): #Here fun is f1 function
	print('f2  function') #Prints the f2 function
	#fun() #Error #As we are passing the result of f1 function so error
	print('Back  to  f2  function') #Prints Back to f2 function
# end of the function
print('Begin') #Prints Begin
f2(f1()) #Here we are passing the result of f1 function to f2 function
print('End') #Prints End
'''outputs:
Begin
f1 function 
f2 function
Error
Back to f2 function
End'''



# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer() #Here ref fun is pointing to function call outer()
print('Hello') #Prints Hello
fun() #Outer() is called using fun ref #Outer function
                                       #Inner function
print('Bye') #
#inner() #Error #undefined inner function as we cannot call inner function of another function outside the outer function



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
f1 = outer(10) #Here ref f1 points to outer function call
f2 = outer(20) #Here f2 points to outer function call
f1()
f2()

'''outputs:
Outer Function
Outer Function
1st inner function
2nd inner function
'''



# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') #Here ref hi_fun points to outer function call with argument Hi
hello_fun = outer('Hello') #Here ref hello_fun points to outer function call with argument Hello
hi_fun() #Hi
hello_fun() #Hello




#  Find  outputs  (Home  work)
def   decor(fun): #Here fun is f1 function
	print(fun . __name__) #Prints the function name f1
	def   inner():
		return   fun() +  2 #f1 + 2 is returned
	return  inner
@decor 
def   f1():
	return  10
# End of the function
print('End') #Prints End
'''outputs:
f1
End
'''




#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): #Here fun is f1 function
	def   inner():
		x = fun() #X points to f1 function call
		return   x + 2 # 10 + 2 i.e 12
	return  inner
def  f1():
        return  10 #initially the f1 function is returned 10 but we are modified 10+2 which is 12
#end  of  the  function
f1 = decor(f1) #Here it can be assumed as @decor
print(f1()) #10 + 2 i.e 12



# Find  outputs(Home  work)
def   decor(fun): #Here fun is wish function
	print(fun . __name__) #Prints wish
	def    inner(name): #Argument of wish function
		if   name  == 'Python':
			print('Hello' , name) 
		else:
			fun(name) #calling the wish function i.e Hi Java 
	return  inner
@decor
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')
'''outputs:
wish
Hello python
Hi Java
'''


# Find  outputs(Home  work)
def   decor(fun): #Here fun is div function
	def  inner(x , y): #10 3
		try:
			return  fun(x , y) #Result of 10 / 3 i.e 3.33
		except:
			return 'Division   by  0  is  not  permitted'
	return  inner
@decor #Here we are modifying the features of div function with disturbing the div function
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10 , 3)) #Error #we cannot call inner function of another function

'''outputs:
3.33
Division by 0 is not permitted'''



# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(x,y):
     return fun(max(x,y),min(x,y))
    return inner
    #How  to  decorate  the  function  such  that  4.5  is  returned
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))

'''outputs:
4.5
4.5
'''




#  Find  outputs (Home  work)
def   decor(fun): #Here fun is f1 function
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun() #Here we are calling the f1 function
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')

'''outputs:
Decorating the f1 function
Hello
Decoration is finished
Bye'''


# Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun): #f1 
	print(fun . __name__) #f1
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x) #(10,)
		fun(*x)  #  *  unpacks  object  'x' #10
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

'''outputs:
f1
f2
f3
f4
(10,)
f1  function  :   10
End  of  decoration
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