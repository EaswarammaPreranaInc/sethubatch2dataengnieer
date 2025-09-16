# Find  outputs  (Home  work)
def  square(fun):
	def  inner1(): # fun is num
		x = fun() # 10
		return  x * x
	return  inner1
def   double(fun): # fun is inner1
	def  inner2():
		y = fun() # fun is inner1() --> x*x --> 100
		return  2 * y # 200
	return   inner2
@double  # num=double(square(num))  --> double(inner1)  --->num=inner2
@square  # num=square(num)
def  num():
	return  10
#end of the function
print(num()) # 200



# Find  outputs  (Home  work)
def   bold(fun): # fun is inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun): #  fun is inner3 
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun): # f1 is fun
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold # f1=bold(itlic(underline(f1)))  -->underline(f1)--->inner3   ----> italic(inner3) --->  inner2 ---> bold(inner2) --->  f1= inner1 -->f1=inner1()
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1()) # <b><i><u>Hello  World</u></i></b>