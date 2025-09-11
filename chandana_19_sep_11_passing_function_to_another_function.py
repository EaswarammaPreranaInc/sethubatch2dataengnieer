#Find outputs
def f1():
    print('f1 function')
def f2(fun):
    print('f2 function')
    fun()
    print('Back to f2 function')
# end of the function
print('Begin')
f2(f1) # passes the function as an argument 
print('End')
'''
o/p:
Begin
f2 function
f1 function
Back to f2 function
End
'''

# find outputs
def f1():
    print('f1 function')
def f2(fun):
    print('f2 function')
    #fun() # NoneType obj is not callable
    print('Back to f2 function')
#end of the function
print('Begin')
f2(f1()) # executes f1 immediately and passes the result
print('End')
'''
o/p:
Begin
f1 function
f2 function
Back to f2 function
End'''


