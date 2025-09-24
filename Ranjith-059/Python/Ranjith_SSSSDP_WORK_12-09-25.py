# Find  outputs  (Home  work)
def  square(fun):
    def  inner1():
	    x = fun() # x=num()
	    return  x * x
    return  inner1
def   double(fun):
    def  inner2():
        y = fun() # y = inner1()
        return  2 * y
    return   inner2
@double
@square  # num=double(inner1) num =inner2()
def  num():
	return  10
#end of the function
print(num())
# 200

# Find  outputs  (Home  work)
def   bold(fun):
    print("bold",fun.__name__) # inner2()
    def  inner1():
	    return  '<b>'  +  fun()  +  '</b>'
    return  inner1
def   italic(fun):
    print("italic",fun.__name__) # inner3
    def   inner2():
        return  '<i>'  +  fun() +  '</i>'
    return  inner2
def   underline(fun): # 
    print("underline",fun.__name__) # f1()
    def   inner3():
    	return  '<u>'  +  fun()  +  '</u>'
    return  inner3
@bold
@italic
@underline
def   f1():  #f1=inner1()
       return  'Hello  World'
# End  of  the  function
print(f1())
# <b> <i> <u> Hello world  </u>  </i>    </b>
