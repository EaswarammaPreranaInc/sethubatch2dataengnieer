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
'''
Begin
f2 function
f1 function
Back  to  f2  function
End
'''

#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun() #Error
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')
'''
Begin
f1 function
f2  function
Error
Back  to  f2  function
End
'''

# Find  outputs (Home  work)
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
Outer  Function
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
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''

# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') #hi_fun=inner
hello_fun = outer('Hello') #hello_fun=inner
hi_fun() #inner() #Hi
hello_fun() #inner() #Hello
'''
Hi
Hello
'''

#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . name) #f1
	def   inner():
		return   fun() +  2
	return  inner
@decor #f1=decor(f1)--> f1=inner
def   f1():
	return  10
# End of the function
print('End')
'''
f1
End
'''

#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): #fun is f1
	def   inner():
		x = fun() #f1()--> x=10
		return   x + 2 #12
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) #f1=inner
print(f1()) 
'''
12
'''

# Find  outputs(Home  work)
def   decor(fun): #fun is wish
	print(fun . name) #wish
	def    inner(name): #inner('Python')
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor #wish=decor(wish)-->wish=inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python') #inner('Python')
wish('Java') #inner('Java')
'''
wish
'Hello' , Python
'Hi',Java
'''

# Find  outputs(Home  work)
def   decor(fun): #fun is div
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor #div=decor(div)-->div=inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) #inner(10,3)
print(div(10 , 0))
print(inner(10 , 3)) #Error
'''
3.333
Division   by  0  is  not  permitted
Error
'''

# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(x,y):
        if x>y:
            return fun(x,y)
        else:
            return fun(y,x)
    return inner
	#How  to  decorate  the  function  such  that  4.5  is  returned
 
@decor #div=decor(div)
def  div(a , b):
    return   a /b
print(div(9 , 2)) #4.5
print(div(2 , 9)) #4.5

#  Find  outputs (Home  work)
def   decor(fun): #fun is f1
	def   inner():
		print(F'Decorating  {fun . name}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor #f1=decor(f1) --> f1=inner
def   f1():
	print('Hello')
# End  of  the  function
f1() #inner()
print('Bye')
'''
Decorating  f1  function
Hello
Decoration  is  finished
Bye
'''

#  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun): #fun is f1
	print(fun . name) 
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x' 
		print('End  of  decoration')
	return  inner
@decor #f1=decor(f1)-->f1=inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor #f2=decor(f2)-->f2=inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor #f3=decor(f3)-->f3=inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor #f4=decor(f4)-->f4=inner
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()
'''
f1
f2
f3
f4
(10,)
f1  function  :   10
End of Decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd' ,  True  , 3 + 4j)
f3 function :  Hyd  True  3+4j
End of Decoration
()
f4 function
End  of  decoration
'''