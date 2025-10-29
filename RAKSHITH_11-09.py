
#  Find  outputs  (Home  work)
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

output:-
Begin
f2 function 
f1 function
Back to f2 function
End



#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun): #fun is pointing to None
	print('f2  function')   # f2 function
	#fun()   # None object is not callable
	print('Back  to  f2  function') # Back to f2 function
# end of the function
print('Begin')  # Begin
f2(f1())        # f1 function
print('End')    # End



# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()   # Outer Function   # fun pointing to inner() function
print('Hello')  # Hello
fun()   # Inner function
print('Bye')    #Bye
inner() # Error inner is not defined


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
f1 = outer(10)  # Outer Function    reference f1 points to inner1()  function
f2 = outer(20)  # Outer Function    reference f2 points to inner2()  function
f1()    # 1st inner function
f2()    # 2nd inner function


# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')    # reference hi_fun pointing to inner() function
hello_fun = outer('Hello')  # reference hello_fun pointing to inner() function
hi_fun()    # Hi
hello_fun() # Hello


#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__) 
	def   inner():
		return   fun() +  2
	return  inner
@decor  # f1=decor(f1)
def   f1():
	return  10
# End of the function
print('End')    

output:-
f1
End

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

output:-
12



# Find  outputs(Home  work)
def   decor(fun):
	print(fun . __name__)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor  # wish=decor(wish)     wish is pointing to inner() function
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')

output:-
wish
Hello Python
Java



# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor  # div=decor(div)      div is pointing to inner() function
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
print(inner(10 , 3))

output:-
3.333333333333
Division by 0 is not permitted
Error inner object is not defined 



# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(a,b):
        if a<b:
            return fun(b,a)
        return fun(a,b)
    return inner
@decor  # div=decor(div)
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))


output:-
4.5
4.5


#  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor  # f1=decor(f1)
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')


output:-
Decorating  f1  function
Hello
Decoration  is  finished
Bye



#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor  # f1=decor(f1)
def   f1(x):
	print('f1  function  :  ' , x)
@decor  # f2=decor(f2)
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor  # f3=decor(f3)
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor  # f4=decor(f4)
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()


output:-
f1
f2
f3
f4
(10,)
f1 function : 10
End  of  decoration
(25,10.8)
f2 function : 25 10.8
End  of  decoration
(Hyd,True,3+4j)
f3 function : Hyd True 3+4j
End  of  decoration
() 
f4 function
End  of  decoration

