#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')                       # f1 function
def   f2(fun):
	print('f2  function')                       # f2 function
	fun()
	print('Back  to  f2  function')             # Back to f2 function
# end of the function
print('Begin')                                  # Begin
f2(f1)
print('End')                                    # End




#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')                       # f1 function
def   f2 (fun):
	print('f2  function')                       # f2 function
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')                                  # Begin
f2(f1())
print('End')




# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')                # Outer function
	def  inner():
		print('Inner function')             # Inner function
	return   inner
# End  of  the  function
fun = outer()
print('Hello')                              # Hello
fun()
print('Bye')                                # Bye
#inner()                                     # Error inner is not defined in global




# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')                    # Outer function
	def  inner1():
		print('1st  inner  function')           # 1st inner function
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")           # 2nd inner function
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



# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()                            # Hi
hello_fun()                         # Hello



#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__)
	def   inner():
		return   fun() +  2              # 12
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')





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
print(f1())                                     # 12



# Find  outputs(Home  work)
def   decor(fun):
	print(fun . __name__)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)                   # Hello python
		else:
			fun(name)
	return  inner
@decor
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')





# Find  outputs(Home  work)
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
print(div(10 , 3))                      # 3.333
print(div(10 , 0))                      # Division by 0 is not permitted
#print(inner(10 , 3))                   # error




# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a,b):                                        # How  to  decorate  the  function  such  that  4.5  is  returned
		if (a==9 and b==2):
			return 4.5
		else:
			return fun(a,b)
	return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))




#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')        # Decorating f1 function
		fun()
		print('Decoration  is  finished')                       # Decoration is finished
	return  inner
@decor
def   f1():
	print('Hello')                                              # Hello
# End  of  the  function
f1()
print('Bye')                                                    # Bye





#  Most  tricky   program
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


#output
'''
(10,)
f1 function : 10
End of decoration
(25,10.8)
f2 function : 25 10.8
End of decoration
('Hyd',True,3+4j)
f3 function : Hyd True 3+4j
End of decoration
()
f4 function 
End of decoration
'''