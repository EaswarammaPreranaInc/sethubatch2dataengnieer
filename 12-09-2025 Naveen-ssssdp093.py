# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x               # 100
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y               # 200
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())





# Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'              # adds bold tag to the result from fun()
	return  inner1                                      # returns the function inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'               # adds italic tag to the result from fun()
	return  inner2                                      # returns the function inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'              # adds underline tag to the result from fun()
	return  inner3                                      # returns the function inner 3
@bold
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())                                             # executes the decorator function




#output
'''
<b><i><u>Hello world</u></i></b>
'''