# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))				# 4+1=5
print(sys . getrefcount(c1()))				# 1
print(sys . getrefcount(352))				# cannot Predicted
print(sys . getrefcount([10 , 20 , 15 , 18]))		# 1
print(sys . getrefcount(10.8))				# cannot Predicted
print(sys . getrefcount({10 , 20 , 15 , 18}))		# 1
print(sys . getrefcount('Hyd'))				# cannot Predicted
print(sys . getrefcount({10 : 20 , 30 : 40}))		# 1
print(sys . getrefcount((10 , 20 , 30 , 40)))		# cannot Predicted




 # Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))	# Constructor : address
		return    None				# None
	def  _del_(self):
		print('Destructor  :  ' , id(self))	# Destructor :  address
		return  25				# 25
# End  of  the  class
t = Test()
print(t . _init_())					# Constructor with same addres
print(sys . getrefcount(t))				# 2
print(t . _del_())					# Destructor with same address
print(sys . getrefcount(t))				# 2
print('Bye')						# Bye




 #  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')		
	def  _del_(self):
		print('Object  is  lost')		
#End  of  the  class
def    f1():
	print('Function  Begin')			
	a  =  c1()					
	print(a)					
	print('Function  end')
	return   a
print('Program  Begin')					# Program Begin
b = f1()
print(b)
print('Program  End')

''' 
	#output
	 Program Begin
	 function Begin
	 Obiect is created
	 address of the c1 class object
	 Function end 
	 address of the object b
	 Program End
	 Object is lost
'''


 #  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')
'''
	#output
	Program Begin
	Function begin
	Function end
	Program End
'''


 #  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
'''	
	#output
	Program Begin
	Function begin
	Function end
	None
	Prgram End
'''



# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')
'''
	# output
	Program Begin
	c2 class object is created
	c1 class object is created
	End  of  c1  class constructor
	End  of  c2  class constructor
 	program end
 	c1  class  object  is  lost
 	c2  class  object  is  lost	
'''	


 #  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

'''
	output:-
 Destructor
 Hello
'''