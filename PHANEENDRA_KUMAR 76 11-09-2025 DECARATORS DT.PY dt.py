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
back to f2 function 
end




#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()----> error
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')


output:

Begin
f1 function 
f2 function
print back to f2 function
end



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
inner()-----> error

output:-
outer function
hello
inner function
bye




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

ouput:-
outer function
outer function
1st inner function
2nd inner function





# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

output:-
hi
hello

#  Find  outputs  (Home  work)
def   decor(fun):
	print(fun . name)
	def   inner():
		return   fun() +  2
	return  inner
@decor f1=decor(f1)    f1=inner
def   f1():
	return  10
# End of the function
print('End')

output:-
f1
end

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

output:
12




# Find  outputs(Home  work)
def   decor(fun):
	print(fun . name)
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)
	return  inner
@decor---->wish=decor(wish)-->inner
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')
wish('Java')

output:-
wish
hello python
hi java



 # Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor       div=decor(div) ---->inner
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
print(inner(10 , 3))

output:-
3.33
Division   by  0  is  not  permitted
error


# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a ,b):
		if b>a:
			return fun(a,b)
		else:
			return fun(b,a)

@decor     div=decor(div)   
def  div(a , b):
    return   a /b
print(div(9 , 2))--->4.5
print(div(2 , 9))--->4.5




 #  Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . name}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')


output:-

decoratinf f1 function
hello
decoration is finished
bye


 #  Most  tricky   program
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . name)
	def   inner(*x):  #   *  is  var-arg  parameter
		print(x)
		fun(*x)  #  *  unpacks  object  'x'
		print('End  of  decoration')
	return  inner
@decor   f1=decor(f1)--->inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor  f2=decor(f2)---->inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor f3=decor(f3)--->inner
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor f4=decor(f4)---->inner
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
f1  function : 10 
end of decoration
(25 , 10.8)
f2  function :  25 10.8
end of decoration
('Hyd' ,  True  , 3 + 4j)
f3 function : hyd true 3+4j
end of decoration
()
f4 function
end of decoration
