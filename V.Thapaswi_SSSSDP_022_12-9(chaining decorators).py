
#1) Find  outputs  
def  square(fun): #fun=num
	def  inner1():
		x = fun()#go to line 14--->10
		return  x * x #10*10=100
	return  inner1
def   double(fun):#fun=inner1
	def  inner2():
		y = fun()#go to line 3--->100
		return  2 * y #2*100=200
	return   inner2
@double #num=double(square(num))-->double(inner1)--->num=inner2
@square #num=square(num)
def  num():
	return  10
#end of the function
print(num()) #200



# 2)  Find  outputs  
def   bold(fun):#fun is inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>' 
	return  inner1
def   italic(fun):#fun is inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):#fun is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold #f1=bold(italic(underline(f1)))->bold(italic(inner3))-> bold(inner2) ->inner1
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())#f1=inner1 --><b><i><u>Hello  World</u></i></b>