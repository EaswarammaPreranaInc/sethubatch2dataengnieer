
# 1) Find  outputs  (Home  work)

def  f1():
	print('f1  function')   # f1  function
def   f2(fun):              # fun is f1
	print('f2  function')   # f2  function
	fun()                   # fun() = f1()
	print('Back  to  f2  function') # Back  to  f2  function
# end of the function
print('Begin')              # Begin
f2(f1)                                   
print('End')                # End

'''
Outputs:
Begin
f2  function
f1  function
Back  to  f2  function
End
'''



# 2) Find  outputs  (Home  work)

def  f1():
	print('f1  function')   # f1 function
def   f2 (fun):
	print('f2  function')   # f2 function
	#fun()                  # Error as 'NoneType' object is not callable  
	print('Back  to  f2  function')
# end of the function
print('Begin')              # Begin
f2(f1())                    # f1() returns None so f2(f1()) becomes f2(None)
print('End')                # end

'''
Outputs:
Begin
f1  function
f2  function
Back  to  f2  function
End
'''



# 3) Find  outputs (Home  work)

def   outer():
	print('Outer  Function')    # Outer  Function
	def  inner():
		print('Inner function') # Inner function
	return   inner
# End  of  the  function
fun = outer()                   # outer() returns inner so fun=inner
print('Hello')                  # Hello
fun()                           # fun() is inner()
print('Bye')                    # Bye
inner()                         # Error because inner function is not visible to outside the fuction

'''
Outputs:
Outer  Function
Hello
Inner function
Bye
'''



# 4) Find  outputs (Home  work)

def  outer(x):
	print('Outer  Function')                    # Outer  Function
	def  inner1():
		print('1st  inner  function')           # 1st  inner  function
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")           # 2nd  inner  function
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
Outputs:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''



# 5) Find  outputs  (Home  work)

def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')        # outer() returns inner 
hello_fun = outer('Hello')  # outer() returns inner
hi_fun()                    # msg is Hi
hello_fun()                 # msg is Hello

'''
Outputs:
Hi
Hello
'''



# 6) Find  outputs  (Home  work)

def   decor(fun): # fun is f1
	print(fun . __name__)            # f1
	def   inner():
		return   fun() +  2
	return  inner
@decor         # f1=decor(f1) returns inner --- f1=inner
def   f1():
	return  10
# End of the function
print('End')                       # End

'''
Outputs:
f1   
End
'''



# 7) How  to  call  f1()  function  when  @decor  tag  is  missing  ?

def   decor(fun):
	def   inner():
		x = fun()   # fun is f1 go to f1 funtion and it returns 10, x=10
		return   x + 2 # 10 + 2 = 12
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)      # returns inner --- f1=inner
print(f1())         # 12 

'''
Outputs:
12 
'''



# 8) Find  outputs(Home  work)

def   decor(fun):                   # f1 is wish
	print(fun . __name__)           # wish
	def    inner(name):                   
		if   name  == 'Python':
			print('Hello' , name)   # Hello Python
		else:
			fun(name)               # fun is wish
	return  inner
@decor      # wish=decor(wish) returns inner --- wish=inner
def   wish(name):
        print('Hi' , name)          # Hi Java
# End  of  the  function
wish('Python')                      
wish('Java')

'''
Outputs:
wish      
Hello Python
Hi Java
'''



# 9) Find  outputs(Home  work)

def   decor(fun):       # fun is div
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor                  # div=decor(div) returns inner --- div=inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))      # Division   by  0  is  not  permitted
print(inner(10,3))      # Error because inner function is not defined globally

'''
Outputs:
3.33
Division   by  0  is  not  permitted
'''



# 10) Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only

def decor(fun):
    def inner(x, y):  # How  to  decorate  the  function  such  that  4.5  is  returned
        if (x == 9 and y == 2) or (x == 2 and y == 9):
            return 4.5    # returns 4.5 if x,y=2,9 or 9,2
        return fun(x, y)  # fun is f1
    return inner
@decor
def div(a, b):
    return a / b
print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5     
      
'''
Outputs:
4.5
4.5	
'''	  



# 11) Find  outputs (Home  work)

def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor          # f1=decor(f1) returns inner --- f1=inner
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')

'''
Outputs:
Decorating f1 function
Hello
Decoration is finished
Bye
'''



# 12) Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures

def   decor(fun):
	print(fun . _name_)
	def   inner(*x):#  *  is  var-arg  parameter
		print(x)
		fun(*x)     #  *  unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor              # f1=decor(f1) returns inner --- f1=inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor              # f2=decor(f2) returns inner --- f2=inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor              # f3=decor(f3) returns inner --- f3=inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor              # f4=decor(f4) returns inner --- f4=inner
def   f4():
	print('f4 function')
# end of function
f1(10)                  # 1 arg
f2(25 , 10.8)           # 2 args
f3('Hyd' , True, 3+4j)  # 3 args
f4()                    # 0 args

'''
Outputs:
f1
f2
f3
f4
(10,)
f1 function : 10
End of decoration
(25, 10.8)
f2 function : 25 10.8
End of decoration
('Hyd', True, (3+4j))
f3 function : Hyd True (3+4j)
End of decoration
()
f4 function
End of decoration
'''
