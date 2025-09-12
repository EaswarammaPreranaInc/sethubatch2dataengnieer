# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())
'''
200
'''


# Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):                          #fun is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold                                         #f1 = inner 1
@italic                                       #f1 = inner2
@underline                                    #f1 = inner3
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())
'''
OUTPUT:
<b><i><u>Hello  World</u></i></b>
'''