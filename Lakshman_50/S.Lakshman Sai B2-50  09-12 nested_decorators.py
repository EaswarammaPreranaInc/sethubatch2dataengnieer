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
'''200'''

#*********************************************************

 # Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())
'''
<b><u><i>Hello World</i></u></b>
'''