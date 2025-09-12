# Find  outputs  (Home  work)
def  square(fun):   # fun is num
	def  inner1():
		x = fun()
		return  x * x
	return  inner1  # return inner1
def   double(fun):  # fun is inner1
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2 # return inner2
@double # double=double(square)=double(square(num))
@square #square=sqaure(num)
def  num():
	return  10
#end of the function
print(num())

'''
num=double(square(num))
square(num)
return inner1
double(square(num))=double(inner1)
return inner2
num=inner2
print(num())
num()=inner2()
y=fun()  fun is inner1
inner1()
x=fun()  fun is num
num( ) return 10
x=10
return 100
y=100
return 200
prints 200
'''


# Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun): # fun is inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):   # fun is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold # f1=bold(italic(underline(f1)))
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())

'''
f1=bold(italic(underline(f1)))
underline(f1)
fun is f1
return inner3
underline(f1)=inner3
italic(inner3)
fun is inner3
return  inner2
italic(inner3)=inner2
bold(inner2)
fun is inner2
return  inner1
bold(inner2)=inner1
f1=inner1
f1()=inner1()
return  '<b>'  +  fun()  +  '</b>'
fun is inner2
'<b>'  +  inner2()  +  '</b>'
in inner2() 
return  '<i>'  +  fun() +  '</i>'
'<b>'  + '<i>'  +  inner3() +  '</i>'  +  '</b>'
fun is inner3
'<u>'  +  fun()  +  '</u>'
fun is f1
'<b>'  + '<i>'  +  '<u>'  +  f1()  +  '</u>' +  '</i>'  +  '</b>'
f1()
return  'Hello  World'
'<b>'  + '<i>'  +  '<u>'  + 'Hello  World' +  '</u>' +  '</i>'  +  '</b>'
'''

