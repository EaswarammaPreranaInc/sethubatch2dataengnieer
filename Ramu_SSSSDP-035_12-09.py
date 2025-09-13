#Ramu(12-09)


# Find  outputs  (Home  work)
def  square(fun): #fun is num 
	def  inner1():
		x = fun() #x=num()-->x=10
		return  x * x 
	return  inner1
def   double(fun): #fun is inner1
	def  inner2():
		y = fun() #y=inner1()-->y=100
		return  2 * y
	return   inner2
@double #-->num= double(square(num))--> num=double(inner1)-->num=inner2
@square #--> num=square(num)
def  num():
	return  10
#end of the function
print(num())#-->inner2()-->200


# Find  outputs  (Home  work)
def   bold(fun): #fun is inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>' #<b><i><u>Hello world</u></i></b>
	return  inner1
def   italic(fun): #fun is inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>' #<i><u>Hello world</u></i>
	return  inner2
def   underline(fun): #fun is f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>' #<u>Hello world</u>
	return  inner3
@bold #f1=bold(italic(underline(f1)))-->f1=bold(italic(inner3))-->f1=bold(inner2)-->f1=inner1
@italic #f1=italic(underline(f1))
@underline #f1=underline(f1)
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1()) #-->inner1()--><b><i><u>Hello  World</u></i></b>