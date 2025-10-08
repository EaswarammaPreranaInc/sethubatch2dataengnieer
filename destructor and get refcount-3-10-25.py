# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))                         # 5  (4 + 1)
print(sys . getrefcount(c1()))                      # 2
print(sys . getrefcount(352))                       # 3
print(sys . getrefcount([10 , 20 , 15 , 18]))       # 2
print(sys . getrefcount(10.8))                      # 2
print(sys . getrefcount({10 , 20 , 15 , 18}))       # 2
print(sys . getrefcount('Hyd'))                     # 3
print(sys . getrefcount({10 : 20 , 30 : 40}))       # 2
print(sys . getrefcount((10 , 20 , 30 , 40)))       # 2




# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . _init_())                             # constructor : id   \n   None
print(sys . getrefcount(t))                     # 2
print(t . _del_())                              # Destructor : id   \n   25
print(sys . getrefcount(t))                     # 2
print('Bye')                                    # Bye




#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')       # Object is created
	def  _del_(self):
		print('Object  is  lost')            # Object is lost
#End  of  the  class
def    f1():
	print('Function  Begin')                # Function Begin
	a  =  c1()
	print(a)                                # class and id 
	print('Function  end')
	return   a
print('Program  Begin')                     # Program Begin
b = f1()
print(b)                                    # Class and id 
print('Program  End')                       # Program End



#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')          # Object is created
	def  _del_(self):
		print('Object  is  lost')               # Object is lost
#End  of  the  class
def    f1():
        print('Function  begin')                # Function begin
        a  =  c1()
        print('Function  end')                  # Function end
        return   a
print('Program  Begin')                         # Program begin
f1()
print('Program  End')                           # Program End



#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')          # Object is created
	def  _del_(self):
		print('Object  is  lost')               # Object is lost
#End  of  the  class
def    f1():
        print('Function  begin')                # Function begin
        a  =  c1()
        print('Function  end')                  # Function end
print('Program  Begin')                         # Program Begin
b = f1()
print(b)                                        # None
print('Program  End')                           # Program End




# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')         # c1 class object is created
		self . b = k
		print('End  of  c1  class constructor')         # End of c1 class constructor
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')         # c2 class object is created
		self . a = c1(self)
		print('End  of  c2  class constructor')         # End of c2 class constructor
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')                                 # Program Begin
x = c2()
print('program end')                                    # Program End



#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')             # Destructor
		global  b
		b = self
a = c1()
del  a
print('Hello')                          # Hello
