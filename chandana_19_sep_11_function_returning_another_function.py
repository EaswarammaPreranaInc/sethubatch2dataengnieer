# find outputs
def outer():
    print('Outer function')
    def inner():
        print('Inner function')
    return inner
# end of the function
fun=outer() # fun = inner
print('Hello')
fun()
print('Bye')
#inner() # error: inner is a local function inside outer, not visible outside
'''
o/p:
Outer function
Hello
Inner function
Bye'''



# find outputs
def outer(x):
    print('Outer function')
    def inner1():
        print('1st inner function')
    # end of inner1
    def inner2():
        print('2nd inner function')
    # end of inner2
    if x==10:
        return inner1
    else:
        return inner2
#end of the function
f1=outer(10) # f1=inner1
f2=outer(20) # f2=inner2
f1()
f2()
'''
o/p:
Outer function
Outer function
1st inner function
2nd inner function'''


# Find  outputs  
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
'''
o/p:
Hi
Hello
'''

