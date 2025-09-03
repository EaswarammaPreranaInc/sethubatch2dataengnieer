#1st program
# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) #20
	dict = globals()
	print(dict['a'])#11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)#10
a += 1 #11
f1()
print(a)#40
'''
10
20
11
40
'''

#2nd program
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# End of the function
f1()
'''
10
10
'''

#3rd program
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)#20
	#print(globals()['x'])#error,x not defined
# End  of  the  function
f1()


#4th program
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
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

#5th program
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)
def   f2():
	global  x
	x = 30
	print(x)
	x += 1 #31
def   f3():
	global  y
	y = 40
	print(y)
	y += 1 #41
def   f4():
	x = 50
#	global   x  #error,cannot define global x as x is lv
#  End  of  the  functions
x = 10
print(x)#10
x += 1#x=11
f1()
print(x)
f2()
print(x)#31
x += 1 #32
f3()
print(y)
f4()
print(x)

'''
10
20
11
30
31
40
41
32
'''

#6th program
# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)#10
f1()
print(a)

'''
10
20
20
30
'''

#7th program
# Find  outputs(Home  work)
def  f1():
	global  a
	#print(a)#error,a is not defined
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)#30
# End  of   f2   function
f1()
f2()
print(a)
'''
10
20
30
30
'''

#8th program
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)#10
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)#40

'''
10
20
30
40

'''


#9th program
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	#print(a) #error ,a not defined
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)#40
'''
10
30
20
40
'''

#10th program
#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a # a defined as lv
        print(a)#10
        global  b
        b = 20
# End  of  f1()  function
f1()#10
#print(a)#error,a not defined
print(b)#20

'''
10
20
'''

#11th program
# Find outputs (Home  work)
def  f1():
        global  a
        print(a)#11
        a += 1#12
def  f2():
        global  a
        print(a)#13
        a += 1#14
# End  of  the  function
a = 10
print(a)#10
a += 1#11
f1()
print(a)
a += 1#13
f2()
print(a)#14
'''
10
11
12
13
14
'''

#12th program
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
def  f2():
	print(a)#11
	a += 1
# End of the function
a = 10
print(a)#10
f1()
a += 1#11
#f2() #error
print(a)#12
'''
10
20
11
'''

#13th program
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a # a defines as local
	print(a)#20
	print(globals()['a'])#11
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10
a += 1#11
f1()
print(a)#40
'''
10
20
11
40
'''

#14th program
#  Find   outputs
def   f1():
    pass
	#x = x + 5 #error ,cannot access x 
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)#15
# End of f2  function
x = 10
f1()
f2()
print(x)#10
'''
15
10
'''

