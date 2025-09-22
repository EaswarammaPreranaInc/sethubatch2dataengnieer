# Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun() #10
		return  x * x #100
	return  inner1
def   double(fun):
	def  inner2():
		y = fun() #100
		return  2 * y #200
	return   inner2
@double #Here that returned value is doubled i.e 200
@square #Here 10 is squared and returned to double i.e 100
def  num():
	return  10
#end of the function
print(num()) #100 #200
'''output:
200
'''



# Find  outputs  (Home  work)
def   bold(fun): #Here fun will be f1()
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>' #fun() will be returned value of f1() i.e <i><u>Hello World </u></i>
	return  inner1
def   italic(fun): #Here fun will be f1()
	def   inner2():
		return  '<i>'  +  fun() +  '</i>' #fun() will be returned value of f1() i.e <u>Hello World </u>
	return  inner2
def   underline(fun): #Here fun will be f1()
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>' #fun() will be returned value of f1() i.e Hello World
	return  inner3
@bold
@italic 
@underline
def   f1():
       return  'Hello  World' 
# End  of  the  function
print(f1()) #<u>Hello World </u>  #<i><u>Hello World </u></i> #<b><i><u>Hello World </u></i></b>

'''output:
<b><i><u>Hello World </u></i></b>
'''