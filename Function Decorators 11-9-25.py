#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor # f1 = decor(f1)
def   f1():
	return  10
# End of the function
print('End')

'''
f1
End
'''


#  How  to  call  f1()  function  when  @decor  tag  is  missing  ? ---> decor(f1)
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) 
print(f1()) # 12



# Find  outputs(Home  work)
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
Wish
Hello Python
Hi Java
'''


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
print(div(10 , 3)) # 3.333
print(div(10 , 0)) # Division   by  0  is  not  permitted
print(inner(10 , 3)) # Error as inner function is not visible to outside


# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	# How  to  decorate  the  function  such  that  4.5  is  returned
	def  innner(x , y):  
			if  x > y:
				return   fun(x , y)  
			else:
				return   fun(y , x)
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) # 4.5
print(div(2 , 9)) # 4.5

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
f3('Hyd' ,  True  , 3 + 4j)
f4()

'''
f1 
f2 
f3 
f4 
(10,) 
f1  function  : 10 
End  of  decoration
(25 , 10.8) 
f2  function  : 25  <space> 10.8 
End  of  decoration
('Hyd' ,  True  , 3 + 4j) 
f3  function  :   Hyd  <space> True   <space>  3 + 4j
End  of  decoration
() 
f4  function  : 
End  of  decoration
'''




