
# 1) Find  outputs  (Home  work)

def  square(fun):       # fun is num
	def  inner1():
		x = fun()       # x = 10
		return  x * x   # 100
	return  inner1
    
def   double(fun):      # fun is inner1
	def  inner2():
		y = fun()       # y = 100
		return  2 * y   # 200
	return   inner2
    
@double     # num=double(square(num)) -> double(inner1) ->inner2 -> num = inner2
@square
def  num():
	return  10
#end of the function
print(num()) # print(inner2()) 

'''
Output: 
200
'''



# 2) Find  outputs  (Home  work)

def bold(fun):          # fun is inner2
    def inner1():
        return '<b>' + fun() + '</b>'  # Adds bold tags to the result from fun()=inner2()
    return inner1                      

def italic(fun):        # fun is inner3
    def inner2():
        return '<i>' + fun() + '</i>'  # Adds italic tags to the result from fun()=inner3()
    return inner2                     

def underline(fun):     # fun is f1
    def inner3():
        return '<u>' + fun() + '</u>'  # Adds underline tags to the result from fun()=f1()
    return inner3                     

@bold       # bold(italic(underline(f1))) --> bold(italic(inner3)) --> bold(inner2) --> f1 = inner1
@italic
@underline
def f1():
    return 'Hello World'             

print(f1())  # print(inner1()) Executes the inner1 fuction

'''
Outputs:
<b><i><u>Hello World</u></i></b>
'''
