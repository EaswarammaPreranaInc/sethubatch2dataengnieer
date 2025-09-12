def  square(fun):#fun is num ,go to line 5 
	def  inner1():
		x = fun()#go to line 15, since fun is pointing to num
		return  x * x  # return 100 to function call in line 9 as  10*10 is 100 
	return  inner1 #return inner1 to function call in line 12
def   double(fun): #fun is inner1 ,go to line 13
	def  inner2(): 
		y = fun()#go to line 2, since fun is pointing to inner1
		return  2 * y #returns result 200 to function call in line 18 as 2*100 is 200
	return   inner2 #return inner2 to function call in line 12
@double  #num = double(square(num)) ,go to line 1 where square function is defined  -#num = double(inner1) ,go to line 6 where double function is defined -#num = inner2, go to line 18 
@square #function already executed in line 13
def  num():
	return  10 # return 10 to function call in line 4
#end of the function
print(num())# go to line 7, since num is pointing to inner2  # result = 200



def   bold(fun):#fun is inner2, go to line 4
	def  inner1(): #go to line 5 since fun points to inner2 
		return  '<b>'  +  fun()  +  '</b>' #return <b><i><u>hello world<u><i><b> to function call in line 19
	return  inner1#return inner1 to funcion call in line 13
def   italic(fun): #fun is inner3, go to line 8
	def   inner2(): #go to line 9 since fun points to inner3 
		return  '<i>'  +  fun() +  '</i>' #return <i><u>hello world<u><i> to function call in line 2
	return  inner2 #return inner2 to funcion call in line 13
def   underline(fun): #fun is f1, go to line 12
	def   inner3():#go to line 16 since fun points to f1 
		return  '<u>'  +  fun()  +  '</u>' #return <u>hello world<u> to function call in line 6
	return  inner3 #return inner3 to funcion call in line 13
@bold #f1=bold(italic(underline(f1))) go to line 9 where underline function is defined --> f1 = bold(italic(inner3)) go to line 5 where italic function is defined --> f1= bold(inner2) go to line 1 where bold is defined --> f1 = inner1 go to line 19 
@italic #function already executed in line 13
@underline #function already executed in line 13
def   f1():
       return  'Hello  World' #return 'hello world' to function call in line 10
# End  of  the  function
print(f1()) #go to line 2 since f1 points to inner function
#result : <b><i><u>hello world<u><i><b>
