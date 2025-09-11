#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')

Output :
Begin
f2  function
f1  function
Back  to  f2  function
End

#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	#fun() # Error 
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')

Output :
Begin
f1  function
f2  function
Back  to  f2  function
End

