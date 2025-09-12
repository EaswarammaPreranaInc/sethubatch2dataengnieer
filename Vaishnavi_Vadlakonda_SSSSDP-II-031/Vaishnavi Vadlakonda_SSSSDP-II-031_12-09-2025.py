# Find  outputs  (Home  work)
def square(fun): # fun = num
	def inner1():
		x = fun() # x = 10
		return  x * x  # 100
	return inner1 
def double(fun): # fun = inner1
	def inner2():
		y = fun() # 100
		return 2 * y # 200
	return inner2
@double # num = double(square(num)) num = double(inner1) num = inner2
@square
def num():
	return  10
#end of the function
print(num()) # print(inner2()) 
'''
Outputs
200
'''









# Find  outputs  (Home  work)
def bold(fun): # fun = inner2
	def inner1():
		return  '<b>'  +  fun()  +  '</b>'  # <b><i><u> Hello World <u><i><b>
	return inner1
def italic(fun): # fun = inner3
	def inner2():
		return  '<i>'  +  fun() +  '</i>'  # <i><u> Hello World <u><i>
	return inner2
def underline(fun): # fun = f1
	def inner3():
		return  '<u>'  +  fun()  +  '</u>' # <u> Hello World <u>
	return inner3
@bold # f1 = bold(italic(underline(f1)))   f1 = bold(italic(inner3))  f1 = bold(inner2) f1 = inner1
@italic
@underline
def f1():
       return  'Hello  World'
# End  of  the  function
print(f1()) # print(inner1())
'''
Outputs
<b><i><u> Hello World <u><i><b>
'''
