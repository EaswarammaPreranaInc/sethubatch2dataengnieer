# #  Tricky  program
# # Find  outputs (Home  work)
# class  c1:
# 	def  __init__(self):
# 		print('Object  is    created')
# 	def  __del__(self):
# 		print('Object  is  lost')
# #End  of  the  class
# def    f1():
#         print('Function  begin')
#         a  =  c1()
#         print('Function  end')
#         return   a                 #object is not destroyed here
# print('Program  Begin')
# f1()                           #object came and destroyed as there is no ref
# print('Program  End')
# '''
# Program Begin
# Function Begin
# Object is created
# Function End
# Object is lost
# Program End
# '''




# #  Tricky  program
# # Find  outputs (Home  work)
# class  c1:
# 	def  __init__(self):
# 		print('Object  is    created')
# 	def  __del__(self):
# 		print('Object  is  lost')
# #End  of  the  class
# def    f1():
#         print('Function  begin')
#         a  =  c1()
#         print('Function  end')
# print('Program  Begin')
# b = f1()
# print(b)
# print('Program  End')
# '''
# Program Begin
# Function begin
# Object is created
# Function end
# Object is lost
# None
# Program End
# '''


# # Most  tricky  program
# # Circular  reference (Home  work)
# class   c1:
# 	def   __init__(self , k):
# 		print('c1  class  object  is  created')
# 		self . b = k
# 		print('End  of  c1  class constructor')
# 	def   __del__(self):
# 		print('c1  class  object  is  lost')
# # End of class c1
# class  c2:
# 	def  __init__(self):
# 		print('c2  class  object  is  created')
# 		self . a = c1(self)
# 		print('End  of  c2  class constructor')
# 	def  __del__(self):
# 		print('c2  class  object  is  lost')
# #End of class c2
# print('Program  begin')
# x = c2()
# print('program end')
# '''
# program begin
# c2 class object is created     #c2.a = new c1ref
# c1 class object is created     #c1.b = same c2ref
# end of c1 class constructor
# end of c2.class constructor
# program end
# c2 class object is lost
# c1 class object is lost
# '''



# #  Lucky  object
# # Find  outputs (Home  work)
# class   c1:
# 	def  __del__(self):
# 		print('Destructor')
# 		global  b
# 		b = self
# a = c1()          
# del  a             
# print('Hello')            
# '''
# Destructor
# Hello

# python doc ref its stated that:
# It is not guaranteed that __del__() methods are called for objects that still exist when the interpreter exits.
# '''

