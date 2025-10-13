#1st program
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) #4+1 -> 5
print(sys . getrefcount(c1())) #1
print(sys . getrefcount(352)) #cannot be determined
print(sys . getrefcount([10 , 20 , 15 , 18]))#1
print(sys . getrefcount(10.8))#cannot be determined
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))#cannot be determined
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#cannot be determined

# 2nd  program
# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() #constructor 1000
print(t . __init__()) #construtor 1000 None
print(sys . getrefcount(t)) #2
print(t . __del__())#destructor 1000 25
print(sys . getrefcount(t)) #2
print('Bye')#Bye
#Destructor 1000


#3rd program
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')#program begin
b = f1() #function begin object is created \n __main__.c1 address \n function end 
# object is lost 
print(b)# __main__.c1 1000
print('Program  End')#Program  End
#object is lost


#4th  program
# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin') #Program  begin
x = c2() # c2 class object is created, c1 class object is created , end of c1 class constructor 
#End  of  c2  class constructor, c1 class object is lost 
print('program end')# program end
#c2  class  object  is  lost
# x={a:None,b:x}
