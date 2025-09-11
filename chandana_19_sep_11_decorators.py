# find outputs
def decor(fun):
     print(fun.__name__)
     def inner():
          return fun()+2
     return inner

@decor # f1 =decor(f1) --> f1 =inner
def f1():
     return 10
# enf of the function
print('End')
'''
f1
End
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
o/p:
12
'''

# Find  outputs
def   decor(fun):
	print(fun . _name_)
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
o/p:
wish
Hello python
Hi Java
'''

# Find  outputs
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
#print(inner(10 , 3)) # error: inner function defined only inside decor. It is not accessible outside.
'''
o/p:
3.33
Division bt 0 is not permitted
'''


# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner
    
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))
'''
o/p:
4.5
4.5
'''


#  Find  outputs 
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
o/p:
Decorating  f1  function
Hello
Decoration  is  finished
Bye'''


# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  # * is var-arg parameter
		print(x)
		fun(*x) # * unpacks object 'x'
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
o/p:
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