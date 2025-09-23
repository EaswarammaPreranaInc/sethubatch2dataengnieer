#  Tricky  program
#   Find  outputs
# def  f1():
# 	global  a
# 	if  a:
# 		print(a)
# 		a = a - 1
# 		f1()
# 		print('Hello')
# 		print('Hi')
# 		print(a)
# 	print('Bye')
# # End  of  the  function
# a = 3
# f1()
# print('End')
# # output:

#   Find  outputs
# def  f1():
# 	a = 3
# 	if  a:
# 		print(a)
# 		a = a - 1
# 		f1()
# 		print('Hello')
# 		print('Hi')
# 		print(a)
# 	print('Bye')
# #End  of  the  function
# a = 3
# f1()
# print('End')

#  Most  tricky   program
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)