# Find  outputs  (Home  work)
def  square(fun):#   fun is  num
	def  inner1():
		x = fun()  #  Executes  function   num()  thru  ref  fun  which  returns  10  #  x =  10
		return  x * x #   100  is  returned to  function call  inner1()
	return  inner1 #  Returned  to  function  call   square(num)
def   double(fun): #  fun  is  inner1
	def  inner2():
		y = fun() #  Executes  inner1()  function  thru  ref  fun  which  returns  100
		return  2 * y  #   200  is  returned to  function call  inner2()
	return   inner2   #  Returned  to  function  call   double(inner1)
@double  #  num = double(square(num))  --->  num = double(inner1)  --->  num = inner2  i.e. Ref  num  points  to  inner2  function
@square
def  num():
	return  10 #  Returned  to function  call   fun() i.e  num()
#end of the function
print(num())  #   Executes  inner2()  function  thru  ref  num  i.e.  print(inner2())  --->  print(200)
'''
@double
@square
@double
@square
def  num():
	return  10'''



# Find  outputs  (Home  work)
def   bold(fun): #  fun  is  inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'  #  return  '<b>'  +  inner2()  +  '</b>'  --->  return  '<b>'  +  '<i><u>Hello  World</u></i>'  +  '</b>'  --->  return  '<b><i><u>Hello  World</u></i></b>'  --->   Returned  to  function  call  inner1()
	return  inner1  #  Returned  to  function  call  bold(inner2)
def   italic(fun): #  fun  is  inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'  #  return  '<i>'  +   inner3() +  '</i>' --->  return  '<i>'  +   '<u>Hello  World</u>' +  '</i>'  --->  return  '<i><u>Hello  World</u></i>'  --->  Returned  to  function  call  inner2()
	return  inner2  #  Returned  to  function  call  italic(inner3))
def   underline(fun): #  fun  is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'  #   return  '<u>'  +  f1()  +  '</u>'  --->  return  '<u>'  +  'Hello  World'  +  '</u>'  --->   return  '<u>Hello  World</u>'  --->  Returned  to  function  call  inner3()
	return  inner3 #  Returned  to  function  call  underline(f1)
@bold  #  f1 = bold(italic(underline(f1)))  --->  f1 =  bold(italic(inner3))  --->  f1 = bold(inner2)  --->  f1 = inner1  i.e.  Ref  f1  points  to  inner1() function
@italic
@underline
def   f1():
       return  'Hello  World'  #  Returned  to  function  call  f1()
# End  of  the  function
print(f1()) # Executes  inner1()  function  thru  ref  f1  i.e. print(inner1())  --->  print('<b><i><u>Hello  World</u></i></b>')  --->  <b><i><u>Hello  World</u></i></b>

