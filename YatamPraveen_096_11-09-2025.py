#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back to f2 function')
# end of the function
print('Begin')                          #Begin
f2(f1)                                  #f2 function<next_line>f1 function<next_line>Back to f2 function
print('End')                            #End





#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()
	print('Back to f2 function')
# end of the function
print('Begin')                          #Begin
f2(f1())                                #f1 functon<next_line>f2 function<next_line>Throws error as f2 tries to call None as None is its argument
print('End')                            #End





# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')                          #Hello
fun()                                   #Throws error as this implies None()
print('Bye')                            #Bye
inner()                                 #Throws error as inner can't be accessed directly outside outer()





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
f1 = outer(10)                              #Outer function
f2 = outer(20)                              #Outer function
f1()                                        #1st inner function
f2()                                        #2nd inner function





# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()                                #Hi
hello_fun()                             #Hello





#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun .__name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor                              #f1
def   f1():
	return  10
# End of the function
print('End')                        #End





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
print(f1())                             #12





# Find  outputs(Home  work)
def   decor(fun):
	print(fun .__name__)
	def    inner(name):
		if   name  == 'Python':
			print('Hello', name)
		else:
			fun(name)
	return  inner
@decor                                          #wish
def    wish(name):
        print('Hi', name)
# End  of  the  function
wish('Python')                                  #Hello Python
wish('Java')                                    #Hi Java





# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return  'Division by 0 is not permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10, 3))                                   #3.33
print(div(10, 0))                                   #Division by 0 is not permitted
print(inner(10, 3))                                 #Error as inner can't be accessed directly outside decor()





# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	#How  to  decorate  the  function  such  that  4.5  is  returned
    def inner(a, b):
        if a>b:
            return a/b
        return b/a 
    return inner
	
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))





#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun .__name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()                                    #Decorating f1 function<next_line>Hello<next_line>Decoration  is  finished
print('Bye')                            #Bye





#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun .__name__)
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x'
		print('End of decoration')
	return  inner
@decor                                              #f1
def   f1(x):
	print('f1  function  :  ' , x)
	
	
@decor                                              #f2
def   f2(x , y):
	print('f2  function  :  ' , x , y )
	
	
@decor                                              #f3
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
	
	
@decor                                              #f4
def   f4():
	print('f4 function')
# end of function
f1(10)                                  #(10,)<next_line>f1 function : 10<next_line>End of decoration
f2(25 , 10.8)                           #(25, 10.8)<next_line>f2 function : 25 10.8<next_line>End of decoration
f3('Hyd', True, 3 + 4j)                 #('Hyd', True, 3+4j)<next_line>f3 function : Hyd True 3+4j<next_line>End of decoration
f4()                                    #()<next_line>f4 function<next_line>End of decoration
