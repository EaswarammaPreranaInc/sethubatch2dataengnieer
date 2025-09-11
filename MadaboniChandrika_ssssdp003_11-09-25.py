#1st program
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function') #f1 function
def   f2(fun):
	print('f2  function') #f2 function
	fun() #control goes to line 2 as fun=f1
	print('Back  to  f2  function') #Back to f2 function
# end of the function
print('Begin') #Begin
f2(f1)
print('End')#End

'''
Begin 
f2 function
f1 function
Back to f2 function
End
'''


#2nd program
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function') #f1 function is printed and None is returned
def   f2 (fun): #fun=f1 function an returned none --->so f2(None)
	print('f2  function') #f2 function
	#fun() #error as None obj is not callable
	print('Back  to  f2  function') #Back to f2 function
# end of the function
print('Begin') #Begin
f2(f1()) #f2(f1 function)
print('End') #End

'''
Begin
f1 function
f2 function
Back to f2 function
End
'''

#3rd program
# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function') #Inner function
	return   inner
# End  of  the  function
fun = outer() #result of outer function is stored in refernce fun --->Outer function is returned
print('Hello')#Hello
fun() #Inner function
print('Bye') #Bye
#inner() #Error , inner function is hidden and cannot be directly called


#4th program
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
f1 = outer(10) #outer function
f2 = outer(20) #outer function
f1()#1st inner function
f2()#2nd inner function


#5th program
# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun() #Hi
hello_fun() #Hello


#6th program
#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__) #f1
	def   inner():
		return   fun() +  2
	return  inner
@decor #f1=decor(f1)
def   f1():
	return  10
# End of the function
print('End') #End


#7th program
#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun() #x=20
		return   x + 2 #10+2
	return  inner #12
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) 
print(f1()) #12


#8th program
# Find  outputs(Home  work)
def   decor(fun):
	print(fun . _name_) #wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor #wish=decor(wish) -->wish=inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python') #Hello Python
wish('Java') #Hi Java


#9th program
# Find  outputs(Home  work)
def   decor(fun):#fun=div
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor #div=decor(div) -->inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) #3.3333333
print(div(10 , 0)) #Division by 0 is not permitted
#print(inner(10 , 3)) #error,the inner cannot be directly called as it is in hidden state


#10th program
# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
    def inner(a,b):
        if a < b:
            return b/a
        return a/b
    return inner
	#How  to  decorate  the  function  such  that  4.5  is  returned
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2))
print(div(2 , 9))


#11th program
#  Find  outputs (Home  work)
def   decor(fun): #fun=f1
	def   inner():
		print(F'Decorating  {fun . _name_}  function') #Decorating f1 function
		fun() #None is returned
		print('Decoration  is  finished') #Decoration is finished
	return  inner
@decor #f1=decor(f1) -->inner
def   f1():
	print('Hello') #Hello is printed
# End  of  the  function
f1()
print('Bye') #Bye


#12th program
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