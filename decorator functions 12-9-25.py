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
@double # num = double(inner1) ---> 
@square
def  num():
	return  10
#end of the function
print(num()) # 200


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
@bold # f1 = blod(italic(underline(f1))) ---> f1 = bold(italic(inner3)) ---> f1 = bold(inner2) ---> f1 = inner1
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1()) # <b><i><u>Hello World</u></i></b>
