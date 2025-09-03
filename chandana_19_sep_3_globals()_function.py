# Find  outputs  
def   f1():
	a = 20
	print(a) # print local variable 'a'
	dict = globals() # get the dictionary of global variables
	print(dict['a']) # print global variable 'a'
	a = 30 # change local variable 'a'
	dict['a'] = 40 # change global variable 'a'
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)
'''
o/p:
10
20
11
40'''


# Find  outputs 
x = 10
def   f1():
	print(x) # print global variable 'x'
	print(globals()['x']) # print global variable 'x'
# End of the function
f1()
'''
10
10'''


# Find  outputs 
def  f1():
	x = 20
	print(x) 
	print(globals()['x']) # error: beacuse there is already local variable 'x'.so, 'x' cannot be treated as global variable
# End  of  the  function
f1()
'''
10'''



# Find outputs 
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals() # get the dictionary of global variables
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100 # change global variable 'a'
	dict['b'] = 200 # change global variable 'b'
	dict['c'] = 300 # change global variable 'c'
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
'''
40 50 60
10 20 30
100 200 300
'''


